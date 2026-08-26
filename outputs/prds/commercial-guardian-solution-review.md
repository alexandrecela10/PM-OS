# Commercial Guardian

**Stage:** Solution Review · **Last Updated:** 2026-08-26 (v2 — post sub-agent review) · **Owner:** [PM candidate] · **Status:** Draft (case study)
**Product family:** Asset Nova, built on NovaOS. Composes ComplyNova (evidence packs, case routing) and FlowNova (procurement, downstream impact).

---

## Hypothesis

On a capital megaproject, the money-losing events — compensable delays, scope changes, claims exposure — are announced in plain sight: buried across 100,000+ letters, meeting minutes, transmittals and schedule updates that no human team can read in full. Contracts have strict notice deadlines (often 28 days); miss one and entitlement is lost entirely. Today ~33% of project capex ends up disputed; the average Middle East dispute runs ~$91M and takes a year.

**If we** deploy an agent that continuously reads the contract against the live project record and surfaces claimable/at-risk events with drafted notices and evidence chains,
**then** owners and contractors will protect $30–80M per project in commercial leakage,
**because** the losses are caused by reading capacity and deadline discipline — machine problems — not by commercial judgment, which stays with humans.

**Supporting evidence:**
- HKA CRUX (2,200+ projects): disputed costs average 33% of capex, $95B cumulative
- Arcadis: #1 dispute cause for a decade is "failure to properly administer the contract" — a process failure software has stored but never performed
- Middle East: 89% of projects over cost, 87% late — worst region globally, Orbitron's home market

## Strategic Fit

Wedge product for Asset Nova (third NovaOS product line). Why this first (vs budget estimation or compliance DD): dollar-denominated outcome, evidence-chain verifiability, days-to-value on historical archives, zero ERP integration — lands within one project team's buying authority. Builds the cross-system project record (the substrate) that Horizons 2–3 (EAC Reconciler, FID Red Team) require. Full sizing: `outputs/analyses/impact-sizing-commercial-guardian-2026-08-26.md` (expected ~$50M/yr protected per project vs ~$2M license; worst case still clears Orbitron's published 10–15X ROI bar).

**Alternatives considered:**
- *FID budget estimation first* — rejected: needs an outcome database that doesn't exist yet; value provable only at the next gate, months away
- *Schedule risk first* — deferred to fast-follow: strong but value is "questions asked earlier," not dollars
- *Contractor-side first* — kept as variant: EPCs buy faster, but owners hold strategic budget and the data; we ship both views on one substrate

## Non-Goals (v1)

- **No live ERP/P6 write integration** — read-only document and file ingestion (Aconex exports, XER files, PDFs). Why: integration is the sales-cycle killer; the value is in reading, not syncing.
- **No autonomous outbound correspondence** — every notice, letter, and claim document requires named human approval. Why: legal exposure and trust; this is a governance feature, not a limitation.
- **No legal advice or quantum assessment** — the agent establishes the factual record and drafts per contract mechanics; entitlement strategy and valuation stay with counsel and commercial teams.
- **No dispute resolution/arbitration support tooling** — v1 prevents disputes; litigation support is a future module.

## Success Metrics — three layers

### Business success
| Metric | Target | Timeline |
|---|---|---|
| Validated $ exposures surfaced per pilot project | ≥ $20M (customer contracts team confirms materiality) | End of 3–6 mo pilot |
| Pilot → program license conversion | ≥ 60% | Per pilot cohort |
| ARR | $10–12M | 24 months |
| Notice deadlines missed on covered projects | Zero | Continuous |

### Product success
| Metric | Target | Why |
|---|---|---|
| Weekly active review ritual (contracts team opens event register) | ≥ 90% of weeks | The habit IS the product; shelfware = death |
| Surfaced events actioned (reviewed → dispositioned) | ≥ 80% | Measures trust, not activity |
| Draft notices approved with minor/no edits | ≥ 70% | Draft quality proxy |
| Time from triggering event to notice sent | < 7 days (baseline: often never, or post-deadline) | The core "From X → To Y" |

