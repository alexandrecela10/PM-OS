# Synthetic source files — Commercial Guardian walkthrough

Illustrative, fully synthetic project record for event EV-047 (Area 7 differing
site conditions) on the Jubail Gas Processing Expansion, EPC Package 3. These
are the inputs the agent "reads" in the walkthrough deck
(`../agent-walkthrough-deck.html`) and the live demo
(`../commercial-guardian-demo.html`).

| File | Simulates | System of record |
|---|---|---|
| 01-contract-extract-gc-4.12.md | Conditions of contract + Amendment 2 | Contract repository / CLM |
| 02-geotech-baseline-extract.md | Geotechnical Baseline Report | Document control |
| 03-daily-reports-area7.md | Contractor daily reports | Aconex |
| 04-correspondence-log.md | Correspondence register + meeting minutes | Aconex / email |
| 05-schedule-extract-p6.csv | P6 schedule export (XER simplified) | Primavera P6 |
| 06-change-register.csv | Change / variation register | Cost system |

## The timeline the agent reconstructs (all synthetic)

- 12 Jan 2025 — GBR baselines rippable ground to 6.5 m in Area 7
- 14 Mar 2026 — Amendment 2 cuts the notice bar to **21 days** for Areas 6-8
- 04 Aug 2026 — DR-1042: rock refusal at 2.1 m (awareness date)
- 12 Aug 2026 — C-1187: contractor's bare "reservation of rights" (no particulars)
- 25 Aug 2026 — contractor's 21-day bar under GC 4.12(b) **expired**
- 26 Aug 2026 — "today" in the demo
- 01 Sep 2026 — Owner's GC 20.1 notice deadline (28 days from awareness): **6 days left**

Bracketed **[...]** notes inside the files mark what the agent extracts; they
are annotations for the reader, not part of the simulated documents.
