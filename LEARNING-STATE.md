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

The initial novice sequence for variables, functions, comparison, return values, calls, assignment, and `print` has completed successfully.

The list/indexing sequence has completed for the current prerequisite purpose, including a real `IndexError` traceback and one neighboring independent reconstruction.

The bounded-repetition sequence with `for` has also completed for the current prerequisite purpose:

```text
worked example
→ manual typing
→ imitation
→ controlled indentation variation
→ neighboring reconstruction without a visible template
```

The explicit-exception sequence with `raise` has now completed for the current prerequisite purpose:

```text
worked example
→ manual typing
→ imitation
→ controlled true/false condition variation
→ neighboring reconstruction without a visible template
→ minimal role-attribution check
```

In the neighboring `raise` task, the learner independently created `age = -1`, guarded `raise ValueError("age cannot be below zero")` with `if age < 0:`, placed `print("accepted")` after the block, correctly predicted and observed the uncaught exception, and correctly predicted the false-condition path where `raise` is skipped and `accepted` prints. After one direct role check, the learner also cleanly stated that the `if` condition decides whether execution reaches the branch while the `raise` statement itself creates the `ValueError`. This is retained as scoped independent reconstruction evidence.

The next new syntax unit is `try` / `except`: handling an exception after it has actually been raised, rather than merely skipping a `raise` statement through control flow.

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
- Basic independent production is observed for literals, variable assignment, `def`, two parameters, `if`, `<`, `return`, function call, assignment of the returned value, and `print`.
- List literals and zero-based indexing are sufficiently stable for the current prerequisite purpose.
- `for` iteration, loop-variable binding, and indentation-based loop-body membership are sufficiently stable for the current prerequisite purpose, including one neighboring independent reconstruction.
- `raise ValueError(...)` guarded by an `if` is sufficiently stable for the current prerequisite purpose, including one neighboring independent reconstruction and explicit separation of `if` reachability from `raise` exception creation.
- Do not re-teach already stable forms from scratch unless friction reappears, but keep correcting terminology when useful.
- Introduce genuinely new syntax before using it as part of a structural assessment.
- For a new syntax form, prefer: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring use.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors should be treated as observable evidence to inspect, not hidden from the learner.
- When an uncaught exception occurs, distinguish statements executed before the failing line from statements that appear later in the file and therefore never run.
- Keep the distinction explicit: a false `if` condition means `raise` never executed; `try` / `except` will introduce the different case where an exception really is raised and then handled.
- A function call returns a value; assignment stores that value; `for` iterates/binds values; indentation determines block membership; `raise` explicitly creates/propagates an exception; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Introduce `try` / `except ValueError:` as a genuinely new syntax form with one tiny worked example. Put a known `raise ValueError(...)` inside the `try` block, handle it in the `except` block with a simple `print`, then place another unindented `print` after the whole structure. The learner should manually type it, predict the exact output, run it, and explain that the exception really occurs, transfers control to the matching `except`, and then normal execution continues after the handled block. Do not combine this first `try` / `except` example with loops, retries, or callbacks.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. The simple function, list/indexing, bounded-repetition, and explicit-`raise` sequences have each now reached one neighboring independent reconstruction.

One execution-order mistake appeared during the list-boundary experiment: the learner initially expected `print` statements located after an uncaught exception to execute. This was corrected after reading the real traceback. The later explicit-`raise` tasks show correct source-order reasoning on both raised and skipped paths.

A narrower role-attribution issue appeared in the neighboring `raise` task: the learner initially said the `if` line produced the exception. A direct contrast resolved this; the learner now states that `if` decides reachability and `raise` produces the `ValueError`. Treat that issue as resolved unless it reappears.

## Unknowns to resolve from live interaction

- `try` / `except` syntax and control flow;
- whether the learner can distinguish “exception never raised” from “exception raised and handled” in execution traces;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
