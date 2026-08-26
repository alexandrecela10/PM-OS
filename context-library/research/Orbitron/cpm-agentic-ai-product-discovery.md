# Agentic AI for Capital Project Management — Product Discovery Report

**Scope:** Mega and giga capital projects (oil & gas, petrochemical, large infrastructure). Target customers: owner-operators (Aramco, ADNOC-scale) and Tier-1 EPC contractors (Bechtel, Fluor, Technip, Samsung E&A-scale).
**Date:** August 2026
**Evidence policy:** Every statistic is sourced (see References). Where evidence is thin or based on practitioner knowledge rather than published data, this is flagged explicitly with ⚠️. Sections 1–3 combine industry-standard frameworks with verified sources; Section 4–5 statistics are all sourced; Section 7 is the thinnest evidentially and should be validated with primary interviews.

---

## 1. The end-to-end capital project lifecycle

The dominant framework in oil & gas and process industries is the **stage-gate / Front-End Loading (FEL) model**, codified by Independent Project Analysis (IPA) and the Construction Industry Institute (CII). Owner organizations (Aramco, ADNOC, Shell, ExxonMobil) each run a branded variant — e.g., Shell's ORP (Opportunity Realization Process), Aramco's Capital Program Efficiency framework — but the skeleton is the same everywhere.

### FEL 1 — Opportunity Identification / Business Case (a.k.a. Appraise, FEL-0/1)
- **What happens:** Corporate strategy identifies an opportunity (new facility, expansion, field development). High-level technical concept, market analysis, rough economics. Cost estimate at **AACE Class 5** (accuracy roughly −50%/+100%).
- **Who:** Owner's business development, strategy, and a small study team. Often a feasibility consultant.
- **Duration:** 3–12 months for a megaproject.
- **Gate decision (G1):** "Is this worth studying?" Decided by a business-unit investment committee. Kills are cheap here; most value destruction happens when weak projects pass this gate on optimistic numbers.

### FEL 2 — Concept Selection (Select / Pre-FEED)
- **What happens:** Multiple technical concepts are compared (e.g., onshore vs offshore processing, technology licensor selection, capacity options). One concept is selected and frozen. **AACE Class 4** estimate (−30%/+50%). Basis of Design produced.
- **Who:** Owner project team forms; pre-FEED engineering contractor(s) engaged, often in parallel competition.
- **Duration:** 6–18 months.
- **Gate decision (G2):** Concept freeze. IPA research consistently shows that changing the concept after this gate is one of the strongest predictors of overrun. ⚠️ (IPA benchmark data is proprietary; direction of finding is well established in their published summaries, exact coefficients are not public.)

### FEL 3 — FEED (Front-End Engineering Design / Define)
- **What happens:** The selected concept is engineered to ~20–30% design completion: P&IDs, plot plans, long-lead equipment specs, execution plan, contracting strategy, **AACE Class 3** estimate (−20%/+30%) that becomes the FID control budget. The FEED package becomes the basis for EPC bids.
- **Who:** FEED contractor (often 2 in competition — "dual FEED"), owner's project management team (PMT), cost estimating, procurement developing the EPC contracting strategy.
- **Duration:** 12–24 months for a megaproject. FEED for a large gas plant or refinery complex commonly costs 2–5% of TIC (total installed cost). ⚠️ (practitioner rule of thumb; verify per asset class)
- **Gate decision (G3): FID — Final Investment Decision.** Board-level approval to commit the full capital. This is the single most consequential gate: the budget and schedule announced at FID are the baseline against which all overrun statistics in Section 4 are measured.