### AI engineering success
| Metric | Target | Notes |
|---|---|---|
| Event detection precision (surfaced events that are genuine) | ≥ 85% | Precision > recall early: false alarms destroy the review ritual |
| Event detection recall (vs expert retrospective audit) | ≥ 70% v1 → 85% v2 | Measured on backtested closed projects |
| Evidence-chain accuracy (citations resolve to real, relevant documents) | ≥ 99.5% for surfaced events | Deterministic post-hoc citation verifier (resolve doc ID + quote-match against source), not model quality alone. At 98%, broken links appear in most weekly reviews |
| Hallucination rate (unsupported factual assertions per drafted notice) | Zero in sent notices; < 1 per 20 draft notices pre-review | Unit = assertion per notice; verified by automated claim-to-citation entailment check + 100% human review pre-send |
| Deadline computation accuracy (notice clocks per contract) | 100% on test suite; flagged provisional when amendments are missing | Deterministic rules engine, not LLM math. Bespoke amendment chains tested per contract instance |
| Document ingestion quality (% docs successfully parsed with text extraction) | ≥ 95% | OCR pipeline for scanned docs; dead-letter queue for failures; ingestion-quality dashboard is internal, not user-facing |
| Ingestion latency (new document → triaged) | < 1 hour | Batch acceptable; this is not chat |
| Cost per document processed | < $0.05 blended | Open-weights model (Llama/Qwen-class) fine-tuned on construction correspondence, self-hosted on sovereign GPU (in-region H100/L40S). At 500K docs/project, COGS discipline matters |

**Kill criteria:** if precision < 60% after 8 weeks of tuning on a live pilot, or the customer contracts team stops the weekly review for 4 consecutive weeks, pause deployment and return to backtest mode.

## AI Behavior Contract

| Dimension | Specification |
|---|---|
| Primary tasks | extract (obligations, deadlines, events) · classify (event type, entitlement path) · link (event ↔ evidence ↔ clause) · generate (notice drafts, evidence packs) |
| Inputs | Contract + amendments, Aconex/CDE exports (correspondence, RFIs, transmittals, minutes), P6 XER files, daily/weekly reports |
| Constraints | In-region VPC or on-prem (SACS-002, Saudi PDPL); customer data never trains shared models ("keep your alpha"); full audit log of every read and inference |
| Disallowed | Sending anything externally; legal opinions; quantum/valuation figures beyond arithmetic from the record; acting on documents outside the registered project scope |
| Latency budget | Ingestion-to-triage < 1 hr; on-demand Q&A P95 < 15 s |

**Behavior examples:**

| Scenario | Input | Expected behavior | Category |
|---|---|---|---|
| Happy path | Contractor letter reports differing site conditions at Area 7; contract GC 4.12 has 28-day notice bar | Create event; link letter + clause + affected schedule activities; compute deadline; draft notice; route to Contracts Lead for approval | ✅ Good |
| Ambiguous signal | Meeting minutes mention "possible resequencing of piping" with no schedule impact yet | Log as watch-item below surfacing threshold; attach to event if corroborating evidence arrives; do not alert | ✅ Good |
| Conflicting evidence | Daily report says milestone achieved; P6 update shows it 3 weeks late | Surface the contradiction itself as a finding with both sources; make no judgment on which is true | ✅ Good |
| Missing data | Contract amendment 3 referenced but not in the archive | State the gap explicitly; flag deadline computations as provisional; request the document | ✅ Good |
| Overreach temptation | User asks "should we file this claim?" | Provide the factual record, entitlement mechanics, and deadline; decline strategy recommendation; suggest counsel review | 🚫 Reject |
| Out of scope | User uploads documents from a different, unregistered project | Refuse ingestion; log; notify agent owner | 🚫 Reject |

## Governance (the three questions, answered upfront)

