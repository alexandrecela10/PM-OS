# AI Engineering PRD: Design Feasibility Check

**Product:** Asset Nova, Product 2
**Stage:** Engineering design
**Date:** 2026-08-27
**Target buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Status:** Draft

## Engineering outcome

For every FEED design revision, return a fast, cited check of compliance, affordability and buildability. The product is advisory and never blocks the engineer. It must explain the code clause and drawing region behind every finding, and preserve the engineer's disputes.

## Nine-step pipeline

```text
INPUT                        PROCESSING                          ACTION                     DETERMINISTIC OR AGENTIC
code edition, pinned      →  index clauses, keep the     [code]
by Priya on day one          page and the exact text
budget ceiling, pinned    →  store as a number           [code]
                                    ↓
drawing / document        →  detect the revision,        [code]   →  start a check run        deterministic trigger
revision (A-207 rev C)       diff against rev B                                              (no human asked for it)
                             read geometry, labels,      [model]
                             specified materials
                                    ↓
                             LEGAL     clause retrieval  [code]
                                       clause-to-drawing [model]  →  finding, clause quoted   agentic proposal
                                       comparison                    verbatim + drawing region
                             AFFORDABLE cost delta       [code]   →  $6.8M vs $4.1M left      deterministic
                             BUILDABLE  clash geometry   [code]
                                        long-lead dates  [code]   →  14 weeks on a critical   deterministic
                                                                     path order
                                    ↓
                             citation check              [code]   →  no clause text, no       deterministic veto
                                                                     finding
                                    ↓
                             HUMAN VERDICT              [human]   →  accept / dispute /       advisory, never blocking:
                                                                     accept with a waiver     the revision can always
                                                                                              be issued
                                    ↓
                             record the dispute reason   [code]   →  a labelled error         deterministic learning
                                                                                              signal
```

The check is advisory, never blocking. The revision can always be issued.

## Deterministic code vs model reasoning

Deterministic code owns document and revision identity, region coordinates, code-version selection, budget ceilings, cost arithmetic, rule checks, confidence aggregation and citation verification. It must also own any deadline, damages or cost-bound arithmetic. The model never creates a budget number or silently substitutes a code edition.

Model reasoning may extract design intent, classify a potential code issue, compare revisions with prior comments, reason about access and build sequence, and draft plain-English finding text. The model proposes; deterministic checks and human review decide what is shown.

## Data contracts

| Input type | Required contract |
|---|---|
| Drawing set | `project_id`, `drawing_id`, `revision`, `discipline`, `sheet`, `page_id`, file hash, extracted text, visual region map, source URI |
| Code set | `jurisdiction`, `code_name`, `edition`, `clause_id`, clause text, effective date, source URI, hash |
| Budget ceiling | `project_id`, work package or region, currency, ceiling, version, effective date, owner |
| Prior review comments | `project_id`, drawing ID and revision, comment ID, region, status, author, date, resolution text |
| Equipment and sequence data | `project_id`, equipment ID, delivery assumption, activity ID, access constraint, source URI, hash |
| Human disposition | `finding_id`, actor, action (`accept`, `dispute`, `defer`), reason, timestamp, resulting artifact ID |

The system must refuse a drawing with no project or revision identity and must flag an unavailable code edition or budget ceiling instead of guessing.

## Retrieval and citation design

Index code clauses, drawing text, page images, region coordinates, prior revisions and linked project records. Retrieval must preserve the source page and region. For a compliance finding, the citation verifier checks the exact code clause and drawing region. For an affordability finding, it checks the budget ceiling and affected work package. For a buildability finding, it checks the equipment, access or sequence source.

**No-citation-no-finding rule:** if the system cannot point to a real clause, drawing region or source record, it withholds the finding. A model explanation without a source is not a customer result.

## Confidence and ROI estimator

Confidence is deterministic aggregation of code-version certainty, source completeness, region match, cross-document agreement and model certainty. A missing budget ceiling, ambiguous region or conflicting revision lowers confidence and routes the item for clarification.

The ROI estimator records the affected work package, the modelled rework or delay exposure, the source of the estimate and the confidence. It must preserve the distinction between an issue surfaced and a cost actually avoided. The first release uses the deck's sourced frame: ~$250M rework on a $5bn project, ~$70M design-caused, and **~$35M avoided** when half is caught in design. Customer validation is required before treating any finding as realised savings.

## Human-review gate

The design manager sees the cited pass or fail list on one screen. Findings are advisory, never blocking. The manager accepts, disputes or defers. A disputed finding carries the reason and can be reviewed in later revisions. No drawing is altered and no permit is submitted by the system.

## Evaluation design

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

### Product 2 success number

Share of flagged findings that would have become field changes, measured on closed revision history, with dispute rate as honest counter-metric.

Build golden sets from closed FEED revision histories and compare recall with a specialist's own findings and the field changes that actually occurred. Include:

- Compliance finding recall and precision on the selected code edition.
- Affordability finding accuracy against the budget ceiling.
- Buildability finding recall against known clashes, access issues and equipment constraints.
- Citation correctness to clause, page and drawing region.
- Zero-tolerance invented-fact rate in cited findings.
- Confidence calibration and ROI traceability.
- Review latency and cost per document or revision.
- Human dispute handling and advisory-only enforcement.

The deck supplies the business evidence and research ranges, including **4:1 to 30:1** cost avoidance and **$200–500** at drawing stage versus **$2,000–8,000** in the field. Precision, recall and cost targets need validation on the first narrow-scope backtest.

## Failure modes

- **Wrong code edition:** refuse or mark the result unavailable; never infer jurisdiction.
- **Unreadable drawing or missing region:** dead-letter the input and request a usable revision.
- **Missing budget ceiling:** do not produce an affordability verdict.
- **False compliance finding:** show the cited clause and region, let the engineer dispute, and tune thresholds.
- **Missed clash or access issue:** capture it in the closed-project golden set and narrow the promise rather than claiming full coverage.
- **Revision mismatch:** refuse comparison when revision identity is not reliable.
- **Professional trust loss:** keep the product advisory, publish coverage and preserve the engineer's decision.

## Deployment constraints

- In-region private cloud for the owner, with no customer data used to train a shared model.
- Read-only design-file access and a full read audit trail.
- Full audit trail of source pages, code clauses, model reasoning, deterministic checks, findings and human disputes.
- One code edition and selected disciplines first. Coverage must be explicit.
- No autonomous drawing changes, permit submission or blocking workflow.
- Backtest on a closed FEED revision history before touching a live project.
- Model adapter and deterministic verifiers must be replaceable without changing data contracts.
