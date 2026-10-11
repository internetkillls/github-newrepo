# Closure and merge contract

## Closure quality classes

```text
DRAFT          worker-produced, unchecked
WITNESSED      one independent evidence/runtime witness passed
CROSS-CHECKED  independent reconstruction/audit agrees within stated scope
CANONICAL      merge gate accepts for downstream use
STALE          upstream evidence/state changed
INVALID        defeated or provenance-broken
```

Canonical is local to case/scope/version. It never means permanently true.

## Merge input

Every merge receives:
- closure packets;
- independence classes;
- provenance and version refs;
- explicit contradiction/overlap map;
- unresolved debts;
- merge criterion.

## Merge outputs

```text
CANONICAL-CLOSURE
PARALLEL-CLOSURES
REOPEN-REQUEST
NON-COMPARABILITY
UNRESOLVED-APORIA
```

A polished synthesis is not itself a merge verdict.
