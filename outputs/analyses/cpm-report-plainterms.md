# Agentic AI for Capital Project Management — Full Report (with plain-English translations)

*Every acronym and technical term is followed by a plain-English translation in [square brackets] the first time it appears, and often again where it helps. Target customers: Aramco/ADNOC-scale owner-operators [the companies that own and pay for the project] and Bechtel-scale EPC contractors [the firms hired to design and build it]. Current as of 26 August 2026.*

---

## What this report is, in one paragraph

Giant construction projects — oil refineries, gas plants, petrochemical complexes, big infrastructure — almost always finish late and over budget, and they've done so at roughly the same rate for 70 years. The reason isn't a shortage of software; it's that the information needed to run a project well is scattered across dozens of separate systems, dozens of separate companies, and millions of documents nobody can read fast enough. That is exactly the kind of problem AI agents [software that can read across systems, reason over documents, and take actions with a human's approval] can now attack. This report maps the pain, the money, the competitors, where agents fit, and how to actually sell into the Gulf oil companies — and it backs the pain with real quotes from the people who live it.

---

## 1. The end-to-end capital project lifecycle

Every mega-project moves through the same funnel of stages, each ending in a "gate" [a formal go/no-go decision you must pass to get funding for the next stage]. The industry calls this **stage-gating** or **FEL** [Front-End Loading — doing the heavy planning and definition work up front, before committing the big money].

The two frameworks that govern this are:
- **AACE estimate classes** [AACE = the Association for the Advancement of Cost Engineering; its "classes" are a 1–5 scale of how accurate a cost estimate is, based on how well-defined the project is].
- **CII/IPA stage-gate models** [CII = Construction Industry Institute; IPA = Independent Project Analysis — two bodies whose research defines industry best practice for how to phase and govern projects].

### FEL-1 — Appraise / Concept Screening
- **What happens:** Framing the business case; rough economics; "is this idea worth studying?"
- **Who? (key personas):** The owner's **business-development / strategy lead** (owns the idea), the **corporate finance / investment planner** (owns the economics), and a **subsurface or market specialist** (owns the "is there really oil/demand here?" question).
- **Why? (why this job exists):** To kill bad ideas cheaply, before anyone spends real money. A wrong "yes" here isn't expensive yet — a wrong "yes" that survives to FID is catastrophic. The whole point is to spend a little to avoid committing a lot to the wrong thing.
- **How long:** Months to a year+ on a giga-project [a project costing many billions].
- **Estimate accuracy:** AACE **Class 5** — the roughest estimate, accuracy about −50% to +100% [i.e. the real cost could be half, or double]. Used for screening only.
- **Gate:** Is this worth spending money to study further?

### FEL-2 — Select / Feasibility ("pre-FEED")
- **What happens:** Comparing options (e.g. onshore vs offshore) and picking one concept.
- **Who? (key personas):** An emerging **owner project manager** (starts to own the project), a **process / lead engineer** (owns the technical concept), a **cost estimator** (prices each option), and **pre-FEED engineering consultants** (do the comparative studies).
- **Why? (why this job exists):** To lock in the single most irreversible choice on the project — *which* concept to build — while options are still cheap to change. IPA's research shows that changing the concept *after* this point is one of the strongest predictors of an overrun. Choosing wrong here bakes cost into the project that no amount of good execution later can undo.
- **How long:** 6–18 months.
- **Estimate accuracy:** AACE **Class 4** — accuracy about −30% to +50%. Decides whether to fund the next stage.
- **Gate:** One concept chosen; approval to start FEED.

