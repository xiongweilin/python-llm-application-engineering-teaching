# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 15 retained learning records. They currently support experience with:

- functions and deterministic gates;
- data scope and rule placement;
- status-driven actions;
- lock scope versus status scope;
- recovery responsibility around short transactions;
- bounded retry and time separation;
- operation identity and database uniqueness;
- locating modules by responsibility;
- method chaining and mutation;
- accumulating errors versus fail-fast control flow;
- implementing and transferring constrained state transitions;
- independently reconstructing one simple Python function structure in a neighboring context;
- independently reconstructing a simple list-plus-indexing structure in a neighboring context;
- independently reconstructing a simple `for` loop in a neighboring context;
- independently reconstructing a simple `if` + `raise ValueError(...)` validation structure in a neighboring context.

These records are scoped evidence. They do not imply independent mastery of all related Python syntax or unfamiliar project diagnosis.

## Current focus

Build the minimum Python execution and syntax baseline needed to return to bounded-retry reconstruction without mixing syntax friction into the structural assessment.

The novice sequences for simple functions, list/indexing, `for`, and explicit `raise` have each reached one neighboring independent reconstruction for the current prerequisite purpose.

The current syntax unit is `try` / `except`. Its first worked example was manually typed and run:

```python
try:
    raise ValueError("invalid value")
except ValueError:
    print("caught")

print("continued")
```

The learner observed `caught` then `continued` with no traceback, but initially compressed “no traceback” into “no exception happened” and attributed `continued` mainly to being unindented.

Because this was a consequential classification gap, the §2 conditional `Distinction judgment` specialization was applied to three tiny traces: raised/unhandled, raised/handled, and never-raised. The learner then classified all three correctly:

- raised + unhandled: `ValueError` occurs, no `except` runs, traceback appears, later code is not reached;
- raised + handled: `ValueError` occurs, matching `except` runs, no traceback appears, later code is reached;
- never raised because a guard is false: no `ValueError` occurs, no `except` runs, no traceback appears, later code is reached.

The learner also explicitly stated that “a `ValueError` happened but was caught” cannot be compressed into the same state as “no error happened.” Treat this distinction as currently stable enough to resume syntax imitation. Keep block membership separate from runtime reachability: unindented code is outside the block, but it executes only if control reaches it.

Likely remaining prerequisites before returning to bounded retry:

```text
`try` / `except`
→ passing a function as a value / callback boundary
```

Do not introduce both in one exercise.

The later retry target remains:

```text
trace
→ reconstruct from behavior contract
→ modify one retry rule
→ diagnose an unseen retry failure
→ transfer without being told the pattern name
```

The key retry distinction remains:

```text
whether another attempt is permitted
!=
how long to wait if another attempt is permitted
```

A successful provider call, a candidate delay value, and an actually executed wait are separate events.

## Current scaffold

- Current default environment: this conversation, VS Code, and a local Python runtime.
- The learner reports Python 3.14.7 and has successfully run multiple `.py` files from the VS Code terminal.
- Basic independent production is observed for literals, assignment, `def`, parameters, `if`, `<`, `return`, calls, returned-value assignment, `print`, list indexing, simple `for`, and guarded `raise ValueError(...)`.
- `try` / `except ValueError:` has one worked-example run plus one successful distinction-judgment check; do not yet assume independent syntax production.
- Matching `except` handles an exception that really occurred; no traceback does not imply no exception.
- Block membership / indentation is not the same as runtime reachability.
- Introduce genuinely new syntax before structural assessment.
- For a new syntax form, prefer: explicit worked example → manual typing → imitation → one controlled variation → neighboring use, inserting a targeted judgment check only when evidence shows a consequential classification gap.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors are observable evidence to inspect.
- Add another tool only when it has a concrete learning or engineering purpose and explain that purpose first.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Return to the `try` / `except` novice sequence with one near imitation while the learner may inspect the worked example. Use a neighboring scenario with `raise ValueError(...)` inside `try`, matching `except ValueError:` printing one message, and a later unindented print. Ask for exact prediction, actual output, whether the exception really occurred, why no traceback appeared, and why later code was reachable. Then run one controlled variation before a neighboring no-template reconstruction.

## Observed friction

The original bounded-retry reconstruction mixed retry structure with unknown runtime/editor/Python syntax; treat that as non-target friction.

One earlier execution-order error around uncaught exceptions was corrected with traceback evidence. The explicit-`raise` sequence later stabilized raised versus skipped paths.

The first `try` / `except` example exposed a new target-specific compression: “no traceback” was treated as “no exception.” The conditional distinction-judgment check corrected this. No further curriculum redesign is warranted unless the distinction collapses again under variation.

## Unknowns to resolve from live interaction

- `try` / `except` syntax production and neighboring transfer;
- whether handled-vs-never-raised remains stable under variation;
- whether block membership remains distinct from reachability;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
