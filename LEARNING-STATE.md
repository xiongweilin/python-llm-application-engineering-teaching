# Learning State

This file is the small, current state used to resume live teaching. It is provisional and should be updated from performance evidence, not from page completion.

## Current phase

Phase A — Python and real-system code ownership.

## Earned evidence

There are 12 retained learning records. They currently support experience with:

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
- independently reconstructing one simple Python function structure in a neighboring context.

These records are scoped evidence. They do not imply independent mastery of all related Python syntax or unfamiliar project diagnosis.

## Current focus

Build the minimum Python execution and syntax baseline needed to return to bounded-retry reconstruction without mixing syntax friction into the structural assessment.

The initial novice sequence for variables, functions, comparison, return values, calls, assignment, and `print` has completed successfully:

```text
worked example
→ manual typing
→ imitation
→ controlled boundary variation
→ neighboring reconstruction without a visible template
```

The neighboring task (`needs_heating`) was reconstructed correctly from natural-language requirements. The learner predicted `True`, observed `True`, and explained the execution path as variables → function definition → function call → comparison → returned value → assignment → printed output. This is retained as scoped independent reconstruction evidence.

The current syntax unit is Python list values and zero-based indexing. Its worked example was completed under full scaffold: the learner manually ran a list containing `1, 2, 4`, predicted and observed the three outputs correctly, explained `delays[0]` as retrieving the first list element, and explained that the third element is at index `2` because indexing starts at zero.

The list imitation step also succeeded. While allowed to inspect the worked example, the learner independently wrote `response_times = [3, 6, 9]`, retrieved the values with indices `[0]`, `[1]`, and `[2]`, predicted and observed `3`, `6`, and `9`, and correctly explained the mapping between zero-based indices and the first, second, and third elements. Treat this as imitation evidence, not yet neighboring independent list reconstruction.

Before returning to bounded retry, introduce the remaining syntax needed by retry code one small unit at a time, using the same sequence when a form is genuinely new. Likely prerequisites include:

```text
list values / indexing
→ repetition (`for` or another bounded loop form)
→ exceptions and `raise`
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
- List literal and zero-based indexing have now been introduced, traced, and reproduced in one near imitation; do not yet assume neighboring independent production.
- Do not re-teach already stable forms from scratch unless friction reappears, but keep correcting terminology when useful.
- Introduce genuinely new syntax before using it as part of a structural assessment.
- For a new syntax form, prefer: explicit worked example → learner manually types it → imitation → one controlled variation → neighboring use.
- Syntax lookup is allowed.
- Do not treat transcription or imitation as independent reconstruction evidence.
- Runtime errors should be treated as observable evidence to inspect, not as something to hide from the learner. When introducing an error type, first let the learner predict the failure, then run it, then read the traceback from the bottom upward: exception type/message, failing line, then local cause.
- A function call returns a value; assignment stores that value; `print` produces terminal output.
- Add another tool only when it has a concrete learning or engineering purpose, and explain that purpose before requiring it.
- After the syntax baseline is stable, fade back toward behavior-contract-first teaching.

## Next evidence target

Run one controlled list-index boundary variation: access index `[3]` in a three-element list, predict what kind of failure should occur without requiring the exact Python exception name, then inspect the real traceback. The learner should identify that valid indices are `0`, `1`, and `2`, locate the failing source line, and connect the bottom-line error message to the invalid index. After that, ask for one neighboring list task without a full template before moving to bounded repetition.

## Observed friction

The original bounded-retry reconstruction task mixed the intended retry-structure target with unknown editor/runtime and Python-syntax requirements. Treat that as non-target friction, not structural retry failure.

That runtime obstruction is removed. No significant syntax failure appeared in the simple function sequence. One terminology issue was corrected during the sequence: the result variable does not call the function; the function call happens first, its returned value is assigned, and `print` later produces terminal output.

No new friction appeared in the list worked example or list imitation. The learner correctly reasons about zero-based indexing. The next uncertainty is whether the learner can use a real out-of-range traceback as evidence rather than only reason about successful accesses.

## Unknowns to resolve from live interaction

- valid list-index boundary and ability to interpret the resulting runtime error;
- list literal and indexing production in a neighboring task without a complete template;
- bounded repetition syntax and traceability;
- exception, `raise`, and `try` / `except` syntax;
- passing and calling function values as arguments;
- whether retry structure can later be reconstructed without a worked example;
- whether the learner can independently locate the stopping condition and side-effect boundary;
- delayed retention and transfer distance.

Do not add new teaching-system complexity to answer these unknowns. Resolve them with tasks and runtime evidence first.