### FEL-3 — Define / FEED
*FEED = Front-End Engineering Design [the detailed design and planning stage that produces the blueprint and the budget the board will vote on].*
- **What happens:** The make-or-break stage. Producing **P&IDs** [Piping and Instrumentation Diagrams — the detailed schematics of what connects to what], equipment lists, plot plans, the build strategy, and the control estimate [the budget everything is later measured against]. Per CII, the quality of this front-end work is the single biggest factor in whether a project succeeds.
- **Who? (key personas):** The **owner's project director** (accountable for the budget the board will vote on), the **owner's lead estimator / cost engineer** (owns the control estimate), the **FEED contractor's engineering manager** (produces the design), and the **owner's contracts lead** (sets the build/contracting strategy).
- **Why? (why this job exists):** To turn a chosen concept into a defined, priceable project *before* the board commits billions — so the FID vote is based on a real number, not a hope. This is where cost, schedule and risk are actually determined; done well, it prevents the master pain (Section 4, #1). Done poorly, every downstream overrun statistic traces back to here. *(The FEED contractor is deliberately often a different firm from the one that later builds it, to keep everyone honest and competitive.)*
- **How long:** 12–24+ months on a megaproject.
- **Estimate accuracy:** AACE **Class 3** — accuracy about −20% to +30%. This is the maturity level the board is supposed to have before committing.
- **Scope-definition score:** **PDRI** [Project Definition Rating Index — a CII checklist that scores how completely a project is defined, on a 1,000-point scale; lower is better]. Projects scoring under 200 consistently beat those over 200 on cost, schedule and change orders.
- **Gate:** **FID — Final Investment Decision** [the moment the board formally approves the full budget and commits the billions]. This is the single most consequential decision in the whole lifecycle: the budget promised here is the one every "over-budget" statistic is later measured against.

### EPC contracting / Award
*EPC = Engineering, Procurement, Construction [a contract where one firm takes responsibility for designing it, buying all the equipment, and building it].*
- **What happens:** Tendering [inviting bids], evaluating them, and awarding the contract. The contract type matters enormously:
  - **LSTK** [Lump-Sum Turnkey — the contractor agrees one fixed price and hands over a working plant; common in the Middle East].
  - **EPCM / reimbursable** [the contractor is paid its costs plus a fee; used when the scope is riskier].
- **Who? (key personas):** The **owner's procurement / contracts manager** (runs the tender and picks the contract type), **owner legal** (owns the risk allocation), and the **bidding contractors' commercial and estimating teams** (price and shape their bids).
- **Why? (why this job exists):** To decide *who* builds it and *on what terms* — and, crucially, *who carries the risk*. The contract type chosen here sets the incentives for the entire multi-year build: a lump-sum deal pushes risk onto the contractor and quietly programs in the future claims war (Section 4, #3). Get the risk allocation wrong and you are managing disputes for the next five years.
- **How long:** 6–12 months for a mega-contract.

### Detailed Engineering, Procurement, Construction (Execution)
- **What happens:** Full detailed design, **long-lead procurement** [ordering equipment that takes many months to build, like giant compressors], **expediting** [chasing suppliers to deliver on time], fabrication, and construction.
- **Who? (key personas):** On the contractor side, the **EPC project manager** (owns delivery and profit), **planners / schedulers**, **quantity surveyors** (the commercial/claims team), and **procurement / expediting**. On the owner side, the **PMT** [Project Management Team — the owner's own oversight staff] — its **project controls (planners + cost engineers)** and **contracts team** — watches over it.
- **Why? (why this job exists):** To actually build the thing — and to keep it on the FID budget and schedule while doing so. This is where the money is *spent* and where overruns *become visible*, so the job is really about early detection and control: catching a slip, a cost drift, or a claim while it's still cheap to fix. It's the stage most software targets, yet the damage is usually already baked in from FEED.
- **How long:** 3–6+ years for a giga-project.
- **Estimate accuracy:** Tightens to **Class 2** then **Class 1** as the design finishes.

### Commissioning, Start-up & Handover
- **What happens:** Testing the finished plant, switching it on safely, running performance tests, and handing over both the physical asset *and* all its data and documents to the operations team. Progress is tracked at the level of individual **tags** [unique ID codes for every valve, pump, instrument etc. — a large plant has tens of thousands].
- **Who? (key personas):** The **commissioning manager** (drives the plant to start-up), **completions engineers** (track readiness tag-by-tag), the **document controllers / handover team** (assemble the data package), and the **owner's O&M receiving team** (must accept it).
- **Why? (why this job exists):** To prove the plant actually works and to hand operations a complete, trustworthy record so they can run and maintain it safely for decades. This is the moment the whole investment starts earning money, so every day of delay here is a day of lost revenue at the worst possible time — the capital is fully spent but nothing is being produced yet.
- **Who? (O&M team):** the owner's **Operations & Maintenance** [the team that will run the plant for decades] staff.
- **How long:** Months to 2+ years — often the most compressed and troubled phase.
- **Gates:** Mechanical completion → **RFSU** [Ready For Start-Up] → provisional acceptance → final acceptance.

### Operations & Maintenance (O&M)
- **What happens:** 20–40 years of running the asset — the reason it was all built. The quality of the handover data determines maintenance efficiency for decades.
- **Who? (key personas):** The **operations team** (runs the plant), **maintenance / reliability engineers** (keep it running), and, later, **brownfield project teams** [the people who design upgrades and expansions to an existing plant] who inherit the same data.
- **Why? (why this job exists):** To turn the built asset into decades of safe, efficient production. Good handover data makes maintenance cheap and the next expansion easy; bad data means engineers spend years re-discovering how their own plant is built.

**The key takeaway:** the budget is *decided* at the very start (FEED/FID) but the overrun only *shows up* years later during construction. Most software only helps during construction — by then the damage is already baked in.

---

## 2. Who does what: the org chart of a capital project

### Owner side (e.g. Aramco/ADNOC's own project staff)

- **Capital Projects Director / Project Director** — owns the whole project's budget and schedule. *Bad week:* the board asks why the forecast final cost jumped by $2 billion. *Judged on:* delivering to the sanctioned [board-approved] cost and schedule, safety, and the first-oil/first-gas date [when the plant starts producing].
- **PMO** [Project Management Office — the central team that consolidates all the reporting] **/ Project Controls** — the cost engineers, planners and schedulers who maintain the master schedule, the cost report, and the **EAC** [Estimate At Completion — the continuously-updated forecast of what the project will finally cost]. *Bad week:* discovering the contractor's reported progress is inflated and the real position is months behind. *Judged on:* forecast accuracy and early warning.
- **Cost Engineers / Estimators** — build the estimates and track **commitments and actuals** [money promised vs money actually spent]. *Bad week:* the numbers in the finance system don't reconcile with the contractor's invoices. *Judged on:* estimate accuracy.
- **Contracts & Procurement** — contract strategy, tendering, and defending against **claims** [formal contractor requests for more money or time]. *Bad week:* a flood of contractor claims arriving faster than they can be assessed. *Judged on:* commercial exposure and claim outcomes.
- **HSE** [Health, Safety & Environment] **/ Compliance** — safety and regulatory approval. *Bad week:* an incident, or a permit blocker. *Judged on:* injury rates and zero major incidents.
- **Interface Managers** — manage the boundaries between different work packages/contractors [e.g. where the bit one contractor builds must connect to the bit another builds]. *Bad week:* two contractors each assumed the *other* was building the connection between them, discovered only at assembly. *Judged on:* closed interface agreements and no nasty surprises.
- **Commissioning Managers** — drive the plant to start-up and handover. *Bad week:* the plant is declared mechanically complete, but thousands of **punch items** [small unfinished/defective jobs on a snagging list] and missing certificates block switch-on. *Judged on:* the start-up date and handover completeness.

### Contractor side (e.g. Bechtel, Fluor, Saipem, Técnicas Reunidas)

- **EPC Project Manager** — owns the contractor's delivery and **margin** [profit]. *Bad week:* margin evaporating as productivity misses and rework climbs on a fixed-price job. *Judged on:* project profit, schedule, client satisfaction.
- **Planners / Schedulers** — build and update the schedule in **Primavera P6** [the industry-standard scheduling software, made by Oracle]. *Bad week:* a monthly update reveals slippage on the **critical path** [the sequence of tasks that directly determines the finish date — a delay here delays everything]. *Judged on:* schedule integrity.
- **Quantity Surveyors (QS) / Cost Controllers** [a QS measures the work done and prices changes — a role standard in Commonwealth/Middle East contracting]. *Bad week:* under-claiming for legitimate extra work and bleeding cash. *Judged on:* protecting margin and recovering claims.
- **Document Controllers** — manage the millions of documents and **transmittals** [formal document hand-offs between parties], usually in **Aconex** [Oracle's document-management platform, the standard on big projects]. *Bad week:* someone built to a superseded [out-of-date] drawing. *Judged on:* revision control.
- **Procurement / Expediting** — buy and chase equipment. *Bad week:* a long-lead supplier slips and threatens the critical path. *Judged on:* on-time delivery.

---

## 3. The tool landscape

### What runs each stage today

- **Scheduling:** **Primavera P6** [Oracle's scheduling tool] is near-universal (about $3,520 per user to buy outright, or ~$1,320/user/year in the cloud). Microsoft Project on smaller jobs.
- **Cost / forecasting / project controls:** **Hexagon EcoSys** [a project-controls platform; licences reportedly start around $40,000], **SAP** [the big enterprise-resource-planning system that holds the owner's financial commitments and actuals], and **Excel** absolutely everywhere.
- **Documents & correspondence:** **Aconex** [Oracle's neutral platform for sharing documents and formal letters between owner and contractors], plus SharePoint and OpenText.
- **Engineering / design:** **Hexagon** (SmartPlant, Smart 3D, SDx), **AVEVA** (E3D, Engineering), **Bentley** (OpenPlant, ProjectWise) — the tools engineers use to design the plant in 3D and manage engineering data.
- **Construction management:** **Procore**, **Autodesk Construction Cloud**, **InEight**.
- **Completions / commissioning:** **WinPCS**, **Hexagon Smart Completions**, **Coreworx**, **Orbit** — tools that track completion tag-by-tag and system-by-system.
- **Reality capture / progress:** **OpenSpace**, **Buildots**, **Doxel**, **Disperse** — camera/laser tools that photograph a site and compare it to the plan to measure real progress.

### Where the data lives — and why it's stuck

The core structural problem: each party keeps its own system with its own **coding structure** [its own private numbering scheme for tasks, costs and equipment — a **WBS** (Work Breakdown Structure, the hierarchical to-do list) and **CBS** (Cost Breakdown Structure, the matching cost buckets)]. The owner's SAP doesn't talk to the contractor's cost system; the P6 schedule is disconnected from what's actually been ordered and designed; and the correspondence sits in Aconex as unstructured PDFs.

- **KPMG** [a Big Four consultancy that surveys the industry] found that a third of owners who have a project-management system have not connected it to their accounting/procurement software — 47% among the biggest organisations.
- **NIST** [the US National Institute of Standards and Technology] estimated ~**$15.8 billion a year** lost in US capital facilities just from systems not being able to exchange data ("interoperability" losses).
- Reporting is **monthly batch** [everything is compiled once a month by hand] — so by the time a problem appears in a report, it's already weeks old and expensive.

### Emerging AI players — verified 2026 status

- **ALICE Technologies** — AI that generates and optimises construction schedules by simulating millions of build sequences. On **14 April 2026, ALICE and McKinsey formalised a commercial alliance** to deploy this; schedule reductions up to 20% (one data-centre case ~40%). It also launched a **Schedule Insights Agent** — a chatbot you can "talk to your schedule" with.
- **nPlan** — AI that forecasts schedule risk, trained on 750,000+ past project schedules (~$2.5 trillion of spend). Raised a **$16M Series B on 17 Oct 2025** led by CapHorn with **Chevron Technology Ventures** and Suffolk Technologies. Says it has saved customers over **$1.2 billion**. Already used on **HS2, Network Rail, and the Transpennine Route Upgrade** in the UK, and **Anglian Water** across 1,400+ projects. Expanding into the Middle East.
- **Document Crunch** — AI that reads construction contracts and flags risky clauses and obligations. **Acquired by Trimble, closed 4 April 2026 for $246.4M.** Serves 400+ customers including **Balfour Beatty, DPR, Swinerton, Webcor, Boldt**; processed $350B+ of construction volume across 10,000+ project kickoffs. Entry pricing reportedly ~$200/month for small teams, enterprise negotiated.
- **Procore** — the biggest incumbent, moving fast: **acquired Datagrid (an agentic-AI startup) on 20 Jan 2026** and on **21 May 2026 launched a suite of AI agents** (5 pre-built + a builder) that search across specs, drawings and RFIs [Requests For Information — formal questions from the builder to the designer] and can draft RFIs and manage submittal reviews [approving the contractor's proposed materials/equipment].
- **OpenSpace / Buildots / Disperse / Doxel** — the camera/progress-tracking group; consolidating (OpenSpace agreed to buy Disperse; Buildots agreed to buy Genda).
- **Trunk Tools** — AI assistants for the field superintendent [the person running the physical site].

**The pattern:** 2026 is a consolidation year — the incumbents (Trimble, Procore, Autodesk, Hexagon) are buying vertical AI startups to bolt agent capabilities onto their platforms. Almost all of this activity is **contractor-side and construction-phase**. The **owner-side, cross-system, front-end (FEED/FID) and commercial/claims layers stay comparatively open** — that's the gap.

---

## 4. Pain points ranked by severity

### The headline numbers (why this market exists)

- **McKinsey** — its 2023 study of 532 projects found average cost overruns of at least **79%** and average delays of **52%**; a separate study found **98% of megaprojects overrun cost by more than 30%; 77% are at least 40% late**.
- **Bent Flyvbjerg** [an Oxford professor whose 16,000+ project database is the definitive record] — only **0.5%** of megaprojects finish on budget, on time, *and* deliver the promised benefits. He calls the pattern the **"Iron Law of Megaprojects": over budget, over time, under benefits, over and over again.**
- **EY** [the consultancy formerly Ernst & Young] — in its study of 365 oil-and-gas megaprojects: **64% over budget, 73% behind schedule**, average final cost **59% above the original estimate**, a cumulative **$500 billion** of overrun. Even *after* FID [after the budget was supposedly locked], 65% still overran, averaging 23% above the approved budget. **The Middle East was the worst-performing region of all** (89% over cost, 87% delayed) — meaning the Aramco/ADNOC region has the worst track record on Earth.

### Ranked pains

**#1 — Cost overruns at/after FID (the master pain).**
*Root cause:* **optimism bias and strategic misrepresentation** [Flyvbjerg's terms — estimates are systematically too low, partly by honest over-optimism and partly because low numbers are what get projects approved]. *Named cases:* **Kashagan** (Caspian oil field, ~$50bn spent, ~11 years late), **Gorgon LNG** [Liquefied Natural Gas plant] (~$37bn → ~$54bn), **Ichthys LNG** ($34bn at FID → ~$45bn per Total's own filing), **Channel Tunnel** (80% over budget). *Why tools don't fix it:* P6 and SAP just report the number after it's already wrong.

**#2 — Schedule slippage and unreliable progress.**
*Evidence:* **HKA** [a global claims-and-disputes consultancy] found in its **CRUX** research (2,200+ projects) that contractors sought time extensions averaging **66% of the planned schedule**. *Root cause:* optimism in the plan + monthly batch reporting hiding the real position + self-reported (often inflated) progress. *Why tools don't fix it:* traditional **QSRA** [Quantitative Schedule Risk Analysis — the standard statistical method for estimating schedule risk] has, in nPlan's words, "consistently failed to overcome" the bias.

**#3 — Claims, disputes and change orders.**
*Evidence:* HKA's CRUX put total sums claimed at **$95 billion**, with disputes averaging **33% of the contract budget**. **Arcadis** [a design-and-consultancy firm that publishes an annual disputes report] put the average US dispute at **$60.1 million** taking **~12.5 months** to resolve, with the Middle East historically carrying the highest values. *Root cause:* fixed-price contracts make owner and contractor adversaries; entitlement [the legal right to more money/time] must be matched to the contract manually, and legal deadlines get missed. *Why tools don't fix it:* the contract sits as a PDF, the evidence sits in Aconex, and nobody reconciles them continuously.

**#4 — Interface failures between EPC packages.**
*Evidence:* an **INCOSE** [International Council on Systems Engineering] study of 45 large projects found those with mature interface management averaged **4% cost growth vs 18% without** — a ~14-point swing. *Caveat:* this rests largely on one dataset. *Why tools don't fix it:* interface registers are static spreadsheets, disconnected from the live design and schedule.

**#5 — Poor commissioning/handover information.**
*Evidence:* **IPA's** Ed Merrow found ~65% of megaprojects hit serious problems; NIST's $15.8bn/yr interoperability loss; **CFIHOS** [Capital Facilities Information HandOver Specification — an industry standard for what data must be handed over, and in what format] work describes a "six-month bottleneck" of manually cross-referencing tens of thousands of documents against **ISO 19650** [the international standard for managing information across a built asset's life]. *Who feels it:* the owner's O&M team, for 20–40 years.

**#6 — Cost forecast (EAC) reconciliation across systems.**
*Evidence:* KPMG found only ~25–31% of projects finish within 10% of budget. *Root cause:* the owner's SAP and the contractor's cost system use incompatible coding, so the monthly forecast is reconciled by hand.

---

## 5. Structural insight: why is this industry still broken?

Decades of software haven't moved the Iron Law because the failures are **structural, not tooling gaps**:

1. **Fragmented data with bespoke coding.** Every project invents its own numbering; every party keeps its own system; there's no shared source of truth.
2. **Adversarial fixed-price contracts.** The contract that shifts risk onto the contractor also gives it a reason to file claims, hide bad news, and fight at handover. Neither side shares honest live data. KPMG: only ~32% of owners have high trust in their contractors.
3. **Optimism bias and strategic misrepresentation.** Estimates are deliberately, structurally low because low estimates win approval — a behavioural/political problem software has never touched.
4. **Every project is a one-off.** Teams disband afterwards; lessons evaporate; the learning curve resets every time.
5. **Thin contractor margins.** Fluor's net margin was about **0.13% in 2023** and **4.72% in 2024**; EPC gross margins are historically ~5–10%. There's no cushion to absorb a bad estimate, so contractors must claim to survive — which fuels the dispute machine.
6. **Monthly batch reporting.** By the time a problem shows up, it's weeks old.
7. **The signal is buried in unstructured text.** The early warning of a claim, a slip, or an interface gap lives in emails, letters and minutes — until now, unreadable at scale.

**The through-line:** the information that could save a project already exists — it's just scattered across systems, parties and unstructured documents, and no human team can read and reconcile it fast enough. That is precisely what AI agents are built to do.

---

## 6. Where agentic AI fits — the highest-value opportunities

Ranked by value × how well an agent can do it × how open the space is (little competition).

**A. Claims / entitlement agent — highest commercial value.**
- *Kills:* pain #3 ($95bn claimed; a third of budgets in dispute).
- *What it does:* continuously reads the contract against the live flood of correspondence, flags when money/time is owed (or being wrongly claimed against you), and drafts the formal **notice** [the contractually-required letter you must send within a deadline to preserve your right to claim] before the deadline lapses — with the evidence attached. A human approves every letter.
- *Why it wasn't possible before LLMs* [Large Language Models — the AI that can read and reason over ordinary human language and documents]: it requires reading thousands of unstructured documents against dense legal language.
- *Demo wow:* "Found 14 unclaimed variations worth $23M and drafted the notices, each citing the exact clause and the email that triggers it."
- *Who's here:* Document Crunch (now Trimble) is closest but contractor-side; owner-side entitlement defence is largely open.

**B. FID red-team agent — highest strategic leverage.**
- *Kills:* pain #1, the master pain (the bad decision at sanction).
- *What it does:* before the board commits, it audits the FEED definition (PDRI-style), stress-tests the estimate against a **reference class** [a set of comparable past projects and how they actually turned out — Flyvbjerg's proven method for beating optimism bias], and challenges the weak assumptions.
- *Demo wow:* "This plan resembles a group of past projects that overran 60%; here are its 9 weakest-defined scope elements."
- *Who's here:* nPlan does reference-class *schedule* risk; the owner-side FID/FEED definition audit is largely open — and it's where the money is decided.

**C. Cost reconciliation (EAC) agent.**
- *Kills:* pain #6.
- *What it does:* continuously matches the owner's SAP against the contractor's cost data despite mismatched coding, producing one live, defensible forecast with variance explanations.
- *Demo wow:* "Your official forecast is $180M light; here are the 6 drivers and the source documents."

**D. Schedule-truth agent.**
- *Kills:* pain #2.
- *What it does:* cross-examines each P6 update against what's actually been ordered and designed — "you show the foundation complete, but the rebar was never delivered and there's no pour record."
- *Who's here:* ALICE/nPlan optimise and forecast the schedule but don't audit it against cross-system reality. Open.

**E. Commissioning/handover completeness agent.**
- *Kills:* pain #5.
- *What it does:* validates handover data against CFIHOS/ISO 19650, auto-matches vendor documents to tags, and flags missing certificates before they block start-up.
- *Demo wow:* "4,200 tags are missing calibration certificates and 380 datasheets don't match the P&ID — here's the auto-generated list."

**F. Interface-management agent.**
- *Kills:* pain #4 (the 4%-vs-18% swing).
- *What it does:* reads across package scopes and correspondence to spot gaps/overlaps before they surface at assembly.

**G. Design-feasibility gate — validates a design in minutes: compliant, on-budget, buildable.**
- *Kills:* the root cause of pain #1 *before* construction — design errors and scope gaps that become rework and change orders. Design errors and omissions drive ~28% of all rework, and design-related issues account for ~70–80% of all cost deviations on projects. Fixing an error in design costs roughly a tenth of fixing it in construction and a hundredth of fixing it after handover (CII's "1-10-100" rule).
- *What it does:* on **every design revision** during FEED/detailed design, it runs three checks in minutes and returns a cited pass/fail list with fixes: **(1) Compliant?** — checks the drawings/BIM against the Saudi Building Code [the national building rulebook, mandatory since 30 June 2025] or Dubai Building Code; **(2) Within cost?** — checks the design against the budget ceiling and cost benchmarks; **(3) Buildable/on-schedule?** — flags constructability problems and long-lead conflicts. Think "spell-check for feasibility," run continuously, instead of a one-off human review weeks later.
- *Data it needs:* the design files (drawings, BIM/IFC models, specs), the applicable building code, the owner's cost benchmarks, and buildability rules.
- *Why it wasn't possible before LLMs:* it needs to *read* thousands of pages of drawings and code text and reason about conflicts between them — exactly what large language and vision models now do.
- *Demo wow:* "This revision has 3 fire-code violations, is 8% over the structural-steel budget, and the compressor's foundation clashes with the pipe rack — here's each one, cited to the drawing and the code clause, in 4 minutes."
- *Who's here / the caveat:* the pure **compliance-check** corner is filling fast and is even being built by regulators themselves (Dubai Municipality is building an AI agent to auto-issue permits by checking drawings against the Dubai Building Code), plus vendors like UptoCode, WhiteHelmet, Buildcheck and Civils.ai. The **defensible, owner-side version is the three-in-one feasibility gate** — the *cost* and *buildability* checks are where the giant-owner value lives and where the permit-focused players don't play. It targets a persona one seat over from the FID red-team (the owner's **design/engineering manager** rather than the projects director), so it's a second door into the same Aramco/ADNOC account, sharing a data foundation.

**Strategic read:** the contractor-side construction-phase space is filling fast. The defensible white space is **owner-side, cross-system and front-end/commercial** — that means **B (FID red-team), A (claims), C (cost), D (schedule-truth) and G (design-feasibility gate)**. That's exactly where Aramco/ADNOC-scale owners feel the most pain and where no incumbent is strong.

---

## 7. Real quotes from the industry — validating the pain *and* the willingness to pay

This is the section you asked for: actual, sourced statements from people inside this world, confirming both that the pain is real and that they will spend money to fix it.

### They confirm the pain is real and expensive

> "On most complex capital programmes, a significant amount of money that one party is entitled to recover is never recovered. The entitlement is real… What most projects lose to poor claims management is not a dispute they should have won, but **entitlement they never assembled the evidence to claim**."
> — Kairos (capital-projects claims advisory), *Construction Claims Management*, 2026. https://www.wearekairos.com/insights/construction-claims-management/
> **Why it matters:** this is a near-perfect articulation of Opportunity A. The money is being left on the table not for lack of a case, but for lack of anyone assembling the evidence in time — exactly the job an agent does.

> "Company leaders were faced with a startling finding from an internal analysis: their world-spanning capital-projects portfolio had yielded only minimal net present value, with more than half of its potential lost to underperformance… all shared a root cause — bias."
> — McKinsey, *Don't cancel or coddle at-risk capital projects — challenge them*, 2025. https://www.mckinsey.com/capabilities/operations/our-insights/dont-cancel-or-coddle-at-risk-capital-projects-challenge-them
> **Why it matters:** an owner losing half its portfolio value to bias at sanction is the exact pain Opportunity B (the FID red-team) attacks.

> "We agree, as our in-depth review of more than 300 billion-dollar-plus megaprojects showed average cost overruns of approximately 80 percent and schedule delays of about 50 percent."
> — McKinsey, *Capital project risk management strategies for success*, 2025. https://www.mckinsey.com/capabilities/operations/our-insights/dont-cancel-or-coddle-at-risk-capital-projects-challenge-them

> "For an average size project, even a 10 percent overrun can lead to a $5 million hit to project profitability… By the time you see the project status, it's already outdated, and can be too late to catch a delay or cost overrun."
> — Deltek, *The True Cost of Project Delay* (white paper). https://www.ceacisp.org/sites/default/files/documents/The-True-Cost-of-Project-Delay-White-Paper.pdf
> **Why it matters:** confirms the "monthly batch reporting is too late" structural pain behind Opportunity D.

### An owner (Saudi Aramco) states its own pain, in its own words

> "[The customer's] needs are simply a facility with no defects, delivered on time and within the given budget… To address the current challenges in program execution — including severe resource constraints and longer procurement lead times for material and equipment — Saudi Aramco has developed and implemented several innovative procurement and contracting strategies."
> — Saudi Aramco, via PMI [Project Management Institute] case study on its Quality Management Information System. https://www.pmi.org/learning/library/saudi-aramco-quality-management-information-system-7013
> **Why it matters:** Aramco itself naming execution pain and actively building systems to fix it — evidence of both need and buying behaviour.

### They will pay real money — the willingness-to-pay proof

> **ADNOC signed a $340 million, three-year contract** for agentic AI, after a proof-of-concept. Its Upstream CEO Musabbeh Al Kaabi said: "ADNOC is on a mission to become the world's most AI-enabled energy company, maximizing the potential of AI to drive efficiency and value creation across our operations." The system is described as "reducing time for essential business processes from months to days."
> — AIQ / Presight press release, 10 March 2025. https://www.prnewswire.com/news-releases/aiq-announces-340-million-contract-for-large-scale-deployment-of-agentic-ai-across-adnoc-operations-302400274.html
> **Why it matters:** this is the single most important data point in the report. A Gulf super-major has already paid $340M for agentic AI, *after a pilot* — proving the appetite, the deal shape (pilot → large multi-year contract), and the price ceiling. (Note: it also shows ADNOC prefers to buy agentic AI through its own JV, AIQ — a channel consideration for us.)

> "With Document Crunch, **we can safely and confidently bid more jobs than before. When you understand your risks upfront, you can be more competitive — you're not padding fees just to cover the unknowns.**" … "I've never heard anyone say grow over a half a billion dollars without a lawyer. For Balfour, it's been possible, in part, because I'm using a tool that streamlines our process and reduces risk."
> — Jeff Brannen, SVP & Chief Legal Officer, **Balfour Beatty** (Texas/Arizona). https://www.trimble.com/en/products/document-crunch
> **Why it matters:** a Tier-1 contractor executive putting hard commercial value on AI contract intelligence — the exact category as Opportunity A. He also quantifies the time saving: risk-review meetings "gone down from four hours before Document Crunch, to two hours." (https://www.documentcrunch.com/blog/save-time-enhance-communication-balfour-beatty)

> "Every contractor has a story about a contract clause that cost them — and **at $200/month, Document Crunch pays for itself with a single caught risk.**"
> — Velocity AI Insights review, 2026. https://insights.velocityaipartners.co/tools/document-crunch
> **Why it matters:** the ROI logic of Opportunity A stated plainly — one caught risk pays for the tool many times over.

> "nPlan's AI is already in use on more than **$500 billion worth of live projects**… To date, nPlan has saved its customers well over **$1.2B**." The Transpennine Route Upgrade "has gone further, **contractualising the use of nPlan** for assuring possessions."
> — nPlan Series B announcement, 17 Oct 2025. https://www.nplan.io/press-releases/nplan-raises-16m-series-b-to-scale-its-ai-led-transformation-of-capital-project-delivery
> **Why it matters:** a customer writing an AI tool *into its contracts* is the strongest possible willingness-to-pay signal — the tool has become mandatory, not optional. And Chevron's venture arm co-led the round, showing an oil major betting on this category.

**Bottom line on validation:** the pain (bias at FID, lost entitlement, late detection) is confirmed in the words of McKinsey, Aramco, and specialist claims advisors; and the willingness to pay is proven by a $340M ADNOC contract, a Tier-1 contractor's CLO crediting the tool for competitive bidding, and a customer writing AI into its contracts. The two owner-side opportunities we favour (A and B) are the least served by today's vendors.

### Validating Opportunity G — the design-feasibility gate

The pain and the value here are unusually well-quantified, and the strongest signal is that a **government is building this itself**.

> Dubai Municipality is delivering "a fully integrated digital system capable of issuing building permits automatically and without human intervention by reading submitted drawings and documents, verifying compliance with the Dubai Building Code."
> — Dubai Municipality, via Zawya, 2026. https://www.zawya.com/en/press-release/government-news/dubai-redefines-the-future-of-building-permits-with-an-ai-system-that-issues-licences-automatically-425918
> **Why it matters:** when the *regulator* automates the compliance check, every developer and consultant in the market suddenly needs to arrive pre-compliant — that is the demand for the private, owner-side version. It also confirms the exact three-discipline scope (plot, architecture, MEP, structural) is technically doable now.

> "We reduced our SBC [Saudi Building Code] compliance review cycle from 6 weeks to 3 days. The AI caught two fire environmental gaps that would have delayed our building permit by months."
> — Customer testimonial, WhiteHelmet (Saudi-based construction-intelligence vendor), 2026. https://www.whitehelmet.sa/products/ai-compliance-analysis
> **Why it matters:** a Gulf customer quantifying both time (6 weeks → 3 days, ~90% faster) and avoided delay (permit delay of "months" prevented) on the exact Saudi Building Code this product would target.

> "What used to take us weeks is now done in days… Every coordination issue that Buildcheck caught saved us from expensive field modifications and potential delays."
> — Customer testimonial, Buildcheck (AI design-review). https://buildcheck.ai/
> **Why it matters:** confirms the "catch it in design, not in the field" value proposition from a paying user's mouth.

**Quantified value (all sourced):**
- **Rework is 5% of project cost on average** (CII IR-153, 144 industrial projects), 90th-percentile 12.4%; design rework adds 1–3 points on top. https://reworkcost.com/cost-of-rework-in-construction
- **~70–80% of cost deviations trace to design**, not construction execution (~17%). https://mycomply.net/info/blog/cost-of-rework-in-construction/
- **Catching an error in design costs ~10× less than in construction, ~100× less than after handover** (CII 1-10-100 rule); thorough pre-construction plan review catches 60%+ of rework-causing errors. https://helonic.com/blog/construction-rework-costs
- Independent ROI modelling on plan review: **4:1 to 30:1 cost-avoidance**, an RFI [a formal design query] costing $200–$500 at drawing stage vs $2,000–$8,000 in the field; AI plan review detects ~100% of MEP clashes vs 40–60% manual. https://miragemetrics.com/blog/ai-construction-plan-review
- Documented outcomes across AI-augmented design tools: **design errors reaching the field cut 50–75%**, material waste down 5–12%, schedule compressed 8–18% on complex projects. https://www.tommasomariaricci.com/blog/ai-for-construction-guide-2026
- **On an Aramco-scale giga-project the arithmetic is stark:** on a $5bn project, ~5% rework = ~$250M, of which ~28% (~$70M) is design-caused; catching half of that early avoids **~$35M on a single project** — before counting schedule/first-oil revenue. On a $20bn project the design-caused rework figure is ~$280M.

**Honest gap:** there is strong *practitioner and vendor* validation (WhiteHelmet, Buildcheck) and a decisive *regulator* signal (Dubai Municipality), but I found **no on-record quote from an Aramco/ADNOC owner executive** naming this specific tool — treat the owner-persona demand as inferred from the regulator move and the mandatory SBC 2024 reset, and validate it in primary interviews.

---

## 8. Buying reality: how Gulf owners buy (and how to sell)

The Gulf is not a "sign up online" market. Expect a long, gated process.

### Saudi Aramco
- **Register through SAP Ariba** [Aramco's mandatory online supplier portal] — you first need a licensed in-Kingdom legal entity via **MISA** [Ministry of Investment of Saudi Arabia, which licenses foreign companies]. Typically **3–6 months** for a foreign company.
- **IKTVA** [In-Kingdom Total Value Add — Aramco's local-content scoring program; a weak score hurts you in every bid]. Aramco aims to keep 75% of its spend in-Kingdom by 2030.
- **SACS-002 → CCC** [SACS-002 is Aramco's mandatory third-party cybersecurity standard; you must earn a Cybersecurity Compliance Certificate before touching Aramco data]. A hard gate.
- **Saudi PDPL** [Personal Data Protection Law] **/ data residency** — sensitive data must be hosted **in-Kingdom** by default. In-Kingdom cloud regions now live: AWS Riyadh, Google Cloud Dammam, Oracle Riyadh/Jeddah, plus national providers.
- **Innovation front doors:** **Wa'ed Ventures** [Aramco's $500M venture-capital arm], **SAIL** [Saudi Accelerated Innovation Lab — Aramco's innovation lab; note the original brief's "LAB7" appears to be a naming confusion], and Aramco Digital.

### ADNOC (UAE)
- **ICV** [In-Country Value — the UAE's equivalent of IKTVA; a stronger score is a decisive advantage]. One certificate per legal entity, valid 18 months.
- **UAE data residency / sovereign cloud** — **G42's Khazna** runs the largest in-UAE capacity; Microsoft, AWS, Google and Oracle all have UAE regions.
- **AIQ** [the ADNOC–G42 AI joint venture] — the key reference point: it won the $340M ENERGYai deal. **ADNOC prefers to build/co-own agentic AI through AIQ**, so position as a partner/technology layer to AIQ rather than a head-on competitor.

### Deal shape, pricing and who signs
- **Pricing:** commonly a **% of project value** — Procore charges on **ACV** [Annual Construction Volume — the total value of construction a customer runs through the platform], roughly 0.1–0.2% of hard costs; industry rule of thumb 0.1–0.3%. On a $10bn giga-project even 0.05% is $5M — trivial against one averted $23M claim.
- **Deal path:** paid **PoC** [Proof of Concept — a small paid pilot on one or two live projects] → multi-year enterprise contract. The $340M AIQ deal followed exactly this.
- **Who signs:** a triangle of the business sponsor (project director/VP), the digital/AI office (Aramco Digital/SAIL; ADNOC's arm/AIQ), and a procurement committee. The exact sign-off body for software is thin in public sources — treat as per-account discovery.
- **Cycle:** budget **9–18+ months** from first contact to enterprise contract.

---

## 9. Recommendations

1. **Pick the wedge now:** lead with the owner-side **FID red-team (B) + claims/entitlement (A)** combination — biggest pain, least competition, best demos, validated by real quotes above. Add cost (C) and schedule-truth (D) as land-and-expand follow-ons.
2. **Make compliance a feature:** in-Kingdom (KSA) and in-UAE hosting, plus SACS-002/CCC and IKTVA/ICV, from day one. You cannot sell without them.
3. **Enter through the innovation arms:** Wa'ed / SAIL / Aramco Digital, and partner with AIQ / Hub71 rather than competing. Run a paid PoC with a pre-agreed success metric and a contractual path to scale.
4. **Price to value:** anchor to a fraction of project value; one avoided claim or 1% of overrun pays for the whole thing many times over.

---

## 10. Caveats and evidence gaps

- Named-project figures (Kashagan, Gorgon, Ichthys) are pinned to primary/authoritative sources where possible; Kashagan's larger lifetime figures come from secondary financial press — treat as estimates.
- Interface-management quantification rests largely on one INCOSE dataset — directional, not definitive.
- A single clean "cost of poor handover" percentage isn't established in public literature; the six-month-bottleneck and NIST $15.8bn/yr are the strongest anchors.
- Gulf sign-off authority and exact software procurement-cycle length are thin in public sources — validate with primary interviews.
- No verified deployment of pure-play schedule/claims AI vendors (nPlan, ALICE) *specifically at Aramco or ADNOC* was found — the proven Gulf AI channels are AIQ, AVEVA, AspenTech/Emerson and Cognite/SLB.
- Several vendor metrics (nPlan's $1.2bn saved; ALICE's savings) are self-reported and should be presented as such.

---

### Full source list
McKinsey (2023 pre-construction study; 2025 risk/at-risk-projects; transparency; schedule-optimization) · EY *Spotlight on Oil & Gas Megaprojects* (2014) · Flyvbjerg, *How Big Things Get Done* (2023) & Oxford database · HKA CRUX Insight (8th ed.) · Arcadis Global Construction Disputes Report (15th ed., 2025) · KPMG Global Construction Survey · NIST GCR 04-867 · INCOSE interface-management study · IPA (Merrow, *Industrial Megaprojects*) · CFIHOS / ISO 19650 literature · AIQ/Presight $340M press release (2025) · nPlan Series B (2025) · Document Crunch / Trimble & Balfour Beatty customer materials · Kairos claims-management insight (2026) · Aramco/PMI QMIS case study · company filings (Total SEC filing for Ichthys; Fluor margins via Macrotrends). Individual URLs are given inline at each statistic and quote.
