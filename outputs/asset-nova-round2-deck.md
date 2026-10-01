# Asset Nova — Round 2 Deck (plain English, ROI first)

Source of truth for `outputs/prototypes/asset-nova-round2-deck.html`.
Evidence base: `context-library/research/Orbitron/cpm-report-plainterms.html`, `context-library/research/Orbitron/cpm-quotes-by-opportunity_2.html`, `context-library/research/Orbitron/cpm-agentic-ai-product-discovery.md`.
Rules for this deck: no jargon, no acronym goes unexplained, every claim either sourced or labelled as our assumption, and every product answers four questions in the same order (what's it worth, will it work, what do you have to do, what do you have to give up).

Date: 2026-08-27. Author: Alexandre Cela.

---

## SLIDE 1 — Title

**Asset Nova**
Three products that protect the money on a giga-project.

Owner-side. Built on files the owner already has. Every output cites its source, and a person presses send.

---

## SLIDE 2 — The whole story in six lines

1. Big projects almost always cost more and take longer than the number the board approved. In oil and gas: 64% over budget, 73% late, 59% average cost growth, and the Middle East is the worst region measured (89% over cost). *(EY, 365 projects over $1bn)*
2. It isn't a software shortage. It's that the facts that would have saved the project are spread across dozens of systems, dozens of companies and millions of documents nobody can read fast enough.
3. Reading is now cheap. That is the only thing that changed, and it changes which problems are solvable.
4. So we sell three reading machines, in the order the owner can actually buy them.
5. Each one pays for itself out of a single avoided loss on a single project.
6. None of them asks the owner to change how they work. That's the design constraint, not a nice-to-have.

---

## SLIDE 3 — What goes wrong, in money

| What happens | How big | Source |
|---|---|---|
| Contractors ask for roughly twice what they eventually settle for | ~2× gap between submitted and settled | IPA via National Academies / Long International |
| Money in dispute on affected projects | 33.4% of the contract budget | HKA CRUX (2,200+ projects) |
| One average dispute | $60.1M and about 12.5 months | Arcadis 2025 |
| Redoing work that was built wrong | ~5% of project cost (top 10% of projects: 12.4%) | CII IR-153 |
| Where those errors come from | 70–80% of cost deviations trace back to design, not building | industry analyses cited in the report |
| Cost of catching an error late | 10× more in construction, 100× more after handover | CII 1-10-100 |
| Overrun after the board has already approved the budget | 23% on average, even post-sanction | EY |

Plain reading: the money leaks in three places. During the build, through claims. In the design office, through errors that get built. And at the moment of approval, through a number that was too hopeful.

Our three products sit exactly on those three leaks.

---

## SLIDE 4 — Why decades of software didn't fix it

- Every project is a one-off. Teams disband, lessons evaporate, and the next project starts from zero.
- The contract makes truth adversarial. Fixed-price deals reward claiming and reward hiding bad news.
- Low estimates win approval, so estimates come in low. That's not a mistake, it's an incentive.
- Reporting is monthly. Any problem is four to eight weeks old before a leader sees it.
- The decisive evidence is prose: letters, minutes, daily reports, drawing comments. Old software could only handle the tidy 20% of data in databases, and the messy 80% was invisible.

The gap is not analysis, it's reading. That's the sentence the whole business rests on.

---

## SLIDE 5 — The owner's lifecycle, and where the money is really decided

```
 IDEA        OPTIONS      DESIGN        APPROVE      BUILD           START-UP      OPERATE
 (screen)    (pick one)   (FEED)        (the vote)   (3-6 years)     (handover)    (20-40 yrs)
    |            |           |             |             |               |             |
 cheap to    cheapest    where cost    the number    where the       where delay    where bad
 kill        moment to   is actually   everything    overrun         costs most     handover
             change      set           is measured   becomes         (money spent,  data costs
             your mind                 against       visible        no revenue)     for decades
```

Two facts that drive our whole product order:

1. Cost is **decided** in design and at the approval vote. It only **shows up** years later, during the build.
2. Almost every AI product in this market works during the build, for the contractor. The owner's seat, the design stage and the approval gate are open ground.

---

## SLIDE 6 — The three products on that map

```
 IDEA    OPTIONS    DESIGN ..................  APPROVE ........  BUILD .................  START-UP   OPERATE
                    [ PRODUCT 2 ]              [ PRODUCT 3 ]     [ PRODUCT 1 ]
                    Design feasibility         FID red team      Claims defence
                    check every revision       pressure-test     & recovery
                                               the number        always on
                    ~ ~ later opportunities ~ ~
 concept   option   drawing chase              gate challenge    cost forecast truth      handover    asset data
 red-team  compare  (deliverables)             book              schedule truth           complete-   feeds the
                                                                 interface gaps           ness        next vote
```

- **Product 1 — Claims defence and recovery.** Ships first. Runs during the build, on the record the owner already controls.
- **Product 2 — Design feasibility.** Ships alongside or just after. Runs during design, on the owner's own drawings.
- **Product 3 — Approval red team (FID).** Switched on after 1 and 2 have earned trust, because it needs the owner's history and it delivers an unwelcome message at the highest-stakes moment.

The greyed items are the roadmap. Each one reuses the same reading layer, so the second product costs a fraction of the first.

---

## SLIDE 7 — One project, one team, one week: the scenario the rest of this deck uses

**The project.** Jebel Nasr Train 4, a $5.2bn gas processing train for a Gulf national oil company. Lump-sum EPC contract with Kaisan Engineering & Construction (KEC), signed with 14 amendments to date. Month 26 of a 48-month build. Late-delivery damages run at $45k per day, capped at 10% of contract value. Claim notices are due within 28 days of the event, and must go to the named recipient.

**The people.**

| Name | Role | Which product |
|---|---|---|
| Faisal Al-Harbi | Owner's contracts and commercial manager, Jebel Nasr Train 4. Team of four. | Product 1, the buyer and the user |
| Mariam Kassab | Senior quantity surveyor in Faisal's team | Product 1, second user |
| Omar Zahra | Owner's in-house counsel | Product 1, review routing |
| Priya Raghavan | Owner's design and engineering manager | Product 2, the user |
| Tom Beckett | Project director, Jebel Nasr | Product 3, the sponsor |
| Layla Haddad | Lead estimator, capital projects | Product 3, the user who gets challenged |

**Day one, the only setup Faisal does: five read-only connections.** No migration, no new system of record.

| Source | What it is | Volume at connection |
|---|---|---|
| `\JN4\02-Contract\` on SharePoint | The EPC contract, 14 amendments, the particular conditions | 61 PDFs |
| `JN4-correspondence-2024-2026.zip` exported from Aconex | Letters, transmittals, notices, minutes | 11,482 documents |
| `\JN4\07-Site\DSR\` | Daily site reports, about 30 a week | 3,140 PDFs |
| `JN4-P6-2026-07.xer` | The monthly schedule update from P6 | 1 file, 8,900 activities |
| `KEC-IPA-039.pdf` | The current interim payment application | 1 file |

Names, clauses and companies are illustrative for a case study.

---

## SLIDE 8 — Product 1: what it actually does, in Faisal's week

For Faisal Al-Harbi, the owner's contracts and commercial manager on Jebel Nasr Train 4. His team of four connects the existing record once, then starts with the event that matters: on 3 August 2026, KEC submits claim 07, `KEC-CL-007.pdf`, for $40.2M and 96 days of extension, built on six delay events.

The agent reads the contract, letters, schedule update and site reports overnight, then gives Faisal a cited position:

- **Event 2 notice was late.** `KEC-L-1987`, dated 41 days after the event in `DSR-2026-02-14`. The 28-day requirement means 13 days late, so the event is barred.
- **Event 4 has no notice at all.** No notice appears in the 11,482 documents.
- **Event 5 went to the wrong recipient.** `KEC-L-2043` is addressed to the site manager, not the named recipient. Defective notice.
- **Events 1, 3 and 6 were properly notified.** Their notices are found and valid.
- **Position.** 41 documents cited. $40.2M claimed, less $12.4M barred, less $5.6M of quantum the record does not support, leaves **$18.0M defensible**.
- **Milestone 4 was certified 47 days late.** Certificate `JN4-MC-004` against the milestone date in the contract means 47 days at $45k, or **$2.1M** chargeable this month.
- **An unregistered exposure.** `KEC-L-2214` of 14 May 2026 signals a claim not in the risk register: **$3.3M**, with 6 days left to reply.

Every item shows the money at stake, how confident the agent is, and the documents behind it. Faisal approves, edits or rejects. The agent writes the letter. A person sends it.

Two things make it credible: it never sends anything itself, and every line clicks through to a page in a real document.

---

## SLIDE 9 — How Product 1 works, end to end

```
INPUT                        PROCESSING                          ACTION                     DETERMINISTIC OR AGENTIC
contract + 14 amendments  →  parse, split by clause      [code]
                             extract obligations,
                             notice windows, recipients  [model]
                                    ↓
letters, notices,         →  classify document type      [model]   →  link to the timeline    deterministic write
minutes (11,482)             extract dates, parties,               [code]                     (a link, not an opinion)
                             the event referred to       [model]
                                    ↓
daily site reports        →  extract event facts:        [model]
(3,140)                      what stopped, where, when
                                    ↓
P6 update (.xer)          →  read dates and float        [code]
                                    ↓
                             ONE PROJECT RECORD: events, obligations, deadlines, documents
                                    ↓
                             notice window test          [code]   →  event valid / barred      deterministic, always
                             damages calculation         [code]   →  47 days x $45k = $2.1M    deterministic, always
                             quantum bounds              [code]   →  supported / unsupported   deterministic, always
                                    ↓
                             build the position          [model]  →  a ranked finding with     agentic proposal,
                             (event to clause mapping,               a money number and an     never an action
                             evidence selection)                     evidence chain
                                    ↓
                             citation check              [code]   →  no citation, no finding   deterministic veto
                                    ↓
                             HUMAN REVIEW               [human]   →  approve / edit / reject   the only gate that
                                                                                               releases anything
                                    ↓
                             draft the notice or         [model]  →  a document in the         agentic drafting,
                             rebuttal                                owner's own template      zero send authority
                                    ↓
                             send                       [human]   →  a person presses send     never the agent
                                    ↓
                             record the outcome          [code]   →  settled at what number,   deterministic learning
                                                                     which findings held        signal
```

Autonomy, stated plainly: the agent is autonomous about reading, linking, calculating and proposing. It has no autonomy over anything that leaves the building.

---

## SLIDE 10 — Product 1: what it's worth, and what it costs you

**Value (money).** On a $5bn project, our conservative model:

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

**Likelihood of delivering: high.** The evidence lives in documents the owner already holds. Deadline maths is arithmetic, not judgement. Every output is checkable against a cited page. The category is already proven commercially: Document Crunch reached 400+ customers and Trimble bought it for $246.4M in April 2026.

**Effort from the persona: low.** Give us a read-only copy of the contract and the correspondence archive. Spend about 20 minutes a day on a ranked queue. Nothing to migrate, no new system of record, no change to the monthly cycle.

**Sacrifice from the persona: real but answerable.** They're letting software read the most commercially sensitive, sometimes legally privileged, material on the project. Our answer: in-Kingdom or in-UAE hosting, private cloud, no training on their data, access mirroring the existing commercial team's permissions, and a full audit trail of what the agent read and why.

---

## SLIDE 11 — Product 2: what it actually does, in Priya's week

For Priya Raghavan, the owner's design and engineering manager on Jebel Nasr Train 4. On 12 June 2026, the design contractor issues sheet `A-207 rev C` for the process area. Priya does nothing different: the revision lands in the same transmittal folder it always did.

Three checks run in four minutes and hand back a cited pass or fail list:

- **Legal.** Fire separation is 1.2 m short. The fire chapter of the Saudi Building Code, clause 7.4.2, is quoted verbatim with the page, next to the drawing region.
- **Affordable.** The change costs $6.8M against $4.1M of remaining design allowance. The cost model line and the approved budget ceiling are shown.
- **Buildable.** Moving the 132 kV transformer adds 14 weeks to a long-lead order already on the critical path. The purchase order date and the P6 activity are shown.

Priya accepts the first finding, disputes the second as "already waived by the authority", and issues the revision with the exception recorded. The dispute becomes a labelled error we report on.

It's a spell-check for feasibility. It catches the error while it costs thousands, not the tens of millions it becomes once it's in the ground.

Strongest demand signal in the market: Dubai Municipality is building a system to issue permits automatically by reading submitted drawings against the Dubai Building Code. When the regulator automates the check, every owner has to arrive pre-compliant.

---

## SLIDE 12 — How Product 2 works, end to end

```
INPUT                        PROCESSING                          ACTION                     DETERMINISTIC OR AGENTIC
code edition, pinned      →  index clauses, keep the     [code]
by Priya on day one          page and the exact text
budget ceiling, pinned    →  store as a number           [code]
                                    ↓
drawing / document        →  detect the revision,        [code]   →  start a check run        deterministic trigger
revision (A-207 rev C)       diff against rev B                                              (no human asked for it)
                             read geometry, labels,      [model]
                             specified materials
                                    ↓
                             LEGAL     clause retrieval  [code]
                                       clause-to-drawing [model]  →  finding, clause quoted   agentic proposal
                                       comparison                    verbatim + drawing region
                             AFFORDABLE cost delta       [code]   →  $6.8M vs $4.1M left      deterministic
                             BUILDABLE  clash geometry   [code]
                                        long-lead dates  [code]   →  14 weeks on a critical   deterministic
                                                                     path order
                                    ↓
                             citation check              [code]   →  no clause text, no       deterministic veto
                                                                     finding
                                    ↓
                             HUMAN VERDICT              [human]   →  accept / dispute /       advisory, never blocking:
                                                                     accept with a waiver     the revision can always
                                                                                              be issued
                                    ↓
                             record the dispute reason   [code]   →  a labelled error         deterministic learning
                                                                                              signal
```

---

## SLIDE 13 — Product 2: what it's worth, and what it costs you

**Value (money).** On a $5bn project:

| Step | Number | Source |
|---|---|---|
| Rework at ~5% of project cost | ~$250M | CII IR-153 |
| Share caused by design (~28%) | ~$70M | industry analyses in the report |
| Catch half of it in design | **~$35M avoided per project** | our model on sourced inputs |
| On a $20bn project, the design-caused pool | ~$280M | same method |
| Review time | 6 weeks down to 3 days on Saudi Building Code review | WhiteHelmet customer testimonial, 2026 (self-reported) |
| Independent return modelling | 4:1 to 30:1 cost avoidance; a query costs $200–500 at drawing stage vs $2,000–8,000 in the field | Mirage Metrics, 2026 |

**Likelihood of delivering: high on a narrow scope, medium if we promise everything.** Reading drawings and code is now doable, and two Gulf vendors already sell a version of it. The honest risk is coverage: we start with one code set and the disciplines that cause the most rework, and we say so.

**Effort from the persona: lowest of the three.** It hooks into the design file drop that already happens. One-time job: confirm which code edition and which budget ceilings apply. After that the designer's habit doesn't change at all.

**Sacrifice from the persona: professional pride, mostly.** A machine is marking an engineer's work inside the engineer's own workflow. Our answer: advisory, never blocking; every finding cites the clause and the drawing region; one click to dispute a finding, and disputes train the next version.

---

## SLIDE 14 — Product 3: what it does, and why it waits

For Tom Beckett, project director of Jebel Nasr, and Layla Haddad, lead estimator for capital projects. Product 3 runs once per gate, later. Train 5 goes to the investment committee with a $6.1bn estimate and 8% contingency.

Before it is used forward, the agent runs backwards on 14 of the owner's own finished projects and shows what it would have said about each. Layla gets the challenge book first, privately. The agent asks nine questions and casts no vote.

The agent pressure-tests the number: it compares this project against how comparable past projects actually turned out, audits the design package for the gaps that predict overruns, and writes the challenge book for the gate meeting.

Why it waits: it needs the owner's own project history, and it tells the most senior people in the room that their number is wrong. That's a sale you make once you're already trusted and already inside the data. Products 1 and 2 buy that position.

The prize is the biggest, though: EY finds a 23% average overrun **after** approval. On a $5bn approval, that's $1.15bn of exposure. Taking a fifth of it off the table is $230M.

---

## SLIDE 15 — How Product 3 works, end to end

```
INPUT                        PROCESSING                          ACTION                     DETERMINISTIC OR AGENTIC
14 finished owner         →  extract sanctioned vs       [model]
projects                     final cost and date         [code]
                                    ↓
                             REFERENCE CLASS: median growth, spread   [code]
                                    ↓
this gate's estimate,     →  definition completeness     [model]  →  what is missing from     agentic proposal
basis of estimate,           audit against the owner's                the definition at this
schedule, contingency        own gate standard                        gate
                             contingency vs the          [code]   →  8% asked, 23% median     deterministic
                             reference class                          historical growth
                                    ↓
                             citation check              [code]   →  every number traced to   deterministic veto
                                                                     a source document
                                    ↓
                             PRIVATE PRE-READ to the     [human]  →  the estimator sees it    no surprise in the room
                             estimator and sponsor                    first and can respond
                             challenge book: nine        [model]  →  questions, not a         the agent never votes
                             questions with evidence                 recommendation
```

The agent never votes. It gives Layla and Tom a cited set of questions before the gate meeting.

---

## SLIDE 16 — The three side by side

| | **1. Claims defence & recovery** | **2. Design feasibility** | **3. Approval red team** |
|---|---|---|---|
| Persona | Contracts / commercial manager | Design / engineering manager | Project director, estimator, investment committee |
| Stage | Build | Design | The approval vote |
| Value per $5bn project | ~$30M | ~$35M | ~$230M of exposure addressed |
| Likelihood of delivering | High | High on a narrow scope | Medium |
| Effort from the persona | Low: read-only files, 20 min/day | Lowest: hooks existing file drop | High: hand over portfolio history |
| Sacrifice | Trusting software with privileged commercial material | Being marked by a machine | Political: an unwelcome message at the biggest vote |
| Data needed | Contract, letters, schedule, site reports | Drawings, code set, budget ceilings | Historical outcomes across the portfolio |
| Verdict | **Ship first** | **Ship in parallel** | **Earn the right, then ship** |

The rule behind the order: value divided by (effort + sacrifice), with delivery confidence as the multiplier. Product 3 wins on value alone and loses on everything else, which is exactly why it's third and not never.

---

## SLIDE 17 — The adoption promise (this is the real product decision)

The fastest way to lose this market is to ask a project team to change how it works mid-project. So we commit to six rules:

1. **Runs on files they already have.** Read-only. No migration, no new system of record.
2. **No new habit.** It arrives where they already look (email or Teams), and reviews happen on one screen.
3. **The agent never sends.** It drafts. A person presses send. Always.
4. **Every claim is clickable.** No assertion without a citation to a page in a real document.
5. **Proof on history first.** We run on last year's closed files and show what it would have caught, before it touches a live project.
6. **Priced against one avoided loss,** and sized so a pilot sits inside one project team's own authority.

That last one matters commercially: ADNOC signed a $340M three-year agentic-AI contract, but only after a proof of concept. The deal shape in this market is small paid pilot, then large multi-year contract.

---

## SLIDE 18 — Proof from people who live it

> "The difference between the amount submitted for a claim versus the amount actually paid at settlement... is as much as half. The owner too must ensure profitability of his project by defending unsupportable claims by a 'low ball' contractor."
> IPA via National Academies and Long International. *Product 1, stated from the owner's seat.*

> "What most projects lose to poor claims management is not a dispute they should have won, but entitlement they never assembled the evidence to claim."
> Kairos, claims advisory, 2026. *The failure mode named exactly.*

> "A fully integrated digital system capable of issuing building permits automatically and without human intervention by reading submitted drawings and documents, verifying compliance with the Dubai Building Code."
> Dubai Municipality, 2026. *Product 2's demand signal, from the regulator.*

> "We reduced our compliance review cycle from 6 weeks to 3 days. The AI caught two fire environmental gaps that would have delayed our building permit by months."
> WhiteHelmet customer, 2026 (self-reported). *Product 2, quantified in the Gulf.*

> "More than half of its potential lost to underperformance... all shared a root cause: bias."
> McKinsey on an owner's capital portfolio, 2025. *Product 3's reason to exist.*

> "ADNOC is on a mission to become the world's most AI-enabled energy company." $340M, three years, after a proof of concept.
> Musabbeh Al Kaabi, ADNOC Upstream CEO, 2025. *The willingness to pay, and the price ceiling.*

Honest gap: no on-record Aramco or ADNOC executive naming a claims, estimating or design-check tool specifically. Owner demand for Product 2 is inferred from the regulator's move and the mandatory building-code reset. We validate that in primary interviews.

---

## SLIDE 19 — How it works, in one picture

```
  FILES THE OWNER ALREADY HAS
  contract · letters & minutes · schedule updates · site reports · drawings · cost ceilings
            |
            v
  1  READ AND FILE          every page split, dated, tagged to a party, a drawing or an activity
            |
  2  BUILD THE RECORD       one linked timeline of events, obligations, revisions and deadlines
            |
  3  APPLY THE RULES        deadline maths, code clauses, cost bounds. Arithmetic, not opinion
            |
  4  REASON OVER IT         "does this event trigger a clause?" "does this revision close last round's comments?"
            |
  5  SIZE THE MONEY         value at stake, confidence, and what happens if you do nothing
            |
  6  SHOW YOUR WORKING      every finding carries citations. No citation, no finding
            |
  7  A HUMAN DECIDES        approve · edit · reject, on a queue ranked by money
            |
  8  DRAFT THE ACTION       the letter, the rebuttal pack, the challenge book
            |
  9  LEARN FROM THE OUTCOME what got approved, what got rejected, what the settlement actually was
```

Two engineering commitments behind that picture:

- **The hard maths is deterministic, the soft reading is the model's job.** Deadlines, damages and cost bounds are computed in code so they're always reproducible. The model reads and proposes, it doesn't do the arithmetic that ends up in a letter.
- **Nothing ships without an eval.** Each skill has a scored test set built from closed projects: did it find the events a specialist found, did it invent anything, did it get the deadline right. Releases are gated on those scores.
- The per-product diagrams are the detail behind that picture.

---

## SLIDE 20 — How we'll know it's working

**Business.** Money kept or recovered per project (the number the pilot is judged on), pilot to contract conversion, share of project value captured in price.

**Product.** Items reviewed per week per manager, share of drafted actions actually sent, time from an event appearing in the record to a human deciding on it, and one honest counter-metric: how often a manager overrides the agent, and whether that falls.

**AI engineering.** Recall against a specialist's own findings on closed projects, invented-fact rate at zero tolerance for cited claims, deadline accuracy, and cost per document read.

---

## SLIDE 21 — What success looks like for the agent

Four gates, in order. Nothing moves to the next gate until the previous one passes. Each gate has a pass mark and a stop rule, and each is measured on the owner's own closed projects before it is measured on a live one.

**Gate 0. Reading is trustworthy (offline, closed project archive)**

| What we measure | Pass mark | Why this number |
|---|---|---|
| Documents read and correctly typed | 98% or better | Below this, the record has holes and every later number is suspect |
| Dates extracted correctly | 99.5% or better | A wrong date is a wrong deadline, which is the one error the product cannot survive |
| Documents refused and queued for human | Reported, not hidden; under 5% of volume | Abstaining is allowed. Guessing is not. |
| Invented facts | Zero. Any occurrence blocks the gate | This is a legal record. |

**Gate 1. Findings are worth a person's attention (offline, against a specialist's own conclusions)**

| What we measure | Pass mark |
|---|---|
| Precision on findings shown as findings | 85% or better |
| Recall against commercial team’s closed-project findings | 80% or better, and at least one material item they missed |
| Evidence chain accuracy | 99.5% or better |
| Deadline arithmetic | 100% |
| Low-confidence items shown as “watching” | 100% |

Stop rule: precision below 60% after eight weeks means return to Gate 0.

---

## SLIDE 22 — What success looks like for the agent (continued)

**Gate 2. A human agrees, in practice (shadow mode on a live project, nothing sent)**

| What we measure | Pass mark |
|---|---|
| Findings actioned rather than only seen | 80% or better |
| Drafts approved with minor edits or none | 70% or better |
| Override rate | Falling week on week |
| Digest ignored two days running | Under 10% of weeks |
| Cost per document read | Under $0.05 blended |

Stop rule: four straight weeks without review pauses the pilot.

**Gate 3. It changed the money (live pilot, the number the pilot is judged on)**

| What we measure | Pass mark |
|---|---|
| Exposures surfaced and countersigned | $20M or more per pilot project |
| Notice deadlines missed on covered scope | Zero |
| Money kept or recovered agreed before pilot | Beats pilot fee by 5x or better |
| Findings surviving to settlement | Reported honestly, including failures |

**The one number for each product**

- Product 1: money kept or recovered per project, countersigned by the customer.
- Product 2: share of flagged findings that would have become field changes, measured on closed revision history, with dispute rate as honest counter-metric.
- Product 3: gate decisions changed, meaning contingency raised, scope re-cut, or approval deferred, with estimator agreement that the question was fair.

---

## SLIDE 23 — Risks, and what we do about them

| Risk | What we do |
|---|---|
| Owner won't give a machine the privileged commercial record | Start on closed projects. In-region private cloud. Permissions that mirror the existing team. Full read audit. |
| Wrong finding damages a legal position | Draft only, never send. Everything cited. Deadline and damages maths in code, not model output. |
| Code coverage in Product 2 is thinner than promised | Narrow first release: one code edition, the disciplines that cause the most rework. Publish what's in scope. |
| Incumbents move (Trimble, Procore, and the AI vendors) | They're contractor-side and build-phase. We're owner-side across design, approval and build, on data they don't have. |
| Product 3 needs history the owner may not have organised | Bundle the history clean-up as the first paid step, and lean on public outcome data until it exists. |
| Buying gates in the Gulf (registration, local content, cyber certification, data residency) | Treat them as features on the roadmap from day one, not paperwork at the end. |

---

## SLIDE 24 — First 90 days

- **Days 1–15.** Ten interviews: owner contracts managers, design managers, one estimator, one investment-committee member. Validate the $400M claims-submission assumption against a real portfolio.
- **Days 16–45.** Product 1 on one closed project's archive. Success test: it finds what the commercial team found, plus at least one thing they missed, all cited.
- **Days 30–60.** Product 2 on one FEED revision history. Success test: it flags the errors that actually became field changes.
- **Days 60–90.** One paid pilot signed on a live project, with the money-kept metric agreed in writing before we start. Compliance work (hosting, cyber certification, local content) running in parallel.

Product 3 gets a retrospective demo only in this window: "here are the twelve flags we'd have raised at your last approval." No sale attached yet.

---

## SLIDE 25 — Product 1 delivery plan on a page

| Phase and weeks | Objective | Key results that matter most | Gate that ends it |
|---|---|---|---|
| Phase 1, weeks 1 to 6 | Show that the agent reads one owner's closed project better than a person could in the time available, with nothing invented. | Documents read and correctly typed: 98% or better; dates extracted correctly: 99.5% or better; invented facts: Zero. One occurrence fails the phase | Gate 0 |
| Phase 2, weeks 7 to 14 | Show that what the agent proposes is worth a commercial manager's attention, and that it knows when to keep quiet. | Precision on items shown as findings: 85% or better; recall against what the commercial team actually found on that closed project: 80% or better; material items the team missed, found and cited: at least one | Gate 1 |
| Phase 3, weeks 15 to 26 | Put the agent beside a live team, in shadow mode with nothing sent, and earn the right to charge. | Findings actioned rather than only seen: 80% or better; drafts approved with light edits or none: 70% or better; cost per document read: under $0.05 blended | Gate 2 |
| Phase 4, months 7 to 12 | Show money kept that the customer will put their name to, and turn one project into a portfolio. | Exposures surfaced and countersigned: $20M or more on the pilot project; money kept or recovered against the pre-agreed metric: beats the pilot fee by 5x or better; notice deadlines missed: Zero | Gate 3 |

**Annual objective:** Turn one owner's closed archive into a paid, renewed, referenceable claims defence deployment, with the money kept counted by the customer and not by us. **Headline annual key results:** $20M or more of countersigned exposures; pilot conversion to a multi-project contract of $2M or more by month 12.

---

## SLIDE 26 — Where this goes

Same reading layer, more skills, in the order the owner will accept them:

- **During the build:** is the cost forecast honest, is the schedule telling the truth, are the gaps between contractors going to bite.
- **In design:** which of the 3,900 late documents actually threaten the finish date.
- **At handover:** what's missing before operations will accept the asset.
- **Then the loop closes:** every finished project becomes evidence for the next approval vote. That history is the owner's own, and it compounds, which is the part no competitor can copy.
