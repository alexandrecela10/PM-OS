# Commercial Guardian Agent — v1 harness

Governance-first agent for surfacing commercial exposure on capital megaprojects, with a runnable eval harness and dummy inputs. Zero external dependencies, zero network, zero data egress — Python 3.10+ stdlib only.

## Run it

```bash
python3 run_evals.py          # human-readable eval report
python3 run_evals.py --json   # machine-readable
```

Exit code 0 only when all 17 evals pass. Governance evals are hard gates.

## What's here

```
agent/
  governance.py   # the core: policy kernel checked BEFORE every node runs
  audit.py        # append-only, hash-chained audit log
  graph.py        # explicit DAG; parallel per-doc extraction, sequential governance chain
  nodes.py        # deterministic citation verifier + deadline rules engine
  llm.py          # model adapter boundary; deterministic dummy + adversarial adapter
  models.py       # datatypes
evals/
  harness.py      # 8 eval suites (detection, evidence, deadlines, hallucination, 4x governance)
  datasets/project_alpha.json  # dummy project: contract, letters, minutes, out-of-scope doc, missing amendment
run_evals.py      # entry point
```

## Design in one paragraph

Governance is the runtime, not a review step: every action passes an allowlist check before execution, out-of-scope documents are refused at ingest, "send" does not exist as a capability, and notices stop at `PENDING_APPROVAL` until a named human from the owner registry approves. LLM judgment (extraction) is fenced by deterministic verifiers: citations must resolve and quote-match real documents or the finding never surfaces, and notice deadlines come from a rules engine, never model math. The dummy adapter makes evals reproducible offline; the production slot is a self-hosted, in-region open-weights model behind the same interface, so the same evals gate the real thing.

Full rationale: `outputs/prds/ai-engineering-prd-commercial-guardian-agent-2026-08-26.md` and the session journal.
