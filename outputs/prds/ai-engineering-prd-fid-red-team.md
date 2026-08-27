# AI Engineering PRD: FID Approval Red Team

**Product:** Asset Nova, Product 3
**Stage:** Engineering design, not now
**Date:** 2026-08-27
**Target buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Status:** Deferred until Products 1 and 2 earn trust

## Engineering outcome

Before an investment committee vote, compare a proposal with the owner's finished projects, find gaps in the definition and produce a cited challenge book. The agent gives the estimator and sponsor a private pre-read, asks questions and casts no vote.

## Primary scenario

Train 5 goes to the investment committee with a $6.1bn estimate and 8% contingency. Before forward use, the agent runs backwards on 14 of the owner's finished projects and shows what it would have said about each. Layla Haddad, lead estimator for capital projects, gets the challenge book privately first. Tom Beckett, project director for Jebel Nasr, sponsors the gate review. The agent asks nine questions and casts no vote.

## Nine-step pipeline

```text
INPUT                        PROCESSING                          ACTION                     DETERMINISTIC OR AGENTIC
14 finished owner         →  extract sanctioned vs       [model]
projects                     final cost and date         [code]
                                    ↓
                             REFERENCE CLASS: median growth, spread   [code]
                                    ↓
this gate's estimate,     →  definition completeness     [model]  →  what is missing from     agentic proposal
basis of estimate,           audit against the owner's                the definition at this
schedule, contingency        own gate standard                        gate
                             contingency vs the          [code]   →  8% asked, 23% median     deterministic
                             reference class                          historical growth
                                    ↓
                             citation check              [code]   →  every number traced to   deterministic veto
                                                                     a source document
                                    ↓
                             PRIVATE PRE-READ to the     [human]  →  the estimator sees it    no surprise in the room
                             estimator and sponsor                    first and can respond
                             challenge book: nine        [model]  →  questions, not a         the agent never votes
                             questions with evidence                 recommendation
```

## Deterministic code vs model reasoning

Deterministic code owns project identity, source hashes, final cost and date calculations, reference-class statistics, contingency comparisons, citation verification and audit events. The model extracts the sanctioned and final outcomes, checks definition completeness against the owner's gate standard and proposes the nine questions. The model never votes and never makes an approval recommendation.

Use a swappable open-weights model adapter self-hosted on in-region GPUs. A deterministic dummy adapter must run the evaluation runner offline.

## Data contracts

| Input type | Required contract |
|---|---|
| Finished owner projects | `project_id`, project type, sanctioned value, final cost, sanctioned date, final date, scope attributes, source URI, hash, residency tag |
| Gate estimate | `project_id`, gate ID, estimate value, currency, basis of estimate, version, owner, source URI, hash |
| Schedule | `project_id`, schedule version, activity ID, baseline and forecast dates, critical-path flag, source URI, hash |
| Contingency | `project_id`, gate ID, contingency percentage, basis, approved by, effective date, source URI, hash |
| Definition package | `project_id`, document ID, revision, discipline, page ID, extracted text, region map, source URI, hash |
| Human disposition | `finding_id`, actor, action (`accept`, `edit`, `reject`, `defer`), reason, timestamp, resulting artifact ID |

Inputs without a project, gate or source identity are refused and logged. A missing outcome, estimate basis or comparable attribute is reported as a gap, not filled by the model.

## Retrieval and citation design

Index finished-project source pages, estimate bases, schedules, contingency approvals and definition-package regions. Retrieval returns source IDs, versions, page IDs, text spans, region coordinates and hashes. The citation verifier checks that every number in the challenge book traces to a registered source document and that the cited text matches the source.

**No-citation-no-finding rule:** a question without a valid source chain is withheld from the private pre-read. Broken or stale citations are logged as failures, not repaired by the model.

## Confidence and ROI estimator

Confidence is code-derived from source completeness, comparable-project match, definition coverage, citation validity and model certainty. Missing history or weak comparability lowers confidence and labels the item for review.

The estimator records the proposal value, contingency, reference-class comparison, evidence chain and potential exposure. It must distinguish an exposure question from money actually avoided. The product's business number is gate decisions changed, meaning contingency raised, scope re-cut or approval deferred, with estimator agreement that the question was fair.

## Human-review gate

Layla receives the private pre-read first, and Tom receives the sponsor copy before the meeting. They can accept, edit, reject or defer each question. The investment committee owns the gate decision. The agent has no vote, no approval action and no authority to alter the estimate or scope.

## Evaluation design

Build golden sets from the owner's 14 finished projects and compare retrospective questions with an estimator's own closed-project findings. Include:

- Recall against the specialist's retrospective findings.
- Zero-tolerance invented-fact rate in cited questions.
- Accuracy of sanctioned versus final cost and date extraction.
- Accuracy of reference-class median growth and spread.
- Citation accuracy for every number.
- Fairness of the questions, recorded by estimator response.
- Cost per document read.
- Enforcement of private pre-read, human decision and no-vote behavior.

### Gate 0: Reading is trustworthy

| What we measure | Pass mark |
|---|---|
| Documents read and correctly typed | 98% or better |
| Dates extracted correctly | 99.5% or better |
| Documents refused and queued for human | Reported, not hidden; under 5% of volume |
| Invented facts | Zero. Any occurrence blocks the gate |

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

### Product 3 success number

Gate decisions changed, meaning contingency raised, scope re-cut or approval deferred, with estimator agreement that the question was fair.

## Failure modes

- **Uncomparable history:** require named source projects and route the question for human review.
- **Missing outcome or estimate basis:** refuse the comparison and report the missing source.
- **Unsupported question:** citation verification fails, so the question is withheld.
- **Invented benchmark:** block the gate and log the source failure.
- **Political rejection:** earn the right through Products 1 and 2 and start with a retrospective demo.
- **Agent treated as decision-maker:** keep the human decision owner explicit and enforce no-vote behavior.
- **Model or GPU outage:** retain the source record and retry; no decision action occurs.

## Deployment constraints

- In-region private cloud, in-Kingdom or in-UAE as required by the customer.
- No training on customer data and no shared-model path that moves customer records outside the customer boundary.
- Read-only access to finished projects and a read audit trail of every page opened and why.
- Full append-only audit trail of source reads, model calls, citations, calculations, questions, edits and gate decisions.
- Owner permissions mirrored at retrieval and human review.
- Open-weights model self-hosted on sovereign GPU with a replaceable adapter.
- Closed-project retrospective before any forward gate use.
- Product 3 remains deferred until Products 1 and 2 have earned trust and built the owner's history.
