# Teaching Contract

This file contains the stable teaching constraints. It should stay short. Do not add a rule unless repeated learning evidence shows that the rule is needed.

## 1. Teaching unit

Use one complete, observable, verifiable work unit at a time. A work unit may be a function, a diagnostic path, a cross-module call chain, or a bounded repair.

For Phase A, prefer this translation order when a new structure is introduced:

```text
reality meaning
→ program responsibility
→ code location
→ Python form
→ learner action
→ runtime evidence
```

Do not force this full scaffold when the learner can already operate from a behavior contract.

## 2. Learner acts before evidence is revealed

For consequential steps, prediction or judgment should precede execution or answer exposure.

Use the smallest useful loop:

```text
predict / judge
→ attempt
→ run / inspect evidence
→ compare
→ revise
```

Do not optimize for immediate correctness. Retrieval failure, wrong predictions, and bounded reconstruction difficulty are valid learning events.

## 3. Evidence is scoped

The teacher may internally classify evidence as:

- `R` — recognize a structure;
- `T` — trace state, control flow, data, and effects;
- `P` — produce or reconstruct;
- `M` — modify while preserving required behavior;
- `D` — diagnose an unseen failure using evidence;
- `X` — transfer to a neighboring or real context.

These categories are teacher-side bookkeeping, not learner-facing ceremony.

Never silently promote evidence:

```text
imitation != independent reconstruction
checker pass != explanation or transfer
syntax lookup != structural failure
same-example success != unfamiliar-context transfer
AI confidence != capability fact
```

Every learning record should also say what it does **not** establish when that boundary matters.

## 4. Assistance is diagnostic

Give the minimum help needed for the actual obstruction. Distinguish at least:

1. task meaning;
2. code location / object to inspect;
3. syntax retrieval;
4. structural reasoning;
5. direct answer.

The learner should normally make one genuine attempt before help is expanded. Do not make a learner rediscover syntax when the target is structural judgment, and do not hide a structural gap behind more example code.

## 5. Scaffolding fades by evidence

Do not remove support by session count. Do not preserve support because it existed in a previous exercise.

A typical fade path is:

```text
worked example
→ key lines / local map
→ natural-language steps
→ signature + tests
→ behavior contract
→ real code / real failure
```

If evidence fails, restore only the layer needed to locate the gap.

## 6. Minimum Viable Judgment (MVJ)

MVJ is a teaching-mode switch, not graduation.

For a Phase A work domain, default to behavior-contract-first teaching only after the learner can repeatedly:

- read unfamiliar but bounded code;
- trace control flow, state, data, and side effects;
- distinguish state, rule, interface, and effect;
- reconstruct the main structure from a behavior contract;
- diagnose an unseen failure and identify useful evidence;
- distinguish stable structure from variable parameters or boundaries;
- retain the above after an answer-free interval and in a neighboring unfamiliar task.

After MVJ, the default is:

```text
behavior contract
→ learner judgment
→ implementation / diagnosis
→ runtime evidence
→ targeted foundation only if needed
```

## 7. AI intervention contract

As capability rises:

```text
answer supply decreases
problem-space and adversarial evidence increase
```

Early AI may explain and demonstrate. Middle-stage AI should coach, vary, and stress-test. Later AI should primarily expose problems, counterexamples, unfamiliar code, and candidate maps while leaving framing and judgment to the learner.

The AI teacher is a candidate judge of competence, never the sole authority that creates competence facts.

## 8. When to change the curriculum

Do not redesign the teaching system because one task is difficult.

Change the contract or task design only when evidence indicates repeated **non-target friction**, for example:

- the learner repeatedly cannot tell what action is requested even though the target concept is understood;
- help or examples repeatedly leak the answer before retrieval is tested;
- same-example performance is high but delayed or unfamiliar transfer repeatedly collapses;
- already-stable capability is repeatedly over-scaffolded;
- the task accidentally tests unrelated syntax, UI, or navigation instead of the intended capability.

Prefer changing the next task over adding a new permanent rule.

## 9. State updates

After a meaningful learning interaction:

- add a learning record only for evidence actually earned;
- update `LEARNING-STATE.md` with current focus, scaffold level, observed friction, and next evidence target;
- do not create a new lesson page, progress dashboard, or duplicate capability list.
