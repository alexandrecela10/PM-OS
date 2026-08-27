# Round 2 addendum: the named scenario, the agentic workflow per product, and the eval gates

This file is the authoritative source for three things the deck and the prototype were missing:

1. One concrete scenario, with named people, a named project and real file names, used everywhere.
2. A per-product diagram of the "how": inputs, processing, action, and whether each action is deterministic or agentic.
3. What success looks like for the agent: eval gates with pass marks, in the order they must be passed.

Everything below is illustrative for a case study. Clause numbers, code references, company and people names are invented to make the story concrete. That is stated on the slide.

---

## Part A. The canonical scenario

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

**Day one, the only setup Faisal does: three read-only connections.** No migration, no new system of record.

| Source | What it is | Volume at connection |
|---|---|---|
| `\JN4\02-Contract\` on SharePoint | The EPC contract, 14 amendments, the particular conditions | 61 PDFs |
| `JN4-correspondence-2024-2026.zip` exported from Aconex | Letters, transmittals, notices, minutes | 11,482 documents |
| `\JN4\07-Site\DSR\` | Daily site reports, about 30 a week | 3,140 PDFs |
| `JN4-P6-2026-07.xer` | The monthly schedule update from P6 | 1 file, 8,900 activities |
| `KEC-IPA-039.pdf` | The current interim payment application | 1 file |

**The event that starts the demo.** On 3 August 2026, KEC submits claim 07: `KEC-CL-007.pdf`, $40.2M and 96 days of extension, built on six delay events.

**What the agent finds overnight, and what it is worth.**

| Finding | The evidence in the record | The arithmetic |
|---|---|---|
| Event 2 notice was late | `KEC-L-1987`, dated 41 days after the event in `DSR-2026-02-14` | 28-day requirement, so 13 days late, event barred |
| Event 4 has no notice at all | No notice in 11,482 documents | Event barred |
| Event 5 notice went to the wrong recipient | `KEC-L-2043` addressed to the site manager, not the named recipient | Defective notice |
| Events 1, 3, 6 were properly notified | Notices found and valid | Stay in play |
| **Position** | 41 documents cited | $40.2M claimed, less $12.4M barred, less $5.6M of quantum the record does not support, leaves **$18.0M defensible** |
| Milestone 4 was certified 47 days late | Certificate `JN4-MC-004` against the milestone date in the contract | 47 days at $45k, **$2.1M** chargeable this month |
| An unregistered exposure | `KEC-L-2214` of 14 May 2026 signals a claim that is not in the risk register | **$3.3M**, 6 days left to reply |

**Product 2, same project, one revision.** On 12 June 2026, the design contractor issues sheet `A-207 rev C` for the process area. Priya does nothing different: the revision lands in the same transmittal folder it always did. Three checks run in four minutes.

| Check | Verdict | Evidence |
|---|---|---|
| Legal | Fire separation is 1.2 m short | The fire chapter of the Saudi Building Code, clause 7.4.2, quoted verbatim with the page, next to the drawing region |
| Affordable | The change costs $6.8M against $4.1M of remaining design allowance | The cost model line and the approved budget ceiling |
| Buildable | Moving the 132 kV transformer adds 14 weeks to a long-lead order already on the critical path | The purchase order date and the P6 activity |

Priya accepts the first finding, disputes the second as "already waived by the authority", and issues the revision with the exception recorded. The dispute becomes a labelled error we report on.

**Product 3, one gate, run backwards first.** Train 5 goes to the investment committee with a $6.1bn estimate and 8% contingency. Before it is used forward, the agent runs on 14 of the owner's own finished projects and shows what it would have said about each. Layla gets the challenge book first, privately. The agent asks nine questions and casts no vote.

---

## Part B. The agentic workflow, one diagram per product

Each diagram has the same four lanes: what goes in, what happens to it, what the agent does at the end, and the gate that decides whether the agent is allowed to do it. `[code]` means deterministic software with a testable answer. `[model]` means a language model reading and reasoning. `[human]` means a named person.

### Product 1: claims defence and recovery (always on)

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

### Product 2: design feasibility (event driven)

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

### Product 3: FID red teaming (once per gate, later)

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
                                    ↓
                             challenge book: nine        [model]  →  questions, not a         the agent never votes
                             questions with evidence                 recommendation
```

