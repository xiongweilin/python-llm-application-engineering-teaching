# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 14 retained learning records. They currently support experience with:

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
- independently reconstructing a simple `for` loop in a neighboring context.

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

In the neighboring loop task, the learner independently created `wait_times = [2, 4, 8]`, iterated with `for wait_time in wait_times:`, printed the loop variable inside the indented body, printed `complete` after the loop, predicted and observed the exact output, and explained the three loop-variable values and the inside/outside indentation boundary. This is retained as scoped independent reconstruction evidence.

The current syntax unit is explicit exception creation with `raise`. Its worked example, near imitation, and controlled true/false condition variation have all succeeded.

The neighboring `raise` task was also reconstructed correctly from natural-language requirements: the learner independently wrote `age = -1`, guarded `raise ValueError("age cannot be below zero")` with `if age < 0:`, placed `print("accepted")` after the block, correctly predicted an uncaught exception with no `accepted` output, and supplied the matching traceback. The learner also correctly predicted that changing `age` to `5` would make the condition false, skip the `raise`, and allow the print to execute.

However, when asked which source line actually creates the exception, the learner answered that the `if` condition does. This is the remaining conceptual attribution gap: `if` decides whether execution reaches the block; the `raise ValueError(...)` statement itself creates/raises the exception. Do not promote this neighboring task to a retained learning record until that distinction is restated correctly without a template.

Before returning to bounded retry, introduce the remaining syntax needed by retry code one small unit at a time.

Likely remaining prerequisites:

```text
exceptions and `raise`
→ `try` / `except`
→ passing a function as a value / callback boundary
```

Do not introduce all of these in one exercise.

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
- `raise` syntax can now be produced in a neighboring task and both the raised and skipped paths are traced correctly, but one conceptual distinction must still be fixed before retaining the skill: `if` controls reachability; `raise` creates the exception.
- Reinforce the distinction between “the condition was false so `raise` never executed” and “an exception was raised and then handled.” The latter has not yet been introduced.
- Do not re-teach already stable forms from scratch unless friction reappears, but keep correcting terminology when useful.
- Introduce genuinely new syntax before using it as part of a structural assessment.
- For a new syntax form, prefer: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring use.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors should be treated as observable evidence to inspect, not hidden from the learner.
- When an uncaught exception occurs, distinguish statements executed before the failing line from statements that appear later in the file and therefore never run.
- A function call returns a value; assignment stores that value; `for` iterates/binds values; indentation determines block membership; `raise` explicitly creates/propagates an exception; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Run one minimal attribution check with no new syntax: given an `if` guarding `raise ValueError(...)`, the learner should state that the `if` decides whether execution reaches the block and the `raise` statement itself creates the exception. If stated correctly, retain the neighboring `raise` reconstruction as a learning record, treat explicit `raise` as sufficiently stable for the current prerequisite purpose, and introduce `try` / `except` with a worked example.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. The simple function, list/indexing, and bounded-repetition sequences have each reached one neighboring independent reconstruction.

One execution-order mistake appeared during the list-boundary experiment: the learner initially expected `print` statements located after an uncaught exception to execute. This was corrected after reading the real traceback. The explicit-`raise` tasks now show correct source-order reasoning on both true and false condition paths.

A narrower terminology/control-flow attribution issue remains: the learner can write and run the correct `if` + `raise` structure, but most recently attributed exception creation to the `if` line rather than to `raise`. Resolve this with one direct contrast before introducing `try` / `except`.

## Unknowns to resolve from live interaction

- whether the learner can cleanly distinguish the role of `if` from the role of `raise` without a template;
- `try` / `except` syntax and control flow;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
