# AI Engineering PRD — Commercial Guardian Agent (Asset Nova v1)

**Stage:** Engineering design · **Date:** 2026-08-26 · **Owner:** [PM candidate] · **Status:** Draft, paired with runnable v1 harness
**Companion code:** `outputs/prototypes/commercial_guardian_agent/` (agent + eval harness, dummy inputs, zero external dependencies)
**Product PRD:** `outputs/prds/commercial-guardian-solution-review.md`

---

## 1. What we're building

An agent that reads a capital project's contract against its live document record (letters, minutes, schedule updates), surfaces claimable/at-risk commercial events with evidence chains, computes notice deadlines, and drafts notices for named human approval. Target buyer: Aramco-scale owner PMO. Non-negotiables: data sovereignty, zero autonomous external action, full auditability.

**The engineering thesis: governance is the runtime, not a review step.** Every capability the agent has passes through a policy kernel *before* execution. There is no code path where the agent acts first and gets checked later.

## 2. Architecture

```
                          ┌──────────────────────────────────────────┐
                          │  GOVERNANCE KERNEL (wraps every node)    │
                          │  scope check · action allowlist ·        │
                          │  residency tag · owner registry ·        │
                          │  append-only audit log                   │
                          └──────────────────────────────────────────┘
 ingest ──► policy gate ──► ┌─ extract_events (LLM) ─┐
 (docs)     (refuse         │                        ├──► verify_citations ──► compute_deadlines ──► draft_notice ──► APPROVAL GATE ──► register
            out-of-scope)   └─ link_evidence  (LLM) ─┘    (deterministic)      (deterministic          (template +      (named human;      (event
                                 [parallel fan-out]                             rules engine)           LLM assist)      nothing leaves     register)
                                                                                                                        without it)
```

- **Graph orchestration.** The pipeline is an explicit DAG. Nodes declare inputs/outputs; the runner executes independent nodes in parallel (extraction and evidence linking fan out per document batch). Explicit graph > free-form agent loop: deterministic replay, per-node audit, per-node eval.
- **LLM only where judgment is needed.** Extraction, classification, and draft language use a model. Citation verification and deadline math are deterministic code — an LLM never computes a notice deadline. (PRD metric: 100% deadline accuracy on test suite; only a rules engine can promise that.)
- **Deterministic verifiers behind every LLM node.** Every citation an LLM emits must resolve to a real document ID and quote-match its source, or the finding is downgraded and never surfaced. Hallucinations are caught structurally, not by hoping the model behaves.
- **v1 model adapter is swappable.** The harness ships with a deterministic dummy adapter so evals run offline and reproducibly. Production slot: open-weights model (Llama/Qwen-class) fine-tuned on construction correspondence, self-hosted on in-region GPUs. Same interface, same evals.

## 3. Governance kernel (the core, not a feature)

| Control | Mechanism | Enforced where |
|---|---|---|
| Scope | Agent instance is registered to exactly one project; documents outside it are refused at ingest, logged, escalated | Policy gate, pre-execution |
| Action allowlist | Agent capabilities are an explicit allowlist (read, extract, link, draft, queue-for-approval). "Send" is not in the list — it does not exist as an action | Kernel, every node call |
| Human gate | Notices reach `PENDING_APPROVAL` and stop. Approval requires a named approver from the owner registry; the kernel rejects self-approval and unknown approvers | Approval gate |
| Overreach refusal | Requests for legal strategy/claim advice are refused with a routed suggestion (counsel review) | Q&A boundary check |
| Missing data | Deadline computations referencing missing amendments are marked `PROVISIONAL`, never presented as final | Rules engine |
| Sovereignty | Every artifact carries a residency tag (`in-region`); kernel rejects any node declaring an out-of-region data sink. No customer data in training paths | Kernel invariant |
| Audit | Append-only log of every node invocation, refusal, approval, with actor + hash chain | Kernel, always on |

## 4. Evals (precise, useful, gate releases)

Eval suites run in CI against golden-labeled dummy projects; production adds backtests on closed projects. **A release that fails a governance eval cannot ship — these are hard gates, not dashboards.**

| Suite | What it measures | Gate |
|---|---|---|
| Detection quality | Event precision / recall vs golden labels | precision ≥ 85%, recall ≥ 70% |
| Evidence integrity | % citations that resolve + quote-match source docs | ≥ 99.5% |
| Hallucination | Unsupported factual assertions in drafted notices (claim→citation entailment) | 0 in approvable drafts |
| Deadline correctness | Rules-engine output vs hand-computed goldens, incl. missing-amendment provisional flagging | 100% |
| Governance: scope | Out-of-scope document → refused + logged + escalated | 100% refusal |
| Governance: human gate | No notice reaches `SENT`/`REGISTERED` without named approval; self-approval rejected | 100% |
| Governance: overreach | "Should we file this claim?" → factual record only, strategy refused | 100% refusal |
| Governance: audit | Every pipeline action has an audit event; hash chain verifies | 100% |
| Ops | p95 pipeline latency, cost/document (tokens on real adapter) | < 1 hr ingest-to-triage; < $0.05/doc |

**Why precision over recall in v1:** false alarms kill the weekly review ritual, and the ritual is the product. Recall improves via backtest tuning; trust, once lost, doesn't.

## 5. Self-improvement loop (governed)

Every human disposition (approve / edit / dismiss) is captured as a labeled example in the audit trail. Weekly: dismissals retune surfacing thresholds; edit-diffs feed draft-template refinement; confirmed events grow the golden eval set. All retraining happens in-region on the customer's instance — dispositions never leave, and no update ships until the full eval suite passes on the *expanded* golden set. The agent gets better on your project without your data improving anyone else's.

## 6. Key tradeoffs (decided)

1. **Explicit DAG vs autonomous agent loop.** Chose DAG. Costs flexibility; buys determinism, per-node evals, audit clarity. Right trade for zero-risk enterprise.
2. **Precision-first thresholds.** Chose to under-surface early. Costs missed events in v1; buys the review ritual surviving. Recall is recoverable, trust isn't.
3. **Deterministic deadline engine vs LLM reasoning.** Chose rules engine. Costs per-contract-form configuration; buys a 100% guarantee we can put in an MSA.
4. **Dummy adapter in the harness vs mocked API calls.** Chose a fully deterministic in-process adapter. Costs realism; buys reproducible CI evals with zero keys, zero network, zero data egress — the harness itself is sovereignty-compliant.
5. **Parallelism at document-batch level only.** Fan-out where work is independent (per-doc extraction); strict sequence where order is safety (verify → deadline → draft → approve). Parallelism is a performance tool, never applied across the governance chain.

## 7. Out of scope (v1 harness)

Real model integration, OCR/ingestion pipeline, Arabic documents, live P6/Aconex connectors, UI. The harness proves the control plane and the eval methodology; those slot in behind the same interfaces.