---

## Part C. What success looks like for the agent

Four gates, in order. Nothing moves to the next gate until the previous one passes. Each gate has a pass mark and a stop rule, and each is measured on the owner's own closed projects before it is measured on a live one.

### Gate 0. Reading is trustworthy (offline, closed project archive)

| What we measure | Pass mark | Why this number |
|---|---|---|
| Documents read and correctly typed | 98% or better | Below this, the record has holes and every later number is suspect |
| Dates extracted correctly | 99.5% or better | A wrong date is a wrong deadline, which is the one error the product cannot survive |
| Documents the agent refuses to classify, queued for a human | Reported, not hidden. Under 5% of volume | Abstaining is allowed. Guessing is not |
| Invented facts, meaning any statement not in a cited source | Zero. Any occurrence blocks the gate | This is a legal record |

### Gate 1. Findings are worth a person's attention (offline, against a specialist's own conclusions)

| What we measure | Pass mark |
|---|---|
| Precision on findings shown as findings | 85% or better |
| Recall against what the commercial team actually found on that closed project | 80% or better, and at least one material item they missed |
| Evidence chain accuracy, every cited page says what the finding claims | 99.5% or better |
| Deadline arithmetic | 100%, because it is a rules engine and not model output |
| Low-confidence items shown as "watching" rather than as findings | 100% |

Stop rule: precision below 60% after eight weeks of tuning means we go back to Gate 0 rather than ship.

### Gate 2. A human agrees, in practice (shadow mode on a live project, nothing sent)

| What we measure | Pass mark |
|---|---|
| Findings actioned rather than only seen | 80% or better |
| Drafts approved with minor edits or none | 70% or better |
| Override rate, and whether it falls week on week | Falling. A flat override rate means the ranking is wrong |
| Digest ignored two days running | Under 10% of weeks |
| Cost per document read | Under $0.05 blended |

Stop rule: if the team stops reviewing for four straight weeks, we pause the pilot. Silence is the real churn signal, not a cancelled contract.

### Gate 3. It changed the money (live pilot, the number the pilot is judged on)

| What we measure | Pass mark |
|---|---|
| Exposures surfaced and countersigned by the customer | $20M or more per pilot project |
| Notice deadlines missed on covered scope | Zero |
| Money kept or recovered, agreed in writing before the pilot starts | Beats the pilot fee by 5x or better |
| Findings that survived to settlement | Reported honestly, including the ones that did not |

### The one number for each product

- Product 1: money kept or recovered per project, countersigned by the customer.
- Product 2: share of flagged findings that would have become field changes, measured on a closed revision history, and the dispute rate as the honest counter-metric.
- Product 3: gate decisions changed, meaning contingency raised, scope re-cut or approval deferred, with the estimator's agreement that the question was fair.

---

## Part D. What to add where

**Deck** (`outputs/asset-nova-round2-deck.md` and the HTML):

- New slide after slide 6: "One project, one team, one week: the scenario the rest of this deck uses." Part A, the project, the people table and the three connections.
- Rewrite slides 7 and 9 to use Faisal, Priya and the real file names instead of the generic persona sentence.
- New slide after slide 7: "How Product 1 works, end to end" using the Product 1 diagram from Part B.
- New slide after slide 9: "How Product 2 works, end to end" using the Product 2 diagram.
- New slide after slide 11: "How Product 3 works, end to end" using the Product 3 diagram.
- New slide after slide 16: "What success looks like for the agent" using the four gates from Part C, one row per gate with its pass mark, plus the one number per product.
- Slide 15 stays as the shared picture. Add one line that says the per-product diagrams are the detail behind it.

**Prototype** (`outputs/prototypes/asset-nova-journeys.html`):

- Replace "Project X" with "Jebel Nasr Train 4" everywhere, and name the people on the screens they use.
- Screen 1 of Product 1 becomes the source-file view: the five connections from Part A with their real volumes, then the overnight counts.
- Add one slide per product with its Part B diagram, in the engineering flow section.
- Add one slide with the four gates and their pass marks, before the closing slide.
