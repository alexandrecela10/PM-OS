# AI Engineering PRD: Design Feasibility Check

**Product:** Asset Nova, Product 2
**Stage:** Engineering design
**Date:** 2026-08-27
**Target buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Status:** Draft

## Engineering outcome

For every FEED design revision, return a fast, cited check of compliance, affordability and buildability. The product is advisory and never blocks the engineer. It must explain the code clause and drawing region behind every finding, and preserve the engineer's disputes.

## Nine-step pipeline

1. **Read and file:** every drawing page is split, dated, versioned, and tagged to a discipline, region and revision.
2. **Build the record:** link revisions, prior comments, open findings, code clauses, budget ceilings and affected activities.
3. **Apply the rules:** apply code clauses, cost bounds and deterministic geometry or schedule checks. Arithmetic is code, not opinion.
4. **Reason over it:** assess whether the revision closes prior comments, is likely compliant, and can be built in the stated sequence.
5. **Size the money:** estimate the value at stake, confidence and consequence of leaving the issue open.
6. **Show the working:** cite the code clause, drawing page and region. No citation, no finding.
7. **A human decides:** the design manager accepts, disputes or defers each finding.
8. **Draft the action:** create the cited review list for the existing design workflow.
9. **Learn from the outcome:** record disputes, accepted findings and field changes that later confirm or disprove the finding.

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
