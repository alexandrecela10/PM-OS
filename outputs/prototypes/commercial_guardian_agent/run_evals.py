#!/usr/bin/env python3
"""Run the full Commercial Guardian eval suite on the dummy dataset.

Usage: python3 run_evals.py [--json]
Exit code 0 only if every eval passes (governance suites are hard gates).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from evals.harness import run_all

DATASET = Path(__file__).parent / "evals" / "datasets" / "project_alpha.json"


def main() -> int:
    evals, result = run_all(DATASET)
    if "--json" in sys.argv:
        print(json.dumps([e.__dict__ for e in evals], indent=2))
    else:
        width = max(len(f"{e.suite}/{e.name}") for e in evals)
        print(f"\nCommercial Guardian — eval run on {DATASET.name}")
        print(f"docs admitted: {len(result.admitted_docs)} · refused: {len(result.refused_docs)} · events surfaced: {sum(e.surfaced for e in result.events)} · notices pending approval: {len(result.notices)}\n")
        for e in evals:
            mark = "PASS" if e.passed else "FAIL"
            print(f"  [{mark}] {f'{e.suite}/{e.name}':<{width}}  {e.detail}")
        passed = sum(e.passed for e in evals)
        print(f"\n{passed}/{len(evals)} evals passed.")
        if passed < len(evals):
            print("RELEASE BLOCKED: failing evals are hard gates.")
    return 0 if all(e.passed for e in evals) else 1


if __name__ == "__main__":
    raise SystemExit(main())
