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

The current syntax unit is explicit exception creation with `raise`. Its first worked example has now been completed under full scaffold. With `temperature = -3` and `if temperature < 0: raise ValueError("temperature cannot be below zero")`, the learner correctly predicted that an exception would be raised and that the later `print("accepted")` would not execute. The supplied traceback showed the failing `raise` line and `ValueError: temperature cannot be below zero`. The learner explained that the final traceback line contains the exception type plus its message and distinguished `raise` from `print`: `raise` creates an exception and can stop normal control flow when uncaught, whereas `print` only produces output. Correct one nuance when needed: `raise` is not magically tied to a pre-existing error condition; it executes whenever control reaches that statement. In this example the surrounding `if` controls whether control reaches it.

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
- `raise` with a built-in `ValueError` has been introduced, traced, and connected to a real traceback under one complete worked example; do not yet assume independent production.
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

Obtain one near imitation of `if` + `raise ValueError(...)` in a neighboring validation scenario while the learner may inspect the worked example. Then run one controlled variation in which the condition is false so the `raise` statement is skipped and a later `print` executes. Do not introduce `try` / `except` until the learner can explain that reaching `raise` creates the exception and not reaching it means normal execution continues.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. The simple function, list/indexing, and bounded-repetition sequences have each reached one neighboring independent reconstruction.

One execution-order mistake appeared during the list-boundary experiment: the learner initially expected `print` statements located after an uncaught exception to execute. This was corrected after reading the real traceback. The first explicit-`raise` example showed correct source-order reasoning: the learner predicted the later `print` would not run.

One terminology nuance remains worth reinforcing: the learner described `raise` as something that executes “when an exception is found.” More precisely, `raise` itself creates/raises the exception whenever execution reaches that statement; the surrounding condition decides whether that line is reached.

## Unknowns to resolve from live interaction

- independent `raise` syntax production and transfer;
- whether the learner can distinguish “condition false, so `raise` is skipped” from “an exception happened but was ignored”;
- `try` / `except` syntax and control flow;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
