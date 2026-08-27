# Session Journal — 2026-08-26 (evening) — Agent design, evals, and harness

Continues `journal-2026-08-26.md`. This session built the AI engineering layer of the Commercial Guardian case: an engineering PRD, a governance-first agent v1, and a runnable eval harness with dummy inputs. New files only; nothing existing was touched.

## What was built

| File | What it is |
|---|---|
| `outputs/prds/ai-engineering-prd-commercial-guardian-agent-2026-08-26.md` | AI engineering PRD: architecture, governance kernel spec, eval gates, self-improvement loop, tradeoffs |
| `outputs/prototypes/commercial_guardian_agent/` | Runnable v1: agent + eval harness, stdlib-only, `python3 run_evals.py` → 17/17 pass |

## Agentic design (what and why)

**Governance is the runtime.** The single most important decision. Ashu's rubric says governance is the product, and Aramco's bar is zero risk to key data and assets. So instead of an agent with a compliance review bolted on, every capability call goes through a `GovernanceKernel.authorize()` check *before* execution. The kernel owns:

1. **Scope** — the agent instance is registered to one project; out-of-scope documents are refused at ingest, logged, and escalated to the named agent owner. (Directly implements the PRD's "out of scope → nothing" answer.)
2. **Action allowlist** — capabilities are enumerated; "send" is not on the list, so autonomous outbound action is structurally impossible, not just discouraged. An eval verifies no send/dispatch method exists.
3. **Human gate** — notices stop at `PENDING_APPROVAL`. Approval requires a named human from the owner registry; unknown approvers and unverified-assertion notices are rejected.
4. **Sovereignty** — every document carries a residency tag; out-of-region data is refused at the gate. The dummy harness itself has zero network calls, so even CI is egress-free.
5. **Audit** — append-only, hash-chained log of every authorization, refusal, and approval. An eval verifies the chain and that every pipeline stage is audited.

**Graph, not loop.** The pipeline is an explicit DAG (ingest → policy gate → parallel extraction → deterministic verification → deterministic deadlines → draft → approval gate), not a free-running agent loop. Parallelism is used exactly where work is independent (per-document extraction fans out on a thread pool) and never across the governance chain, which is strictly sequential.

**LLM fenced by determinism.** The model does judgment (extract, classify, draft language). Two things it never does: verify its own citations (a deterministic verifier resolves every doc ID and quote-matches the source; failures are downgraded and never surfaced) and compute deadlines (a rules engine does contract math; missing amendments force a PROVISIONAL flag). This is how the PRD's 99.5% citation accuracy and 100% deadline accuracy targets become enforceable rather than aspirational.

## The evals

17 evals across 8 suites, run by `run_evals.py`, exit non-zero on any failure:

- **Detection**: precision ≥ 85%, recall ≥ 70% vs golden labels; golden non-events (a watch item, routine recovered slippage) must stay suppressed. The dummy dataset deliberately includes a signal the extractor misses (recall 75%, above gate) so the metric measures something.
- **Evidence**: every surfaced citation resolves and quote-matches (gate 99.5%).
- **Deadlines**: exact dates vs hand-computed goldens, including the missing-amendment case (GC 13.1 amended by AMD-3, absent from archive → deadline must come back PROVISIONAL).
- **Hallucination defense**: an adversarial `HallucinatingExtractor` fabricates a citation to a nonexistent document; the verifier must downgrade it and no notice may be drafted from it.
- **Governance (hard gates)**: out-of-scope refusal + logging, pipeline stops at PENDING_APPROVAL, no send capability exists, unauthorized approver rejected, named approver accepted, claim-strategy question refused with counsel routing, audit hash chain verifies, all stages audited.

## Tradeoffs and decisions

| Decision | Tradeoff accepted | Why |
|---|---|---|
| Explicit DAG over autonomous loop | Less flexible; new behaviors need new nodes | Determinism, per-node evals, per-node audit. Right call for zero-risk enterprise; a loop can't promise an MSA-grade guarantee |
| Precision-first (surface threshold 0.6) | Misses borderline events in v1 | False alarms kill the weekly review ritual, and the ritual is the product. Recall recovers via backtests; trust doesn't |
| Deterministic deadline engine | Per-contract-form configuration cost | Only code can hit 100%; an LLM computing a 28-day notice bar is a liability, not a feature |
| Deterministic dummy adapter (not mocked API) | Less realistic than replayed model traffic | Evals run offline, reproducibly, keyless — CI is itself sovereignty-compliant. Production model slots behind the same interface |
| Adversarial adapter in the suite | Extra maintenance | Tests the verifier, not the model. Hallucination defense must be structural |
| Governance evals as hard release gates | Slower iteration when a gate trips | "Governance at the core, not after the fact" has to mean a failing scope eval blocks the release |
| Parallelism only at doc-batch level | Slower than full-graph parallelism | Speed where safe, sequence where order is safety |

## Open items

- Swap in a real extractor (in-region open-weights) behind `ExtractorAdapter`; rerun the identical suite.
- Grow the golden set from backtests on closed projects; wire disposition capture (approve/edit/dismiss) into threshold tuning — the governed self-improvement loop from the PRD.
- Arabic documents, OCR ingestion, Aconex/P6 connectors — out of v1 scope, same interfaces.
- Consider showing `run_evals.py` output live in the interview: 17/17 with governance gates is a stronger artifact than a slide about governance.
