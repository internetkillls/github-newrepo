# Live validation

The first consultation was actually submitted; the legacy message selector produced a false failure. Modern message selectors recovered one exact user prompt, two sent attachments and three assistant responses. URL: https://chatgpt.com/c/6acc981b-bf1c-83ec-9b49-3cad8b6e5a92 . GPT-6.1 Sol/high confirmed. Completion was not inferred from progress text.

Five-worker support uses persistent distinct Chrome rooms. Calls are serialized by the browser lock; simultaneous generation is not established. Spawn retains successful bindings on partial failure, reuses recorded roles on repeat, and rejects duplicate roles or more than five workers.
