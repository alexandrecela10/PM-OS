# Asset Nova — Strategy Decision & Long-Term Roadmap

Status: working draft for case study. Sources: `context-library/research/Orbitron/cpm-agentic-ai-product-discovery.md` + `outputs/analyses/orbitron-context-synthesis.md`. Date: 2026-08-26.

## Strategic thesis (agreed)

- Every AI competitor in capital projects is construction-phase, single-silo, contractor-side. The open seat: **owner-side, cross-system, full-lifecycle intelligence** for process-industry megaprojects. Middle East = worst pain globally (89% over cost, 87% late) = Orbitron's home turf.
- The real product is the **substrate**: a cross-system, document-grounded project record (contracts, correspondence, schedules, costs, registers). Agents are composable skills on top — pure NovaOS architecture, "skills compound, dashboards decay."
- Asset Nova composes existing Orbitron agents: ComplyNova (evidence packs, case routing, audit) and FlowNova (procurement, expediting, contracting, control tower).

## Wedge decision (Hormozi value equation)

**First product: Commercial Guardian** ("money-leak detector") — reads contracts + live project record continuously, detects compensable events/claims exposure, warns before contractual notice deadlines, drafts notices with evidence chains, human approves.

Why it wins: dollar-denominated dream outcome (33% of capex disputed, $60M avg dispute) × provable likelihood (document evidence chains) ÷ days-to-value (runs on historical files) × minimal effort (read-only document ingestion, no ERP integration, lands within one project team's buying authority).

Deprioritized as wedge (kept in roadmap): budget estimation (needs outcome database that doesn't exist yet) and compliance DD (ComplyNova already covers the GRC flavor; CPM-specific compliance folds into Guardian + later phases).

## Roadmap — three horizons

### Horizon 1: Land (months 0–6) — "Find the money leaks"
- **Commercial Guardian** (owner + contractor variants)
- **Schedule Interrogator** — forensic XER diffing + cross-examination against procurement/correspondence; "10 questions to ask the contractor this month"
- Deployment: in-region VPC/sovereign, document-based, paid pilot on 1–2 live projects, success metric = $ exposures surfaced
- Substrate v1 built as a byproduct: contracts + correspondence + schedules indexed and linked

### Horizon 2: Expand (months 6–18) — "Run the monthly grind"
- **EAC Reconciler** — live cost forecast reconciling SAP, contractor claims, trend registers; drafts monthly cost report. Daily-retention workhorse; integrations deepen the moat
- **Deliverable Chaser** — ranks overdue documents by critical-path impact, pre-reviews revisions, drafts chase correspondence
- Substrate v2: cost + document register joined to the record; agent skills registered/versioned in NovaStudio

### Horizon 3: Differentiate (months 18+) — "Gatekeeper of capital"
- **FID Red Team** — audits front-end definition packages, reference-class forecasting against the owner's own portfolio history ("your productivity assumption exceeds the P90 of comparable Gulf projects"). No competitor touches FEL. Speaks to boards. Customer's own history = compounding data moat ("keep your alpha")
- **Handover Assembler** — tag-level completeness auditing, vendor dossier classification; bridge into O&M/digital twin market and future brownfield projects
- Asset Nova becomes the capital-allocation gatekeeper, closing the full lifecycle loop (each finished project trains the next FID review)

## Commercial model
- Outcome-anchored pricing (industry anchor: 0.1–0.3% of project value → 8-figure potential on $10B programs), consistent with Orbitron's "ROI guaranteed" motion
- KSA-first: IKTVA localization, SACS-002 cybersecurity cert, in-Kingdom data residency, pilot below mega-procurement thresholds

## Case study demo plan (36h)
1. Live prototype: Commercial Guardian finds a $40M exposure with a 6-day notice deadline in a correspondence archive, drafts the notice with evidence chain, human approves
2. One orchestration scene: Guardian's finding triggers ComplyNova (evidence pack) + FlowNova (downstream impact) in a NovaStudio-style canvas
3. Deck narrative: industry pain → structural insight (why software never fixed it) → substrate thesis → wedge → 3-horizon roadmap → GTM → governance answers (agent owner, scope, escalation, value metric) → 90-day PM plan
