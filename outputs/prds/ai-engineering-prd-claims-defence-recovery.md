# AI Engineering PRD: Claims Defence & Recovery

**Product:** Asset Nova, Product 1
**Stage:** Engineering design
**Date:** 2026-08-27
**Target buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Status:** Draft

## Engineering outcome

Read the owner's contract and live project record, surface claimable or at-risk commercial events, compute deadlines and damages in code, and draft a cited notice or rebuttal for named human approval. The pipeline is read-only until the human gate. The agent never sends.

## Nine-step pipeline

```text
INPUT                        PROCESSING                          ACTION                     DETERMINISTIC OR AGENTIC
contract + 14 amendments  →  parse, split by clause      [code]
                             extract obligations,
                             notice windows, recipients  [model]
                                    ↓
letters, notices,         →  classify document type      [model]   →  link to the timeline    deterministic write
minutes (11,482)             extract dates, parties,               [code]                     (a link, not an opinion)
                             the event referred to       [model]
                                    ↓
daily site reports        →  extract event facts:        [model]
(3,140)                      what stopped, where, when
                                    ↓
P6 update (.xer)          →  read dates and float        [code]
                                    ↓
                             ONE PROJECT RECORD: events, obligations, deadlines, documents
                                    ↓
                             notice window test          [code]   →  event valid / barred      deterministic, always
                             damages calculation         [code]   →  47 days x $45k = $2.1M    deterministic, always
                             quantum bounds              [code]   →  supported / unsupported   deterministic, always
                                    ↓
                             build the position          [model]  →  a ranked finding with     agentic proposal,
                             (event to clause mapping,               a money number and an     never an action
                             evidence selection)                     evidence chain
                                    ↓
                             citation check              [code]   →  no citation, no finding   deterministic veto
                                    ↓
                             HUMAN REVIEW               [human]   →  approve / edit / reject   the only gate that
                                                                                               releases anything
                                    ↓
                             draft the notice or         [model]  →  a document in the         agentic drafting,
                             rebuttal                                owner's own template      zero send authority
                                    ↓
                             send                       [human]   →  a person presses send     never the agent
                                    ↓
                             record the outcome          [code]   →  settled at what number,   deterministic learning
                                                                     which findings held        signal
```

The agent is autonomous about reading, linking, calculating and proposing. It has no autonomy over anything that leaves the building.

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

### Gate 0: Reading is trustworthy

| What we measure | Pass mark | Why this number |
|---|---|---|
| Documents read and correctly typed | 98% or better | Below this, the record has holes and every later number is suspect |
| Dates extracted correctly | 99.5% or better | A wrong date is a wrong deadline, which is the one error the product cannot survive |
| Documents refused and queued for human | Reported, not hidden; under 5% of volume | Abstaining is allowed. Guessing is not. |
| Invented facts | Zero. Any occurrence blocks the gate | This is a legal record. |

### Gate 1: Findings are worth a person's attention

| What we measure | Pass mark |
|---|---|
| Precision on findings shown as findings | 85% or better |
| Recall against commercial team's closed-project findings | 80% or better, and at least one material item they missed |
| Evidence chain accuracy | 99.5% or better |
| Deadline arithmetic | 100% |
| Low-confidence items shown as "watching" | 100% |

Stop rule: precision below 60% after eight weeks means return to Gate 0.

### Gate 2: A human agrees, in practice

| What we measure | Pass mark |
|---|---|
| Findings actioned rather than only seen | 80% or better |
| Drafts approved with minor edits or none | 70% or better |
| Override rate | Falling week on week |
| Digest ignored two days running | Under 10% of weeks |
| Cost per document read | Under $0.05 blended |

Stop rule: four straight weeks without review pauses the pilot.

### Gate 3: It changed the money

| What we measure | Pass mark |
|---|---|
| Exposures surfaced and countersigned | $20M or more per pilot project |
| Notice deadlines missed on covered scope | Zero |
| Money kept or recovered agreed before pilot | Beats pilot fee by 5x or better |
| Findings surviving to settlement | Reported honestly, including failures |

### Product 1 success number

Money kept or recovered per project, countersigned by customer.

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
