export const now = () => performance.now();
export const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export async function listTargets(port, { timeoutMs = 5000 } = {}) {
  const response = await fetch(`http://127.0.0.1:${port}/json`, { signal: AbortSignal.timeout(timeoutMs) });
  if (!response.ok) throw new Error(`CDP /json -> ${response.status}`);
  return response.json();
}

export async function connectToPage(port, { matchUrl, retries = 30, delayMs = 100 } = {}) {
  let lastError;
  let inspected = false;
  for (let attempt = 0; attempt < retries; attempt++) {
    try {
      const targets = await listTargets(port);
      inspected = true;
      const pages = targets.filter((target) => target.type === "page" && target.webSocketDebuggerUrl);
      const target =
        matchUrl ? pages.find((page) => (page.url || "").startsWith(matchUrl)) : pages[0];
      if (target) return await CdpSession.open(target.webSocketDebuggerUrl);
    } catch (error) {
      lastError = error;
      // Chrome may still be starting; retry below.
    }
    await sleep(delayMs);
  }
  const error = new Error(inspected ? "No matching inspectable page target. Run browser warm first." : "Cannot reach or inspect the CDP endpoint.");
  error.errorCode = inspected ? "browser.target_unavailable" : "browser.cdp_unreachable";
  error.cause = lastError;
  throw error;
}

export async function evaluate(cdp, expression, options = {}) {
  const { result, exceptionDetails } = await cdp.send("Runtime.evaluate", {
    expression,
    returnByValue: true,
    awaitPromise: true,
  }, options);
  if (exceptionDetails) {
    throw new Error(
      exceptionDetails.exception?.description || exceptionDetails.text || "evaluate failed",
    );
  }
  return result.value;
}

export async function clickAt(cdp, x, y) {
  await cdp.send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y });
  await cdp.send("Input.dispatchMouseEvent", {
    type: "mousePressed",
    x,
    y,
    button: "left",
    clickCount: 1,
  });
  await cdp.send("Input.dispatchMouseEvent", {
    type: "mouseReleased",
    x,
    y,
    button: "left",
    clickCount: 1,
  });
}

export class CdpSession {
  constructor(ws, { commandTimeoutMs = 120000 } = {}) {
    this.ws = ws;
    this.commandTimeoutMs = positiveTimeout(commandTimeoutMs);
    this.closed = false;
    this.nextId = 1;
    this.pending = new Map();
    this.listeners = new Map();
    this.messageHandler = (event) => this.#onMessage(event);
    this.closeHandler = () => this.#terminate(cdpError('browser.cdp_closed', 'CDP connection closed'));
    this.errorHandler = () => this.#terminate(cdpError('browser.cdp_socket_error', 'CDP socket failed'));
    ws.addEventListener('message', this.messageHandler);
    ws.addEventListener('close', this.closeHandler);
    ws.addEventListener('error', this.errorHandler);
  }

  static open(wsUrl, { timeoutMs = 10000, commandTimeoutMs = 120000, signal, WebSocketImpl = globalThis.WebSocket } = {}) {
    positiveTimeout(timeoutMs); positiveTimeout(commandTimeoutMs);
    if (signal?.aborted) return Promise.reject(cdpError('browser.cdp_aborted', 'CDP connection cancelled'));
    return new Promise((resolve, reject) => {
      const ws = new WebSocketImpl(wsUrl);
      let settled = false;
      const cleanup = () => { clearTimeout(timer); ws.removeEventListener('open', opened); ws.removeEventListener('close', closed); ws.removeEventListener('error', failed); signal?.removeEventListener('abort', aborted); };
      const fail = (error) => { if (settled) return; settled = true; cleanup(); try { ws.close(); } catch {} reject(error); };
      const opened = () => { if (settled) return; settled = true; cleanup(); resolve(new CdpSession(ws, { commandTimeoutMs })); };
      const closed = () => fail(cdpError('browser.cdp_closed', 'CDP closed before connecting'));
      const failed = () => fail(cdpError('browser.cdp_socket_error', 'CDP connection failed'));
      const aborted = () => fail(cdpError('browser.cdp_aborted', 'CDP connection cancelled'));
      const timer = setTimeout(() => fail(cdpError('browser.cdp_connect_timeout', 'CDP connection timed out')), timeoutMs);
      ws.addEventListener('open', opened); ws.addEventListener('close', closed); ws.addEventListener('error', failed);
      signal?.addEventListener('abort', aborted, { once: true });
      if (signal?.aborted) aborted();
    });
  }

  send(method, params = {}, { timeoutMs = this.commandTimeoutMs, signal } = {}) {
    if (this.closed) return Promise.reject(cdpError('browser.cdp_closed', 'CDP session is closed'));
    if (signal?.aborted) return Promise.reject(cdpError('browser.cdp_aborted', 'CDP command cancelled before send'));
    positiveTimeout(timeoutMs);
    const id = this.nextId++;
    return new Promise((resolve, reject) => {
      const finish = (error, result) => {
        if (!this.pending.has(id)) return;
        this.pending.delete(id); clearTimeout(timer); signal?.removeEventListener('abort', aborted);
        if (error) reject(error); else resolve(result);
      };
      const aborted = () => finish(cdpError('browser.cdp_aborted', 'CDP command cancelled; remote outcome may be unknown'));
      const timer = setTimeout(() => finish(cdpError('browser.cdp_command_timeout', 'CDP command timed out; remote outcome may be unknown')), timeoutMs);
      this.pending.set(id, { resolve: result => finish(null, result), reject: error => finish(error) });
      signal?.addEventListener('abort', aborted, { once: true });
      if (signal?.aborted) { aborted(); return; }
      try { this.ws.send(JSON.stringify({ id, method, params })); }
      catch (error) { finish(cdpError('browser.cdp_send_failed', String(error.message))); }
    });
  }

  on(method, handler) {
    if (!this.listeners.has(method)) this.listeners.set(method, new Set());
    this.listeners.get(method).add(handler);
    return () => this.listeners.get(method)?.delete(handler);
  }

  async close() {
    this.#terminate(cdpError('browser.cdp_closed', 'CDP session closed by caller'));
  }

  #terminate(error) {
    if (this.closed) return;
    this.closed = true;
    this.ws.removeEventListener('message', this.messageHandler);
    this.ws.removeEventListener('close', this.closeHandler);
    this.ws.removeEventListener('error', this.errorHandler);
    for (const entry of [...this.pending.values()]) entry.reject(error);
    this.listeners.clear();
    try {
      this.ws.close();
    } catch {
      // Already closed.
    }
  }

  #onMessage(event) {
    let message;
    try {
      message = JSON.parse(typeof event.data === "string" ? event.data : event.data.toString());
    } catch {
      return;
    }

    if (message.id && this.pending.has(message.id)) {
      const { resolve, reject } = this.pending.get(message.id);
      if (message.error) reject(new Error(`${message.error.message} (code ${message.error.code})`));
      else resolve(message.result);
      return;
    }

    if (!message.method) return;
    const handlers = this.listeners.get(message.method);
    if (handlers) for (const handler of [...handlers]) handler(message.params);
  }
}

function positiveTimeout(value) {
  if (!Number.isInteger(value) || value < 1 || value > 2147483647) throw new Error('CDP timeout must be a positive bounded integer');
  return value;
}
function cdpError(code, message) {
  const error = new Error(message); error.errorCode = code;
  // Transport cancellation/disconnection is never evidence that a remote action did not execute.
  error.remoteOutcome = 'unknown'; error.automaticResendAllowed = false;
  return error;
}
