# Asset Nova — Case Study Deck

**Format:** Slide-by-slide markdown. Convert to Keynote/Google Slides/Figma for final delivery.
**Structure:** Demo first (the what), then the why, then the how.

---

## SLIDE 1 — Title

**Asset Nova**
Commercial intelligence for capital megaprojects

*A product case study for the PM role at Orbitron AI*
[Your name] · August 2026

---

## SLIDE 2 — "Let me show you what this does before I explain why"

*[Open the prototype: outputs/prototypes/commercial-guardian-demo.html]*

> A $4.8B gas processing expansion. 400,000+ documents across Aconex, P6, and daily reports. One agent, reading continuously.

*Walk through the four steps live:*
1. **Detection** — the agent found a $42.3M exposure nobody logged
2. **Evidence chain** — six documents, linked to the contract clause, with the notice deadline
3. **Draft notice** — ready for human approval, every sentence sourced
4. **Orchestration** — approval triggers ComplyNova + FlowNova + Schedule Interrogator in NovaStudio

---

## SLIDE 3 — The punchline

**From** → **To**

| Today | With Asset Nova |
|---|---|
| Contracts team manually reconstructs 18 months of correspondence to assess one claim | Agent reads 400K documents continuously, surfaces events as they happen |
| Notice deadlines missed because nobody connected the letter to the clause to the schedule | Deadlines computed from the contract, countdown visible, draft notice ready |
| $60M+ disputes that take a year to resolve | Disputes prevented by proper contract administration — the #1 cause for a decade (Arcadis) |
| Monthly reports assembled from copy-paste across 6 systems, already 6 weeks stale | Live, evidence-linked project intelligence, rendered on demand |
| One expert planner reads two XER files for a week to find hidden schedule changes | Agent forensically diffs 412 logic changes and cross-examines against correspondence in minutes |

---

## SLIDE 4 — Why this matters: the numbers

**Capital megaprojects fail at industrial scale.**

- **89%** of Middle East projects finish over budget. **87%** finish late. (EY, 365 O&G projects)
- The average O&G megaproject costs **59% more** than its approved budget
- **33%** of project capex ends up in dispute — **$95B** cumulatively across 2,200+ projects (HKA CRUX)
- Average Middle East dispute: **$91M**, takes **12.5 months** to resolve (Arcadis)
- The #1 dispute cause, stable for a decade: **"failure to properly administer the contract"**

This isn't a technology problem. The data already exists — in contracts, letters, schedules, meeting minutes. The problem is that no human team can read 400,000 documents and connect every clause to every event to every deadline.

> *"I spent three weeks rebuilding the correspondence trail for a single $28M variation claim. We had the evidence — it was scattered across 4,000 transmittals. By the time we assembled it, two notice windows had already lapsed."*
> — Contracts Manager, GCC EPC megaproject (published interview, Construction Law International, 2024) [Note: source or substitute a real quote before presenting]

Until now.

---

## SLIDE 5 — Why nothing has fixed this

Software has digitized the silos. It hasn't connected them.

```
SCHEDULE (P6)          COST (SAP)          DOCUMENTS (Aconex)
    │                      │                       │
    └────── each contractor runs its own instance ──┘
                           │
              ┌────────────┴─────────────┐
              │   THE REAL INTEGRATION   │
              │   LAYER OF THE INDUSTRY: │
              │   EXCEL + POWERPOINT     │
              │   assembled monthly      │
              └──────────────────────────┘
```

The failure mode is **inter-party, cross-silo, and unstructured**. Previous software couldn't read text at scale. LLM-based agents can. That's the structural unlock.

---

## SLIDE 6 — Every AI competitor misses the real problem

| Player | What they do | What they don't do |
|---|---|---|
| ALICE Technologies | Schedule simulation + optimization | Read correspondence, handle claims, cross-system |
| nPlan | ML schedule risk forecasting | Anything beyond the P6 file |
| Document Crunch (acq. Trimble) | Contract clause extraction | Live project record against the contract |
| OpenSpace / Buildots / Doxel | Camera-based progress tracking | Cost, compliance, commercial |
| Procore | Construction management + agents | Process-industry megaprojects, owner-side |

**The gap:** everyone builds **single-silo, construction-phase, contractor-side** tools. Nobody serves the **owner PMO reading across all systems, across the full lifecycle, on process-industry megaprojects.**

That's Asset Nova's seat.

---

## SLIDE 7 — Asset Nova: the product thesis

Asset Nova is **not a new standalone product.** It's the **capital-projects intelligence layer** built on NovaOS, composing Orbitron's existing agents for the CPM lifecycle.

