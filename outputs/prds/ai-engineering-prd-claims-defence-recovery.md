# AI Engineering PRD: Claims Defence & Recovery

**Product:** Asset Nova, Product 1
**Stage:** Engineering design
**Date:** 2026-08-27
**Target buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Status:** Draft

## Engineering outcome

Read the owner's contract and live project record, surface claimable or at-risk commercial events, compute deadlines and damages in code, and draft a cited notice or rebuttal for named human approval. The pipeline is read-only until the human gate. The agent never sends.

## Nine-step pipeline

1. **Read and file:** every page is split, dated, and tagged to a party, drawing or activity.
2. **Build the record:** create one linked timeline of events, obligations, revisions and deadlines.
3. **Apply the rules:** calculate deadline maths, code clauses and cost bounds. This is arithmetic, not opinion.
4. **Reason over it:** decide whether an event triggers a clause and whether evidence closes a previous issue.
5. **Size the money:** estimate value at stake, confidence and what happens if the owner does nothing.
6. **Show the working:** attach citations to every finding. No citation, no finding.
7. **A human decides:** approve, edit or reject on a queue ranked by money.
8. **Draft the action:** produce the letter, rebuttal pack or challenge book.
9. **Learn from the outcome:** capture what was approved, rejected and what the settlement actually was.

## Deterministic code vs model reasoning

Deterministic code owns document identity, page and quote matching, deadline maths, notice clocks, damages arithmetic, cost bounds, confidence calculation from defined signals, ROI arithmetic and policy enforcement. Deadlines, damages and cost bounds are never model output.

Model reasoning may extract obligations, classify event type, link an event to relevant evidence, judge whether a document may trigger a clause, identify contradictions, and draft language from verified facts. The model proposes. Code verifies. A finding without a resolvable citation is not surfaced.

Use a swappable open-weights model adapter, such as a Llama/Qwen-class model fine-tuned on construction correspondence, self-hosted on in-region GPUs. A deterministic dummy adapter must run the evaluation runner offline.

## Data contracts

| Input type | Required contract |
|---|---|
| Contract and amendments | `project_id`, `document_id`, `version`, `effective_date`, `page_id`, extracted text, language, source URI, hash, access policy |
| Letters, RFIs, minutes and transmittals | `project_id`, `document_id`, `author`, `recipient`, `date`, `subject`, page-level text, referenced clause/activity, source URI, hash |
| Schedule updates | `project_id`, `schedule_version`, activity ID, baseline and current dates, status, predecessor/successor links, source URI, hash |
| Daily and weekly reports | `project_id`, report date, author, work area, activity IDs, progress text, constraints, source URI, hash |
| Customer permissions | `project_id`, user ID, role, allowed document scope, approval role, residency tag |
| Human disposition | `finding_id`, actor, action (`approve`, `edit`, `reject`), reason, timestamp, resulting artifact ID |

Input outside the registered project is refused, logged and escalated. Missing amendments make dependent deadline calculations `PROVISIONAL`.

## Retrieval and citation design

Index source pages and preserve document IDs, versions, dates, page IDs, text spans and hashes. Retrieval returns a bounded evidence set with the source metadata attached. The citation verifier checks that every cited document exists in the registered project and that the quoted text matches the source page. It also checks that each draft assertion is entailed by a citation.

**No-citation-no-finding rule:** a finding with no valid citation is downgraded to an internal diagnostic and never reaches the customer queue or a draft notice. Broken or stale citations are logged as failures, not silently repaired by the model.

## Confidence and ROI estimator

The estimator is code. Confidence is derived from evidence completeness, source agreement, clause match, deadline-data completeness and model certainty, with thresholds configured per contract form. It must show the signals behind the score and downgrade conflicting or missing evidence.

ROI is also code. It stores the source amount, the calculation path, the avoided-loss scenario and the confidence band. It must not turn a model guess into a dollar claim. The customer can override or reject the estimate, and the override is logged.

## Human-review gate

Every surfaced item enters a queue ranked by money at stake and confidence. A named customer approver must approve, edit or reject it. The system has no `send` action. Only an approved draft can be handed to the customer's existing outbound process. Self-approval and unknown approvers are rejected. The audit trail records the finding, evidence, calculation, draft, edits and final disposition.

## Evaluation design

Build golden sets from closed projects and compare recall with a specialist's retrospective findings. Include:

- Event detection precision and recall.
- Evidence-chain resolution and quote match.
- Zero-tolerance invented-fact rate in sent notices.
- Deadline accuracy against hand-computed goldens, including missing-amendment cases.
- Damages and cost arithmetic against fixed goldens.
- Confidence and ROI estimate traceability.
- Cost per document.
- Governance tests for out-of-scope input, no-citation findings and human approval.

Release targets from the deck are **85%+ event precision**, **99.5%+ evidence-chain accuracy**, **zero hallucinations in sent notices**, **100% deadline accuracy**, and **<$0.05 per document** blended cost. A release that violates the no-citation rule or human gate cannot ship, regardless of model quality.

## Failure modes

- **Wrong deadline:** rules engine fails the test or marks the result provisional when an amendment is missing.
- **Unsupported finding:** citation resolution or entailment fails, so the finding is withheld.
- **Conflicting sources:** surface the contradiction with both sources; make no unsupported judgment.
- **Out-of-scope document:** refuse ingestion, log and escalate.
- **Low confidence:** keep in triage or watch status; do not alert as a material finding.
- **False alarms:** raise surfacing threshold and tune against human dispositions.
- **Sensitive data exposure:** enforce project scope, permission mirror and residency tag.
- **Model or GPU outage:** retain the source record and retry; no outbound action occurs.

## Deployment constraints

- In-region private cloud, in-Kingdom or in-UAE as required by the customer.
- No training on customer data and no shared-model path that moves customer records out of the customer boundary.
- Read-only source access and a read audit trail of every page and inference.
- Full append-only audit trail of reads, model calls, citations, calculations, refusals, approvals and edits.
- Customer permissions mirrored at retrieval and human approval.
- Open-weights model self-hosted on sovereign GPU; adapter swappable.
- Closed-project backtest before live data, then a controlled paid pilot.
