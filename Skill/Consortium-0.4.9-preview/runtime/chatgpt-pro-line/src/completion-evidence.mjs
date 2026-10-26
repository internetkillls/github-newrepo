/** Conservative anchored-generation completion gate.
 * An absent stop button is not itself completion evidence.
 * DOM evidence remains heuristic; on ambiguous evidence do not claim success.
 */
export class CompletionEvidence {
  constructor({ stableMs = 4000, minTerminalPolls = 3, minPollSpanMs = 1000 } = {}) {
    if (!(Number.isFinite(stableMs) && stableMs >= 1000)) throw new Error('stableMs must be >= 1000');
    this.stableMs = stableMs;
    this.minTerminalPolls = minTerminalPolls;
    this.minPollSpanMs = minPollSpanMs;
    this.lastText = '';
    this.changedAt = null;
    this.sawActive = false;
    this.polls = 0;
    this.firstCandidateAt = null;
    this.lastObserved = null;
    this.completed = false;
    this.reason = null;
  }
  observe({ at, text, active, terminal = false, bound = false, placeholder = false } = {}) {
    if (!Number.isFinite(at)) throw new Error('A monotonic poll timestamp is required');
    if (this.completed) return this.result(at);
    const value = String(text ?? '').trim();
    if (this.lastText !== value) {
      this.lastText = value;
      this.changedAt = at;
      this.polls = 0;
      this.firstCandidateAt = null;
    }
    if (active === true) this.sawActive = true;
    this.lastObserved = { at, hasResponse: Boolean(value), active, terminal, bound, placeholder };
    const stableFor = Math.max(0, at - (this.changedAt ?? at));
    const earnedTerminalEvidence = terminal || this.sawActive;
    const requiredStableMs = terminal && this.sawActive ? this.stableMs
      : terminal ? this.stableMs * 2
      : Math.max(this.stableMs * 2, 6000);
    const eligible = Boolean(bound && value && !placeholder && active === false && earnedTerminalEvidence && stableFor >= requiredStableMs);
    if (!eligible) {
      this.polls = 0;
      this.firstCandidateAt = null;
      return this.result(at);
    }
    if (this.firstCandidateAt === null) this.firstCandidateAt = at;
    this.polls++;
    if (this.polls >= this.minTerminalPolls && at - this.firstCandidateAt >= this.minPollSpanMs) {
      this.completed = true;
      this.reason = terminal ? 'anchored_terminal_controls_and_stability' : 'observed_active_then_stable_inactive';
    }
    return this.result(at);
  }
  result(at) {
    return {
      completed: this.completed,
      reason: this.reason,
      sawActive: this.sawActive,
      polls: this.polls,
      stableForMs: Math.max(0, at - (this.changedAt ?? at)),
      observed: this.lastObserved,
    };
  }
}
