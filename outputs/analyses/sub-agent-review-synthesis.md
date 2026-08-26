# Sub-Agent Review Synthesis — Commercial Guardian PRD

Date: 2026-08-26. Five reviewers: engineer, skeptic, executive, legal, customer-voice.

## Top findings by severity

### Critical (must fix for the case study)

1. **Discoverability of the exposure register is the #1 customer objection** (Legal + Customer-voice + Skeptic). An AI-logged register of "known but unactioned exposures" is discoverable in arbitration and internal audits. The Capital Projects Director said it plainly: "Every flagged event is a variance I now must explain." The Contracts Manager is "terrified" of signing dispositions that create a "you knew" trail.
   - **Fix:** Add governance of visibility as a design principle. Customer counsel as agent owner where possible. Customer-controlled retention/deletion. Disposition as team decision, not individual. Add this risk to the PRD risk table with mitigations.

2. **Liability for wrong deadline computation** (Legal). A wrong date can extinguish a $60M entitlement. "100% on test suite" isn't a legal shield for bespoke amendments.
   - **Fix:** Add to risk table. Contractual liability cap, express disclaimer, mandatory customer verification step, tech E&O insurance. The deterministic engine is right but the PRD must acknowledge bespoke contracts.

3. **Value chain confuses "surfaced" with "recovered"** (Skeptic + Executive). $30-80M stacks two low-confidence assumptions. "Validated exposures" is a soft metric — customers can bless big numbers costlessly. ARR math ($10-12M) isn't bottoms-up.
   - **Fix:** Separate owner math (claims defended) from contractor math (entitlement preserved). Anchor demo on one real backtested lapsed time-bar. Build bottoms-up ARR bridge for the deck.

### Serious (should fix)

4. **Hallucination metric is undefined** (Engineer). <0.5% per what unit? Weekly spot-audit can't give statistical confidence. Evidence-chain accuracy at 98% means broken citations in most reviews.
   - **Fix:** Redefine as unsupported assertions per drafted notice, verified by automated claim-to-citation entailment check + 100% human review pre-send. Evidence-chain accuracy target to 99.5%+ for surfaced events via deterministic citation verifier.

5. **Model stack is invisible** (Engineer + Executive). No mention of which models, on-prem GPU sizing, OCR pipeline. Interviewer will ask "which model on what hardware."
   - **Fix:** Add one paragraph: open-weights fine-tuned (Llama/Qwen-class), sovereign GPU, OCR preprocessing pipeline with ingestion quality metrics.

6. **Contracts teams may not want this / incentive inversion** (Skeptic + Customer-voice). The tool grades their homework. Adoption risk is political, not technical.
   - **Fix:** Reframe as workload relief. Phase 0 backtest on closed project (no live political cost). Disposition as team, not individual. Triage volume cap per week.

7. **Confidentiality restrictions in underlying contracts** (Legal). Aramco-form contracts prohibit sharing correspondence with third parties. On-prem helps but customer reps/warranties needed.
   - **Fix:** Already partially covered. Add customer rep/warranty requirement to open questions.

### Minor (good to address)

8. **Competitive depth thin** — SuperHive, Sypro, Nodes & Links, CLM vendors unnamed (Executive + Skeptic). Fix: add one competitive slide to deck.
9. **XER parsing underestimated** (Engineer). Fix: acknowledge complexity; scope v1 to diff + flag, not full scheduling engine.
10. **Arabic language coverage** (Engineer). Fix: flag as open question for v1 scope.
11. **Unauthorized practice of law risk** (Legal). Fix: position as document automation under counsel supervision; get local counsel opinion.
12. **Both sides running agents creates adversarial dynamics** (Skeptic + Customer-voice QS). Fix: hard contractual separation between owner/contractor instances; name this as a feature, not a risk.

## Conflicts between reviewers

- **Executive wants bolder ARR numbers** and outcome-based pricing committed. **Skeptic says the value math is already inflated.** Resolution: show the math transparently with ranges, don't inflate; the discipline is the signal.
- **Engineer wants more metrics (OCR, ingestion quality).** **Customer-voice says the weekly review is already too much new work.** Resolution: internal engineering metrics (don't surface to user); simplify the user-facing ritual.

## What all five agreed on

- The backtest-on-closed-projects is the strongest move — de-risks the product, produces the sales artifact, and avoids live political cost.
- The governance section is a standout; keep it prominent in the deck.
- Read-only, no ERP integration is a credible deployment story.
- The "From X → To Y" framing resonates across all personas.
