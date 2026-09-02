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

The current syntax unit is `try` / `except`.

The first worked example exposed a consequential distinction gap: the learner initially equated “no traceback” with “no exception happened.” The §2 conditional `Distinction judgment` specialization was then applied to three traces: raised/unhandled, raised/handled, and never-raised. The learner classified all three correctly and stated that “an exception happened but was caught” cannot be compressed into “no exception happened.”

The near-imitation step has now also succeeded syntactically and behaviorally. The learner independently wrote:

```python
try:
    raise ValueError("invalid stock")
except ValueError:
    print("handled")

print("continued")
```

They correctly predicted and observed `handled` then `continued`, correctly predicted no traceback, correctly explained that `continued` is outside the `try` / `except` block and is reachable because the exception is handled, and correctly explained that matching `except ValueError:` suppresses the uncaught traceback path.

One conceptual attribution gap reappeared in the same imitation: when asked whether the `ValueError` really occurred, the learner answered “no, because it was caught.” Correct this explicitly: `raise ValueError(...)` really does create the exception; the matching `except` handles that already-raised exception. Treat the distinction-judgment result as promising but not yet robust under syntax production. Do not promote this imitation to independent reconstruction evidence.

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
- `try` / `except ValueError:` now has one worked-example run, one targeted distinction-judgment check, and one successful near imitation; do not yet assume neighboring independent production.
- Matching `except` handles an exception that really occurred; no traceback does not imply no exception.
- Keep three materially different states separate: never raised; raised and handled; raised and unhandled.
- Block membership / indentation is not the same as runtime reachability.
- Introduce genuinely new syntax before structural assessment.
- For a new syntax form, prefer: explicit worked example → manual typing → imitation → one controlled variation → neighboring use, inserting a targeted judgment check only when evidence shows a consequential classification gap.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors are observable evidence to inspect.
- Add another tool only when it has a concrete learning or engineering purpose and explain that purpose first.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Use one controlled variation with no new syntax in which the `try` block completes normally without any `raise`. Ask the learner to predict that the `except ValueError:` block is skipped, no traceback appears, and later code still runs. Explicitly compare this never-raised path with the previous raised-and-handled path. If the learner can state that the observable no-traceback outcome is shared while the internal control flow differs, then ask for one neighboring `try` / `except` task without a full template.

## Observed friction

The original bounded-retry reconstruction mixed retry structure with unknown runtime/editor/Python syntax; treat that as non-target friction.

One earlier execution-order error around uncaught exceptions was corrected with traceback evidence. The explicit-`raise` sequence later stabilized raised versus skipped paths.

The first `try` / `except` example exposed the compression “no traceback means no exception.” A targeted distinction-judgment check corrected it in isolation, but the same compression partially reappeared during the subsequent imitation when the learner said the `ValueError` did not occur because it was caught. This is a target-specific robustness issue, not a reason to redesign the curriculum. Use one controlled contrast between never-raised and raised-and-handled before moving to neighboring production.

## Unknowns to resolve from live interaction

- whether handled-vs-never-raised remains stable during actual syntax production;
- `try` / `except` neighboring transfer;
- whether block membership remains distinct from reachability;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