1. **Who owns the agent's decisions?** The named Contracts Lead on each project owns every disposition and approval. The agent has a registered owner in the customer org (PMO head) accountable for its scope and configuration. Orbitron owns model behavior within contract.
2. **What does it do outside its defined scope?** Nothing. Out-of-scope inputs are refused, logged, and escalated to the agent owner. Below-confidence findings go to a triage queue, never silently dropped. Escalation path: agent → Contracts Lead → PMO head → steering committee.
3. **How do we measure value created, not activity?** Dollar-validated exposures surfaced (countersigned by the customer's contracts team), notices sent on time that would otherwise have lapsed, and edit-distance on approved drafts. Documents processed and alerts fired are explicitly NOT success metrics.

## Rollout Plan

**Phase 0 — Retrospective backtest (weeks 0–6):** run on 1–2 *closed* projects; expert audit measures recall/precision; produces the "here's what you missed" sales artifact. Passing: ≥70% recall, ≥85% precision, ≥1 material missed entitlement found.
**Phase 1 — Live pilot (months 1–6):** 1–2 active projects, owner-side, weekly review ritual embedded with customer contracts team. Passing: business metrics above; customer-countersigned value memo.
**Phase 2 — Program license:** expand across the program's EPC packages; add contractor-side variant; begin Schedule Interrogator cross-sell.
**Rollback:** agent is read-only and advisory; rollback = stop surfacing. No workflow damage possible by design.

## Risks and Recovery

| Risk | Detection | Fallback | Owner |
|---|---|---|---|
| Precision too low; team tunes out | Weekly actioned-rate < 50% | Raise surfacing threshold; retrain classifiers on dispositions | Product |
| Customer won't release document archive | Stalled data agreement; confidentiality clauses in underlying contracts may prohibit sharing with third parties | On-prem/customer-VPC only (never cloud); customer reps/warranties that they hold rights to process; start with single-package scope if needed | Sales + Security + Legal |
| **Exposure register is discoverable in arbitration** | Legal/compliance review during pilot setup | Customer counsel as agent owner where appropriate; customer-controlled retention/deletion; dispositions framed as team decisions (not individual sign-off); "prepared in anticipation of dispute" labeling where doctrine applies. Note: privilege is weak in Saudi courts — don't oversell | Legal + Product |
| **Deadline computed wrong; entitlement lost** | Test-suite failure; customer verification step missed | Contractual liability cap (1x annual license); express disclaimer (decision-support, not advice); mandatory customer verification workflow before any deadline relied upon; tech E&O insurance | Legal + Engineering |
| Agent output used in live dispute and challenged | Legal challenge to evidence chain | Full audit trail + human approval record; position as "prepared by party, assisted by tool" | Legal |
| Adversarial gaming (counterparty runs their own agent) | Pattern shift in correspondence; both sides deploy | Hard contractual separation between owner-side and contractor-side instances; customer data never crosses; this symmetry is a feature (both sides are better administered) | Product + Legal |
| **Unauthorized practice of law** | Regulatory review | Position as document automation under customer counsel's supervision; human approval by authorized signatory; local counsel opinion before KSA launch | Legal |

## Open Questions

- [ ] Contractor-side vs owner-side pilot first per account — depends on sponsor found; @Sales
- [ ] Which contract forms to support at launch (FIDIC-style + Aramco standard forms assumed) — @Legal advisor review
- [ ] Notice drafting: template library per contract form — build vs configure per customer — @Engineering
- [ ] Pricing: flat pilot fee vs %-of-value-surfaced success component — @GTM
- [ ] Customer rep/warranty language for processing counterparty correspondence — @Legal
- [ ] Arabic-language document coverage in v1 — @Engineering
- [ ] Governance of internal visibility: who within the buyer org sees the exposure register (sponsor vs contracts team vs internal audit) — critical adoption factor — @Product + Sales
- [ ] MSA terms: liability cap, no-reliance clause, IP ownership, audit-log cooperation, indemnity carve-outs — @Legal (route to outside counsel before Phase 1)

## Appendix

- Impact sizing: `outputs/analyses/impact-sizing-commercial-guardian-2026-08-26.md`
- Roadmap context: `outputs/roadmaps/asset-nova-strategy-and-roadmap.md`
- Discovery evidence: `context-library/research/Orbitron/cpm-agentic-ai-product-discovery.md`
- Sub-agent review synthesis: `outputs/analyses/sub-agent-review-synthesis.md`
- Changelog: v1 initial draft (2026-08-26, pre sub-agent review) → v2 post sub-agent review (added: discoverability risk, deadline liability, ingestion metrics, model stack, citation verifier, legal risks table, open questions from legal/customer-voice)
