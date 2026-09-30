---
name: prd-graph
description: Run the full PRD revision graph — maker rewrites the PRD, 6 reviewer agents run in parallel, an evaluator scores against your goal file's exit criteria, and a router loops or advances. Requires a validated goal file (run /goal-gate first). Use when a PRD has blockers from a prior review and needs a structured revision pass, not a blank-slate rewrite. Saves a state file after every run so the next session picks up where this one ended.
user-invocable: true
disable-model-invocation: false
---

# /prd-graph — PRD Revision Graph

When the PM types `/prd-graph`, run the full PRD revision graph: goal gate → maker → parallel reviewers → evaluator → router (advance or loop).

**What this is not:** A first draft. Use `/prd-draft` for that. This skill revises an existing PRD that has already been reviewed and has specific named blockers to resolve.

---

## Quick Start

```
/prd-graph                                              → Auto-detect PRD and goal file
/prd-graph --prd control-tower --goals session-goals   → Specify both files
/prd-graph --loop-limit 2                              → Cap at 2 revision loops (default: 3)
```

---

## Draft mode vs Revision mode

**Before doing anything else, determine which mode applies:**

| Signal | Mode | What happens next |
|---|---|---|
| An existing PRD file is named or found in `outputs/prds/` | **Revision** | Proceed to Context Routing → Step 0 |
| No existing PRD, or PM says "from scratch" / "restart" | **Draft** | Run clarifying questions first (see below) |

**If Draft mode:** run the clarifying questions from `/prd-draft` Step 1 before the maker writes a word. Do not skip them. The minimum required:

1. What problem are we solving? (specific user pain, not a category)
2. What's the hypothesis? ("If we build X, then Y will happen because Z")
3. How does this fit the current strategy? (reference a specific goal or OKR)
4. What PRD stage is this? (Team Kickoff / Planning Review / XFN Kickoff / Solution Review / Launch Readiness)
5. What are the non-goals — what is explicitly NOT in v1?
6. What does success look like — what metric or observable behaviour changes?
7. Who are the key stakeholders and decision-makers?

Check `context-library/` for existing answers before asking — skip any question already answered by context files or the PM's prompt. Confirm the brief with the PM in one paragraph before proceeding to Context Routing.

---

## Context Routing

**Read in this order before doing anything:**
1. Goal file — `outputs/prds/*-goals.md` (or path provided). **Halt if missing.**
2. Prior state file — `outputs/prds/*-state.json` (load if exists; start fresh if not)
3. Input PRD — `outputs/prds/[prd-name].md`
4. Prior review synthesis — `outputs/prds/[prd-name]-review-synthesis.md` (if exists)
5. `context-library/strategy/` — strategic context for the evaluator
6. `{pm-os}/sub-agents/` — reviewer personas

---

## Workflow

### Step 0: Goal Gate Check

Read the goal file. For each exit criterion, verify it is binary-resolvable (the evaluator can answer yes or no without interpretation).

**If any criterion is vague or missing:**
```
HALT — goal file is not valid.
Run /goal-gate first to lock the exit criteria.
Failing criterion: "[criterion text]"
Problem: [why it's not binary]
```

Do not proceed until all criteria pass. The evaluator has nothing to score against without them.

**If goal file is valid:** Read the passing bar (e.g., "5 of 6 criteria must pass"). Load it into working memory. Proceed.

---

### Step 1: Load State and Prior Context

Read the state file if it exists. Extract:
- `blockers_from_prior_review` — the specific issues the maker must resolve
- `loop_count` — how many revision loops have already run this session
- `criteria_failed_last_run` — which criteria failed in the last evaluator pass (empty on first run)
- `decisions_made` — any owner decisions or scope changes already recorded

If no state file: initialize with loop_count = 0, all other fields empty.

Read the input PRD and prior review synthesis. Identify the open questions, named blockers, and any parked decisions that are within this session's scope.

---

### Step 2: Maker Pass

