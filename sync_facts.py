# -*- coding: utf-8 -*-
"""Pulls every number the site states out of the MMRF runtime's own artifacts.

    python sync_facts.py [--runtime ../mmrf-runtime]

Writes src/facts.json. The site never hardcodes a count, a hash, or a density;
content.py reads them from here, so a figure on the page cannot drift away from
the artifact it claims to describe. If an artifact is missing or fails its own
hash check this refuses to write, rather than leaving the previous values in
place looking current.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def canonical(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(value) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def read(path: Path):
    if not path.exists():
        raise SystemExit(f"missing artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runtime", default="../mmrf-runtime")
    args = ap.parse_args()
    rt = (ROOT / args.runtime).resolve()

    manifest = read(rt / "stable_data" / "stable_manifest_v1.0.json")
    core = {k: v for k, v in manifest.items() if k != "manifest_sha256"}
    if manifest["manifest_sha256"] != sha256_json(core):
        raise SystemExit("stable manifest failed its own hash check")

    baseline = read(rt / "results_v10" / "stable_baseline_output.json")
    body = {k: v for k, v in baseline.items() if k != "output_sha256"}
    if baseline["output_sha256"] != sha256_json(body):
        raise SystemExit("baseline output failed its own hash check")
    if baseline["stable_manifest_sha256"] != manifest["manifest_sha256"]:
        raise SystemExit("baseline was computed against a different manifest")

    citation = read(rt / "citations" / "dataset_citation_v09.json")
    receipt = read(rt / "results_v09" / "promotion_receipt_v09.json")
    proposal = read(rt / "results_v09" / "dataset_proposal_v09.json")
    graph = read(rt / "provenance" / "provenance_graph_v09.json")
    reviews = [
        read(rt / "results_v09" / "review_math.json"),
        read(rt / "results_v09" / "review_security.json"),
    ]
    workflow = read(rt / "workflows" / "prime-distribution-baseline.workflow.json")

    baseline_py = (rt / "workflows" / "stable_baseline.py").read_bytes()

    facts = {
        "release_id": "MMRF-1.0.0",
        "dataset": {
            "dataset_id": manifest["dataset_id"],
            "generation": manifest["generation"],
            "schema_version": manifest.get("schema_version"),
            "prime_count": manifest["prime_count"],
            "shard_count": manifest["shard_count"],
            "limit_exclusive": manifest["limit_exclusive"],
            "columns": manifest.get("columns") or manifest.get("column_order"),
            "manifest_sha256": manifest["manifest_sha256"],
        },
        "baseline": baseline,
        "workflow": {
            "shipped": workflow,
            "stable_baseline_sha256": hashlib.sha256(baseline_py).hexdigest(),
            "output_sha256": baseline["output_sha256"],
        },
        "governance": {
            "proposal": {
                "proposal_id": proposal["proposal_id"],
                "purpose": proposal["purpose"],
                "safety": proposal["safety"],
                "migration_profile": proposal["migration_profile"],
                "candidate_manifest_sha256": proposal["candidate_manifest_sha256"],
                "base_manifest_sha256": proposal["base_manifest_sha256"],
                "sha256": receipt["proposal_sha256"],
            },
            "reviews": [
                {
                    "reviewer_id": r["reviewer_id"],
                    "decision": r["decision"],
                    "findings": r["findings"],
                    "document_sha256": r["document_sha256"],
                }
                for r in reviews
            ],
            "receipt": {
                "promotion_id": receipt["promotion_id"],
                "approval_count": receipt["approval_count"],
                "approval_threshold": receipt["approval_threshold"],
                "promoted_at": receipt["promoted_at"],
                "receipt_sha256": receipt["receipt_sha256"],
            },
            "provenance_nodes": [
                {
                    "node_id": n["node_id"],
                    "node_type": n["node_type"],
                    "content_sha256": n["content_sha256"],
                }
                for n in graph["nodes"]
            ],
            "provenance_edges": graph.get("edges", []),
        },
        "citation": citation,
    }

    out = ROOT / "src" / "facts.json"
    out.write_text(
        json.dumps(facts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    b = facts["baseline"]
    print(f"wrote {out.relative_to(ROOT)}")
    print(f"  dataset      {facts['dataset']['prime_count']:,} primes "
          f"in {facts['dataset']['shard_count']} shards")
    print(f"  manifest     {facts['dataset']['manifest_sha256']}")
    print(f"  baseline     {b['output_sha256']}")
    print(f"  governance   {len(facts['governance']['provenance_nodes'])} provenance nodes, "
          f"{facts['governance']['receipt']['approval_count']}/"
          f"{facts['governance']['receipt']['approval_threshold']} approvals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
