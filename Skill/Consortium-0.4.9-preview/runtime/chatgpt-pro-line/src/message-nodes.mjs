// Serialized into the page: no hidden-text reads, sidebar fallback or text-based deduplication.
export function conversationMessageNodes() {
  const root = document.querySelector?.('main') || document;
  const role = e => e.getAttribute('data-message-author-role')
    || (e.hasAttribute('data-user-message-bubble') ? 'user'
      : e.getAttribute('data-markdown-text-style') === 'assistant-message' ? 'assistant' : '');
  const nodes = [...new Set([
    ...root.querySelectorAll('[data-message-author-role]'),
    ...root.querySelectorAll('[data-user-message-bubble], [data-markdown-text-style="assistant-message"]'),
  ])].filter(e => {
    if (!['user', 'assistant'].includes(role(e))) return false;
    if (typeof e.getBoundingClientRect !== 'function') return true; // minimal offline DOM fixtures
    const r = e.getBoundingClientRect(), s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.display !== 'none' && s.visibility !== 'hidden';
  });
  // Legacy role wrappers can contain modern markers for the SAME turn.
  const outer = nodes.filter(e => !nodes.some(p => p !== e && role(p) === role(e) && p.contains?.(e)));
  return outer.sort((a, b) => {
    const order = a.compareDocumentPosition?.(b) || 0;
    return order & 2 ? 1 : order & 4 ? -1 : 0;
  });
}