Revise the PRD. The maker's job is narrow: **resolve the specific items in `criteria_failed_last_run` (or all blockers on the first pass), and nothing else.**

**Maker constraints:**
- Do not rewrite sections that passed in the prior evaluator run
- Do not add scope, features, or sections not referenced in the goal file
- Do not change the PRD's stage or structural format
- For each blocker resolved, add a one-line note at the bottom of the relevant section: `[Revised: {what changed and why}]`
- If a blocker requires information the maker does not have (e.g., an unanswered owner decision), write: `[Open: {question} — owner: {name}]` and move on

Save the revised PRD draft internally (do not overwrite the input file yet — wait for evaluator pass).

---

### Step 3: Parallel Reviewer Pass

**CRITICAL: Launch all 6 reviewers in a single message as parallel Task calls.**

Give each reviewer:
- The revised PRD draft (full text)
- The specific exit criteria from the goal file relevant to their perspective
- Instruction: flag only what is still broken relative to those criteria — not general feedback

**The 6 reviewers and their focus for this pass:**

| Reviewer | File | Focus |
|---|---|---|
| Engineer | `{pm-os}/sub-agents/engineer-reviewer.md` | Technical feasibility, scope creep, implementation gaps |
| Executive | `{pm-os}/sub-agents/executive-reviewer.md` | Strategic fit, business case, whether the problem is validated |
| Legal | `{pm-os}/sub-agents/legal-advisor.md` | Compliance gaps, PII handling, unanswered legal questions |
| UXR | `{pm-os}/sub-agents/uxr-analyst.md` | Research validation, unvalidated assumptions, projection vs evidence |
| Skeptic | `{pm-os}/sub-agents/skeptic.md` | Logical gaps, value proposition stability, what could still be wrong |
| Customer Voice | `{pm-os}/sub-agents/customer-voice.md` | Whether the user would actually use this, friction points |

Each reviewer returns:
- `still_failing`: list of exit criteria from the goal file that this reviewer judges not yet met
- `evidence`: one specific quote or observation from the revised PRD per failing criterion
- `passing`: list of exit criteria this reviewer judges now met

Collect all 6 outputs before proceeding.

---

### Step 4: Evaluator Pass

Score the revised PRD against every exit criterion in the goal file.

For each criterion:
1. Collect the verdict from every reviewer who covered it
2. Apply the rule: a criterion **passes** if zero reviewers flag it as `still_failing`; **fails** if one or more do
3. Record the evidence for every failure (the specific quote the reviewer cited)

Produce a scoring table:

```
Criterion 1: [text] → PASS (0 reviewers flagged)
Criterion 2: [text] → FAIL (2 reviewers flagged)
  - Engineer: "The run count question has no SQL query or observed number"
  - Skeptic: "The two counts were never run — the PRD still assumes the screen"
Criterion 3: [text] → PASS
...
```

Count passes. Compare to passing bar from goal file.

---

### Step 5: Router

**If passes ≥ passing bar → ADVANCE**

- Overwrite the input PRD with the revised draft
- Write updated state file (see State File section)
- Report:
  ```
  Graph complete. [N/N] criteria passed.

  PRD saved: outputs/prds/[filename]
  State file updated: outputs/prds/[name]-state.json

  Failing criteria (if any below bar — none here):
  [list]

  Next trigger: [from state file — e.g., "Re-run after Chris answers Q1"]
  ```

- **Decision reminder (always run after ADVANCE):**
  Scan the state file's `decisions_made` and `still_open` fields. For every item in `decisions_made`, prompt:

  ```
  Decisions made this session that should be filed:

  1. [Decision title] — [one-line summary]
  2. [Decision title] — [one-line summary]

  Run /decision-doc to file these with full metadata, or say "file decisions" and I'll do it now using {pm-os}/templates/decision-template.md.
  Fields I'll capture: date, product_area, feature, prd_stage, decided_by, what was decided, alternatives rejected, consequences, review trigger.

  Unfiled decisions will be lost when this context window closes.
  ```

  If `decisions_made` is empty, skip this prompt silently.

