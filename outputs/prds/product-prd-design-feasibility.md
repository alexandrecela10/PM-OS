# Product PRD: Design Feasibility Check

**Product family:** Asset Nova
**Stage:** Solution Review
**Date:** 2026-08-27
**Buyer:** Gulf owner-operator at Aramco/ADNOC scale
**Primary persona:** Owner design / engineering manager during FEED
**Status:** Draft, case study

## Problem in plain English

Design revisions are produced faster than an owner team can check them for compliance, cost and buildability. An error that costs thousands in design can become tens of millions once it is in the ground. Around 70–80% of cost deviations trace back to design, not building, and rework is about 5% of project cost on average.

The product checks every design revision in minutes and returns a cited pass or fail list. It is advisory, never blocking. It catches a problem while it is still cheap to fix, inside the design workflow the team already uses.

**Hypothesis:** If every FEED revision receives a fast, cited feasibility check, then the owner will prevent design-driven rework and permit delay, because the current review cycle is too slow and too dependent on manual reading.

## Persona and their week

The owner design / engineering manager owns the design-to-budget promise. During FEED, they coordinate design disciplines, receive repeated drawing revisions, confirm which code edition applies, check budget ceilings and resolve clashes, access constraints and long-delivery equipment assumptions. They carry the rework and delay risk if a design error reaches the field.

The product hooks into the design file drop that already happens. The manager confirms the code edition and budget ceilings once, then reviews cited findings and disputes false findings in the same workflow. The habit does not change.

## Job to be done

On every design revision during FEED, check in minutes that it is compliant with the building code, within cost and buildable, so scope errors are caught while they cost thousands, not the tens of millions they become in the field.

## Value decomposition

### Value (money)

On a $5bn project:

| Step | Number | Source |
|---|---|---|
| Rework at ~5% of project cost | ~$250M | CII IR-153 |
| Share caused by design (~28%) | ~$70M | industry analyses in the report |
| Catch half of it in design | **~$35M avoided per project** | our model on sourced inputs |
| On a $20bn project, the design-caused pool | ~$280M | same method |
| Review time | 6 weeks down to 3 days on Saudi Building Code review | WhiteHelmet customer testimonial, 2026 (self-reported) |
| Independent return modelling | 4:1 to 30:1 cost avoidance; a query costs $200–500 at drawing stage vs $2,000–8,000 in the field | Mirage Metrics, 2026 |

### Likelihood of delivering

**High on a narrow scope, medium if we promise everything.** Reading drawings and code is now doable, and two Gulf vendors already sell a version of it. We start with one code set and the disciplines that cause the most rework, and say so.

### Effort from the persona

**Lowest of the three.** It hooks into the design file drop that already happens. One-time work is confirming the code edition and budget ceilings. After that the designer's habit does not change.

### Sacrifice from the persona

The machine marks an engineer's work inside the engineer's own workflow. The answer is advisory, never blocking. Every finding cites the clause and drawing region. One click disputes a finding, and disputes train the next version.

## Scope

### V1

- Read each design revision from the existing design file drop.
- Check one agreed building-code edition, starting with the disciplines that cause the most rework.
- Check stated budget ceilings for the relevant part of the works.
- Check clashes, access and long-delivery equipment assumptions.
- Return a cited pass or fail list in minutes.
- Link each finding to the code clause and drawing region.
- Let the engineer dispute a finding.
- Preserve revisions, findings and disputes in a read audit trail.
- Backtest one FEED revision history before a live project.

### Explicit non-goals

- No promise to cover every code set, discipline or jurisdiction in v1.
- No blocking approval of a drawing.
- No autonomous changes to drawings or design systems.
- No replacement for the engineer of record, regulator or formal permit process.
- No owner-side FID red team in this product.
- No migration to a new design system of record.

## User journeys

### Primary journey: every FEED revision

1. The design team drops a revised drawing set as it already does.
2. The manager's configured code edition and budget ceilings are applied.
3. The product checks compliance, affordability and buildability.
4. The manager receives a cited pass or fail list in minutes.
5. The manager opens a clause and drawing region, accepts or disputes each finding.
6. The revised design continues through the existing process. Findings and disputes remain in the record.

### Alternate 1: historical FEED backtest

Run on one closed FEED revision history. Compare findings with the field changes and errors that actually occurred. Use the result to test whether the narrow scope catches the problems that became expensive.

### Alternate 2: permit-readiness check

Run a focused compliance review against the applicable building code before a permit submission. The demand signal is Dubai Municipality building a system to issue permits automatically by reading submitted drawings against the Dubai Building Code. The product helps the owner arrive pre-compliant, without claiming to replace the regulator.

## Success metrics

### Business

- Design-caused rework avoided per project, validated against field changes.
- Review cycle measured against the deck's **6 weeks down to 3 days** example.
- Cost-avoidance return measured against the research range of **4:1 to 30:1**.
- Permit delay avoided, where a customer can validate it.

### Product

- Share of design revisions checked.
- Time from revision drop to cited result.
- Share of findings disputed and resolved.
- Share of findings accepted by the design manager.
- Design manager continues the existing revision habit rather than moving to a new system.

### AI

- Recall against a specialist's own findings and the field changes that followed.
- Invented-fact rate at zero tolerance for cited claims.
- Citation accuracy to the code clause and drawing region.
- Cost per document or revision read.

Targets for the product and AI measures above need validation on the first FEED backtest. The product remains advisory regardless of the measured score.

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
| Code coverage is thinner than promised | Narrow first release to one code edition and the disciplines that cause the most rework; publish what is in scope |
| A machine undermines professional pride | Advisory, never blocking; clause and drawing-region citations; one-click dispute |
| Wrong finding causes an expensive design change | Show source and confidence, retain human decision, and compare with a closed-project history first |
| The regulator moves faster than the product | Position this as owner-side preparation for the building-code reset, not as a replacement for a permit authority |

## Open questions needing validation

- [ ] Which building-code edition and jurisdiction should launch first? Needs validation with the first owner.
- [ ] Which disciplines cause the most rework in the target portfolio? Needs validation with the design / engineering manager.
- [ ] Which budget ceilings are available at each revision? Needs validation with the estimator and project director.
- [ ] Which drawing formats and regions can be cited reliably? Needs validation with engineering and the first FEED archive.
- [ ] What level of finding recall is useful without harming trust? Needs validation through the closed-project backtest.