### EPC — Engineering, Procurement, Construction (Execute)
- **What happens:** Detailed engineering (to issued-for-construction drawings), procurement of thousands of equipment packages and bulk materials, fabrication, modularization, site construction. Contract forms: lump-sum turnkey (LSTK) EPC dominant in the Middle East; reimbursable EPCM more common where scope risk is high.
- **Who:** EPC contractor(s) — a mega project typically splits into multiple EPC packages (e.g., Aramco's Jafurah program let packages to multiple contractors) — coordinated by the owner PMT and often a PMC (Project Management Consultant, e.g., KBR, Worley, Wood).
- **Duration:** 3–5+ years for oil & gas megaprojects.
- **Gates within execution:** Mechanical completion per system/area; milestone payments tied to progress.

### Commissioning, Start-up & Handover
- **What happens:** Pre-commissioning (flushing, loop checks), commissioning (energization, dynamic tests), performance test runs, punch-list closure, and transfer of the asset plus its documentation (as-builts, vendor dossiers, tag databases) to operations.
- **Who:** Dedicated commissioning teams (contractor + owner ops personnel seconded early), completions management systems (e.g., Hexagon Smart Completions, Orbit/WinPCS ⚠️ verify current vendor names).
- **Duration:** 6–18 months; frequently the most underestimated phase. Delays here are extremely expensive because capital is fully spent but revenue hasn't started.
- **Gate:** Provisional acceptance / performance acceptance certificates; warranty period begins.

### Operations & Maintenance (Operate)
- **What happens:** 20–40 years of operation. The quality of handover data (tag integrity, as-built accuracy) determines O&M efficiency and later brownfield project cost. Poor handover is a chronic, well-known industry failure — it is a key motivation for ISO 19650-style information management and digital-twin programs.

**Product implication:** Overruns are *measured* in Execute but *caused* in FEL. IPA's core finding across decades is that front-end definition quality is the strongest controllable predictor of outcomes. An AI product that only touches construction is treating symptoms.

---

## 2. Who does what: the org chart of a capital project

### Owner side

| Role | Core job | What a bad week looks like | Measured on |
|---|---|---|---|
| **Capital Projects Director / VP Projects** | Owns the portfolio; answers to the board for FID promises | A flagship project announces a re-baseline; must explain a $1B+ variance to the ExCom | Portfolio-level cost/schedule performance vs FID, safety record |
| **Project Director / Project Manager (per project)** | Delivers one project to the FID basis | Contractor files a massive claim; a critical vendor slips a long-lead delivery; a fatality investigation | Cost variance, schedule variance, HSE (TRIR/LTIF), predictability |
| **PMO / Project Controls Manager** | The reporting machine: consolidates cost, schedule, risk into monthly stewardship reports | Three contractors submitted progress in incompatible formats; the month-end report is late and the numbers don't reconcile with SAP | Report accuracy/timeliness, forecast reliability (EAC vs final) |
| **Cost Engineers / Estimators** | Build FID estimates; track commitments, expenditures, forecasts (EAC); manage contingency | Actuals in SAP don't map to the cost breakdown structure; a trend review reveals $200M of unbooked exposures | Estimate accuracy class compliance, forecast drift |
| **Planners / Schedulers (owner)** | Own the integrated master schedule; interrogate contractor P6 updates | Contractor's monthly P6 file has 400 logic changes and hidden re-sequencing; critical path shifted and nobody flagged it | Schedule health metrics (DCMA 14-point), float erosion, milestone forecast accuracy |
| **Contracts & Procurement** | Contracting strategy, tendering, contract administration, change orders, claims defense | A contractor notice of claim arrives citing 14 events; team must reconstruct 18 months of correspondence to assess entitlement | Award cycle time, change order value/ratio, claims outcomes, local-content compliance (IKTVA/ICV) |
| **HSE Manager** | Safety systems, permits, environmental compliance | A high-potential incident stops work on the critical path | TRIR, LTIF, audit findings, regulatory notices |
| **Interface Manager** | Manages technical/schedule interfaces between EPC packages | Two contractors both claim the other's underground works block them; a battery-limit tie-in spec mismatch surfaces at site | Interface register closure rates, interface-driven delays |
| **Commissioning / Handover Manager** | Systems completion, documentation handover to O&M | 30,000 punch items open; vendor dossiers missing for 200 tags; ops refuses care/custody transfer | Systems turnover rate, documentation completeness |

### Contractor (EPC) side

| Role | Core job | What a bad week looks like | Measured on |
|---|---|---|---|
| **EPC Project Manager** | Deliver the contract at or above bid margin | Productivity is running 60% of plan; the owner rejected a $150M change order; cash flow turning negative | Project margin vs as-sold, milestone achievement, claims recovery |
| **Project Controls / Planners** | Build and statuse the P6 schedule; produce progress reports the owner will accept | Owner's planner found the hidden re-sequencing; must produce a recovery schedule in 5 days | SPI/CPI, progress measurement acceptance, payment milestone certification |
| **Quantity Surveyors / Commercial Managers** | Measure work done, price variations, prepare claims, manage subcontractor accounts | A notice deadline under the contract (e.g., 28-day bar under FIDIC-style clauses) was missed on a compensable event — entitlement potentially lost | Certified revenue, variation/claim recovery rate, subcontractor cost control |
| **Engineering Manager** | Deliverable production against the engineering schedule | Owner comments on a critical P&ID revision for the third cycle; IFC drawings late, holding procurement | Deliverable curve (planned vs actual), comment cycle times, rework rate |
| **Procurement / Expediting** | Buy thousands of packages; expedite vendors; logistics to remote sites | A compressor vendor slips 3 months; the shipping window for a module closes; substitute sourcing needed | PO cycle times, on-time vendor delivery, material availability at workface |
| **Construction Manager / Superintendents** | Direct-hire or subcontracted field execution | Scaffolding shortage idles 800 workers; a subcontractor walks off over payment | Installed quantities vs plan, labor productivity factors, rework, safety |
| **Document Controllers** | The circulatory system: transmittals, revisions, correspondence in Aconex/CDE | 4,000 documents overdue for review; an outdated drawing revision was used at site | Transmittal turnaround, overdue register, audit compliance |

**Product implication:** the owner PMO/project controls function and the contractor commercial function are the two highest-pain, highest-information-density seats. Both spend most of their week manually reconciling data across systems that don't talk — this is the daily work an agent can absorb.

---

## 3. The tool landscape

### Incumbent stack (what actually runs a megaproject today)

| Layer | Dominant tools | Where the data lives | Silo characteristics |
|---|---|---|---|
| **Scheduling** | Oracle Primavera P6 (near-universal on megaprojects); MS Project on smaller scopes | P6 EPPM databases — often one per contractor, exchanged as XER files monthly | XER file exchange = snapshot-based, no live integration; each contractor's WBS/activity coding differs |
| **Cost / ERP** | SAP (S/4HANA, formerly ECC) for owner cost actuals & procurement; Oracle EBS in some owners; contractor job-cost systems (often bespoke or Oracle) | Owner's SAP holds commitments/actuals; contractor cost lives in the contractor's own system | The single most consequential silo: schedule (P6) and cost (SAP) reconcile only via manual monthly effort; contractor and owner cost views never natively align |
| **Cost management / project controls** | Hexagon EcoSys, Oracle Primavera Unifier, Contruent (ex-ARES PRISM), InEight, Excel | Project-controls databases; heavy Excel export/import at the edges | Multiple "systems of record" for the same number (EAC in EcoSys vs SAP vs the monthly report deck) |
| **Documents / correspondence / contracts admin** | Oracle Aconex (dominant on Middle East megaprojects), SharePoint, Bentley ProjectWise (infrastructure), Autodesk Construction Cloud | Aconex holds millions of documents, transmittals, RFIs, formal correspondence per project | Rich but unstructured: the ground truth for claims/disputes is buried in correspondence threads nobody re-reads until a dispute |
| **Engineering design / data** | Hexagon Smart 3D, SmartPlant/SDx; AVEVA E3D, Engineering, Unified Engineering; Bentley OpenPlant | Proprietary 3D/engineering databases at the design contractor | Owner rarely has live access; handover of engineering data to O&M is a known chronic failure |
| **Field / construction management** | Procore (commercial construction; growing in industrial), InEight, Oracle Primavera Cloud, paper + Excel on many industrial sites | Contractor field systems, daily reports often in Excel/PDF | Progress data quality depends on manual reporting; lags reality by days–weeks |
| **Completions / commissioning** | Hexagon Smart Completions, WinPCS, Orbit ⚠️ (verify current market shares) | Tag/system databases built late in the project | Frequently disconnected from engineering source data → massive manual tag reconciliation |
| **The universal glue** | **Excel and PowerPoint** | Everyone's laptop and email | The real integration layer of the industry. The monthly stewardship report is a PowerPoint assembled from Excel extracts of all of the above |

**Integration reality:** Point integrations exist (P6↔EcoSys, Aconex↔P6 references, SAP↔EcoSys) but on real projects the operative "integration" is monthly manual export-reconcile-report cycles, because each contractor runs its own instances with its own coding structures, and commercial adversarialism discourages live data sharing. ⚠️ (Structural description from practitioner knowledge; consistent with McKinsey's characterization of fragmented, digitization-resistant stakeholders — see References 6, 7.)

### Emerging AI players (verified as of mid-2026)

- **ALICE Technologies** — generative/simulation-based scheduling: simulates millions of schedule scenarios to optimize sequencing and recovery; published results claim ~17% average duration reduction; launched a conversational "Schedule Insights Agent"; formed a **commercial alliance with McKinsey (2026)** to deploy AI generative scheduling on capital projects, targeting up to 20% timeline reduction. [43, 44, 45]
- **nPlan** — machine learning schedule-risk forecasting trained on large historical schedule datasets; forecasts P6 schedule outcomes and quantifies delay risk. ⚠️ (Well-established player; current product scope/traction should be re-verified in the deep-dive.)
- **Foresight (foresight.works)** — schedule analytics/delay-risk platform aimed at capital projects. [36]
- **OpenSpace / Buildots / Doxel / Disperse** — computer-vision progress tracking: 360° capture or LiDAR compared against BIM/schedule to produce objective progress and earned-value data; Doxel emphasizes real-time earned value; Buildots automated delay prediction from full BIM. [34, 41]
- **Document Crunch** — construction-specific contract AI (clause/risk/obligation extraction, playbooks); used on 10,000+ projects by 500+ contractors; **acquired by Trimble in April 2026** — a strong market signal that contract intelligence is consolidating into incumbent platforms. [42, 45, 48]
- **Trunk Tools** — AI agents over construction project documents for field question-answering, reporting and compliance workflows. [40]
- **Procore** — the incumbent moving fast: **launched a suite of construction agents in 2026**, acquired Datagrid (early 2026) for AI data integration, AWS strategic collaboration; $359M revenue in Q1 2026 (+16% YoY), 17,850 customers. [42, 43]
- **Market signal:** six contech startups raised $126M in early 2026 with a striking share pointed at *document intelligence* rather than jobsite hardware; Trimble/Autodesk/AECOM all made AI-adjacent acquisitions in the same window. [48]

**Gap analysis:** The emerging players are overwhelmingly **construction-phase, single-silo tools** (scheduling OR vision OR contracts), oriented to contractors and commercial construction. Almost nothing serves the **owner PMO on process-industry megaprojects reading across P6 + SAP + Aconex + completions data**, and almost nothing touches **FEL/FEED**, where outcomes are actually determined. That cross-system, owner-side, full-lifecycle seat is the open territory.

---

## 4. Pain points ranked by severity

### The headline base rates (the market's "why now")

- **The Iron Law (Flyvbjerg, Oxford):** across a database now exceeding 16,000 projects, nine out of ten megaprojects overrun cost; overruns up to 50% in real terms are common, above 50% not uncommon; only **0.5% of projects deliver on budget, on time, and on benefits**; the pattern is constant across 70+ years, 100+ countries, public and private sectors. [2, 7, 8, 9, 10]
- **McKinsey:** the average large capital project completes **~20 months behind schedule and ~80% over budget**; **98% of megaprojects suffer cost overruns >30%; 77% are at least 40% late**; construction labor productivity has grown ~1%/year for two decades vs 2.8% for the global economy. [31, 32, 35, 39]
- **Oil & gas specifically (EY, "Spotlight on Megaprojects," 365 projects >$1B):** **64% over budget, 73% behind schedule**, average completion cost **59% above initial estimate** — a cumulative **$500B** overrun ($1.2T planned → $1.7T). Even **after FID**, 65% of projects faced overruns averaging **23% above the approved FID budget**. [11, 12, 13]
- **The Middle East is the worst-performing region in that dataset: 89% of projects over cost, 87% delayed** — i.e., the Aramco/ADNOC neighborhood has the highest measured pain on Earth. [11, 20]
- **Disputes (the monetized end-state of all upstream failures):** Arcadis 2025 puts the average North American construction dispute at **$60.1M taking ~12.5 months to resolve**; the Middle East has historically posted the highest dispute values (~$91M average in the 2017 dataset). HKA's CRUX analysis of 2,200+ projects in 114 countries found **disputed costs averaging 33% of project capex, cumulatively $95B**. [21, 23, 28]
- **Named examples** ⚠️ (magnitudes widely reported; exact figures to be re-verified with primary sources in the deep-dive): Kashagan (Caspian oil, original ~$10B-scale phase-1 estimates vs ~$50B+ actual, years of delay), Gorgon LNG (US$37B FID → ~US$54B), Ichthys LNG (~US$34B → ~US$45B), Channel Tunnel (80% construction cost overrun, 140% financing overrun [36]).

### Ranked pain points

**#1 — Estimate & scope quality at FID (FEL failure) — the root of everything**
- **What:** FID budgets systematically understate cost and duration due to optimism bias and strategic misrepresentation (Flyvbjerg's terms) and incomplete front-end definition; EY lists "aggressive estimates" and "optimism bias" among top internal failure factors. [8, 19]
- **Who feels it:** The board that approved FID; the projects director whose predictability metrics collapse; ultimately shareholders/state.
- **Cost:** This is the delta behind the 59%-average O&G overrun. [11]
- **Why tools don't solve it:** Estimating tools (Aspen Capital Cost Estimator, Cleopatra) compute what they're told; nothing systematically confronts a new estimate with the *outcome distribution of comparable past projects* (reference-class forecasting) or audits the FEL package for the definition gaps that IPA correlates with overrun.

**#2 — Change, claims & commercial leakage during execution**
- **What:** Scope changes, delayed drawings, site conditions and interface failures generate variations and claims; contractual notice regimes have strict time bars; correspondence evidencing entitlement is scattered across Aconex/email. Top dispute causes per Arcadis, stable for a decade: failure to properly administer the contract; poorly drafted/unsubstantiated claims; failure to understand contractual obligations. [21, 22, 23]
- **Who feels it:** Contractor QS teams (margin), owner contracts teams (exposure), both parties' executives when it escalates.
- **Cost:** 33% of capex disputed on affected projects (HKA); $60M+/12.5-month average disputes (Arcadis). [28, 21]
- **Why tools don't solve it:** Aconex *stores* the evidence but doesn't *read* it. Document Crunch reads contracts but not the live project record against them; the entitlement signal lives in the join between contract clauses, the schedule, and thousands of correspondence items.

**#3 — Schedule opacity & late detection of slippage**
- **What:** Monthly XER exchanges, contractor-massaged progress, hidden re-sequencing; owners learn of critical-path erosion months late. 77% of megaprojects ≥40% late (McKinsey). [35]
- **Who feels it:** Owner planners/PMO (blindsided), project directors (forecast credibility), operations (delayed revenue — for a large LNG train, months of delay = billions in deferred revenue ⚠️ order-of-magnitude, verify per asset).
- **Why tools don't solve it:** P6 is an authoring tool, not an intelligence layer; nPlan/ALICE address forecasting/optimization within the schedule silo but don't cross-examine the schedule against procurement status, engineering deliverables, and correspondence — where the true early-warning signals live.

**#4 — Cost forecast (EAC) unreliability and slow reconciliation**
- **What:** The monthly cost report requires reconciling SAP commitments/actuals, contractor progress claims, trend registers and currency effects across incompatible coding structures; EACs lag reality, contingency drawdown surprises. Only ~25% of projects finish within 10% of budget (KPMG). [38]
- **Who feels it:** Cost engineers (nights and weekends at month-end), PMO, CFO.
- **Why tools don't solve it:** EcoSys/Unifier assume clean inputs; the pain is the *reconciliation across systems and parties*, which is done by hand in Excel.

**#5 — Engineering deliverable and document-cycle drag**
- **What:** Late IFC drawings hold procurement, which holds construction; multi-cycle owner comment loops; on megaprojects the document register runs to hundreds of thousands of items. Delayed drawings/design issues are among the most common claim causations. [47]
- **Who feels it:** Engineering managers, document control, then everyone downstream.
- **Why tools don't solve it:** Aconex/ProjectWise track status but don't prioritize by downstream schedule impact, chase, or pre-review.

**#6 — Interface management across EPC packages**
- **What:** Mega programs split into many EPC packages; battery-limit mismatches and sequence conflicts between contractors are a classic megaproject failure mode, adjudicated slowly through interface registers and meetings.
- **Who feels it:** Owner interface managers, both contractors (each blames the other → claims feeding #2).
- **Evidence:** ⚠️ Ubiquitous in practitioner literature and claims causation lists, but hard quantification is thin — flag for the deep-dive (IPA/CII publications likely have data behind paywalls).

**#7 — Commissioning & handover information chaos**
- **What:** Tag databases, vendor dossiers and as-builts assembled late and incompletely; punch lists in the tens of thousands; ops refuses acceptance; O&M inherits unreliable data for 30 years. This is the driver behind ISO 19650 / CDE and digital-twin initiatives.
- **Who feels it:** Commissioning managers, operations, and future brownfield projects.
- **Evidence:** ⚠️ Chronic and universally acknowledged; published cost quantification is weak — a genuine gap the deep-dive should attack (look for CFIHOS adoption literature and IPA start-up studies).

---

## 5. Structural insight: why is this industry still broken?

Decades of software have digitized *documents and transactions* without fixing *outcomes*, because the failure modes are structural:

1. **Every project is a prototype.** Unlike manufacturing, there is no stable production line to optimize. Teams disband at completion; lessons evaporate. Learning curves reset every time — Flyvbjerg's data shows no improvement over 70 years precisely because the industry cannot accumulate learning the way repeatable operations do. [8, 9]
2. **Optimism bias and strategic misrepresentation are load-bearing.** Underestimation is not merely error: projects are approved *because* their numbers look good, and every actor at FID (developers, contractors bidding low to win, political sponsors) is incentivized toward optimistic figures. Misinformation about costs and benefits "is the norm throughout project development." [7, 8]
3. **Adversarial contracting fragments truth.** Lump-sum risk transfer means the contractor's commercial survival depends on claims recovery and the owner's on claims defense. Neither side is incentivized to share live, honest data — which is why "integration" between owner and contractor systems is structurally, not technically, blocked. The #1 dispute cause for a decade is failure to properly administer the contract — a *process* failure software has stored but never performed. [22, 23]
4. **Data is fragmented across dozens of parties and coding schemes.** Owner SAP, contractor job-cost, multiple P6 instances, Aconex, engineering databases — each with bespoke WBS/CBS/tag conventions per project. Schema-level integration projects die because the schemas themselves are one-off (see point 1).
5. **The signal is in unstructured text.** The true state of a megaproject — emerging delays, brewing claims, vendor trouble — lives in correspondence, meeting minutes, daily reports and transmittal comments. Pre-LLM software could only handle the structured 20%; the decisive 80% was unreadable by machines, so humans (expensively, partially, monthly) were the integration layer.
6. **Thin contractor margins throttle tech adoption.** EPC net margins are low-single-digit ⚠️ (widely reported; verify current figures), so contractors underinvest in tooling, and stakeholders across the ecosystem have historically resisted digital adoption (McKinsey names this resistance explicitly as a cause alongside complexity). [31]
7. **Monthly cadence institutionalizes lateness.** The entire control system (progress cycles, stewardship reports, gate reviews) runs on a monthly batch rhythm inherited from paper. Problems are structurally 4–8 weeks old before leadership sees them, and another cycle passes before action.

**The synthesis:** software to date has digitized silos owned by single parties, while megaproject failure is an *inter-party, cross-silo, unstructured-data* phenomenon operating on a monthly human batch cycle. That is exactly the shape of problem LLM-based agents address and previous software could not.

---

## 6. Where agentic AI fits: the 6 highest-value opportunities

Selection criteria: kills a Section-4 pain; requires reading across systems/documents (not a dashboard); action-oriented with human approval; impossible pre-LLM; demo-able.

### 6.1 The Commercial Guardian (claims, notices & entitlement agent)
- **Pain killed:** #2 (commercial leakage/disputes — 33% of capex disputed [28]).
- **What it does:** Continuously reads the contract (obligations, notice clauses, time bars) against the live project record — correspondence, schedule updates, daily reports, RFIs, meeting minutes. Detects compensable/excusable events as they emerge, drafts the required notice within the contractual window with evidence attached, maintains a running entitlement file per event, and (owner-side variant) flags incoming claims' weaknesses. Human approves every outbound item.
- **Data needed:** Contract documents, Aconex/CDE correspondence + transmittals, P6 updates, daily reports.
- **Why not possible before:** Required reading tens of thousands of unstructured documents *against* legal language, continuously. Zacua's 2026 industry report describes exactly this agent pattern (monitoring schedules/RFIs/logs for entitlement triggers and prompting notice templates) as an emerging frontier. [47]
- **Demo wow:** Load a real (anonymized) project's correspondence archive; the agent surfaces a compensable event with a notice deadline in 6 days that the team hadn't logged, drafts the notice, and shows the evidence chain. For an owner demo: it flags that an incoming $40M claim rests on events for which the contractor missed its own notice bars.

### 6.2 The Schedule Interrogator (cross-system early-warning & recovery agent)
- **Pain killed:** #3 (late detection of slippage; 77% of megaprojects ≥40% late [35]).
- **What it does:** On each XER drop, forensically diffs the schedule (logic changes, re-sequencing, float erosion, hidden crashing), then cross-examines it against procurement status (SAP POs, vendor expediting), engineering deliverable curves, and correspondence — catching contradictions ("schedule shows piping starting in March; the correspondence shows the pipe-rack steel vendor slipped to May"). Drafts the challenge questions for the monthly review and proposes recovery options.
- **Data needed:** P6/XER history, SAP procurement, deliverable registers, Aconex.
- **Why not possible before:** Schedule-diff tools exist (Acumen Fuse), but the *cross-examination against unstructured evidence* is human-only work today. nPlan/ALICE optimize within the schedule; nothing prosecutes the schedule against the rest of the record.
- **Demo wow:** Feed two consecutive monthly XERs plus the correspondence folder; the agent produces the "10 questions the owner should ask the contractor this month," each with document-level evidence — replicating in 3 minutes what a top-decile planning consultant does in a week.

### 6.3 The EAC Reconciler (cost intelligence agent)
- **Pain killed:** #4 (forecast unreliability; only ~25% of projects within 10% of budget [38]).
- **What it does:** Continuously reconciles SAP commitments/actuals, contractor payment applications, trend/change registers and P6 progress into a live, evidence-linked EAC; explains variances in natural language; flags unbooked exposures found in correspondence ("contractor's letter of 14 May signals a claim intention not in the trend register"); drafts the monthly cost report.
- **Data needed:** SAP extracts, contractor invoices/progress claims, project-controls system, trend register, correspondence.
- **Why not possible before:** The mapping across incompatible coding structures plus exposure-hunting in text was exactly the human month-end grind; LLMs handle both schema-fuzzy joins and text.
- **Demo wow:** "Your official EAC is $4.21B; evidence in the record supports $4.38B — here are the seven exposures and the documents behind each."

### 6.4 The FID Red Team (reference-class & definition-audit agent)
- **Pain killed:** #1 (the root cause — 59% average O&G overrun vs FID [11]; Middle East 89% [20]).
- **What it does:** At each FEL gate, audits the definition package against FEL-completeness checklists (CII PDRI-style), runs reference-class forecasting against outcome data of comparable projects (Flyvbjerg-style outside view), stress-tests estimate assumptions against the record ("your productivity assumption exceeds the P90 of comparable Gulf projects"), and drafts the gate-review challenge book.
- **Data needed:** FEED deliverables, estimate basis, historical project outcomes (public datasets + the owner's own history — a data moat that compounds per customer).
- **Why not possible before:** Reference-class forecasting existed as consultancy (Flyvbjerg's own practice) but required manual benchmarking; reading a 5,000-document FEED package for definition gaps was economically impossible.
- **Demo wow:** For a sanctioned-but-troubled project: "Here are the 12 red flags this agent would have raised at FID." Retrospective demos on famous overruns are extremely persuasive to boards.
- **Honest caveat:** the outcome-database is the hard part; early versions lean on the customer's own portfolio history plus published datasets. ⚠️

### 6.5 The Deliverable Chaser (engineering & document-flow agent)
- **Pain killed:** #5 (deliverable drag holding procurement/construction).
- **What it does:** Reads the document register + schedule to rank overdue deliverables by downstream critical-path impact; pre-reviews revisions against previous comment cycles ("Rev C does not close comments 4 and 11 from Rev B — likely another rejection cycle"); drafts chase correspondence; predicts which review cycles will bust their turnaround.
- **Data needed:** Aconex/CDE register + document content, P6 links, comment history.
- **Why not possible before:** Required actually reading drawings/comment sheets at register scale. The 2026 funding wave into "AEC document intelligence" ($126M into six startups, disproportionately document-focused) validates this as the recognized frontier. [48]
- **Demo wow:** "Of your 3,900 overdue documents, these 14 are the ones actually threatening the critical path — and here's why, per document."

### 6.6 The Handover Assembler (completions & information-handover agent)
- **Pain killed:** #7 (commissioning/handover chaos; delayed revenue at the worst possible time).
- **What it does:** From engineering databases, vendor documents and completions systems, builds and continuously audits tag-level information completeness against the handover specification (CFIHOS/ISO 19650 profiles); auto-classifies vendor dossiers to tags; produces the "what's blocking system 34's turnover" answer instantly; drafts punch-list closure evidence packs.
- **Data needed:** Tag registers, vendor documentation dumps, completions database, handover spec.
- **Why not possible before:** Vendor documentation arrives as heterogeneous PDF chaos; mapping it to tags was armies of document controllers.
- **Demo wow:** Ingest a vendor dossier dump; the agent maps it to the tag register and shows the completeness heat-map by system — a week of manual work in minutes.
- **Strategic note:** this is the natural bridge from project delivery into the digital-twin/O&M data market, and connects directly to CDE/ISO 19650 positioning.

**Sequencing logic:** 6.1 and 6.2 have the fastest emotional resonance (money and blame) and demo virality; 6.3 is the daily-retention workhorse; 6.4 is the strategic differentiator no construction-phase competitor touches and the one that speaks to owner boards; 6.5/6.6 deepen the moat. All six share one substrate — **a cross-system, document-grounded project record** — which is the actual product; the agents are workflows on top.

---

## 7. Buying reality: how Aramco-type organizations purchase software

⚠️ **Evidence caveat:** this section rests on practitioner knowledge and stable, verifiable public frameworks (IKTVA, ICV, vendor-registration regimes) more than on published statistics. Treat it as a hypothesis set to validate through primary interviews; the deep-dive should verify current thresholds, certification names and cloud-region status.

**Vendor qualification is a gate before any deal.** Aramco requires vendor registration through its SAP Ariba-based portal and pre-qualification against commodity codes; ADNOC runs an equivalent regime. Without registration you cannot receive a PO regardless of product love.

**Local content is scored, not optional.** Aramco's **IKTVA** (In-Kingdom Total Value Add) program and ADNOC's **ICV** (In-Country Value) program score suppliers on localization (local hiring, local spend, local entity) and weight that score in award decisions. Foreign SaaS vendors typically need a local entity/partner and a localization narrative. Expect this to shape corporate structure, not just sales strategy.

**Cybersecurity certification is a hard gate at Aramco.** Third parties handling Aramco data must comply with its Third-Party Cybersecurity Standard (**SACS-002**) and obtain the corresponding cybersecurity compliance certificate via authorized audit firms. ⚠️ Verify current certificate classes and process timelines.

**Data residency:** Saudi PDPL and sectoral rules push toward in-Kingdom processing; hyperscaler regions in KSA and the UAE (and sovereign-cloud players like G42 in the UAE) exist precisely for this market. For an agentic product, "where do the documents and the LLM inference live" will be one of the first three questions asked. In-region deployment (or air-gapped/VPC options) is close to table stakes for project data classed as commercially sensitive.

**Who buys and who signs:** Typical constellation — a **business sponsor** in Projects/Project Management (VP Capital Projects, PMO head) who feels the pain; a **digital/IT gatekeeper** (digital transformation office) who owns architecture and security review; **procurement** which runs the commercial process and localization scoring; and for material spend, a **committee sign-off** (business + IT + procurement). Innovation arms (e.g., Aramco's venture/entrepreneurship vehicles, ADNOC's technology programs) can open doors and fund pilots but do not substitute for the line-business budget owner.

**Cycle and deal shapes:** Realistic expectations for an unproven vendor: **9–18+ months** from first meeting to enterprise contract, usually via a structured **paid pilot / proof-of-concept on 1–2 live projects (3–6 months)** with success criteria agreed upfront, then a project-based or program license. EPC contractors buy faster than owners (quarters, not years) and per-project — a plausible wedge — but owners hold the strategic budget and the data. Pricing conventions in the space anchor to project value: established construction-AI platforms reportedly charge ~0.1–0.3% of project budget for full deployment [46] — on a $10B program that framing supports 8-figure contracts, which is why per-seat SaaS pricing undersells this market.

**Practical implication for the product strategy:** design for (a) in-region/VPC deployment from day one, (b) a pilot package that lands inside one project team's authority (below mega-procurement thresholds), (c) a localization story, and (d) success metrics tied to the buyer's stewardship KPIs (forecast accuracy, claim outcomes, milestone predictability) rather than generic productivity.

---

## What the evidence does NOT yet support (honest gaps for the deep-dive)

1. **Quantified pain for interface management and handover failure** — universally acknowledged, poorly measured in public sources. Target: IPA/CII paywalled research, CFIHOS case studies.
2. **Current-state verification of nPlan, Foresight, and the completions-software market** — fast-moving; my characterizations are directionally sourced but need refresh.
3. **Aramco/ADNOC procurement specifics** (SACS-002 classes, IKTVA thresholds, current cloud-region compliance status, real pilot-to-contract case studies for AI vendors) — practitioner knowledge, needs primary verification.
4. **Named-project overrun figures** (Kashagan, Gorgon, Ichthys) — magnitudes are widely reported but should be pinned to primary sources before use in external material.
5. **Willingness-to-pay evidence** — no public data on what owners pay for project-controls software at program level; requires primary interviews.

---

## References

1. — *(reserved)*
2. Tozija, "The Iron Law of Megaprojects: Patterns, Failures, and Facts," Medium, 2025. https://medium.com/@tozija/the-iron-law-of-megaprojects-patterns-failures-and-facts-7c44c225b2a2
7. Flyvbjerg, "Megaprojects: Over Budget, Over Time, Over and Over," Cato Policy Report, 2017. https://www.cato.org/policy-report/january/february-2017/megaprojects-over-budget-over-time-over-over
8. Flyvbjerg, "What You Should Know About Megaprojects and Why," PMI research summary. https://www.pmi.org/-/media/pmi/documents/public/pdf/research/research-summaries/flyvbjerg_megaprojects.pdf
9. "The Iron Law of Megaprojects," budgetoverrun.com, 2026. https://budgetoverrun.com/iron-law-of-megaprojects
10. "Flyvbjerg project database," budgetoverrun.com (base rates from Flyvbjerg & Gardner, *How Big Things Get Done*, 2023). https://budgetoverrun.com/studies/flyvbjerg-megaproject-database
11. EY, "Spotlight on oil and gas megaprojects," 2014 (365 projects). Coverage: https://www.greencarcongress.com/2014/08/20140815-ey.html
12. World Pipelines coverage of EY report (post-FID overrun figures). https://www.worldpipelines.com/business-news/14082014/ey-mega-project-over-spending/
13. PRNewswire, EY megaprojects release. https://www.prnewswire.com/news-releases/oil-and-gas-megaproject-overruns-to-cost-industry-more-than-us500b-271227501.html
14. EY, "Spotlight on oil and gas megaprojects" (full PDF, incl. IPA 2011: 78% of upstream megaprojects over budget or late). https://aegex.com/images/uploads/white_papers/EY-spotlight-on-oil-and-gas-megaprojects.pdf
20. "A Study of Selected Projects from Oil & Gas Sector" (Middle East: 89% cost / 87% schedule, per EY 2014). https://www.acseusa.org/journal/index.php/aijbms/article/download/109/108/108
21. ENR on Arcadis 2025 Global Construction Disputes Report ($60.1M US average, ~12.5 months). https://www.enr.com/articles/61716-zero-disputes-and-stronger-relationships-a-new-vision-for-construction-says-ceo
22. Construction Dive on Arcadis disputes trends. https://www.constructiondive.com/news/arcadis-resolution-time-for-global-construction-disputes-on-the-rise/420534/
23. Pinsent Masons on Arcadis 2018 report (Middle East $91M average). https://www.pinsentmasons.com/out-law/news/arcadis-global-construction-value-disputes
28. Hardline, dispute statistics roundup incl. HKA CRUX (2,200+ projects, $95B disputed, 33% of capex). https://www.hardlineapp.com/insights/how-to-prevent-construction-disputes-before-they-start-the-documentation-first-approach
31. McKinsey, "Navigating the digital future: The disruption of capital projects" (20 months / 80%; adoption resistance). https://www.mckinsey.com/capabilities/operations/our-insights/navigating-the-digital-future-the-disruption-of-capital-projects
32. Geo Week News on McKinsey "Imagining construction's digital future" (2016). https://geoweeknews.com/news/where-the-construction-industry-stands-six-years-after-mckinsey-s-technology-report
34. OpenSpace, construction delay statistics (McKinsey $1B+ project review: ~80% cost overrun, ~50% schedule delay). https://www.openspace.ai/blog/construction-project-delay-statistics/
35. McKinsey, "The construction productivity imperative" (98% of megaprojects >30% overrun; 77% ≥40% late). https://www.mckinsey.com/capabilities/operations/our-insights/the-construction-productivity-imperative
36. Foresight, "The True Cost of Delays at Scale" (Channel Tunnel figures; dam delay data). https://www.foresight.works/blog/the-true-cost-of-delays-at-scale
38. BuildAgent, cost overrun data roundup (McKinsey 28–33% average; KPMG 25% within 10% of budget). https://buildagent.to/blog/why-construction-projects-go-over-budget
39. McKinsey/MGI deck via CalPERS (98%+ over budget; 80% avg overrun; 20-month avg delay; productivity levers). https://www.calpers.ca.gov/docs/board-agendas/201807/full/day1/03core-economy-mckinsey-ppt_a.pdf
40. Mastt, "Top 10 AI Construction Tools in 2026" (ALICE, Document Crunch, Trunk Tools). https://www.mastt.com/software/ai-construction-tools
41. Fastio, "Best AI for Construction 2026" (ALICE results 17%/14%/12%; OpenSpace/Buildots/Doxel positioning). https://fast.io/resources/best-ai-for-construction-2026/
42. ALICE Technologies blog, "The Autonomous Construction Company" (Trimble–Document Crunch April 2026; Procore agents 2026; assistant→agent framing). https://blog.alicetechnologies.com/news/the-autonomous-construction-company
43. Construction Digital, "Top 10 AI Tools in Construction" (Procore Q1 2026 revenue $359M; Datagrid acquisition; AWS collaboration). https://constructiondigital.com/top10/top-ai-tools-in-construction
44. ALICE Technologies news page (McKinsey–ALICE alliance; Schedule Insights Agent). https://blog.alicetechnologies.com/news
45. Construction Dive, "McKinsey, ALICE Technologies partner on generative AI scheduling" (up to 20% acceleration; Trimble–Document Crunch; Autodesk–Rhumbix). https://www.constructiondive.com/news/mckinsey-alice-technologies-partner-generative-ai-schedule/817580/
46. Ricci, "AI for Construction: A Practical Guide for Firms in 2026" (pricing 0.1–0.3% of project value). https://www.tommasomariaricci.com/blog/ai-for-construction-guide-2026
47. Zacua Ventures, "AI for Construction · Industry Report 2026" (entitlement-monitoring agent pattern; Document Crunch positioning). https://zacuaventures.com/ai-for-construction-%C2%B7-industry-report-2026/
48. AEC Foundry, "AI Can't Read Your Drawings" (2026 M&A/funding wave; $126M into six contech startups; document-intelligence thesis). https://www.aecfoundry.com/blog/ai-can-t-read-your-drawings---inside-the-race-to-build-aec-s-knowledge-layer

*Reference numbers match search-result indices used during compilation; gaps in numbering are intentional.*
