# Product PRD: Claims Defence & Recovery

**Product family:** Asset Nova
**Stage:** Solution Review
**Date:** 2026-08-27
**Buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Primary persona:** Owner contracts / commercial manager on a live build
**Status:** Draft, case study

## Problem in plain English

On a live build, the money-losing events are spread across the contract, letters, meeting minutes, schedule updates and site reports. The owner's commercial team cannot read the whole record every day. A contractor can ask for roughly twice what it eventually settles for, while the owner can also lose its own entitlement because evidence was not assembled before a notice deadline.

The product reads the record the owner already controls and keeps a ranked list of money moves worth making. It does not replace commercial judgment. It makes the evidence easier to find, does the deadline arithmetic, and drafts the action for a named person to approve and send.

**Hypothesis:** If we read the owner's contract and project record every day, then the contracts team will keep more money and recover more of what it is owed, because the current failure is reading capacity and deadline discipline, not the absence of human judgment.

## Persona and their week

The owner contracts / commercial manager defends against claims, recovers liquidated damages (late-delivery damages) and back-charges. Their week is a stream of contractor letters, claims, meeting minutes, schedule updates and site reports. They reconstruct events, check the contract, chase missing evidence, decide what deserves attention, and prepare a rebuttal or notice. Reporting is often monthly, so a problem can be four to eight weeks old before a leader sees it.

The product fits the existing week. It reads in the background, sends a ranked queue to the place the team already looks, and gives the manager one review screen. The manager approves, edits or rejects. The agent drafts. A person presses send.

## Job to be done

Assess incoming contractor claims fast, rebut unsupported ones, catch where the contractor missed its own notice deadline, and pursue the owner's own liquidated damages and back-charges before deadlines lapse, off a record the owner controls.

## Value decomposition

### Value (money)

On a $5bn project, our conservative model:

| Step | Number | Where it comes from |
|---|---|---|
| Claims submitted over the build | ~$400M (8% of project value) | our assumption, to validate with the owner's own history |
| Typically settled at about half | ~$200M paid | IPA: submitted vs settled gap "as much as half" |
| Sharper, evidenced defence on 10% of that | **$20M kept** | our model |
| Late-delivery damages and back-charges pursued properly (from ~40% to ~70% of what's owed) | **~$9M recovered** | our model, using a $30M entitlement pool |
| One dispute kept out of formal proceedings | **$5–8M of legal and expert cost avoided**, plus 12.5 months of management time | Arcadis: $60.1M and 12.5 months per average dispute |
| **Total per project** | **~$30M** | |
| Price at 0.05% of project value | $2.5M | industry pricing runs 0.1–0.3% of project value |
| **Return** | **~10:1** | |

### Likelihood of delivering

**High.** The evidence lives in documents the owner already holds. Deadline maths is arithmetic, not judgment. Every output is checkable against a cited page. Document Crunch reached 400+ customers and Trimble bought it for $246.4M in April 2026, which shows the category is commercially proven.

### Effort from the persona

**Low.** Give us a read-only copy of the contract and correspondence archive. Spend about 20 minutes a day on a ranked queue. Nothing to migrate, no new system of record, and no change to the monthly cycle.

### Sacrifice from the persona

The team lets software read the most commercially sensitive, sometimes legally privileged, material on the project. The answer is in-Kingdom or in-UAE hosting, private cloud, no training on customer data, access mirroring the existing commercial team's permissions, and a full audit trail of what the agent read and why.

## Scope

### V1

- Read-only ingestion of the contract, amendments, letters, minutes, schedule updates and site reports.
- A linked record of events, obligations, revisions and deadlines.
- Detection of claimable or at-risk commercial events.
- Evidence chains that link each finding to real document pages.
- Deterministic deadline, damages and cost arithmetic.
- A queue ranked by money at stake and confidence.
- Draft rebuttals, notices and evidence packs.
- Human review with approve, edit or reject dispositions.
- Delivery through email or Teams and one review screen.
- A closed-project backtest before a live pilot.

### Explicit non-goals

- No writing back to ERP, P6 or Aconex in v1.
- No autonomous outbound correspondence. The agent never sends.
- No legal advice, entitlement strategy or quantum assessment beyond arithmetic from the record.
- No dispute-resolution, arbitration or litigation-support tooling.
- No contractor-first product. The target buyer is the owner.
- No requirement that the customer change its monthly reporting habit.

## User journeys

### Primary journey: daily ranked queue

1. The owner provides a read-only contract and project archive.
2. New documents are read and linked to the project record.
3. The manager opens a queue ranked by money and confidence.
4. A finding shows the event, the clause, the deadline or calculation, and clickable source pages.
5. The manager approves, edits or rejects the finding.
6. The agent drafts the notice or rebuttal.
7. A named person presses send and the disposition is recorded.

### Alternate 1: closed-project proof

Run the same pipeline on last year's closed files. Show what the agent would have caught, including at least the evidence the commercial team found and any material item it missed. Use the result to validate the $400M claims-submission assumption and agree the live-pilot metric.

### Alternate 2: signal before a claim is registered

A letter, dated 14 May, signals a claim that is not in the risk register. The agent surfaces it as a watch or finding, links the letter to the contract and related events, and gives the manager the chance to assemble evidence before the notice clock expires.

## Success metrics

### Business

- Money kept or recovered per project, with exposures customer-countersigned.
- **$20M+** validated exposures surfaced per pilot.
- Zero notice deadlines missed on covered projects.
- Pilot-to-contract conversion and share of project value captured in price.
- **$10–12M ARR at 24 months** from the deck's path of 5 pilots, 3 conversions and 6 projects.

### Product

- **90%+** weekly review-ritual adoption.
- **80%+** of surfaced events actioned, not just seen.
- **70%+** of draft notices approved with minor or no edits.
- Time from event appearing in the record to a human decision.
- Share of drafted actions actually sent.
- Honest counter-metric: how often managers override the agent, and whether that falls.

### AI

- **85%+** event-detection precision.
- Recall against a specialist's own findings on closed projects.
- **99.5%+** evidence-chain accuracy.
- Zero invented facts in sent notices.
- **100%** deadline accuracy because deadline maths is a rules engine, not model output.
- **<$0.05 per document** blended cost.

**Kill criteria:** precision below 60% after eight weeks, or the team stops reviewing for four straight weeks. Pause and return to backtest.

## Adoption rules

1. **Runs on files they already have.** Read-only. No migration, no new system of record.
2. **No new habit.** It arrives where they already look (email or Teams), and reviews happen on one screen.
3. **The agent never sends.** It drafts. A person presses send. Always.
4. **Every claim is clickable.** No assertion without a citation to a page in a real document.
5. **Proof on history first.** We run on last year's closed files and show what it would have caught, before it touches a live project.
6. **Priced against one avoided loss,** and sized so a pilot sits inside one project team's own authority.

## Risks

| Risk | Response |
|---|---|
| The owner will not give a machine the privileged commercial record | Closed-project start, in-region private cloud, mirrored permissions and full read audit |
| A wrong finding damages a legal position | Draft only, citations on every finding, deterministic deadline and damages maths, named human approval |
| The exposure register is discoverable in arbitration | Customer-controlled retention, privilege labeling and customer counsel involvement; do not oversell privilege |
| The team tunes out false alarms | Precision-first thresholds and a weekly actioned-rate check |
| Buying gates in the Gulf delay the sale | Treat hosting, cyber certification, registration and local content as roadmap features from day one |

## Open questions needing validation

- [ ] Validate the **~$400M** claims-submission assumption against the owner's own history. Needs validation with owner contracts leadership.
- [ ] Which contract forms and amendment chains must launch first? Needs validation with customer legal.
- [ ] Who can see the exposure register inside the buyer organisation? Needs validation with the sponsor, contracts team and internal audit.
- [ ] Should the pilot price be flat, value-based, or include a success component? Needs validation with the buyer and GTM.
- [ ] What customer-representative and warranty language permits processing counterparty correspondence? Needs validation with legal.
- [ ] Which Arabic-language documents are required in v1? Needs validation with engineering and the first customer.
