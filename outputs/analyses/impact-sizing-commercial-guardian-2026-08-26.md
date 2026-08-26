# Impact Sizing: Commercial Guardian (Asset Nova wedge)

Date: 2026-08-26 · Run non-interactively; all assumptions stated with confidence levels.
Sources: `context-library/research/Orbitron/cpm-agentic-ai-product-discovery.md` (all stats cited there), `outputs/roadmaps/asset-nova-strategy-and-roadmap.md`.
Note: business-info-template.md and metrics/ are empty; no internal baselines exist. This sizing uses industry data + explicit assumptions.

## What we're sizing

An agent that continuously reads contracts + the live project record (correspondence, schedules, reports) on capital megaprojects, detects compensable/claimable events, warns before contractual notice deadlines, and drafts notices with evidence chains. Human approves every outbound item. Two value lenses:

1. **Customer value** (what the pilot must prove)
2. **Orbitron revenue** (what the business case must show)

---

## Lens 1: Customer value per project

### Driver tree ($5B representative GCC megaproject, owner-side deployment)

```
$5B project capex
  ↓ × 33% = $1.65B potentially disputed (HKA CRUX avg on affected projects; conservative haircut to 20% → $1.0B)
  ↓ Commercial leakage addressable by better notice discipline + evidence:
      • Missed/late notices under time bars (entitlement lost entirely)
      • Weak substantiation (claims settled at discount)
      • Late detection (positions harden, disputes escalate to $60–91M avg, 12.5 months)
  ↓ Guardian intervention rate: agent surfaces 70% of trigger events vs ~40% caught manually today (assumption)
  ↓ Value capture on incremental events: 3–8% of at-risk value protected/recovered
  = $30M–$80M protected per project  (expected case: $50M)
```

### Scenarios per project

| Scenario | Key variable | Value protected | Multiple on $2M/yr license |
|---|---|---|---|
| Worst | Agent finds only what humans already catch; value = faster dispute prep only | $5–10M (avoided legal/consulting spend + settlement uplift on 1 dispute) | 2–5x |
| Expected | 1–2 material missed-notice saves + stronger substantiation across ~30 events/yr | ~$50M | ~25x |
| Best | One Kashagan-class save (single preserved entitlement or defeated claim) | $100M+ | 50x+ |

**The floor case still clears 10-15X ROI, which is Orbitron's published FlowNova claim. The pilot success metric should be dollar-denominated exposures surfaced, validated by the customer's contracts team.**

### Usage funnel (within one deployed project)

| Stage | Volume | Drop-off | Reason |
|---|---|---|---|
| Documents ingested | 100K–500K docs (Aconex archive + weekly increments) | — | Read-only export; no integration barrier |
| Candidate events detected | ~200–400/yr | — | Correspondence + schedule + daily report triggers |
| Events surfaced to humans (above confidence threshold) | ~100–150/yr | 60% | Precision filter; noise kills trust (see AI metrics in PRD) |
| Events reviewed by contracts team | ~90% of surfaced | 10% | Requires weekly review ritual; adoption risk |
| Notices/actions drafted | ~30–50/yr | — | Only where entitlement path exists |
| Approved & sent by humans | 70–85% of drafts | 15–30% | Draft quality + commercial judgment overrides |

Biggest funnel risk: **the review ritual**. If precision is low in week 1-4, the contracts team stops looking. This drives the AI engineering bar (precision > recall early).

---

## Lens 2: Orbitron revenue

### Funnel (GCC + adjacent, 24 months)

| Stage | Count | Assumption |
|---|---|---|
| Target accounts (GCC owner-operators + Tier-1 EPCs + PMCs) | ~40 | Aramco, ADNOC, QatarEnergy, PIF giga-projects, SABIC + 10 EPCs |
| Qualified conversations (vendor-registered, sponsor identified) | 12 | 30%; Orbitron's existing KSA presence accelerates |
| Paid pilots (3–6 months, 1–2 projects each) | 5 | 40%; pilot priced $300–500K |
| Convert to program license | 3 | 60%; pilot proves $ surfaced |
| Avg ACV at license | $1.5–3M/project-year | 0.05–0.1% of project value on $3–5B projects (half the 0.1–0.3% industry anchor, entry pricing) |

### Revenue scenarios (by end of year 2)

| Scenario | Pilots | Conversions | Projects live | ARR |
|---|---|---|---|---|
| Worst | 3 | 1 | 2 | ~$3M |
| Expected | 5 | 3 | 6 | ~$10–12M |
| Best (one Aramco program-wide deal) | 6 | 4 | 15+ | $25M+ |

Key sensitivity: **one program-wide owner deal changes everything** — Aramco's Jafurah-scale programs run 10+ EPC packages. Land one program, not one project.

---

## Assumption risk table

| Assumption | Confidence | Risk if wrong | De-risking action |
|---|---|---|---|
| 33% of capex disputed (HKA) generalizes to GCC megaprojects | Med | Overstates addressable leakage | Use customer's own claims history in pilot scoping; ME dispute values ($91M avg) suggest conservative |
| Agent detects 70% of trigger events at usable precision | Low | Product fails trust test | Retrospective backtest on a closed project's archive BEFORE live pilot — this is the single most important de-risk and doubles as the sales demo |
| 3–8% of at-risk value protected | Low | ROI story collapses to "faster paperwork" | Define pilot metric as exposures surfaced + validated by customer counsel, not recovery (recovery takes years) |
| Owners will share Aconex archives with a vendor | Med | No substrate, no product | In-region VPC/sovereign deployment from day 1 (SACS-002, PDPL); read-only exports lower the ask |
| Contracts teams adopt weekly review ritual | Med | Shelfware | Design agent output as their existing artifact (event register + notice log), not a new dashboard |
| $300–500K pilots land within project-team authority | Med | 18-month procurement cycles | Confirm delegation-of-authority thresholds per account; EPC contractors as faster wedge if owners stall |

## Recommendation

**Proceed.** Expected case: ~$50M/yr protected per project against a ~$2M license (25x ROI), with a worst case that still clears Orbitron's published 10-15X ROI bar. The two low-confidence assumptions (detection rate, value capture) are both de-riskable with one artifact: **a retrospective backtest on a completed project's document archive** — which is also the case-study demo. Strategic fit: dollar-denominated wedge that builds the substrate for Horizons 2-3 (EAC Reconciler, FID Red Team) per the roadmap.

**For the deck:** lead with "33% of capex ends up disputed; the average Middle East dispute is $91M and takes a year; most losses trace to notices missed and evidence scattered — problems of reading, not judgment."