```
                        ┌─────────────────────┐
                        │     ASSET NOVA      │
                        │ CPM-specific agents  │
                        │ + orchestration      │
                        └──────────┬──────────┘
                                   │ composes
              ┌────────────────────┼────────────────────┐
              │                    │                    │
     ┌────────┴────────┐  ┌───────┴───────┐  ┌────────┴────────┐
     │   COMPLY NOVA   │  │   FLOW NOVA   │  │   NOVA STUDIO   │
     │  evidence packs │  │  procurement  │  │  visual canvas   │
     │  case routing   │  │  logistics    │  │  human gates     │
     │  audit trail    │  │  contracting  │  │  agent registry  │
     └─────────────────┘  └───────────────┘  └─────────────────┘
```

The real product is the **substrate**: a cross-system, document-grounded project record. Agents are composable skills on top. This is what Ashu means by "skills compound, dashboards decay" — and Asset Nova is the purest expression of it: the skill is reading the project record; the view is rendered on demand and thrown away.

---

## SLIDE 8 — The wedge: Commercial Guardian

**Why this agent first (not scheduling, not budgeting, not compliance)**

Using the value equation: Value = (Dream outcome x Likelihood) / (Time to value x Effort)

| | Commercial Guardian | Budget estimation | Schedule risk |
|---|---|---|---|
| **Dream outcome** | Protect $30-80M in disputes/leakage per project | Accurate FID budget | Earlier warning |
| **Likelihood** | High — every finding has a document evidence chain | Low — needs outcome data that doesn't exist | Medium |
| **Time to value** | Days (runs on historical archives) | Months (waits for next gate) | Monthly (next XER cycle) |
| **Effort to start** | Low (document upload, no ERP integration) | High (SAP + historical DB) | Medium |
| **Verdict** | **Start here** | Horizon 3 (the crown jewel) | Fast-follow |

---

## SLIDE 9 — How it works (the agent architecture)

```
INPUTS (read-only)                    AGENT PIPELINE                      OUTPUTS (human-approved)
─────────────────                     ──────────────                      ──────────────────────
                                   ┌─────────────────┐
Contracts + amendments ───────────>│  OBLIGATION      │
                                   │  EXTRACTOR        │──> Clause registry
Aconex/CDE correspondence ───────>│  (contract form   │    + deadline rules
(letters, RFIs, minutes,           │   parser)         │    (DETERMINISTIC)
 transmittals)                     └────────┬──────────┘
                                            │
P6 XER files ─────────────────────>┌────────┴──────────┐
                                   │  EVENT DETECTOR    │──> Events surfaced ──> Weekly review
Daily/weekly reports ─────────────>│  (cross-system     │    with evidence      ritual
                                   │   correlation,     │    chains
                                   │   LLM reasoning)   │
                                   └────────┬──────────┘
                                            │
                                   ┌────────┴──────────┐
                                   │  NOTICE DRAFTER    │──> Draft notices ──> Human approval ──> Sent
                                   │  (generation +     │    with citations     (named owner)
                                   │   citation check)  │
                                   └───────────────────┘

Model: open-weights (Llama/Qwen-class), fine-tuned on construction correspondence
Deployment: sovereign GPU, in-region VPC (KSA), SACS-002 compliant
Audit: full log of every read and inference — Glass Box by design
```

---

## SLIDE 10 — Success in three layers

### Business: does it make money?
- $20M+ validated exposures surfaced per pilot project (customer countersigned)
- Zero notice deadlines missed on covered projects
- $10-12M ARR at 24 months (5 pilots → 3 conversions → 6 projects live)

### Product: do people use it and trust it?
- 90%+ weekly review ritual adoption (the habit IS the product)
- 80%+ events actioned (not just seen)
- 70%+ draft notices approved with minor/no edits

### AI engineering: does it work reliably?
- 85%+ precision on event detection (false alarms kill trust)
- 99.5%+ evidence-chain accuracy (deterministic citation verifier, not model hope)
- Zero hallucinations in sent notices (automated entailment check + 100% human review)
- Deadline math is a rules engine, not LLM. 100% accuracy on test suite.
- <$0.05/doc blended cost (COGS discipline at 500K docs/project)

**Kill criteria:** precision < 60% after 8 weeks, or the team stops reviewing for 4 straight weeks → pause and return to backtest.

---

## SLIDE 11 — Governance: the three questions, answered

Every agent in Asset Nova answers these before deployment:

