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

The bounded-repetition sequence with `for` has completed for the current prerequisite purpose.

The explicit-exception sequence with `raise` has completed for the current prerequisite purpose, including one neighboring independent reconstruction and an explicit role distinction between `if` reachability and `raise` exception creation.

The current syntax unit is `try` / `except`. Its first worked example was manually typed and run:

```python
try:
    raise ValueError("invalid value")
except ValueError:
    print("caught")

print("continued")
```

The learner observed the actual output `caught` then `continued` with no traceback. However, the pre-run prediction expected a traceback, and the post-run explanation incorrectly said the `raise` did not really produce an exception. The learner correctly recognized that `except ValueError` catches the exception and prints `caught`, but attributed `continued` mainly to being unindented. The missing causal distinction is that the exception genuinely occurs, matching `except` handles it, and therefore control can continue after the `try` / `except`; being outside the block only describes block membership and does not by itself guarantee the line will be reached.

The latest `TEACHING-CONTRACT.md` §2 now includes a conditional `Distinction judgment` specialization for tasks that depend on classification, representation, or boundary choice. Apply that specialization here because the present gap is exactly a consequential distinction problem. Do not turn it into a learner-facing ritual for unrelated tasks.

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
- `raise ValueError(...)` guarded by an `if` is sufficiently stable for the current prerequisite purpose, including one neighboring independent reconstruction.
- `try` / `except ValueError:` has only one worked-example run so far; do not assume even basic control-flow understanding yet.
- Before more imitation, use a minimal distinction judgment because current errors concern classification of three materially different states: exception never raised, exception raised and handled, exception raised and unhandled.
- Keep another distinction explicit: block membership / indentation is not the same as reachability. A statement outside a block still will not run if earlier unhandled control flow prevents reaching it.
- Introduce genuinely new syntax before using it as part of a structural assessment.
- For a new syntax form, prefer: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring use, but insert a targeted judgment check when the evidence shows a consequential classification gap.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors should be treated as observable evidence to inspect, not hidden from the learner.
- A function call returns a value; assignment stores that value; `for` iterates/binds values; indentation determines block membership; `raise` explicitly creates/propagates an exception; matching `except` handles a raised exception and changes the subsequent control path; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Use the §2 conditional distinction-judgment specialization on three tiny traces with no new syntax:

1. an exception is raised and unhandled;
2. an exception is raised inside `try` and handled by matching `except`;
3. a guarded `raise` is skipped because its `if` condition is false.

For each, ask the learner to judge whether a `ValueError` actually occurs, whether an `except` block runs, whether a traceback appears, and whether later code is reached. Then ask which distinctions must be retained because they change observable behavior. Only after these classifications are reliable should the course return to `try` / `except` imitation and controlled variation.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. The simple function, list/indexing, bounded-repetition, and explicit-`raise` sequences have each reached one neighboring independent reconstruction.

The first `try` / `except` worked example exposed a new target-specific control-flow gap. The learner expected a traceback even with matching `except`, then after seeing `caught` / `continued` said the `raise` had not actually produced an exception. This indicates the learner is currently compressing “no traceback” into “no exception happened,” which is not a safe compression because handled and non-raised paths have different control-flow meaning.

A second attribution issue appeared in explaining `continued`: the learner used indentation as the main cause. Indentation correctly marks that `print("continued")` is outside the `try` / `except`, but actual execution still depends on whether control reaches it. Reinforce membership versus reachability.

Use the new distinction-judgment specialization only because these differences change prediction, explanation, and control-flow behavior.

## Unknowns to resolve from live interaction

- whether the learner can reliably distinguish exception-never-raised, raised-and-handled, and raised-unhandled paths;
- `try` / `except` syntax production and transfer after the distinction stabilizes;
- whether the learner can distinguish block membership from runtime reachability;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
