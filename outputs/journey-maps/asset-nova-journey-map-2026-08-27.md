# Journey map: the three Asset Nova products

**Date:** 2026-08-27
**Companion artifacts:** `outputs/prototypes/asset-nova-journeys.html` (wireframe slides), `outputs/prototypes/asset-nova-round2-deck.html` (deck), `outputs/prds/`

One rule shapes all three journeys: the product runs on files the owner already has, arrives where the team already looks, and never sends anything itself.

## Product 1: claims defence and recovery (always on)

**Persona:** owner contracts and commercial manager, live build.
**Trigger:** the record changed. This is the only always-on product.
**Cadence:** a daily queue, about 20 minutes to clear.

| Stage | What the person does | What the product does | Feeling | Risk of drop-off |
|---|---|---|---|---|
| Setup | Points us at a read-only copy of the contract and correspondence archive | Reads and links the record, no migration | Cautious about privileged material | High. Answer with in-region private cloud, mirrored permissions, read audit |
| Overnight | Nothing | Reads new documents, applies deadline rules, sizes money | Neutral | Low |
| Morning digest | Opens email or Teams | Sends the ranked queue, money first | "This is about my week" | Medium if the digest is noisy |
| Queue | Scans five to ten items | Ranks by money at stake with confidence and deadline visible | In control | Medium. Precision matters more than recall here |
| Evidence | Opens one finding | Shows the event, the clause, the arithmetic, clickable source pages | Trust or suspicion, decided here | High if any claim lacks a citation |
| Decision | Approves, edits or rejects | Records the disposition as a label | Ownership | Low |
| Action | Reviews the draft, presses send | Drafts the notice, rebuttal or evidence pack. Never sends | Relief | Medium if drafts need heavy editing |
| Outcome | Logs settlement or recovery | Tracks money kept against what was claimed | Proof | Low |
| Month end | Asks for the brief | Assembles exposures and recoveries on demand | Credit with the sponsor | Low |

**Alternates considered:** (a) closed-project backtest only, which is how we prove value but is not a product, and (b) a claim-arrival workflow triggered by each contractor letter, which misses the owner's own recovery clock. The daily always-on queue wins because it covers both directions of money, and it is the only shape that catches a deadline the owner would otherwise let lapse.

## Product 2: design feasibility (event driven)

**Persona:** owner design and engineering manager, design and FEED.
**Trigger:** a drawing or document revision is issued.
**Cadence:** minutes per revision.

| Stage | What the person does | What the product does |
|---|---|---|
| Setup | Names the code edition and the budget ceiling | Pins both, so findings are checkable |
| Revision arrives | Nothing, the existing file drop is the input | Checks compliance, affordability and buildability |
| Verdict | Reads a cited finding | Quotes the clause verbatim and shows the drawing region |
| Disagree or accept | One click, with a reason | Records the reason as a labelled error, issues anyway if asked |
| Issue | Issues the revision | Writes any exception onto the record |

Advisory, never blocking. An engineer overruled by a machine once will route around it forever.

**Alternates considered:** a design-review meeting pre-read pack, and a gate checklist at the end of FEED. Both are slower feedback and lose the labelled-dispute data. Per-revision checking wins.

## Product 3: FID red teaming (waits)

**Persona:** project director, lead estimator, investment committee, at the approval vote.
**Trigger:** a gate date in the diary.
**Cadence:** once per gate.

Retrospective analysis on the owner's own finished projects first, then a private sponsor pre-read, then a challenge book for the meeting. The agent asks questions and never casts a vote. This product waits because it challenges the most senior people in the room and it needs historical project outcomes that only a trusted supplier gets access to.

## Where the next opportunities sit

Same reading layer, further along the same lifecycle: concept red-teaming and option comparison before design, drawing-chase and late-deliverable warning during design, cost-forecast and schedule truth during build, handover completeness at start-up, and finished-project history feeding the next approval vote.
