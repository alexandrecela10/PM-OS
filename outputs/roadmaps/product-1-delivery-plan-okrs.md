# Product 1 delivery plan: Asset Nova Claims Defence and Recovery

**Date:** 2026-08-27
**Product:** Asset Nova Claims Defence and Recovery (always-on agent, owner side, build phase)
**Reference scenario:** Jebel Nasr Train 4, Faisal Al-Harbi's team. See `outputs/asset-nova-round2-agentic-and-scenario.md`.
**Companion docs:** `outputs/prds/product-prd-claims-defence-recovery.md`, `outputs/prds/ai-engineering-prd-claims-defence-recovery.md`

## The one-sentence plan

Four phases in twelve months, each ending on a gate that can stop the programme: prove the reading on a closed archive, run silently beside a live team, get paid for one project, then repeat it on three more. The eval gates in the deck are the phase exits, so the delivery plan and the quality bar are the same document.

**Annual objective.** Turn one owner's closed archive into a paid, renewed, referenceable claims defence deployment, with the money kept counted by the customer and not by us.

**Annual key results.**

| KR | Target | Source of truth |
|---|---|---|
| KR1 | One paid pilot signed by day 90, at $250k or more | Signed order |
| KR2 | $20M or more of exposures surfaced and countersigned by the customer within the pilot | Customer-countersigned exposure register |
| KR3 | Zero notice deadlines missed on covered scope, all year | Deadline audit against the record |
| KR4 | Pilot converts to a multi-project contract of $2M or more by month 12 | Signed contract |
| KR5 | Two more owners in paid pilot by month 12 | Signed orders |

Sequencing rule: no phase starts before the previous gate passes. If a gate fails, we spend the next four weeks fixing it rather than starting the next phase, and we say so out loud.

---

## Phase 1, weeks 1 to 6. Prove the reading

**Objective.** Show that the agent reads one owner's closed project better than a person could in the time available, with nothing invented.

**Key results**

| KR | Target |
|---|---|
| Documents read and correctly typed on the closed archive | 98% or better |
| Dates extracted correctly | 99.5% or better |
| Documents refused and queued for a human, reported openly | Under 5% of volume |
| Invented facts | Zero. One occurrence fails the phase |
| Golden set built from the closed project, agreed with the customer's own commercial lead | 200 labelled events or more |

**What we build.** Ingestion for the five source types in the scenario (contract and amendments, correspondence export, minutes, daily site reports, P6 update). Document typing and date extraction. The linked project record. The deterministic notice-window, damages and quantum-bounds engine, with unit tests as the specification. No user interface beyond an internal review tool.

**Team.** Two engineers on ingestion and the record, one on the rules engine, one PM on the golden set with the customer, part-time counsel review.

**Dependencies we must have.** One closed project archive under a read-only agreement, one named commercial lead who will label events with us, and an in-region environment.

**Exit decision.** Gate 0 from the deck. Fail means the record has holes, and we fix reading before touching findings.

---

## Phase 2, weeks 7 to 14. Prove the findings

**Objective.** Show that what the agent proposes is worth a commercial manager's attention, and that it knows when to keep quiet.

**Key results**

| KR | Target |
|---|---|
| Precision on items shown as findings | 85% or better |
| Recall against what the commercial team actually found on that closed project | 80% or better |
| Material items the team missed, found and cited | At least one |
| Evidence chain accuracy, every cited page says what the finding claims | 99.5% or better |
| Deadline arithmetic | 100%, because it is code |
| Low-confidence items presented as "watching" rather than as findings | 100% |

**What we build.** Event-to-clause mapping, evidence selection, the money estimate as visible arithmetic, the confidence model, the citation veto that drops any uncited finding, and the ranked queue screen. Drafting starts here in rough form.

**Team.** Same, plus one applied AI engineer on evals.

**Exit decision.** Gate 1. Stop rule: precision below 60% after eight weeks of tuning sends us back to Phase 1 instead of forward.

**Commercial track running in parallel.** Ten discovery interviews, and the $400M claims-submission assumption validated against a real portfolio. That assumption underwrites the whole ROI story, so it gets checked before it is quoted to a buyer.

