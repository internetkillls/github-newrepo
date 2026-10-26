import { existsSync, readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { resolve } from "node:path";
import { CdpSession, listTargets } from "./cdp-client.mjs";
import { DEFAULT_TARGET_URL, stateRoot } from "./runtime-config.mjs";
import { canonicalSessionRegistryPath, ensureProjectState } from "./project-state.mjs";
import { writeJsonAtomic } from "./atomic-json.mjs";
import { withProjectStateLockSync } from "./project-state-lock.mjs";
import {parseChatGptUrl,conversationIdFromUrl as sharedConversationId,sameConversationUrl,isChatGptPageUrl,uniqueConversationTarget} from './conversation-url.mjs';

export const legacySessionRegistryPath = resolve(stateRoot, "chatgpt-sessions.json");
export const sessionRegistryPath = canonicalSessionRegistryPath(ensureProjectState().projectId);

const RECENT_RUN_LIMIT = 10;
const DEFAULT_STALE_AFTER_DAYS = 21;

const roomDefaults = {
  main: {
    purpose: "Primary repo collaboration room",
    lifecycle: "long_lived",
  },
  debug: {
    purpose: "Focused failure/debugging room",
    lifecycle: "bug_family",
  },
  critic: {
    purpose: "Independent review room",
    lifecycle: "review",
  },
  scratch: {
    purpose: "Disposable prompt/context check room",
    lifecycle: "disposable",
  },
};

function nowIso() {
  return new Date().toISOString();
}

function sha256(text) {
  return createHash("sha256").update(String(text || "")).digest("hex");
}

function mismatchError(name, saved, project) {
  const error = new Error(
    `ChatGPT session alias "${name}" belongs to a different project. Use --rebind-alias to bind it to this repo.`,
  );
  error.errorCode = "session.alias_project_mismatch";
  error.details = {
    alias: name,
    currentProjectId: project.projectId,
    currentRepoRoot: project.repoRoot,
    aliasProjectId: saved?.projectId || null,
    aliasRepoRoot: saved?.repoRoot || null,
  };
  return error;
}

function threadIdFromUrl(url, fallback = "") {
  const id=sharedConversationId(url);if(id)return `chatgpt:${id}`;
  if (fallback) return `target:${fallback}`;
  return `unknown:${sha256(url).slice(0, 16)}`;
}

export function conversationIdFromUrl(url) {
  return sharedConversationId(url);
}

function roomError(errorCode, message, details = {}) {
  const error = new Error(message);
  error.errorCode = errorCode;
  error.details = details;
  return error;
}

function roomPurpose(name, saved, project) {
  return saved?.purpose
    || roomDefaults[name]?.purpose
    || `ChatGPT ${name} room for ${project.displayName}`;
}

function roomLifecycle(name, saved) {
  return saved?.lifecycle || roomDefaults[name]?.lifecycle || "long_lived";
}

function normalizeLineage({ name, saved, activeThreadId, activeConversationUrl, createdAt }) {
  const existing = Array.isArray(saved?.lineage) ? saved.lineage : [];
  if (existing.length) return existing;
  if (!activeConversationUrl) return [];

  return [
    {
      threadId: activeThreadId,
      conversationUrl: activeConversationUrl,
      status: "active",
      openedAt: createdAt,
      openedByRunId: saved?.lastRunId || null,
      openedReason: saved?.openedReason || `migrated ${name} alias`,
      closedAt: null,
      closedByRunId: null,
      closedReason: null,
      firstRunId: saved?.lastRunId || null,
      lastRunId: saved?.lastRunId || null,
      lastReceiptPath: saved?.lastReceiptPath || null,
    },
  ];
}

function normalizeRecentRuns(saved) {
  if (Array.isArray(saved?.recentRuns)) return saved.recentRuns.slice(0, RECENT_RUN_LIMIT);
  if (!saved?.lastRunId) return [];
  return [
    {
      runId: saved.lastRunId,
      receiptPath: saved.lastReceiptPath || null,
      transcriptPath: saved.lastTranscriptPath || null,
      createdAt: saved.lastUsedAt || saved.updatedAt || saved.createdAt || nowIso(),
    },
  ];
}

function normalizeRoom(name, saved = {}, project = ensureProjectState()) {
  const activeConversationUrl = saved.activeConversationUrl || saved.conversationUrl || saved.url || "";
  const targetId = saved.targetId || null;
  const activeThreadId = saved.activeThreadId || saved.threadId || threadIdFromUrl(activeConversationUrl, targetId);
  const createdAt = saved.createdAt || saved.updatedAt || nowIso();
  const lastUsedAt = saved.lastUsedAt || saved.updatedAt || null;
  return {
    alias: name,
    projectId: saved.projectId || project.projectId,
    repoRoot: saved.repoRoot || project.repoRoot,
    projectDisplayName: saved.projectDisplayName || project.displayName,
    purpose: roomPurpose(name, saved, project),
    lifecycle: roomLifecycle(name, saved),
    activeThreadId,
    activeConversationUrl,
    conversationUrl: activeConversationUrl,
    url: activeConversationUrl,
    targetId,
    title: saved.title || "",
    responseMode: saved.responseMode || "blocking",
    createdAt,
    lastUsedAt,
    updatedAt: saved.updatedAt || nowIso(),
    lastRunId: saved.lastRunId || null,
    lastReceiptPath: saved.lastReceiptPath || null,
    lastTranscriptPath: saved.lastTranscriptPath || null,
    callCount: Number(saved.callCount || (saved.lastRunId ? 1 : 0)),
    staleAfterDays: Number(saved.staleAfterDays || DEFAULT_STALE_AFTER_DAYS),
    roomTargetVerification: saved.roomTargetVerification || null,
    lastTargetRepair: saved.lastTargetRepair || null,
    recentRuns: normalizeRecentRuns(saved),
    lineage: normalizeLineage({ name, saved, activeThreadId, activeConversationUrl, createdAt }),
  };
}

function normalizeFreshThreads(raw) {
  return Array.isArray(raw?.freshThreads) ? raw.freshThreads : [];
}

export function normalizeSessionRegistry(raw, project = ensureProjectState()) {
  const sourceRooms = raw?.rooms || raw?.aliases || raw?.sessions || {};
  const normalized = {
    schemaVersion: 2,
    projectId: project.projectId,
    ...(raw?.projectId && raw.projectId !== project.projectId ? { migratedProjectIdFrom: raw.projectId } : {}),
    rooms: {},
    freshThreads: normalizeFreshThreads(raw),
  };

  for (const [name, saved] of Object.entries(sourceRooms)) {
    normalized.rooms[name] = normalizeRoom(name, saved, project);
  }

  return normalized;
}

function registryPathForProject(project = ensureProjectState()) {
  return canonicalSessionRegistryPath(project.projectId);
}

function readRegistry() {
  const project = ensureProjectState();
  const canonicalPath = registryPathForProject(project);
  try {
    return normalizeSessionRegistry(JSON.parse(readFileSync(canonicalPath, "utf8")), project);
  } catch {
    if (existsSync(legacySessionRegistryPath)) {
      try {
        const migrated = normalizeSessionRegistry(JSON.parse(readFileSync(legacySessionRegistryPath, "utf8")), project);
        return withProjectStateLockSync({ project, reason: "migrate-legacy-session-registry" }, () => {
          writeRegistry(migrated);
          return migrated;
        });
      } catch {
        // Fall through to an empty registry.
      }
    }
    return normalizeSessionRegistry({ rooms: {} }, project);
  }
}

function writeRegistry(registry) {
  const project = ensureProjectState();
  const canonicalPath = registryPathForProject(project);
  writeJsonAtomic(canonicalPath, normalizeSessionRegistry(registry, project));
}

function isChatGptTarget(target) {
  return isChatGptPageUrl(target.url);
}

function selectLiveTarget(sessions,{targetId,conversationUrl}={}){
 if(targetId)return sessions.find(t=>t.id===targetId)||null;
 let candidates=sessions;
 if(conversationUrl){const p=parseChatGptUrl(conversationUrl);if(!p)throw roomError('room.conversation_url_invalid','Unsupported binding URL.');
  if(p.kind==='conversation')return uniqueConversationTarget(sessions,conversationUrl);
  candidates=sessions.filter(t=>parseChatGptUrl(t.url)?.canonicalUrl===p.canonicalUrl);
 }
 if(candidates.length>1)throw roomError('room.target_ambiguous','An explicit target is required for an ambiguous binding.');
 return candidates[0]||null;
}

function targetSummary(target, aliases = []) {
  return {
    id: target.id,
    type: target.type,
    title: target.title,
    url: target.url,
    aliases,
    webSocketDebuggerUrl: target.webSocketDebuggerUrl,
  };
}

function targetFromConversationUrl(url, {
  id = "",
  title = "",
  webSocketDebuggerUrl = "",
} = {}) {
  const conversationId = conversationIdFromUrl(url);
  if (!conversationId) {
    const error = new Error(`Invalid ChatGPT conversation URL: ${url}`);
    error.errorCode = "room.conversation_url_invalid";
    error.details = { conversationUrl: url || null };
    throw error;
  }
  return targetSummary({
    id: id || `registry:${conversationId}`,
    title: title || `ChatGPT conversation ${conversationId}`,
    url,
    webSocketDebuggerUrl,
  });
}

function targetThreadId(target) {
  return threadIdFromUrl(target?.url, target?.id);
}

function archiveActiveLineage(lineage, { closedAt, closedByRunId, closedReason } = {}) {
  return lineage.map((entry) => entry.status === "active"
    ? {
        ...entry,
        status: "archived",
        closedAt,
        closedByRunId: closedByRunId || null,
        closedReason: closedReason || "replaced by new active thread",
      }
    : entry);
}

function bindRoomToTarget({ room, name, target, project, openedReason, archivePrevious = true }) {
  const timestamp = nowIso();
  const activeThreadId = targetThreadId(target);
  const activeConversationUrl = target.url || "";
  let lineage = Array.isArray(room?.lineage) ? [...room.lineage] : [];

  const changedThread = room?.activeThreadId && room.activeThreadId !== activeThreadId;
  if (changedThread && archivePrevious) {
    lineage = archiveActiveLineage(lineage, {
      closedAt: timestamp,
      closedByRunId: null,
      closedReason: openedReason || "new active thread",
    });
  }

  const activeIndex = lineage.findIndex((entry) =>
    entry.threadId === activeThreadId && entry.conversationUrl === activeConversationUrl,
  );
  const activeEntry = {
    threadId: activeThreadId,
    conversationUrl: activeConversationUrl,
    status: "active",
    openedAt: activeIndex >= 0 ? lineage[activeIndex].openedAt : timestamp,
    openedByRunId: activeIndex >= 0 ? lineage[activeIndex].openedByRunId : null,
    openedReason: activeIndex >= 0 ? lineage[activeIndex].openedReason : openedReason || "alias binding",
    closedAt: null,
    closedByRunId: null,
    closedReason: null,
    firstRunId: activeIndex >= 0 ? lineage[activeIndex].firstRunId : null,
    lastRunId: room?.lastRunId || null,
    lastReceiptPath: room?.lastReceiptPath || null,
  };
  if (activeIndex >= 0) lineage[activeIndex] = activeEntry;
  else lineage.push(activeEntry);

  const createdAt = room?.createdAt || timestamp;
  return {
    ...normalizeRoom(name, room || {}, project),
    projectId: project.projectId,
    repoRoot: project.repoRoot,
    projectDisplayName: project.displayName,
    activeThreadId,
    activeConversationUrl,
    conversationUrl: activeConversationUrl,
    url: activeConversationUrl,
    targetId: target.id,
    title: target.title,
    createdAt,
    lastUsedAt: timestamp,
    updatedAt: timestamp,
    lineage,
  };
}

export async function listChatGptSessions(port) {
  const registry = readRegistry();
  const project = ensureProjectState();
  const targets = (await listTargets(port))
    .filter((target) => target.type === "page" && target.webSocketDebuggerUrl && isChatGptTarget(target));

  return targets.map((target) => {
    const aliases = Object.entries(registry.rooms)
      .filter(([, saved]) => saved.projectId === project.projectId)
      .filter(([, saved]) =>
        saved.targetId === target.id
        || saved.activeConversationUrl === target.url
        || saved.conversationUrl === target.url
        || saved.url === target.url,
      )
      .map(([alias]) => alias);
    return targetSummary(target, aliases);
  });
}

async function cdpJson(port, path, { method = "GET" } = {}) {
  const response = await fetch(`http://127.0.0.1:${port}${path}`, { method, signal:AbortSignal.timeout(5000) });
  if (!response.ok) throw new Error(`CDP ${path} -> ${response.status}`);
  return response.json();
}

async function openChatGptTarget(port, url) {
  const identity=parseChatGptUrl(url);
  if(!identity)throw roomError('room.conversation_url_invalid','Unsupported ChatGPT opening URL.');
  let target;
  try {
    // A lost PUT acknowledgement may already have created a tab. Never replay it as GET.
    target = await cdpJson(port, `/json/new?${encodeURIComponent(identity.canonicalUrl)}`, { method: "PUT" });
    if(typeof target?.id!=='string'||!target.id)throw Error('Missing created target identity');
    await activateChatGptSession(port, { targetId: target.id });
    return target;
  } catch(error) {
    error.errorCode=error.errorCode||'room.open_outcome_unknown';
    error.remoteOutcome='unknown';error.automaticRetryAllowed=false;
    error.details={...error.details,openedTargetId:target?.id||null,expectedUrl:identity.canonicalUrl};
    throw error;
  }
}

export async function newChatGptSession(port, { name, url = DEFAULT_TARGET_URL, bind = Boolean(name) } = {}) {
  const target = await openChatGptTarget(port, url);
  if (name && bind) {
    await aliasChatGptSession(port, {
      name,
      targetId: target.id,
      openedReason: "new bound thread",
      roomTargetVerification: conversationIdFromUrl(target.url) ? "verified_live" : "uncommitted_live_target",
    });
  }
  return targetSummary(target, name && bind ? [name] : []);
}

export async function aliasChatGptSession(port, {
  name,
  targetId,
  conversationUrl,
  openedReason = "alias binding",
  archivePrevious = true,
  roomTargetVerification = "",
  lastTargetRepair = null,
} = {}) {
  const project = ensureProjectState();
  if (!name) throw new Error("Session alias name is required.");
  const sessions = await listChatGptSessions(port);
  const target = selectLiveTarget(sessions,{targetId,conversationUrl});
  if (!target) throw new Error(`ChatGPT target not found for id/url: ${targetId || conversationUrl || "(first)"}`);

  return withProjectStateLockSync({ project, reason: `alias:${name}` }, () => {
    const registry = readRegistry();
    const existing = registry.rooms[name];
    if (existing?.projectId && existing.projectId !== project.projectId) {
      throw mismatchError(name, existing, project);
    }
    registry.rooms[name] = bindRoomToTarget({
      room: existing,
      name,
      target,
      project,
      openedReason,
      archivePrevious,
    });
    if (roomTargetVerification) registry.rooms[name].roomTargetVerification = roomTargetVerification;
    if (lastTargetRepair) registry.rooms[name].lastTargetRepair = lastTargetRepair;
    writeRegistry(registry);
    return { name, ...registry.rooms[name] };
  });
}

export function bindChatGptRoomRegistryOnly({
  name,
  conversationUrl,
  targetId = "",
  title = "",
  openedReason = "explicit registry-only rebind",
  verification = "not_verified_registry_only",
} = {}) {
  const project = ensureProjectState();
  if (!name) {
    const error = new Error("Room alias is required.");
    error.errorCode = "session.alias_required";
    throw error;
  }
  const target = targetFromConversationUrl(conversationUrl, { id: targetId, title });
  return withProjectStateLockSync({ project, reason: `rooms:registry-rebind:${name}` }, () => {
    const registry = readRegistry();
    const existing = registry.rooms[name];
    if (existing?.projectId && existing.projectId !== project.projectId) {
      throw mismatchError(name, existing, project);
    }
    registry.rooms[name] = {
      ...bindRoomToTarget({
        room: {
          ...existing,
          projectId: project.projectId,
          repoRoot: project.repoRoot,
          projectDisplayName: project.displayName,
        },
        name,
        target,
        project,
        openedReason,
        archivePrevious: true,
      }),
      roomTargetVerification: verification,
      lastTargetRepair: null,
    };
    writeRegistry(registry);
    return { name, ...registry.rooms[name], registryOnly: true, roomTargetVerification: verification };
  });
}

export async function rebindChatGptSessionAlias(port, { name, targetId, conversationUrl } = {}) {
  if (!name) throw new Error("Session alias name is required.");
  const sessions = await listChatGptSessions(port);
  let target = selectLiveTarget(sessions,{targetId,conversationUrl});
  if (!target && conversationUrl) {
    target = targetSummary(await openChatGptTarget(port, conversationUrl), [name]);
  }
  if (!target) throw new Error(`ChatGPT target not found for id/url: ${targetId || conversationUrl || "(first)"}`);
  const project = ensureProjectState();
  return withProjectStateLockSync({ project, reason: `rebind:${name}` }, () => {
    const registry = readRegistry();
    const existing = registry.rooms[name];
    registry.rooms[name] = bindRoomToTarget({
      room: {
        ...existing,
        projectId: project.projectId,
        repoRoot: project.repoRoot,
        projectDisplayName: project.displayName,
      },
      name,
      target,
      project,
      openedReason: "explicit rebind",
      archivePrevious: true,
    });
    registry.rooms[name].roomTargetVerification = "verified_live";
    writeRegistry(registry);
    return { name, ...registry.rooms[name], rebound: true };
  });
}

export async function resolveChatGptSession(port, selector, { allowRebind = false, conversationUrl = "" } = {}) {
  const project = ensureProjectState();
  if (allowRebind && selector && !selector.startsWith("http")) {
    await rebindChatGptSessionAlias(port, { name: selector, conversationUrl });
  }
  const sessions = await listChatGptSessions(port);
  if (!selector) return selectLiveTarget(sessions);

  const registry = readRegistry();
  const saved = registry.rooms[selector];
  if (saved) {
    if (saved.projectId !== project.projectId) throw mismatchError(selector, saved, project);
    const url=saved.activeConversationUrl||saved.conversationUrl||saved.url;
    if(conversationIdFromUrl(url))return uniqueConversationTarget(sessions,url);
    const p=parseChatGptUrl(url),byTarget=sessions.find(t=>t.id===saved.targetId);
    return p?.kind==='uncommitted'&&parseChatGptUrl(byTarget?.url)?.kind==='uncommitted'&&parseChatGptUrl(byTarget?.url)?.canonicalUrl===p.canonicalUrl?byTarget:null;
  }

  const explicit=sessions.find(t=>t.id===selector);if(explicit)return explicit;
  const aliases=sessions.filter(t=>t.aliases.includes(selector));
  if(aliases.length>1)throw roomError('room.target_ambiguous','Multiple targets match this alias.');
  return aliases[0]||uniqueConversationTarget(sessions,selector);
}

function baseRoomTarget({ project, selector, saved, expectedUrl, threadMode = "continue" }) {
  return {
    projectId: project.projectId,
    alias: selector || null,
    threadMode,
    expectedConversationUrl: expectedUrl || null,
    expectedConversationId: conversationIdFromUrl(expectedUrl),
    savedTargetId: saved?.targetId || null,
    savedTargetUrl: saved?.activeConversationUrl || saved?.conversationUrl || saved?.url || null,
    resolution: "failed",
    verified: false,
    repaired: false,
    repairReason: "none",
    actualTargetId: null,
    actualTargetUrl: null,
    actualConversationId: null,
    targetBoundToRoom: false,
    checkedAt: nowIso(),
  };
}

function finishRoomTarget(roomTarget, target, { resolution, repaired = false, repairReason = "none" } = {}) {
  return {
    ...roomTarget,
    resolution,
    verified: true,
    repaired,
    repairReason,
    actualTargetId: target.id,
    actualTargetUrl: target.url,
    actualConversationId: conversationIdFromUrl(target.url),
    targetBoundToRoom: true,
  };
}

function roomTargetFailure(roomTarget, { errorCode, message, repairReason = "none", target = null }) {
  return roomError(errorCode, message, {
    roomTarget: {
      ...roomTarget,
      repairReason,
      actualTargetId: target?.id || null,
      actualTargetUrl: target?.url || null,
      actualConversationId: conversationIdFromUrl(target?.url),
    },
  });
}

export async function resolveVerifiedRoomTarget(port, selector, {
  allowRebind = false,
  conversationUrl = "",
  threadMode = "continue",
} = {}) {
  const startedAt = Date.now();
  const project = ensureProjectState();
  if (allowRebind && selector && !selector.startsWith("http")) {
    await rebindChatGptSessionAlias(port, { name: selector, conversationUrl });
  }

  const registry = readRegistry();
  const sessions = await listChatGptSessions(port);
  const saved = selector ? registry.rooms[selector] : null;
  if (!selector) {
    if(sessions.length>1)throw roomError('room.target_ambiguous','A worker selector is required when multiple ChatGPT pages are open.');
    const target = sessions[0] || null;
    if (!target) return { target: null, room: null, roomTarget: null };
    return {
      target,
      room: null,
      roomTarget: {
        ...finishRoomTarget(baseRoomTarget({ project, selector, saved: null, expectedUrl: target.url, threadMode }), target, {
          resolution: "current_target",
        }),
        durationMs: Date.now() - startedAt,
      },
    };
  }

  if (saved) {
    if (saved.projectId !== project.projectId) throw mismatchError(selector, saved, project);
    const expectedUrl = conversationUrl || saved.activeConversationUrl || saved.conversationUrl || saved.url || "";
    const roomTarget = baseRoomTarget({ project, selector, saved, expectedUrl, threadMode });
    if (!expectedUrl) {
      throw roomTargetFailure(roomTarget, {
        errorCode: "room.conversation_url_missing",
        message: `Room "${selector}" has no active conversation URL.`,
        repairReason: "expected_url_missing",
      });
    }
    const expectedIdentity=parseChatGptUrl(expectedUrl);
    if (!expectedIdentity || (expectedIdentity.kind!=='conversation' && !saved.targetId)) {
      throw roomTargetFailure(roomTarget, {
        errorCode: "room.conversation_url_invalid",
        message: `Room "${selector}" has an invalid ChatGPT conversation URL: ${expectedUrl}`,
        repairReason: "expected_url_invalid",
      });
    }

    const byTarget = sessions.find((session) => session.id === saved.targetId);
    const byUrl=uniqueConversationTarget(sessions,expectedUrl);
    if(byUrl&&parseChatGptUrl(byUrl.url)?.legacy)throw roomError('room.target_redirect_pending','Observe the legacy target until it reaches the committed modern origin.');
    if (byTarget && sameConversationUrl(byTarget.url, expectedUrl)) {
      await activateChatGptSession(port, { targetId: byTarget.id });
      return {
        target: byTarget,
        room: saved,
        roomTarget: {
          ...finishRoomTarget(roomTarget, byTarget, { resolution: "saved_target_verified" }),
          durationMs: Date.now() - startedAt,
        },
      };
    }
    if (byTarget && expectedIdentity.kind==='uncommitted' && !expectedIdentity.legacy && parseChatGptUrl(byTarget.url)?.kind==='uncommitted' && parseChatGptUrl(byTarget.url)?.canonicalUrl===expectedIdentity.canonicalUrl) {
      await activateChatGptSession(port, { targetId: byTarget.id });
      return {
        target: byTarget,
        room: saved,
        roomTarget: {
          ...finishRoomTarget(roomTarget, byTarget, { resolution: "saved_uncommitted_target_verified" }),
          targetBoundToRoom: true,
          durationMs: Date.now() - startedAt,
        },
      };
    }

    if(expectedIdentity.kind==='uncommitted')throw roomError('room.uncommitted_target_changed','An uncommitted room cannot be restored as a new chat; reconcile its prior send outcome.');
    const repairReason = byTarget
      ? "saved_target_url_mismatch"
      : saved.targetId
        ? "saved_target_closed"
        : "saved_target_missing";
    if (byUrl) {
      await activateChatGptSession(port, { targetId: byUrl.id });
      return {
        target: byUrl,
        room: saved,
        roomTarget: {
          ...finishRoomTarget(roomTarget, byUrl, {
            resolution: "found_matching_open_target",
            repaired: true,
            repairReason,
          }),
          durationMs: Date.now() - startedAt,
        },
      };
    }

    const opened = await openChatGptTarget(port, expectedIdentity.canonicalUrl);
    if(!sameConversationUrl(opened.url,expectedUrl)||parseChatGptUrl(opened.url)?.legacy)throw roomError('room.opened_target_unverified','New target metadata did not confirm the expected conversation; observe before any retry.',{openedTargetId:opened.id});
    return {
      target: targetSummary(opened, [selector]),
      room: saved,
      roomTarget: {
        ...finishRoomTarget(roomTarget, opened, {
          resolution: "opened_expected_url",
          repaired: true,
          repairReason: repairReason === "none" ? "expected_url_not_open" : repairReason,
        }),
        durationMs: Date.now() - startedAt,
      },
    };
  }

  const directById=sessions.find(session=>session.id===selector);
  const aliasCandidates=sessions.filter(session=>session.aliases.includes(selector));
  if(aliasCandidates.length>1)throw roomError('room.target_ambiguous','Multiple pages advertise the requested alias.');
  const directTarget=directById||aliasCandidates[0]||uniqueConversationTarget(sessions,selector);
  if(directTarget&&parseChatGptUrl(directTarget.url)?.legacy)throw roomError('room.target_redirect_pending','Legacy URL is not a dispatch-ready origin.');
  if (directTarget) {
    await activateChatGptSession(port, { targetId: directTarget.id });
    return {
      target: directTarget,
      room: null,
      roomTarget: {
        ...finishRoomTarget(baseRoomTarget({ project, selector, saved: null, expectedUrl: directTarget.url, threadMode }), directTarget, {
          resolution: "direct_target",
        }),
        durationMs: Date.now() - startedAt,
      },
    };
  }

  return { target: null, room: null, roomTarget: null };
}

export async function activateChatGptSession(port, { name, targetId } = {}) {
  const target = targetId
    ? (await listChatGptSessions(port)).find((session) => session.id === targetId)
    : await resolveChatGptSession(port, name);
  if (!target) throw new Error(`ChatGPT session not found: ${name || targetId || "(first)"}`);
  await fetch(`http://127.0.0.1:${port}/json/activate/${target.id}`);
  return target;
}

export async function closeChatGptSession(port, { name, targetId } = {}) {
  const target = targetId
    ? (await listChatGptSessions(port)).find((session) => session.id === targetId)
    : await resolveChatGptSession(port, name);
  if (!target) throw new Error(`ChatGPT session not found: ${name || targetId || "(first)"}`);
  await fetch(`http://127.0.0.1:${port}/json/close/${target.id}`);
  return target;
}

export async function connectToChatGptSession(port, selector, { allowRebind = false, conversationUrl = "" } = {}) {
  const resolved = await resolveVerifiedRoomTarget(port, selector, { allowRebind, conversationUrl });
  const target = resolved.target;
  if (!target) throw new Error(`ChatGPT session not found: ${selector || "(first)"}`);
  await activateChatGptSession(port, { targetId: target.id });
  const cdp = await CdpSession.open(target.webSocketDebuggerUrl);
  return { cdp, target, room: resolved.room, roomTarget: resolved.roomTarget };
}

function capRecentRuns(runs) {
  return runs.slice(0, RECENT_RUN_LIMIT);
}

export function recordFreshThread({ aliasHint, target, runId, receiptPath, transcriptPath } = {}) {
  const project = ensureProjectState();
  return withProjectStateLockSync({ project, reason: "record-fresh-thread" }, () => {
    const registry = readRegistry();
    const entry = {
      threadId: targetThreadId(target),
      conversationUrl: target?.url || "",
      aliasHint: aliasHint || null,
      runId: runId || null,
      receiptPath: receiptPath || null,
      transcriptPath: transcriptPath || null,
      createdAt: nowIso(),
      projectId: project.projectId,
      repoRoot: project.repoRoot,
    };
    registry.freshThreads = [entry, ...registry.freshThreads].slice(0, RECENT_RUN_LIMIT);
    writeRegistry(registry);
    return entry;
  });
}

export function recordChatGptAliasUse({ name, target, runId, receiptPath, transcriptPath } = {}) {
  if (!name) return null;
  const project = ensureProjectState();
  return withProjectStateLockSync({ project, reason: `record-alias-use:${name}` }, () => {
    const registry = readRegistry();
    const saved = registry.rooms[name];
    if (!saved) return null;
    if (saved.projectId !== project.projectId) throw mismatchError(name, saved, project);
    const timestamp = nowIso();
    const activeThreadId = target ? targetThreadId(target) : saved.activeThreadId;
    const activeConversationUrl = target?.url || saved.activeConversationUrl || saved.conversationUrl || saved.url || "";
    const recentRun = {
      runId: runId || saved.lastRunId || null,
      receiptPath: receiptPath || saved.lastReceiptPath || null,
      transcriptPath: transcriptPath || saved.lastTranscriptPath || null,
      createdAt: timestamp,
    };
    const lineage = saved.lineage.map((entry) => entry.threadId === activeThreadId
      ? {
          ...entry,
          lastRunId: runId || entry.lastRunId || null,
          firstRunId: entry.firstRunId || runId || null,
          lastReceiptPath: receiptPath || entry.lastReceiptPath || null,
        }
      : entry);
    registry.rooms[name] = {
      ...saved,
      targetId: target?.id || saved.targetId || null,
      activeThreadId,
      activeConversationUrl,
      conversationUrl: activeConversationUrl,
      url: activeConversationUrl,
      title: target?.title || saved.title || "",
      lastUsedAt: timestamp,
      updatedAt: timestamp,
      lastRunId: runId || saved.lastRunId || null,
      lastReceiptPath: receiptPath || saved.lastReceiptPath || null,
      lastTranscriptPath: transcriptPath || saved.lastTranscriptPath || null,
      callCount: Number(saved.callCount || 0) + 1,
      recentRuns: capRecentRuns([recentRun, ...(saved.recentRuns || [])]),
      lineage,
    };
    writeRegistry(registry);
    return registry.rooms[name];
  });
}

// A verified first prompt establishes room identity before generation finishes.
// It does not increment completed-call counters or certify a final response.
export function recordChatGptPromptBinding({name,target,runId,receiptPath}={}) {
  if(!name||!target?.id||!conversationIdFromUrl(target.url))throw roomError('room.prompt_binding_requires_committed_identity','A verified prompt needs an exact committed target.');
  const project=ensureProjectState();
  return withProjectStateLockSync({project,reason:`record-prompt-binding:${name}`},()=>{
    const registry=readRegistry(),saved=registry.rooms[name];
    if(!saved||saved.projectId!==project.projectId||saved.targetId!==target.id)throw roomError('room.prompt_binding_target_changed','Reconcile the original role before recording its prompt.');
    registry.rooms[name]={...bindRoomToTarget({room:saved,name,target,project,openedReason:'first verified prompt',archivePrevious:true}),
      lastPromptBinding:{runId,receiptPath,at:nowIso(),scope:'PROMPT_VERIFIED_NOT_RESPONSE_COMPLETION'}};
    writeRegistry(registry);return registry.rooms[name];
  });
}