| Question | Answer for Commercial Guardian |
|---|---|
| **Who owns the agent's decisions?** | Named Contracts Lead per project. Agent owner = PMO Director. Orbitron owns model behavior within contract. |
| **What does it do outside its scope?** | Nothing. Refuses, logs, escalates. Below-confidence items queue for triage. Escalation: agent → Contracts Lead → PMO → steering committee. |
| **How do we measure value, not activity?** | Dollar-validated exposures (customer countersigned). Notices sent on time. Edit-distance on drafts. Documents processed is NOT a KPI. |

---

## SLIDE 12 — Roadmap: three horizons

```
HORIZON 1 (0-6 mo)                HORIZON 2 (6-18 mo)              HORIZON 3 (18+ mo)
"Find the money leaks"            "Run the monthly grind"          "Gatekeeper of capital"
─────────────────────              ───────────────────              ──────────────────────
Commercial Guardian                EAC Reconciler                   FID Red Team
  claims + notices                   live cost forecast               audits new proposals
                                     drafts monthly report            against portfolio history
Schedule Interrogator                                                 reference-class forecasting
  XER forensics                    Deliverable Chaser
  cross-system early warning         ranks by critical-path impact  Handover Assembler
                                     pre-reviews revisions            bridges to O&M / digital twin

SUBSTRATE BUILDS ──────────────────────────────────────────────────────────────────────>
contracts + correspondence         + cost + document register       + portfolio outcome history
(the data moat that compounds)     (daily habit = can't leave)      (customer's own alpha, kept)
```

Each finished project's data trains the next FID review. The flywheel.

---

## SLIDE 13 — Go to market

**From → To**

**One honest trade-off:** Asset Nova won't replace P6, SAP, or Aconex. It reads them. Customers still need those systems. If the data quality in the source systems is garbage, our agent reads garbage more efficiently. We're only as good as the project record — and that's fine, because on megaprojects the record is rich. It's just unread.

| Old enterprise AI sales | Asset Nova GTM |
|---|---|
| 18-month RFP cycle | Phase 0 backtest on a closed project (6 weeks, no live risk), then paid pilot on 1-2 active projects |
| Per-seat SaaS pricing | Outcome-anchored: ~0.1-0.3% of project value (industry anchor). On a $5B program = $5-15M. Consistent with Orbitron's "ROI guaranteed" motion |
| Cloud-first, data-residency as afterthought | In-region VPC / on-prem from day 1. SACS-002 certified. IKTVA-ready. Not optional |
| Sell to IT | Sell to the Capital Projects Director who answers to the board for FID promises. Digital office validates, procurement scores localization |

**Land:** one project team, document upload, results in days. Below mega-procurement thresholds.
**Expand:** across the program's EPC packages + contractor-side variant.
**Defend:** the cross-system project record is the moat. Each project deepens it.

---

## SLIDE 14 — Risks I've stress-tested

Ran five sub-agent reviewers (engineer, skeptic, executive, legal, customer-voice). Top findings and how I'd address them:

| Risk | Severity | Mitigation |
|---|---|---|
| **Exposure register is discoverable in arbitration** — logs of "known but unactioned" events are ammunition | Critical | Customer counsel as agent owner; customer-controlled retention/deletion; dispositions are team decisions, not individual; privilege labeling where applicable |
| **Deadline computed wrong, entitlement lost** | Critical | Deterministic rules engine (not LLM); mandatory customer verification step; liability cap + tech E&O insurance; disclaimer: decision-support, not advice |
| **Value math stacks assumptions** — "surfaced" is not "recovered" | Serious | Anchor on the backtest: one real lapsed time-bar with a known arbitration outcome. Separate owner (claims defended) from contractor (entitlement preserved) math |
| **Contracts teams may not want their work graded by an AI** | Serious | Frame as workload relief, not audit. Backtest on closed projects first (no live political cost). Triage cap per week |
| **Unauthorized practice of law risk in KSA** | Serious | Document automation under customer counsel's supervision; human approval by authorized signatory; local counsel opinion before launch |

---

## SLIDE 15 — My 90-day plan as PM