**If passes < passing bar → LOOP**

- Check loop_count against loop_limit (default: 3)
- If loop_count < loop_limit:
  - Increment loop_count in state
  - Pass the evaluator's failure evidence back to Step 2 as `criteria_failed_last_run`
  - Run the maker again — with the specific failure evidence, not a general "try again"
- If loop_count = loop_limit:
  - **SURFACE TO PM — do not loop again**
  ```
  Loop limit reached ([N] passes). Still failing after [limit] revisions:

  Criterion 2: [text]
  Root cause: [why the maker couldn't resolve it]
  What's needed: [specific information or decision required]
  Owner: [who can unblock this]

  The PRD has NOT been overwritten. Revised draft available for review.
  Recommended: resolve the blocker above, then re-run /prd-graph.
  ```

---

## State File

After every run, write `outputs/prds/[prd-name]-state.json`:

```json
{
  "prd": "[filename]",
  "last_run": "[ISO date]",
  "loop_count": 0,
  "graph_result": "advanced | looped | surfaced",
  "criteria_passed": ["Criterion 1", "Criterion 3"],
  "criteria_failed": ["Criterion 2"],
  "criteria_failed_evidence": {
    "Criterion 2": [
      "Engineer: 'The run count question has no SQL query or observed number'",
      "Skeptic: 'The two counts were never run'"
    ]
  },
  "blockers_resolved_this_run": ["Blocker 1 description"],
  "still_open": ["Blocker 2 — needs owner decision from Chris"],
  "decisions_made": [],
  "next_trigger": "Re-run after Chris confirms Q1 and the two SQL counts are observed"
}
```

The next session reads this file before doing anything. The maker uses `criteria_failed_evidence` as its specific brief. Nothing starts blank.

---

## Model Assignment

| Role | Model | Reason |
|---|---|---|
| Orchestrator (this skill) | Sonnet | Routing logic, state management — medium judgment |
| Maker | Sonnet | PRD revision — structured, not open-ended |
| Parallel reviewers (6) | Sonnet | Parallel read + focused output — cost matters |
| Evaluator (Step 4) | Opus | Hard judgment — scoring against binary criteria requires the best model |

Override with `--evaluator-model sonnet` if cost is a constraint (reduces accuracy on close calls).

---

## Integration with Other Skills

**Before `/prd-graph`:**
- `/prd-draft` — create the PRD if it doesn't exist
- `/prd-review-panel` — run first to discover blockers and generate a review synthesis
- `/goal-gate` — validate exit criteria (required before this skill proceeds)

**After `/prd-graph`:**
- `/decision-doc` — document any decisions the graph surfaced but couldn't resolve
- `/ralph-wiggum` — adversarial final pass before stakeholder review
- `/prd-review-panel` — full 7-agent review at the next PRD stage

**Iterative pattern:**
```
/prd-review-panel   → discover blockers
/goal-gate          → lock exit criteria
/prd-graph          → revise until criteria pass or surface to PM
/decision-doc       → document unresolved decisions
/prd-graph          → re-run after decisions are made
```

---

## Output Quality Self-Check

Before reporting results:

- [ ] Goal file was validated (binary-resolvable criteria) before any revision ran
- [ ] All 6 reviewers ran in parallel (single message, multiple Task calls)
- [ ] Each reviewer received the **complete, verbatim PRD text** — no abbreviations, no placeholders, no summaries of sections. Truncated prompts cause false criterion failures and invalidate the evaluator pass.
- [ ] Evaluator scored against the goal file's criteria — not against general PRD quality
- [ ] Every failing criterion has specific evidence (a quote, not a summary)
- [ ] The PRD file was NOT overwritten unless the graph advanced
- [ ] State file was written with `next_trigger` field populated
- [ ] If surfaced: the specific blocker, root cause, and owner are named — not "needs more work"