---

## Phase 3, weeks 15 to 26. Prove a human agrees, then get paid

**Objective.** Put the agent beside a live team, in shadow mode with nothing sent, and earn the right to charge.

**Key results**

| KR | Target |
|---|---|
| Findings actioned rather than only seen | 80% or better |
| Drafts approved with light edits or none | 70% or better |
| Override rate | Falling week on week |
| Weeks where the digest was ignored two days running | Under 10% |
| Cost per document read | Under $0.05 blended |
| Paid pilot signed, money-kept metric agreed in writing before start | By day 90 |

**What we build.** The morning digest into email and Teams, the decision and routing flow (approve, edit, reject, route to counsel), drafting in the owner's own templates, the outcome tracker, and the month-end brief on demand. Compliance work runs alongside: in-region private cloud, permissions mirroring the commercial team, the read audit trail, cyber certification and local content paperwork.

**Team.** Add one engineer on the digest and drafting surface, one delivery lead in-region.

**Exit decision.** Gate 2, plus a signature. Stop rule: four straight weeks without review pauses the pilot, because silence is the real churn signal.

---

## Phase 4, months 7 to 12. Prove it changed the money, then repeat

**Objective.** Show money kept that the customer will put their name to, and turn one project into a portfolio.

**Key results**

| KR | Target |
|---|---|
| Exposures surfaced and countersigned | $20M or more on the pilot project |
| Money kept or recovered against the pre-agreed metric | Beats the pilot fee by 5x or better |
| Notice deadlines missed | Zero |
| Findings that survived to settlement | Reported honestly, including the ones that did not |
| Conversion to a multi-project contract | $2M or more signed |
| New owners in paid pilot | Two |

**What we build.** Multi-project deployment, the portfolio view for the sponsor, learning from recorded dispositions and settlements, and the second contract form family.

**Exit decision.** Gate 3. A pass here is the case study that sells Product 2.

---

## How we will know early, not late

Leading indicators, watched weekly, because the lagging ones arrive too late to act on.

| Leading | Why it predicts | Lagging it predicts |
|---|---|---|
| Share of the digest opened within two hours | Attention is the first thing to go | Actioned rate, then renewal |
| Edits per approved draft | Rising edits mean the drafting is drifting | Drafts approved with light edits |
| Time from a document landing to a human decision | The product's whole claim is speed against a deadline | Deadlines missed |
| Watching-to-finding promotion rate | Tells us whether the confidence model is honest | Precision |
| Cost per document | A product that reads everything daily has to be cheap | Gross margin |

Honest counter-metrics we report even when they look bad: override rate, false alarm rate, and how often the team went back to their own spreadsheet.

## What we are deliberately not doing this year

- No writing back into ERP, P6 or Aconex.
- No autonomous sending, in any phase.
- No second product before Gate 2 passes.
- No third language beyond English and Arabic document handling.
- No self-serve. This is a named-account product with a delivery lead.

## Risks that could break the plan, and the response

| Risk | Response |
|---|---|
| No closed archive is released, so Phase 1 cannot start | Make the archive a condition of the discovery agreement, and offer to work on a redacted subset |
| The customer's commercial lead has no time to label the golden set | Buy the time: pay for their quantity surveyor's hours as part of the phase |
| Precision plateaus below the gate | The stop rule exists on purpose. Return to reading quality rather than shipping a noisy queue |
| Legal blocks processing counterparty correspondence | Counsel involved from week 1, customer-controlled retention, privilege labelling, and no overselling of privilege |
| Buying gates in the Gulf delay the pilot signature | Compliance runs in parallel from Phase 1, not at the end |
| The $400M assumption does not hold on real data | Reprice the pilot against the real number before quoting it. The story survives a smaller number, it does not survive a wrong one |

## Open decisions I need from you

- [ ] Is the pilot price flat, value-based, or part success fee?
- [ ] Which owner is Phase 1, and do we already have a route to their closed archive?
- [ ] Are we willing to pay for the customer's labelling time in Phase 1?
- [ ] Does Product 2 start in parallel at Phase 3, or strictly after Gate 3?
