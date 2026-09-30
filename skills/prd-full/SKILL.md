---
name: prd-full
description: Run the complete PRD pipeline end-to-end, /prd-draft's clarifying-questions + first-draft workflow (the ONLY step that talks to the PM), save it, auto-derive exit criteria from the draft itself, then run /prd-graph autonomously (maker/reviewer/evaluator/router, looping without further PM interaction) until it advances or hits the loop limit. Use when the PM wants a finished, review-quality PRD in one sitting instead of running the three skills by hand and babysitting each handoff.
user-invocable: true
disable-model-invocation: false
---

# /prd-full: End-to-End PRD Pipeline

When the PM types `/prd-full`, run all three PRD skills back to back as one workflow: draft → lock goals → autonomous revision graph → report. This exists because the three skills, run by hand, require the PM to re-engage at every handoff (confirm the draft, answer `/goal-gate`'s questions, watch the graph loop, decide whether to keep going). `/prd-full` collapses that to one checkpoint.

**What this is not:** a replacement for `/prd-draft`, `/goal-gate`, or `/prd-graph`. Those still exist standalone for when the PM wants to control a step directly (see Integration, below). This is a fixed sequencing of all three for the common case.

---

## Quick Start

```
/prd-full [feature idea or rough brief]      → Full pipeline, from a blank slate
/prd-full --stage "planning review"          → Set the PRD stage upfront
/prd-full --loop-limit 2                     → Cap the autonomous graph at 2 revision loops (default: 3)
```

---

## The one rule this skill exists to enforce

**Ask the PM once, at the start. Never ask again until you either advance or get stuck.**

A PRD pipeline that asks clarifying questions, then asks goal-setting questions, then surfaces every graph loop for a "keep going?" check, has turned three decisions the PM already made in Step 1 into three separate interruptions. `/prd-full` is the fix: front-load everything the PM needs to decide into one clarifying-questions pass, then run everything downstream of that on the PM's own stated intent, including deriving the goal file's exit criteria from what the PM already said, not a second round of questions.

If you find yourself wanting to ask the PM something in Step 2 or Step 3, that's a signal the Step 1 questions were incomplete. Fix Step 1 next time. Don't patch it with a mid-pipeline question now.

---

## Workflow

### Step 1: Opportunity gate, then draft (the only interactive step)

**First, check for an existing opportunity analysis** (added 2026-09-07) in `outputs/opportunity-analyses/` (or this project's override path). If one exists with a `Go` recommendation, skip straight to the draft below. Its answers cover most of what Step 1 would otherwise ask. If it's `No-go`/`Parked`, stop and surface that to the PM before doing anything else. If none exists, run `/opportunity-analysis`'s Step 1 clarifying questions (4 questions) folded into the SAME single checkpoint as the questions below. Don't make the PM answer two separate rounds. Produce the opportunity analysis first; only proceed to the PRD draft if its recommendation comes out `Go`.

Run `/prd-draft`'s Step 0 (context check against `context-library/`) and Step 1 (clarifying questions) exactly as documented in that skill:

- Use the **Adaptive Questions Rule**: skip anything `context-library/` or the PM's own prompt already answers. Open with "Based on what I found, I have [X, Y, Z]. Let me confirm: [summary]. A few remaining questions: [only the gaps].", never re-ask something context already settled.
- Ask in **plain conversational prose**, not a forced-choice UI. This is a "talk it through" step, not a form.
- Do not skip the questions because the PM seems eager to get to a draft. The entire rest of this pipeline runs unattended on the strength of this one answer set, if it's thin, everything downstream inherits that thinness silently.
- **Confirm the one-paragraph brief with the PM before drafting.** Wait for their answer. This is a real stop, not a rhetorical one.

Once confirmed, run `/prd-draft` Step 2 (generate first draft) using the template, stage-length guidance, and writing guidelines from that skill. Save to `outputs/prds/[feature-name]-[stage].md`.

---

### Step 2: Auto-derive the goal file (no new questions)

Do **not** run `/goal-gate`'s interactive four-question mode, that would be a second round-trip to the PM for information Step 1 already produced. Instead, derive exit criteria yourself from what Step 1 generated:

1. **One criterion per Open Question in the draft that has a checkable resolution condition.** Turn "should X?, @stakeholder" into something binary: "the PRD states a decided answer to X, or explicitly names why it's still open and who owns resolving it."
2. **One or two criteria from `/prd-draft`'s own Output Quality Self-Check**, adapted to what this specific PRD actually contains (hypothesis is testable; non-goals each have a stated reason; success metrics have baselines/targets or an explicit "unobserved, first measurement due at X"; every load-bearing factual claim is cited to a real file or marked unobserved).
3. **Passing bar:** default 5 of 6 criteria; scale proportionally if the derived list isn't exactly 6.

Validate every derived criterion yourself against `/goal-gate`'s binary test ("can the evaluator answer this yes/no without interpretation?"). Since you wrote them, fix any that fail the test silently, do not surface a "goal file BLOCKED" message to the PM for criteria you authored; that message exists in `/goal-gate` for PM-authored criteria, not this auto-derived case.

Save the goal file in `/goal-gate`'s format to `outputs/prds/[feature-name]-goals.md`.

---

### Step 3: Run the graph autonomously

Run `/prd-graph`'s full loop (maker → 6 parallel reviewers → evaluator → router) against the auto-derived goal file, exactly as that skill specifies, **with one change: on LOOP, do not surface anything to the PM.** Keep looping automatically:

- Increment `loop_count`, pass the evaluator's specific failure evidence back to the maker, revise, re-review, re-evaluate.
- Repeat until ADVANCE, or until `loop_count` reaches `loop_limit` (default 3, overridable via `--loop-limit`).

**The one case allowed to interrupt the PM mid-pipeline:** hitting `loop_limit` without advancing. Surface it exactly as `/prd-graph` Step 5 specifies, the specific still-failing criterion, the root cause, and who/what is needed to unblock it. Do not keep looping past the limit, and do not silently advance a PRD that hasn't met its bar.

---

### Step 4: Report

Once advanced (or surfaced at the loop limit), report to the PM in one pass:

- Final PRD path and stage
- How many loop iterations it took
- Every exit criterion's final pass/fail state
- The strongest **additional concerns** reviewers raised that weren't gate-blocking, prioritize ones flagged independently by 2+ reviewers, since convergence across different perspectives is itself a signal
- The `/prd-graph` Step 5 decision-reminder: any `decisions_made` this session that should be filed via `/decision-doc`

---

## Integration with the three underlying skills

Use the three skills individually instead of `/prd-full` when:

- The PM wants to set or negotiate exit criteria themselves → `/goal-gate` standalone
- A PRD already has a review synthesis with named blockers from a prior session → `/prd-graph` standalone (it reads `outputs/prds/[prd-name]-review-synthesis.md`, which `/prd-full`'s auto-derived path does not produce)
- The PM wants to stop after the first draft and not run the graph at all → `/prd-draft` standalone

`/prd-full` is the fixed-sequence path for a brand-new PRD where the PM wants a finished, review-passed draft without re-engaging at every handoff.

---

## Model Assignment

Same as `/prd-graph`: maker and parallel reviewers on the standard model; the evaluator pass gets the strongest available model, since scoring against binary criteria is the highest-judgment step in the loop.

---

## Output Quality Self-Check

- [ ] The PM was asked Step 1's questions (or given the adaptive-questions summary to confirm) before any drafting happened, this is the pipeline's only checkpoint and must not be skipped
- [ ] No question was asked in Steps 2–4 that the PM didn't already answer in Step 1
- [ ] The goal file's criteria are binary-resolvable, self-validated against `/goal-gate`'s test
- [ ] All 6 reviewers ran in parallel per loop iteration, each given the complete verbatim PRD text, no summaries, no truncation
- [ ] The PRD file was only overwritten when the graph advanced, never mid-loop
- [ ] If surfaced at the loop limit: the specific blocker, root cause, and owner are named, not "needs more work"