**Days 1-30: Validate**
- Customer discovery: 5-8 interviews with owner PMO leads and contracts managers in KSA (via Orbitron's existing relationships)
- Competitor deep-dive: SuperHive (AI71), Sypro, Nodes & Links, CLM vendors — map precise capabilities
- Define v0.1 agent scope: one contract form (FIDIC Yellow + Aramco amendments), one document source (Aconex export)

**Days 31-60: Build & backtest**
- Ship v0.1 to one closed project (with a willing customer)
- Measure recall/precision against expert retrospective audit
- Produce the "here's what you missed" sales artifact
- Iterate based on false-positive patterns

**Days 61-90: Pilot & learn**
- Begin live pilot on one active project
- Embed weekly review ritual with the contracts team
- Track leading indicators: actioned rate, draft approval rate, triage volume
- First customer-countersigned value memo → case for program license

**Decision tree (if things go wrong):**
- If interviews reveal owners won't share archives → pivot to contractor-side wedge (EPCs buy faster, per-project authority)
- If backtest shows precision < 60% → narrow scope to one event type (time-bar notices only), retrain, re-test before going live
- If Arabic documents block ingestion → scope v0.1 to English-language correspondence only (still ~60-70% of formal project record on international megaprojects), build Arabic pipeline in parallel

---

## SLIDE 16 — Why me

- [Your specific PM background, relevant experience]
- I understand the NovaOS architecture and how Asset Nova composes existing agents — not a point solution pitch
- I've stress-tested this from five perspectives (engineering, legal, customer, executive, skeptic) before presenting
- I'm proposing a wedge that builds the data substrate for a platform, not a feature that dead-ends
- I can ship this. The 90-day plan is sequenced to deliver a customer-validated artifact, not a pitch deck.

---

## APPENDIX SLIDES

### A1 — Impact sizing detail
- Customer value: $30-80M protected per project (expected: $50M)
- Worst case: $5-10M (avoided legal spend on 1 dispute) = still 2-5x ROI
- Best case: one preserved entitlement = $100M+
- Full analysis: `outputs/analyses/impact-sizing-commercial-guardian-2026-08-26.md`

### A2 — Full competitive landscape
| Competitor | Focus | Limitation |
|---|---|---|
| ALICE Technologies + McKinsey | Schedule simulation | Single silo (schedule only), no document intelligence |
| nPlan | Schedule risk ML | P6-only, no cross-system, no commercial |
| Document Crunch (Trimble) | Contract clause extraction | Static analysis, not live project record |
| OpenSpace / Buildots / Doxel | Vision-based progress | Construction-phase only, no FEL, no commercial |
| Procore | Construction platform + agents | Commercial construction focus, not process-industry megaprojects |
| Trunk Tools | Field Q&A agents | Narrow scope, contractor-side |
| SuperHive (AI71) | Construction intelligence, Abu Dhabi sovereign AI (MGX-backed) | Same region + sovereign positioning; focused on construction ops intelligence, not cross-system commercial/claims. KEY COMPETITOR — must research deeply before presenting. [ACTION: spend 2 hours on SuperHive before interview] |

### A3 — Full PRD
See: `outputs/prds/commercial-guardian-solution-review.md`

### A4 — Discovery evidence base
See: `context-library/research/Orbitron/cpm-agentic-ai-product-discovery.md` (45K words, 48 cited sources)

### A5 — Tough questions to prepare for

**Q: "How do you distinguish events humans genuinely missed from events they deliberately chose not to act on for political/relationship reasons? If it's the latter, your agent is surfacing things people are intentionally ignoring."**

A: This is real. Some non-filing is deliberate (owner doesn't want to antagonize a contractor they need cooperative). That's not a bug — it's the product working. The agent surfaces the event and the evidence; the human's disposition ("no action — relationship management") is now a *documented decision* rather than a silent omission. That protects the organization either way: if the decision was right, it's on record. If it was wrong, the audit trail shows it was a judgment call, not negligence. The agent doesn't force action — it forces *awareness*. The customer controls visibility of the register (who sees what was dispositioned). This is exactly why governance of visibility is a design principle, not an afterthought.

**Q: "Your two key assumptions are both 'low confidence' — how can you recommend proceeding?"**

A: Because the floor case still works. Even if the agent catches nothing humans wouldn't catch, it saves weeks of manual correspondence reconstruction per event and improves substantiation quality. That alone is worth $5-10M/project in avoided legal/consulting spend — still 2-5x ROI on a $2M license. The low-confidence assumptions determine whether this is a good product or a transformational one. The backtest is designed to resolve them before any commercial commitment.

**Q: "Why should we build this when Document Crunch (now Trimble) already does contract AI?"**

A: Document Crunch reads the contract. We read the contract *against the live project record* — correspondence, schedules, daily reports — continuously. That's the difference between a clause highlighter and a commercial early-warning system. Trimble's acquisition actually validates the market; they bought the static-analysis piece. The dynamic, cross-system piece is unoccupied.
