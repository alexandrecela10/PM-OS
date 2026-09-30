---
name: goal-gate
description: Validate that a session's exit criteria are binary-resolvable before running any graph or review loop. Use this before /prd-graph or any multi-agent loop. Halts if any criterion is vague, compound, or unverifiable — so the evaluator has something checkable to score against. Run it with a goal file path, a PRD name, or no arguments for interactive mode.
user-invocable: true
disable-model-invocation: false
---

# /goal-gate — Pre-Run Goal Validation

When the PM types `/goal-gate`, validate that a session's exit criteria are binary-resolvable before any graph or review loop runs.

**Why this exists:** An evaluator can only score against criteria it can answer yes or no. Vague criteria ("improve the PRD", "address blockers") produce hallucinated passes. This skill locks the scoring rubric before execution, so every loop iteration has a specific reason rather than a general instruction.

---

## Quick Start

```
/goal-gate                                   → Interactive mode: build a goal file from scratch
/goal-gate outputs/prds/my-feature-goals.md → Validate an existing goal file
/goal-gate --prd control-tower               → Auto-detect goals from an existing PRD's open questions
```

---

## Context Routing

**Check first:**
1. `outputs/prds/` — look for an existing `*-goals.md` file matching the session
2. `context-library/strategy/` — confirm the work type is aligned to current priorities
3. `context-library/decisions/` — check if related decisions have already been made

---

## Workflow

### Step 1: Find or Build the Goal File

**If the PM provides a file path:**
- Read the file
- Jump to Step 2

**If the PM provides a PRD name:**
- Scan `outputs/prds/` for the PRD
- Extract its open questions and blockers
- Draft a goal file from them and show it to the PM before validating
- Ask: "Is this the right scope for this session, or do you want to adjust?"

**If no argument:**
- Ask these four questions (only these four):
  1. What PRD or document is this session working on?
  2. What are the 3–6 specific things that must be true when this session is done?
  3. What is explicitly out of scope today?
  4. What's the minimum passing bar — how many criteria must pass to advance?

- Draft a goal file in this format and confirm with the PM before validating:

```markdown
# [Work name] — session goals

Date: [today]
Work type: [prd-revision / strategy-sprint / metrics-design / etc.]
Input file: [path]
Prior state: [path to state file, or "none"]

## Exit criteria
1. [Criterion]
2. [Criterion]
3. [Criterion]

## Out of scope this session
- [Item]
- [Item]

## Passing bar
[N] of [total] criteria must pass to advance. Fewer → loop back.
```

---

### Step 2: Validate Each Criterion

For each criterion, apply the binary test: **"Can the evaluator answer this yes or no by checking whether ___?"**

Score each criterion:

| Status | Meaning |
|---|---|
| ✓ Binary | The evaluator can check it directly — no interpretation needed |
| ~ Rewrite needed | The criterion is real but needs to be made specific |
| ✗ Remove | The criterion is untestable in principle (opinion, tone, "feel") |

**Common failure modes and fixes:**

| Failing criterion | Problem | Fix |
|---|---|---|
| "Improve the tone" | Subjective — evaluator can't score it | Remove or rewrite: "The recommendation section uses no hedging words (maybe, consider, perhaps)" |
| "Address the blockers" | Compound — which blockers? | Split: one criterion per named blocker |
| "The PRD is clearer" | Comparative with no baseline | Remove or rewrite: "Every open question has a named owner and a proposed action" |
| "Stakeholders are considered" | Vague — which stakeholders, which consideration | Rewrite: "The legal section names a specific next step and who owns it" |
| "Better than before" | No observable test | Remove — "better" requires a comparison the evaluator can't make |

---

### Step 3: Output

**If all criteria are binary (or rewritten to binary):**

```
Goal file: VALID

[N] criteria, all binary-resolvable.
Passing bar: [N] of [total].

Ready to run /prd-graph or any review loop.
Goal file saved to: [path]
```

**If any criteria fail the binary test:**

```
Goal file: BLOCKED — [N] criteria need work before the graph can run.

Criterion 2: "Improve the legal section"
→ Problem: No observable test.
→ Fix: "The legal section names a next step, a decision owner, and a deadline."

Criterion 4: "The PRD is better"
→ Problem: Comparative with no baseline.
→ Fix: Remove. Or rewrite as: "Every open question from the prior review has a proposed resolution."

Revise and re-run /goal-gate, or say "apply fixes" and I'll rewrite them.
```

**If the PM says "apply fixes":**
- Rewrite the failing criteria with the suggested fixes
- Re-validate
- Save the goal file to `outputs/[work-type]/[session]-goals.md`

---

## Integration with Other Skills

**Before `/goal-gate`:**
- `/prd-draft` — create the PRD being revised
- `/prd-review-panel` — run if you need to discover what the blockers are before setting goals

**After `/goal-gate`:**
- `/prd-graph` — the graph reads the validated goal file as its evaluator rubric
- `/ralph-wiggum` — adversarial pass; use the same goal file as the scoring bar

**Never run `/prd-graph` without a passing goal-gate first.** The graph's evaluator has no criteria to score against.

---

## Output Quality Self-Check

Before presenting results:

- [ ] Every criterion can be completed by the sentence: "The evaluator can answer this yes or no by checking whether ___."
- [ ] No criterion contains "improve", "better", "clearer", "consider", "address", "more", or "stronger" without a specific observable standard attached
- [ ] Compound criteria (those using "and") are split into separate items
- [ ] The out-of-scope section exists and has at least one item
- [ ] The passing bar is a specific number, not "most" or "enough"
- [ ] The goal file is saved to `outputs/` before reporting VALID
