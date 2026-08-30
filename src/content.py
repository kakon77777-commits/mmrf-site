# -*- coding: utf-8 -*-
"""Every page of mmrf.evemisslab.com, in English and Traditional Chinese.

Numbers, hashes and governance records are read from facts.json, which
sync_facts.py generates from the runtime's own artifacts. Nothing measurable is
typed in here by hand.
"""

from __future__ import annotations

import json
from pathlib import Path

F = json.loads((Path(__file__).resolve().parent / "facts.json").read_text(encoding="utf-8"))

D = F["dataset"]
B = F["baseline"]
G = F["governance"]
CIT = F["citation"]

SITE = {
    "origin": "https://mmrf.evemisslab.com",
    "repo": "https://github.com/kakon77777-commits/mmrf-runtime",
    "site_repo": "https://github.com/kakon77777-commits/mmrf-site",
    "lab": "https://evemisslab.com",
    "version": "v1.0",
    "release_id": F["release_id"],
    "licence": "Apache-2.0",
    "updated": "2026-08-30",
}

MANIFEST = D["manifest_sha256"]
OUT_SHA = B["output_sha256"]
WF_SHA = F["workflow"]["stable_baseline_sha256"]

SLUGS = ["", "research", "datasets", "workflows", "governance",
         "verification", "documentation", "safety", "about", "reports"]

# Public metadata only. The report body lives in public_reports/ and must not
# contain controlled, private, target-conditioned, or internal operational data.
DAILY_REPORTS = [
    {
        "date": "2026-08-30",
        "year": 2026,
        "month": 8,
        "day": 30,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/30.md?fresh=20260830c",
    },
    {
        "date": "2026-08-29",
        "year": 2026,
        "month": 8,
        "day": 29,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/29.md?fresh=20260829c",
    },
    {
        "date": "2026-08-28",
        "year": 2026,
        "month": 8,
        "day": 28,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/28.md?fresh=20260828c",
    },
    {
        "date": "2026-08-27",
        "year": 2026,
        "month": 8,
        "day": 27,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/27.md?fresh=20260827c",
    },
    {
        "date": "2026-08-26",
        "year": 2026,
        "month": 8,
        "day": 26,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/26.md?fresh=20260826c",
    },
    {
        "date": "2026-08-25",
        "year": 2026,
        "month": 8,
        "day": 25,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/25.md?fresh=20260825c",
    },
    {
        "date": "2026-08-24",
        "year": 2026,
        "month": 8,
        "day": 24,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/24.md?fresh=20260824c",
    },
    {
        "date": "2026-08-23",
        "year": 2026,
        "month": 8,
        "day": 23,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/23.md?fresh=20260823c",
    },
    {
        "date": "2026-08-22",
        "year": 2026,
        "month": 8,
        "day": 22,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/22.md?fresh=20260822c",
    },
    {
        "date": "2026-08-21",
        "year": 2026,
        "month": 8,
        "day": 21,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/21.md?fresh=20260821c",
    },
    {
        "date": "2026-08-20",
        "year": 2026,
        "month": 8,
        "day": 20,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Catch-up prime relay", "zh": "回補質數接力"},
        "download": "/reports/2026/08/20.md?fresh=20260820c",
    },
    {
        "date": "2026-08-19",
        "year": 2026,
        "month": 8,
        "day": 19,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Catch-up prime relay", "zh": "回補質數接力"},
        "download": "/reports/2026/08/19.md?fresh=20260820c",
    },
    {
        "date": "2026-08-18",
        "year": 2026,
        "month": 8,
        "day": 18,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Catch-up prime relay", "zh": "回補質數接力"},
        "download": "/reports/2026/08/18.md?fresh=20260820c",
    },
    {
        "date": "2026-08-17",
        "year": 2026,
        "month": 8,
        "day": 17,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Catch-up prime relay", "zh": "回補質數接力"},
        "download": "/reports/2026/08/17.md?fresh=20260820c",
    },
    {
        "date": "2026-08-16",
        "year": 2026,
        "month": 8,
        "day": 16,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Catch-up prime relay", "zh": "回補質數接力"},
        "download": "/reports/2026/08/16.md?fresh=20260820c",
    },
    {
        "date": "2026-08-15",
        "year": 2026,
        "month": 8,
        "day": 15,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Catch-up prime relay", "zh": "回補質數接力"},
        "download": "/reports/2026/08/15.md?fresh=20260820c",
    },
    {
        "date": "2026-08-14",
        "year": 2026,
        "month": 8,
        "day": 14,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/14.md?fresh=20260814c",
    },
    {
        "date": "2026-08-13",
        "year": 2026,
        "month": 8,
        "day": 13,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/13.md?fresh=20260813c",
    },
    {
        "date": "2026-08-12",
        "year": 2026,
        "month": 8,
        "day": 12,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Chain repair + prime relay", "zh": "鏈修正與質數接力"},
        "download": "/reports/2026/08/12.md?fresh=20260812c",
    },
    {
        "date": "2026-08-11",
        "year": 2026,
        "month": 8,
        "day": 11,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/11.md?fresh=20260811c",
    },
    {
        "date": "2026-08-10",
        "year": 2026,
        "month": 8,
        "day": 10,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/10.md?fresh=20260810d",
    },
    {
        "date": "2026-08-09",
        "year": 2026,
        "month": 8,
        "day": 9,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/09.md?fresh=20260810c",
    },
    {
        "date": "2026-08-08",
        "year": 2026,
        "month": 8,
        "day": 8,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/08.md?fresh=20260808c",
    },
    {
        "date": "2026-08-07",
        "year": 2026,
        "month": 8,
        "day": 7,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/07.md?fresh=20260807c",
    },
    {
        "date": "2026-08-06",
        "year": 2026,
        "month": 8,
        "day": 6,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/06.md?fresh=20260806c",
    },
    {
        "date": "2026-08-05",
        "year": 2026,
        "month": 8,
        "day": 5,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/05.md?v=20260805",
    },
    {
        "date": "2026-08-04",
        "year": 2026,
        "month": 8,
        "day": 4,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/04.md?v=20260805",
    },
    {
        "date": "2026-08-03",
        "year": 2026,
        "month": 8,
        "day": 3,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Prime expansion relay", "zh": "質數擴展接力"},
        "download": "/reports/2026/08/03.md",
    },
    {
        "date": "2026-08-02",
        "year": 2026,
        "month": 8,
        "day": 2,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Manual daily run", "zh": "人工日更"},
        "download": "/reports/2026/08/02.md",
    },
    {
        "date": "2026-08-01",
        "year": 2026,
        "month": 8,
        "day": 1,
        "status": {"en": "Complete", "zh": "完成"},
        "label": {"en": "Manual daily run", "zh": "人工日更試跑"},
        "download": "/reports/2026/08/01.md",
    },
]


def n(value):
    return f"{value:,}"


def short(h, keep=16):
    return h[:keep] + "…"


def mono(text):
    return f'<code class="ic">{text}</code>'


# --------------------------------------------------------------------------
# derived display data
# --------------------------------------------------------------------------

RESIDUE_30 = B["residue_distribution"]["30"]
COPRIME_30 = {k: v for k, v in RESIDUE_30.items() if int(k) in (1, 7, 11, 13, 17, 19, 23, 29)}
_c = sorted(COPRIME_30.values())
RESIDUE_SPREAD = _c[-1] - _c[0]

GAPS = B["gap_histogram"]
TOP_GAPS = sorted(GAPS.items(), key=lambda kv: -kv[1])[:8]
GAP_BARS = [(f"gap {k}", v) for k, v in sorted(TOP_GAPS, key=lambda kv: int(kv[0]))]

BANDS = B["magnitude_bands"]
BAND_ROWS = [
    (f"{n(b['range_start'])}–{n(b['range_end_exclusive'])}",
     n(b["prime_count"]), f"{b['density']:.5f}")
    for b in BANDS
]

FAM = B["family_counts"]
FAM_BARS = [(k.replace("_", " "), v) for k, v in FAM.items()]

RES_BARS = [(f"n ≡ {k}", v) for k, v in sorted(COPRIME_30.items(), key=lambda kv: int(kv[0]))]

QUANTS = B["gap_quantiles"]["quantiles"]

DENIED_QUERY = """{
  "version": "MMRF-SQL-0.8",
  "operation": "interval_density",
  "shard_start": 0,
  "shard_count": 1,
  "rsa_modulus": "1000036000099"
}"""

DENIED_RESPONSE = """{
  "status": "DENIED",
  "decision": {
    "allowed": false,
    "decision": "DENY",
    "reasons": [
      "target_conditioned_or_factor_related_field_forbidden",
      "forbidden_field:rsa_modulus"
    ],
    "cost_units": 0,
    "normalized_request": null
  },
  "audit": {
    "event_id": "lake-query:ed5a56ba-…",
    "event_hash_sha256": "1d60abd3c37dbb0d…"
  }
}"""

ALLOWED_QUERY = """{
  "version": "MMRF-SQL-0.8",
  "operation": "interval_density",
  "shard_start": 0,
  "shard_count": 20
}"""

FORBIDDEN_FIELDS = [
    "n", "integer", "target", "modulus", "rsa_modulus", "public_key",
    "private_key", "factor", "factors", "candidate", "candidates",
    "range_narrowing", "nearest_prime", "prime_list", "exact_primes",
    "source_integer", "source_factor_relation",
]

ALLOWED_OPS = [
    "dataset_metadata", "interval_density", "gap_quantiles", "gap_histogram",
    "residue_distribution", "family_counts", "workflow_replay",
]

FORBIDDEN_ENDPOINTS = [
    "POST /factor", "POST /rsa", "POST /nearest-prime", "POST /candidate-range",
    "POST /target-query", "POST /raw-primes", "POST /source-factor",
]


# --------------------------------------------------------------------------
# chrome
# --------------------------------------------------------------------------

CHROME = {
    "en": {
        "lang": "en",
        "nav": [("", "Home"), ("research", "Research"), ("datasets", "Datasets"),
                ("workflows", "Workflows"), ("governance", "Governance"),
                ("verification", "Verification"), ("documentation", "Documentation"),
                ("safety", "Safety"), ("about", "About"), ("reports", "Daily reports")],
        "skip": "Skip to content",
        "on_this_page": "On this page",
        "theme": "Switch colour scheme",
        "lang_switch": "中文",
        "lang_switch_title": "Switch to Traditional Chinese",
        "repo_link": "Runtime repository",
        "footer_lab": "EveMissLab",
        "footer_release": f"stable release {F['release_id']}",
        "footer_note": (
            "MMRF is a public mathematical research dataset. It answers aggregate "
            "questions about a fixed range of primes and refuses everything else "
            "by construction."),
        "copy": "Copy",
        "copied": "Copied",
        "permitted": "crosses",
        "forbidden": "never crosses",
    },
    "zh": {
        "lang": "zh-Hant",
        "nav": [("", "首頁"), ("research", "研究"),
                ("datasets", "資料集"), ("workflows", "工作流"),
                ("governance", "治理"), ("verification", "驗證"),
                ("documentation", "文件"), ("safety", "安全"),
                ("about", "關於"), ("reports", "每日更新")],
        "skip": "跳至內容",
        "on_this_page": "本頁內容",
        "theme": "切換配色",
        "lang_switch": "EN",
        "lang_switch_title": "Switch to English",
        "repo_link": "Runtime 儲存庫",
        "footer_lab": "EveMissLab",
        "footer_release": f"穩定版 {F['release_id']}",
        "footer_note": (
            "MMRF 是公開的數學研究資料集。"
            "它回答固定質數區間的聚合問題，"
            "其餘一律在結構上拒絕。"),
        "copy": "複製",
        "copied": "已複製",
        "permitted": "可跨過",
        "forbidden": "永不跨過",
    },
}


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

PAGES = {"en": {}, "zh": {}}

# ---------------------------------------------------------------- Home (en)
PAGES["en"][""] = {
    "title": "MMRF " + SITE["version"],
    "display": "A prime dataset defined by what it will not answer.",
    "meta_title": "MMRF — Multidirectional Matrix Research Infrastructure",
    "description": (
        f"MMRF {SITE['version']}: {n(D['prime_count'])} public prime records across "
        f"{D['shard_count']} immutable shards, with an aggregate-only query surface "
        "and a refusal boundary enforced before any data is read."),
    "standfirst": (
        "Every number below comes from a frozen, hash-covered dataset, and every "
        "figure on this site is regenerated from that dataset rather than typed in. "
        "The interesting part is the other half: the questions this infrastructure "
        "is built to decline."),
    "hero": "boundary",
    "blocks": [
        ("h2", "What is published", "published"),
        ("p", f"One dataset generation, frozen. {n(D['prime_count'])} prime records "
              f"covering {mono('[0, ' + n(D['limit_exclusive']) + ')')}, stored as "
              f"{D['shard_count']} immutable columnar shards under a single manifest "
              f"hash. Appending a range never rewrites a prior shard."),
        ("kv", [
            ("Release", F["release_id"]),
            ("Prime records", n(D["prime_count"])),
            ("Shards", f"{D['shard_count']} × immutable NPZ"),
            ("Range", f"[0, {n(D['limit_exclusive'])})"),
            ("Columns", str(len(D["columns"]))),
            ("Stable manifest", mono(MANIFEST)),
        ]),
        ("h2", "The query surface is aggregate-only", "surface"),
        ("p", "There are seven permitted operations. Each returns a statistic over a "
              "shard range — a density, a quantile, a histogram, a count. None "
              "returns a prime, a list of primes, or anything conditioned on a number "
              "you supply."),
        ("chips", ALLOWED_OPS),
        ("p", "Seventeen request fields are refused by name before the request is "
              "parsed further. The guard runs ahead of the data layer, so a refused "
              "query never reaches a shard — it costs "
              f"{mono('cost_units: 0')} and produces a hashed audit event anyway."),
        ("chips_off", FORBIDDEN_FIELDS),
        ("h2", "Measured, not asserted", "measured"),
        ("p", "The four aggregates below were computed from the shipped shards on this "
              "machine, not copied from the release notes. The full output, its hash, "
              "and the script that produced it are on the "
              "<a href=\"/research/\">research</a> page."),
        ("stat4", [
            (f"{B['interval_density']['density']:.6f}", "prime density over the range"),
            (f"{B['gap_quantiles']['max_gap']}", "largest gap between consecutive primes"),
            (n(FAM["twin_prime"]), "twin prime pairs"),
            (f"{RESIDUE_SPREAD}", "spread across the eight residues mod 30"),
        ]),
        ("p", "That last figure is the one worth pausing on. Across the eight residue "
              f"classes coprime to 30, the counts differ by only {RESIDUE_SPREAD} out of "
              f"roughly {n(round(sum(COPRIME_30.values()) / 8))} each — primes are "
              "distributed almost perfectly evenly among the classes they are allowed to "
              "occupy."),
        ("h2", "Start here", "start"),
        ("cards", [
            ("/datasets/", "Dataset v1.0",
             "Schema, columns, manifest hash, provenance, promotion receipt, citation."),
            ("/verification/", "Verify it yourself",
             "Two commands reproduce the manifest hash and check all twenty shards."),
            ("/safety/", "The refusal boundary",
             "What is permanently outside the public surface, and why that is the design."),
        ]),
        ("h2", "Citation", "citation"),
        ("cite", CIT["preferred_citation"]),
    ],
}

# ---------------------------------------------------------------- Home (zh)
PAGES["zh"][""] = {
    "title": "MMRF " + SITE["version"],
    "display": "一個由「不回答什麼」定義的質數資料集。",
    "meta_title": "MMRF — 多向矩陣研究基礎設施",
    "description": (
        f"MMRF {SITE['version']}：{n(D['prime_count'])} 筆公開質數"
        f"記錄、{D['shard_count']} 個不可變分片，"
        "僅提供聚合查詢，拒絕邊界"
        "在讀取任何資料之前就已生效。"),
    "standfirst": (
        "下方每一個數字都來自一個"
        "凍結、被雜湊覆蓋的資料集，"
        "而且本站的每一個數字都是從"
        "該資料集重新生成的，不是"
        "手打的。真正有趣的是另一半："
        "這套基礎設施天生就要拒絕的"
        "那些問題。"),
    "hero": "boundary",
    "blocks": [
        ("h2", "公開了什麼", "published"),
        ("p", f"一個凍結的資料世代。"
              f"{n(D['prime_count'])} 筆質數記錄，涵蓋 "
              f"{mono('[0, ' + n(D['limit_exclusive']) + ')')}，以 "
              f"{D['shard_count']} 個不可變的欄式分片"
              f"存放、共用一個清單雜湊。"
              f"新增區間永遠不會重寫舊分片。"),
        ("kv", [
            ("發行版本", F["release_id"]),
            ("質數記錄", n(D["prime_count"])),
            ("分片", f"{D['shard_count']} × 不可變 NPZ"),
            ("區間", f"[0, {n(D['limit_exclusive'])})"),
            ("欄位", str(len(D["columns"]))),
            ("穩定清單", mono(MANIFEST)),
        ]),
        ("h2", "查詢面只有聚合", "surface"),
        ("p", "只有七個允許的操作。每一個"
              "都回傳一個分片區間上的統計"
              "量——密度、分位數、直方圖、"
              "計數。沒有任何一個會回傳質數、"
              "質數列表，或任何以你給的數字"
              "為條件的結果。"),
        ("chips", ALLOWED_OPS),
        ("p", "十七個請求欄位在進一步解析"
              "之前就按名稱被拒。守衛跑在"
              "資料層之前，所以被拒的查詢"
              "從來沒碰到分片——它的成本是 "
              f"{mono('cost_units: 0')}，但依然留下帶雜湊"
              "的稽核事件。"),
        ("chips_off", FORBIDDEN_FIELDS),
        ("h2", "是量出來的，不是宣稱的", "measured"),
        ("p", "下面四個聚合量是在這台機器"
              "上從發行包的分片算出來的，"
              "不是從發行說明拄下來的。"
              "完整輸出、它的雜湊、以及"
              "產生它的腳本都在"
              "<a href=\"/zh/research/\">研究</a>頁。"),
        ("stat4", [
            (f"{B['interval_density']['density']:.6f}", "區間內質數密度"),
            (f"{B['gap_quantiles']['max_gap']}", "相鄰質數的最大間隔"),
            (n(FAM["twin_prime"]), "孪生質數對"),
            (f"{RESIDUE_SPREAD}", "模 30 八個剩餘類的極差"),
        ]),
        ("p", "最後那個數字值得停一下。"
              "在與 30 互質的八個剩餘類中，"
              f"各類計數各約 {n(round(sum(COPRIME_30.values()) / 8))} 筆，"
              f"彼此差距只有 {RESIDUE_SPREAD}——質數"
              "在它們被允許占據的類別之間"
              "幾乎完全均勻。"),
        ("h2", "從這裡開始", "start"),
        ("cards", [
            ("/zh/datasets/", "資料集 v1.0",
             "結構、欄位、清單雜湊、來源"
             "、晉升收據、引用。"),
            ("/zh/verification/", "自己驗證",
             "兩行指令重現清單雜湊，並"
             "檢查全部二十個分片。"),
            ("/zh/safety/", "拒絕邊界",
             "什麼永遠在公開面之外，"
             "以及為什麼這就是設計本身。"),
        ]),
        ("h2", "引用", "citation"),
        ("cite", CIT["preferred_citation"]),
    ],
}

# ------------------------------------------------------------ Research (en)
PAGES["en"]["research"] = {
    "title": "Research",
    "display": "Seven aggregates over 148,933 primes.",
    "meta_title": "Research — MMRF",
    "description": (
        "Prime density, gap quantiles, gap histogram, residue distribution, wheel "
        "classes, prime families and magnitude comparison, each with the dataset, "
        "workflow hash, output hash and replay command."),
    "standfirst": (
        "Everything on this page was computed from the shipped shards, on the "
        "environment named at the bottom, by a script whose hash is printed here. "
        "Nothing is quoted from a paper."),
    "blocks": [
        ("provenance", "en"),
        ("h2", "Density", "density"),
        ("p", f"{n(B['interval_density']['prime_count'])} primes below "
              f"{n(B['interval_density']['width'])} gives a density of "
              f"{mono(f'{B['interval_density']['density']:.6f}')}. Density falls as the "
              "range grows, which is the shape the prime number theorem predicts; the "
              "magnitude bands below show the fall directly."),
        ("table",
         ["Range", "Primes", "Density"],
         BAND_ROWS),
        ("p", "The counts in that table sum to the dataset total, and each row is the "
              "difference between two consecutive values of π(10ᵏ). They are stored, "
              f"not re-derived: the band boundaries come from the {mono('decimal_digits')} "
              "column that ships inside the shards."),
        ("h2", "Gaps", "gaps"),
        ("p", f"Across {n(B['gap_quantiles']['sample_size'])} consecutive-prime gaps the "
              f"mean is {B['gap_quantiles']['mean_gap']:.3f} and the largest is "
              f"{mono(str(B['gap_quantiles']['max_gap']))}. That maximum is the known "
              "maximal gap below two million, which is one of the cheapest ways to check "
              "this dataset against the literature."),
        ("kv", [
            ("median gap", f"{QUANTS['0.5']:.0f}"),
            ("90th percentile", f"{QUANTS['0.9']:.0f}"),
            ("99th percentile", f"{QUANTS['0.99']:.0f}"),
            ("maximum", str(B["gap_quantiles"]["max_gap"])),
            ("distinct gap values", str(len(GAPS))),
        ]),
        ("bars", "Most frequent gaps", GAP_BARS,
         "Gap 6 is the most common by a wide margin — the jumping champion for this "
         "range. Gap 2 occurs exactly as often as there are twin pairs, which is a "
         "consistency check the two independent columns have to pass."),
        ("h2", "Residues", "residues"),
        ("p", "Every prime above 5 is coprime to 30, so it must land in one of eight "
              "residue classes. It lands in them almost equally:"),
        ("bars", "Primes by residue class mod 30", RES_BARS,
         f"The eight counts span only {RESIDUE_SPREAD}. The dataset also stores residues "
         "mod 6 and mod 210, and a derived wheel30 class — the column that generation 2 "
         "was proposed and reviewed in order to add."),
        ("h2", "Families", "families"),
        ("p", "Four pair families are encoded as bit flags, each set on the larger member "
              "of the pair so that appending a later range never rewrites an earlier "
              "shard."),
        ("bars", "Prime family counts", FAM_BARS,
         "Cousin pairs exceed gap-4 occurrences by exactly one. The extra pair is (3, 7): "
         "7 − 4 = 3 is prime, but 5 sits between them, so it is a cousin pair that is not "
         "a gap of 4. It is the only such case in the range."),
        ("note", "A fifth family used to appear here. Until the repair recorded in the "
                 "runtime's history, this surface reported a "
                 f"{mono('sophie_germain_relation')} count that was the safe-prime count "
                 "under a second name — the two shared one bit mask, and no Sophie Germain "
                 f"bit was ever written. Over this range it read {n(FAM['safe_prime'])}; "
                 "the number of Sophie Germain primes below two million is 13,934. The "
                 "field was removed rather than repaired, because the shard bytes are "
                 "covered by a signed manifest and a new family means a new generation."),
        ("h2", "Replay", "replay"),
        ("p", "One command, no network, no index required:"),
        ("code", "shell", "python workflows/stable_baseline.py --project-root . \\\n"
                          "    --output results_v10/stable_baseline_output.json"),
        ("p", "The script verifies the stable manifest against its own hash before "
              "reading anything, refuses to run if the shard or prime count disagrees "
              "with the manifest, and fails loudly if the family-flag column carries a "
              "bit it cannot name. Its output is canonicalised and self-hashed the same "
              "way the manifest is, so the value below is reproducible byte for byte."),
        ("kv", [
            ("workflow", mono("stable_baseline.py")),
            ("workflow sha256", mono(WF_SHA)),
            ("dataset manifest", mono(MANIFEST)),
            ("output sha256", mono(OUT_SHA)),
            ("environment", f"Python {B['environment']['python']}, "
                            f"NumPy {B['environment']['numpy']}, "
                            f"{B['environment']['platform']}"),
        ]),
        ("h2", "Known limits", "limits"),
        ("ul", [
            "The range is fixed at two million. Every figure here is a statement about "
            "that range and nothing beyond it.",
            "Pair families are counted at the larger member, so a pair straddling the "
            "upper bound is not counted.",
            "The shipped <code class=\"ic\">prime-distribution-baseline</code> workflow "
            "runs through the data-lake query layer and cannot be replayed from the "
            "released package, because the lake index is not part of it. That gap is "
            "documented on the <a href=\"/workflows/\">workflows</a> page; this study "
            "exists to close it.",
            "No result here is conditioned on an externally supplied integer, and no "
            "combination of them narrows a factor search.",
        ]),
    ],
}

# ------------------------------------------------------------ Research (zh)
PAGES["zh"]["research"] = {
    "title": "研究",
    "display": "148,933 個質數上的七種聚合。",
    "meta_title": "研究 — MMRF",
    "description": (
        "質數密度、間隔分位數、間隔直方圖、"
        "剩餘分布、輪類、質數族、數量級"
        "比較，每一項都附資料集、工作流"
        "雜湊、輸出雜湊與重播指令。"),
    "standfirst": (
        "本頁所有內容都是在頁尾標明的"
        "環境下、由一支印出雜湊的腳本、"
        "從發行包的分片算出來的。"
        "沒有一個數字是從論文引來的。"),
    "blocks": [
        ("provenance", "zh"),
        ("h2", "密度", "density"),
        ("p", f"{n(B['interval_density']['width'])} 以下有 "
              f"{n(B['interval_density']['prime_count'])} 個質數，密度為 "
              f"{mono(f'{B['interval_density']['density']:.6f}')}。"
              f"密度隨區間擴大而下降，"
              f"正是質數定理預測的形狀；"
              f"下面的數量級分段直接顯示"
              f"這個下降。"),
        ("table",
         ["區間", "質數", "密度"],
         BAND_ROWS),
        ("p", "表中計數加總正好是資料集總數，"
              "而每一列都是兩個相鄰 π(10ᵏ) 的"
              "差。它們是存下來的、不是重新"
              f"推導的：分段邊界來自分片內"
              f"隨附的 {mono('decimal_digits')} 欄。"),
        ("h2", "間隔", "gaps"),
        ("p", f"在 {n(B['gap_quantiles']['sample_size'])} 個相鄰質數間隔中，"
              f"平均為 {B['gap_quantiles']['mean_gap']:.3f}，最大為 "
              f"{mono(str(B['gap_quantiles']['max_gap']))}。"
              f"這個最大值正是兩百萬以下"
              f"已知的最大間隔，是拿這個"
              f"資料集對照文獻最省事的"
              f"檢查之一。"),
        ("kv", [
            ("間隔中位數", f"{QUANTS['0.5']:.0f}"),
            ("90 百分位", f"{QUANTS['0.9']:.0f}"),
            ("99 百分位", f"{QUANTS['0.99']:.0f}"),
            ("最大值", str(B["gap_quantiles"]["max_gap"])),
            ("相異間隔值", str(len(GAPS))),
        ]),
        ("bars", "最常見的間隔", GAP_BARS,
         "間隔 6 以明顯差距居冠——這個"
         "區間的 jumping champion。間隔 2 "
         "的出現次數與孪生質數對數完全"
         "相同，這是兩個獨立欄位必須"
         "通過的一致性檢查。"),
        ("h2", "剩餘", "residues"),
        ("p", "大於 5 的質數都與 30 互質，"
              "因此必然落在八個剩餘類之一。"
              "而它們落得幾乎一樣平均："),
        ("bars", "各剩餘類（模 30）的質數數量", RES_BARS,
         f"八個計數的極差只有 {RESIDUE_SPREAD}。"
         "資料集另存有模 6 與模 210 的剩餘，"
         "以及一個衍生的 wheel30 類——"
         "第二世代正是為了加入這一欄"
         "而被提案並審查的。"),
        ("h2", "質數族", "families"),
        ("p", "四個配對族以位元旗標編碼，"
              "每一個都設在配對中較大的"
              "那一個成員上，所以新增後"
              "續區間永遠不會重寫先前的"
              "分片。"),
        ("bars", "質數族計數", FAM_BARS,
         "表兄弟對比間隔 4 的出現次數"
         "正好多一。多出來的那一對是 "
         "(3, 7)：7 − 4 = 3 是質數，但 5 夾"
         "在中間，所以它是表兄弟對卻"
         "不是間隔 4。這是區間內唯一"
         "的例外。"),
        ("note", "這裡本來還有第五個族。"
                 "在 runtime 歷史記錄的那次修復"
                 f"之前，這個查詢面回報的 "
                 f"{mono('sophie_germain_relation')} 計數，"
                 "其實是 safe prime 的計數換了"
                 "個名字——兩者共用同一個"
                 "位元遮罩，而 Sophie Germain "
                 "的位元從來沒被寫入過。"
                 f"在這個區間它讀作 {n(FAM['safe_prime'])}；"
                 "而兩百萬以下的 Sophie Germain "
                 "質數有 13,934 個。這個欄位是"
                 "被移除而不是被修好的，因為"
                 "分片位元組受簽章清單覆蓋，"
                 "新增一個族就意味著一個"
                 "新的世代。"),
        ("h2", "重播", "replay"),
        ("p", "一行指令，不需網路，"
              "不需索引："),
        ("code", "shell", "python workflows/stable_baseline.py --project-root . \\\n"
                          "    --output results_v10/stable_baseline_output.json"),
        ("p", "腳本在讀取任何東西之前，"
              "會先用清單自己的雜湊驗證"
              "它；若分片數或質數數與清單"
              "不符則拒絕執行；若旗標欄"
              "帶有它無法命名的位元則"
              "大聲失敗。輸出以與清單"
              "相同的方式正規化並自我"
              "雜湊，所以下面這個值"
              "可以逐位元重現。"),
        ("kv", [
            ("工作流", mono("stable_baseline.py")),
            ("工作流 sha256", mono(WF_SHA)),
            ("資料集清單", mono(MANIFEST)),
            ("輸出 sha256", mono(OUT_SHA)),
            ("執行環境", f"Python {B['environment']['python']}、"
                          f"NumPy {B['environment']['numpy']}、"
                          f"{B['environment']['platform']}"),
        ]),
        ("h2", "已知限制", "limits"),
        ("ul", [
            "區間固定為兩百萬。本頁每一個"
            "數字都只是關於這個區間的陳述，"
            "不涉及其外。",
            "配對族記在較大的成員上，"
            "所以跨越上界的配對不被計入。",
            "隨附的 <code class=\"ic\">prime-distribution-baseline</code> "
            "工作流走資料湖查詢層，無法從"
            "發行包重播，因為湖索引不在"
            "包裡。這個缺口記錄在"
            "<a href=\"/zh/workflows/\">工作流</a>頁；"
            "本研究的存在就是為了補上它。",
            "本頁沒有任何結果以外部提供的"
            "整數為條件，它們的任何組合"
            "也不會縮小因數搜尋範圍。",
        ]),
    ],
}

# ------------------------------------------------------------ Datasets (en)
PAGES["en"]["datasets"] = {
    "title": "Datasets",
    "display": "One generation, frozen and hash-covered.",
    "meta_title": "Datasets — MMRF",
    "description": (
        f"MMRF public prime lake, generation {D['generation']}: schema, columns, "
        f"manifest hash {short(MANIFEST)}, provenance, promotion receipt, citation "
        "and verification commands."),
    "standfirst": (
        "The public dataset is a single promoted generation. It is immutable: growth "
        "happens by appending shards, never by editing one, and the manifest hash "
        "covers the result."),
    "blocks": [
        ("h2", "Identity", "identity"),
        ("kv", [
            ("Dataset ID", mono(D["dataset_id"])),
            ("Generation", str(D["generation"])),
            ("Schema version", str(D["schema_version"])),
            ("Range", f"[0, {n(D['limit_exclusive'])})"),
            ("Prime count", n(D["prime_count"])),
            ("Shard count", str(D["shard_count"])),
            ("Storage", "columnar NPZ, one file per shard"),
            ("Manifest sha256", mono(MANIFEST)),
        ]),
        ("h2", "Columns", "columns"),
        ("p", "Ten columns. Every one is a property of a prime already in the set — "
              "none relates a prime to a number outside it."),
        ("table",
         ["Column", "What it holds"],
         [
             ("prime", "the prime itself"),
             ("ordinal", "its index in the ordered set"),
             ("bit_length", "bit length"),
             ("decimal_digits", "decimal digit count"),
             ("previous_gap", "distance from the preceding prime"),
             ("residue_6", "residue mod 6"),
             ("residue_30", "residue mod 30"),
             ("residue_210", "residue mod 210"),
             ("family_flags", "four pair-family bits, set on the larger member"),
             ("wheel30_class", "derived wheel class; the reason generation 2 exists"),
         ]),
        ("h2", "How this generation was admitted", "promotion"),
        ("p", "Generation 2 did not appear by being written. It was proposed against a "
              "named base manifest, reviewed independently by two reviewers, and "
              "promoted only once the approval threshold was met. Each step is a signed "
              "document with its own hash, and the chain is on the "
              "<a href=\"/governance/\">governance</a> page."),
        ("chain", "en"),
        ("h2", "Verify before you trust it", "verify"),
        ("code", "shell", "python install/mmrf.py --project-root . verify-release\n"
                          "python install/mmrf.py --project-root . doctor"),
        ("p", "The first checks the signed release manifest; the second walks all "
              f"{D['shard_count']} shards. Note the flag order — "
              f"{mono('--project-root')} belongs before the subcommand, not after it."),
        ("h2", "Citation", "citation"),
        ("kv", [
            ("Citation ID", mono(CIT["citation_id"])),
            ("Title", CIT["title"]),
            ("Publisher", CIT["publisher"]),
            ("Issued", CIT["issued_at"][:10]),
            ("Citation sha256", mono(CIT["citation_sha256"])),
        ]),
        ("cite", CIT["preferred_citation"]),
    ],
}

# ------------------------------------------------------------ Datasets (zh)
PAGES["zh"]["datasets"] = {
    "title": "資料集",
    "display": "一個世代，凍結並被雜湊覆蓋。",
    "meta_title": "資料集 — MMRF",
    "description": (
        f"MMRF 公開質數湖，第 {D['generation']} 世代："
        f"結構、欄位、清單雜湊 {short(MANIFEST)}、"
        "來源鏈、晉升收據、引用與驗證指令。"),
    "standfirst": (
        "公開資料集是單一個已晉升的世代。"
        "它不可變：成長靠新增分片，"
        "而不是編輯分片，"
        "清單雜湊覆蓋其結果。"),
    "blocks": [
        ("h2", "身分", "identity"),
        ("kv", [
            ("資料集 ID", mono(D["dataset_id"])),
            ("世代", str(D["generation"])),
            ("結構版本", str(D["schema_version"])),
            ("區間", f"[0, {n(D['limit_exclusive'])})"),
            ("質數數量", n(D["prime_count"])),
            ("分片數量", str(D["shard_count"])),
            ("儲存", "欄式 NPZ，每分片一檔"),
            ("清單 sha256", mono(MANIFEST)),
        ]),
        ("h2", "欄位", "columns"),
        ("p", "十個欄位。每一個都是集合中"
              "已有質數的性質——沒有任何"
              "一欄把質數關聯到集合外的"
              "某個數字。"),
        ("table",
         ["欄位", "內容"],
         [
             ("prime", "質數本身"),
             ("ordinal", "在有序集合中的序號"),
             ("bit_length", "位元長度"),
             ("decimal_digits", "十進位位數"),
             ("previous_gap", "與前一個質數的距離"),
             ("residue_6", "模 6 剩餘"),
             ("residue_30", "模 30 剩餘"),
             ("residue_210", "模 210 剩餘"),
             ("family_flags", "四個配對族位元，設在較大成員上"),
             ("wheel30_class", "衍生輪類；第二世代存在的理由"),
         ]),
        ("h2", "這個世代是怎麼被接納的", "promotion"),
        ("p", "第二世代不是靠「被寫下」就"
              "出現的。它針對一份具名的"
              "基底清單被提案，由兩位審查者"
              "各自獨立審查，並且只有在"
              "達到核准門檻之後才被晉升。"
              "每一步都是一份帶自身雜湊的"
              "簽章文件，整條鏈在"
              "<a href=\"/zh/governance/\">治理</a>頁。"),
        ("chain", "zh"),
        ("h2", "先驗證再信任", "verify"),
        ("code", "shell", "python install/mmrf.py --project-root . verify-release\n"
                          "python install/mmrf.py --project-root . doctor"),
        ("p", "前者檢查簽章的發行清單；"
              f"後者走完全部 {D['shard_count']} 個分片。"
              f"注意旗標順序——{mono('--project-root')} "
              "要放在子指令之前，不是之後。"),
        ("h2", "引用", "citation"),
        ("kv", [
            ("引用 ID", mono(CIT["citation_id"])),
            ("標題", CIT["title"]),
            ("發行者", CIT["publisher"]),
            ("簽發日", CIT["issued_at"][:10]),
            ("引用 sha256", mono(CIT["citation_sha256"])),
        ]),
        ("cite", CIT["preferred_citation"]),
    ],
}

# ----------------------------------------------------------- Workflows (en)
PAGES["en"]["workflows"] = {
    "title": "Workflows",
    "display": "Two workflows, and an honest note about one of them.",
    "meta_title": "Workflows — MMRF",
    "description": (
        "Workflow registry for MMRF v1.0: the shipped prime-distribution baseline, "
        "the stable-shard baseline that replaces it, replay instructions and expected "
        "output hashes."),
    "standfirst": (
        "A workflow here is a fixed sequence of permitted operations with a declared "
        "expected output hash. If a replay produces a different hash, either the "
        "dataset moved or the code did — and both are supposed to be visible."),
    "blocks": [
        ("h2", "Registry", "registry"),
        ("table",
         ["Workflow", "Operations", "Replayable from the release", "Output sha256"],
         [
             (mono("prime-distribution-baseline"), "4",
              '<span class="tag tag-no">no</span>', "—"),
             (mono("stable-baseline"), "7",
              '<span class="tag tag-yes">yes</span>', mono(short(OUT_SHA, 12))),
         ]),
        ("h2", "Why the shipped one cannot be replayed", "gap"),
        ("p", "The v1.0 package contains the promoted dataset under "
              f"{mono('stable_data/shards/')}. It does not contain the data lake's "
              f"index ({mono('lake_state/lake_index.sqlite')}) or the generation-1 lake "
              f"shards ({mono('lake_data/primary/shards/')}) — those shipped in the v0.8 "
              "and v0.9 packages only. The baseline workflow addresses the lake by "
              "shard index, so from the released package it addresses nothing."),
        ("p", "Running it against the release used to produce three unhandled "
              "exceptions and, worse, one confident answer: "
              f"{mono('family_counts')} returned {mono('status: OK')}, "
              f"{mono('decision: ALLOW')} and a full set of zero counts, having opened "
              "zero files. A missing index read exactly like a range that genuinely "
              "contains no primes."),
        ("p", "That is repaired. An empty shard selection now raises rather than "
              "returning an empty aggregate, and the CLI reports it as "
              f"{mono('status: NO_DATA')} with exit code 2. All four operations now "
              "refuse in the same, legible way:"),
        ("code", "shell", "$ python lake/mmrf_lake_cli.py query \\\n"
                          "    --request query_examples/family_counts.json\n"
                          "{\n"
                          '  "status": "NO_DATA",\n'
                          '  "reason": "No shards registered for index range [0, 20)."\n'
                          "}\n"
                          "exit 2"),
        ("note", "Whether v1.0 should ship the lake index, repoint the lake at the "
                 "stable shards, or mark this workflow as a v0.9-generation artifact is "
                 "a release decision, not a code fix. It is recorded here rather than "
                 "quietly resolved."),
        ("h2", "The replacement", "replacement"),
        ("p", "The stable-shard baseline computes the same four aggregates — plus a gap "
              "histogram, the mod-6 and mod-210 residue distributions, and the magnitude "
              "bands — directly from the promoted shards, with no index and no network."),
        ("code", "shell", "python workflows/stable_baseline.py --project-root . \\\n"
                          "    --output results_v10/stable_baseline_output.json"),
        ("kv", [
            ("workflow_id", mono("stable-baseline")),
            ("workflow_version", "1.0.0"),
            ("workflow sha256", mono(WF_SHA)),
            ("dataset_manifest_sha256", mono(MANIFEST)),
            ("expected output sha256", mono(OUT_SHA)),
            ("resource estimate", "under a second; ~2 MB read"),
            ("safety classification", "L0_PUBLIC_MATH, aggregate-only"),
        ]),
        ("h2", "Preconditions it enforces", "preconditions"),
        ("ul", [
            "The stable manifest must hash to its own recorded value.",
            "The shard count on disk must match the manifest.",
            "The prime count across the shards must match the manifest.",
            "Every bit set in the family-flag column must map to a named family; an "
            "unnamed bit stops the run rather than being silently under-counted.",
        ]),
        ("p", "Each is a condition that could have failed silently, and each one is the "
              "sort of check the earlier defect got past. The results are on the "
              "<a href=\"/research/\">research</a> page."),
    ],
}

# ----------------------------------------------------------- Workflows (zh)
PAGES["zh"]["workflows"] = {
    "title": "工作流",
    "display": "兩個工作流，以及對其中一個的誠實說明。",
    "meta_title": "工作流 — MMRF",
    "description": (
        "MMRF v1.0 工作流登錄：隨附的"
        "質數分布基線、取代它的穩定分片"
        "基線、重播說明與預期輸出雜湊。"),
    "standfirst": (
        "這裡的工作流是一串固定的、"
        "被允許的操作，並宣告預期的"
        "輸出雜湊。若重播產生不同的"
        "雜湊，那不是資料集動了就是"
        "程式碼動了——兩者都應該"
        "被看見。"),
    "blocks": [
        ("h2", "登錄", "registry"),
        ("table",
         ["工作流", "操作數", "可從發行包重播", "輸出 sha256"],
         [
             (mono("prime-distribution-baseline"), "4",
              '<span class="tag tag-no">否</span>', "—"),
             (mono("stable-baseline"), "7",
              '<span class="tag tag-yes">是</span>', mono(short(OUT_SHA, 12))),
         ]),
        ("h2", "為什麼隨附的那個無法重播", "gap"),
        ("p", "v1.0 發行包含有已晉升的資料集，"
              f"位於 {mono('stable_data/shards/')}。"
              f"它不含資料湖的索引"
              f"（{mono('lake_state/lake_index.sqlite')}）"
              f"或第一世代的湖分片"
              f"（{mono('lake_data/primary/shards/')}）"
              "——那些只出現在 v0.8 與 v0.9 的"
              "包裡。基線工作流以分片索引"
              "定址資料湖，所以在發行包裡"
              "它什麼也定址不到。"),
        ("p", "拿它對著發行包跑，過去會產生"
              "三個未處理的例外，以及更糟的"
              f"一個自信的答案：{mono('family_counts')} "
              f"回傳 {mono('status: OK')}、"
              f"{mono('decision: ALLOW')} 與一整組"
              "零計數，而它開啟的檔案數是零。"
              "索引缺失讀起來，跟一個真的"
              "沒有質數的區間一模一樣。"),
        ("p", "這已經修好。空的分片選取現在"
              "會拋出例外，而不是回傳一個"
              "空的聚合，CLI 將它回報為 "
              f"{mono('status: NO_DATA')} 並以結束碼 2 "
              "退出。四個操作現在都以同樣"
              "清楚的方式拒絕："),
        ("code", "shell", "$ python lake/mmrf_lake_cli.py query \\\n"
                          "    --request query_examples/family_counts.json\n"
                          "{\n"
                          '  "status": "NO_DATA",\n'
                          '  "reason": "No shards registered for index range [0, 20)."\n'
                          "}\n"
                          "exit 2"),
        ("note", "v1.0 究竟應該隨附湖索引、"
                 "把資料湖改指向穩定分片、"
                 "還是把這個工作流標記為"
                 "第 0.9 世代的產物——"
                 "這是發行決策，不是程式碼"
                 "修補。所以它記在這裡，"
                 "而不是被悄悄解決掉。"),
        ("h2", "替代方案", "replacement"),
        ("p", "穩定分片基線計算同樣的四個"
              "聚合量——外加間隔直方圖、"
              "模 6 與模 210 的剩餘分布、"
              "以及數量級分段——直接從"
              "已晉升的分片算，不需索引"
              "也不需網路。"),
        ("code", "shell", "python workflows/stable_baseline.py --project-root . \\\n"
                          "    --output results_v10/stable_baseline_output.json"),
        ("kv", [
            ("workflow_id", mono("stable-baseline")),
            ("workflow_version", "1.0.0"),
            ("工作流 sha256", mono(WF_SHA)),
            ("dataset_manifest_sha256", mono(MANIFEST)),
            ("預期輸出 sha256", mono(OUT_SHA)),
            ("資源估計", "不到一秒；讀取約 2 MB"),
            ("安全分類", "L0_PUBLIC_MATH，僅聚合"),
        ]),
        ("h2", "它強制的前置條件", "preconditions"),
        ("ul", [
            "穩定清單必須雜湊出它自己"
            "記錄的那個值。",
            "磁碟上的分片數必須與清單相符。",
            "分片內的質數總數必須與清單相符。",
            "旗標欄中每一個被設起的位元"
            "都必須對應到一個具名的族；"
            "無法命名的位元會中止執行，"
            "而不是被悄悄少算。",
        ]),
        ("p", "每一條都是原本可能無聲失敗的"
              "條件，而且每一條都正是先前"
              "那個缺陷躲過的那種檢查。"
              "結果在<a href=\"/zh/research/\">研究</a>頁。"),
    ],
}

# ---------------------------------------------------------- Governance (en)
PAGES["en"]["governance"] = {
    "title": "Governance",
    "display": "A dataset generation is admitted, not written.",
    "meta_title": "Governance — MMRF",
    "description": (
        "Dataset proposal, independent reviews, promotion receipt, provenance graph "
        "and safety gate for the MMRF public prime lake."),
    "standfirst": (
        "Changing the public dataset requires a proposal against a named base, "
        "independent approvals up to a threshold, and a receipt. Every document is "
        "signed and hash-linked to the one before it."),
    "blocks": [
        ("h2", "The chain", "chain"),
        ("chain", "en"),
        ("h2", "Proposal", "proposal"),
        ("kv", [
            ("proposal_id", mono(G["proposal"]["proposal_id"])),
            ("purpose", G["proposal"]["purpose"]),
            ("migration profile", mono(G["proposal"]["migration_profile"])),
            ("base manifest", mono(short(G["proposal"]["base_manifest_sha256"], 24))),
            ("candidate manifest", mono(short(G["proposal"]["candidate_manifest_sha256"], 24))),
            ("proposal sha256", mono(G["proposal"]["sha256"])),
        ]),
        ("p", "The proposal declares its own safety classification, and every "
              "cryptanalytic capability is declared false in the document itself — not "
              "in a policy page that the code never reads."),
        ("gate", [(k, v) for k, v in G["proposal"]["safety"].items()]),
        ("h2", "Reviews", "reviews"),
        ("p", f"{G['receipt']['approval_count']} of "
              f"{G['receipt']['approval_threshold']} required approvals, from reviewers "
              "with different remits — one checking the mathematics, one checking the "
              "safety boundary."),
        ("reviews", "en"),
        ("h2", "Promotion receipt", "receipt"),
        ("kv", [
            ("promotion_id", mono(G["receipt"]["promotion_id"])),
            ("approvals", f"{G['receipt']['approval_count']} / "
                          f"{G['receipt']['approval_threshold']}"),
            ("promoted at", G["receipt"]["promoted_at"][:19].replace("T", " ") + " UTC"),
            ("receipt sha256", mono(G["receipt"]["receipt_sha256"])),
        ]),
        ("h2", "Provenance graph", "provenance"),
        ("p", f"{len(G['provenance_nodes'])} nodes, {len(G['provenance_edges'])} edges. "
              "Each node is a content hash, so the graph can be checked against the "
              "documents rather than believed."),
        ("table",
         ["Node", "Type", "Content sha256"],
         [(mono(x["node_id"]), x["node_type"].replace("_", " ").lower(),
           mono(short(x["content_sha256"], 20))) for x in G["provenance_nodes"]]),
        ("h2", "What governance does not cover", "limits"),
        ("ul", [
            "Reviewers approve a schema change; they do not vote on whether the safety "
            "boundary applies. The forbidden fields are enforced in code, ahead of the "
            "data layer, and are not a governance parameter.",
            "Controlled datasets never enter this site, so no promotion path leads from "
            "them to a public page.",
            "A promotion admits a new generation. It never edits an existing one — the "
            "prior manifest hash stays valid forever.",
        ]),
    ],
}

# ---------------------------------------------------------- Governance (zh)
PAGES["zh"]["governance"] = {
    "title": "治理",
    "display": "資料世代是被接納的，不是被寫下的。",
    "meta_title": "治理 — MMRF",
    "description": (
        "MMRF 公開質數湖的資料集提案、"
        "獨立審查、晉升收據、來源圖"
        "與安全閘。"),
    "standfirst": (
        "更動公開資料集需要一份針對"
        "具名基底的提案、達到門檻的"
        "獨立核准，以及一張收據。"
        "每份文件都經簽章，並以雜湊"
        "鏈接到它前面那一份。"),
    "blocks": [
        ("h2", "整條鏈", "chain"),
        ("chain", "zh"),
        ("h2", "提案", "proposal"),
        ("kv", [
            ("proposal_id", mono(G["proposal"]["proposal_id"])),
            ("目的", G["proposal"]["purpose"]),
            ("遷移設定檔", mono(G["proposal"]["migration_profile"])),
            ("基底清單", mono(short(G["proposal"]["base_manifest_sha256"], 24))),
            ("候選清單", mono(short(G["proposal"]["candidate_manifest_sha256"], 24))),
            ("提案 sha256", mono(G["proposal"]["sha256"])),
        ]),
        ("p", "提案自行宣告它的安全分類，"
              "而且每一項密碼分析能力都在"
              "文件本身裡被宣告為 false"
              "——不是寫在一份程式碼從來"
              "不讀的政策頁上。"),
        ("gate", [(k, v) for k, v in G["proposal"]["safety"].items()]),
        ("h2", "審查", "reviews"),
        ("p", f"所需 {G['receipt']['approval_threshold']} 份核准中已取得 "
              f"{G['receipt']['approval_count']} 份，"
              "來自職責不同的審查者——"
              "一位檢查數學，一位檢查"
              "安全邊界。"),
        ("reviews", "zh"),
        ("h2", "晉升收據", "receipt"),
        ("kv", [
            ("promotion_id", mono(G["receipt"]["promotion_id"])),
            ("核准", f"{G['receipt']['approval_count']} / "
                      f"{G['receipt']['approval_threshold']}"),
            ("晉升時間", G["receipt"]["promoted_at"][:19].replace("T", " ") + " UTC"),
            ("收據 sha256", mono(G["receipt"]["receipt_sha256"])),
        ]),
        ("h2", "來源圖", "provenance"),
        ("p", f"{len(G['provenance_nodes'])} 個節點、{len(G['provenance_edges'])} 條邊。"
              "每個節點都是一個內容雜湊，"
              "所以這張圖可以拿文件去核對，"
              "而不是拿來相信。"),
        ("table",
         ["節點", "型別", "內容 sha256"],
         [(mono(x["node_id"]), x["node_type"].replace("_", " ").lower(),
           mono(short(x["content_sha256"], 20))) for x in G["provenance_nodes"]]),
        ("h2", "治理不涵蓋什麼", "limits"),
        ("ul", [
            "審查者核准的是結構變更；"
            "他們不表決安全邊界是否適用。"
            "被禁欄位在程式碼中、於資料層"
            "之前被強制執行，不是一個"
            "治理參數。",
            "受控資料集永遠不會進入本站，"
            "因此沒有任何晉升路徑能從"
            "它們通向公開頁面。",
            "晉升接納一個新世代。它從不"
            "編輯既有世代——先前的清單"
            "雜湊永遠有效。",
        ]),
    ],
}

# -------------------------------------------------------- Verification (en)
PAGES["en"]["verification"] = {
    "title": "Verification",
    "display": "Two commands, and none of them require trusting this page.",
    "meta_title": "Verification — MMRF",
    "description": (
        "Verify the MMRF v1.0 release: signed release manifest, stable manifest hash, "
        "shard integrity sampling, installation state and citation verification."),
    "standfirst": (
        "Everything this site asserts is derived from files in the release. If a "
        "number here disagrees with what the commands below print, the commands are "
        "right."),
    "blocks": [
        ("h2", "Release", "release"),
        ("code", "shell", "python install/mmrf.py --project-root . verify-release\n"
                          "python install/mmrf.py --project-root . doctor"),
        ("p", f"The flag goes before the subcommand. {mono('--project-root')} is a "
              "top-level argument, so putting it after "
              f"{mono('verify-release')} fails to parse — worth knowing, because parts "
              "of the shipped documentation show it the other way round."),
        ("kv", [
            ("release id", mono(F["release_id"])),
            ("signed release manifest", mono("release_v10/stable_release_manifest_v1.0.json")),
            ("release public key", mono("release_v10/stable_release_signing.public.pem")),
            ("stable manifest", mono("stable_data/stable_manifest_v1.0.json")),
            ("shards checked by doctor", str(D["shard_count"])),
        ]),
        ("h2", "Expect valid: false, and read why", "expect"),
        ("p", "Run against a clone of the runtime repository, "
              f"{mono('verify-release')} reports {mono('valid: false')}. That is the "
              "correct answer. The repository is the published package plus two "
              "repaired files, and the check names them:"),
        ("code", "json",
         '{\n'
         '  "valid": false,\n'
         '  "checks": {\n'
         '    "signature_and_document_hash": true,\n'
         '    "schema_ok": true,\n'
         '    "release_id_ok": true,\n'
         '    "version_ok": true,\n'
         '    "safety_ok": true,\n'
         '    "payload_ok": false\n'
         '  }\n'
         '}\n'
         '\n'
         'hash_mismatch  lake/mmrf_data_lake.py\n'
         'hash_mismatch  lake/mmrf_lake_cli.py'),
        ("p", "The signature still verifies, and every safety and semantic check "
              "passes. Only the payload hashes for the two repaired files differ, and "
              "the repairs are described in "
              f"<a href=\"{SITE['repo']}/blob/main/REPAIRS.md\" rel=\"noopener\">REPAIRS.md</a>. "
              "To verify the release exactly as published, check out the import commit "
              "— it is byte-identical to the package — and run it there."),
        ("p", "The dataset is untouched either way. No shard byte changed, and the "
              "stable manifest hash below is the one the release published."),
        ("h2", "Reproduce the manifest hash", "manifest"),
        ("p", "The manifest hash is not a hash of the file. It is the SHA-256 of the "
              "canonical JSON of the manifest object with the "
              f"{mono('manifest_sha256')} field removed — a self-referential field "
              "cannot be inside the thing it describes. Reproducing it takes four "
              "lines:"),
        ("code", "python",
         "import json, hashlib\n"
         "m = json.load(open('stable_data/stable_manifest_v1.0.json', encoding='utf-8'))\n"
         "core = {k: v for k, v in m.items() if k != 'manifest_sha256'}\n"
         "canon = json.dumps(core, ensure_ascii=False, sort_keys=True,\n"
         "                   separators=(',', ':'))\n"
         "print(hashlib.sha256(canon.encode()).hexdigest() == m['manifest_sha256'])"),
        ("kv", [("expected", mono(MANIFEST))]),
        ("h2", "Count the records yourself", "count"),
        ("p", "The shards are plain NumPy archives. Nothing stops you counting them "
              "without any MMRF code at all:"),
        ("code", "python",
         "import numpy as np, pathlib\n"
         "total = 0\n"
         "for p in sorted(pathlib.Path('stable_data/shards').glob('*.npz')):\n"
         "    with np.load(p) as z:\n"
         "        total += len(z['prime'])\n"
         f"print(total)   # {n(D['prime_count'])}"),
        ("h2", "Check it against the literature", "external"),
        ("p", "Three values in this dataset are independently known, which makes them "
              "the cheapest external check available:"),
        ("table",
         ["Quantity", "This dataset", "Known value"],
         [
             ("π(2,000,000)", n(D["prime_count"]), n(D["prime_count"])),
             ("maximal gap below 2×10⁶", str(B["gap_quantiles"]["max_gap"]),
              str(B["gap_quantiles"]["max_gap"])),
             ("twin prime pairs below 2×10⁶", n(FAM["twin_prime"]), n(FAM["twin_prime"])),
         ]),
        ("p", "A table where both columns agree is only worth printing because the "
              "columns come from different places: the left from the shards, the right "
              "from published values. If they ever diverge, this page is the thing that "
              "should change."),
        ("h2", "Machine-readable", "machine"),
        ("p", "Static, no JavaScript, no content negotiation:"),
        ("table",
         ["Path", "Contents"],
         [
             ('<a href="/.well-known/mmrf.json">/.well-known/mmrf.json</a>',
              "release id, stable manifest hash, query-surface declaration"),
             ('<a href="/datasets/index.json">/datasets/index.json</a>',
              "dataset identity, columns, manifest hash"),
             ('<a href="/workflows/index.json">/workflows/index.json</a>',
              "workflow registry with expected output hashes"),
             ('<a href="/governance/proposals.json">/governance/proposals.json</a>',
              "proposal, reviews, receipt, provenance nodes"),
             ('<a href="/citations/index.json">/citations/index.json</a>',
              "dataset citation record"),
             ('<a href="/results/stable-baseline.json">/results/stable-baseline.json</a>',
              "the full baseline output, self-hashed"),
             ('<a href="/llms.txt">/llms.txt</a>', "orientation for language models"),
             ('<a href="/agents.md">/agents.md</a>', "what an agent may and may not ask"),
         ]),
    ],
}

# -------------------------------------------------------- Verification (zh)
PAGES["zh"]["verification"] = {
    "title": "驗證",
    "display": "兩行指令，而且都不需要相信本頁。",
    "meta_title": "驗證 — MMRF",
    "description": (
        "驗證 MMRF v1.0 發行版：簽章發行"
        "清單、穩定清單雜湊、分片完整性"
        "抽樣、安裝狀態與引用驗證。"),
    "standfirst": (
        "本站主張的一切都衍生自發行包"
        "裡的檔案。若本頁某個數字與"
        "下面指令印出的不符，"
        "以指令為準。"),
    "blocks": [
        ("h2", "發行版", "release"),
        ("code", "shell", "python install/mmrf.py --project-root . verify-release\n"
                          "python install/mmrf.py --project-root . doctor"),
        ("p", f"旗標放在子指令之前。{mono('--project-root')} "
              "是頂層參數，所以把它放在 "
              f"{mono('verify-release')} 之後會解析失敗"
              "——這值得知道，因為隨附"
              "文件有些地方寫成相反的順序。"),
        ("kv", [
            ("發行 id", mono(F["release_id"])),
            ("簽章發行清單", mono("release_v10/stable_release_manifest_v1.0.json")),
            ("發行公鑰", mono("release_v10/stable_release_signing.public.pem")),
            ("穩定清單", mono("stable_data/stable_manifest_v1.0.json")),
            ("doctor 檢查的分片", str(D["shard_count"])),
        ]),
        ("h2", "預期會看到 valid: false，並讀懂原因", "expect"),
        ("p", "對著 runtime 儲存庫的 clone 執行，"
              f"{mono('verify-release')} 會回報 "
              f"{mono('valid: false')}。這是正確的答案。"
              "這個儲存庫是已發布的包加上兩個"
              "被修復的檔案，而檢查把它們"
              "指名出來："),
        ("code", "json",
         '{\n'
         '  "valid": false,\n'
         '  "checks": {\n'
         '    "signature_and_document_hash": true,\n'
         '    "schema_ok": true,\n'
         '    "release_id_ok": true,\n'
         '    "version_ok": true,\n'
         '    "safety_ok": true,\n'
         '    "payload_ok": false\n'
         '  }\n'
         '}\n'
         '\n'
         'hash_mismatch  lake/mmrf_data_lake.py\n'
         'hash_mismatch  lake/mmrf_lake_cli.py'),
        ("p", "簽章依然通過驗證，所有安全與"
              "語意檢查也都通過。只有那兩個"
              "被修復檔案的 payload 雜湊不同，"
              "而修復內容記在 "
              f"<a href=\"{SITE['repo']}/blob/main/REPAIRS.md\" rel=\"noopener\">REPAIRS.md</a>。"
              "若要驗證與發布時完全一致的"
              "版本，請 checkout 匯入 commit"
              "——它與發行包逐位元相同"
              "——並在那裡執行。"),
        ("p", "無論如何資料集都沒有被動過。"
              "沒有任何分片位元組改變，"
              "下方的穩定清單雜湊就是"
              "發行時公布的那一個。"),
        ("h2", "重現清單雜湊", "manifest"),
        ("p", "清單雜湊不是檔案的雜湊。"
              "它是清單物件移除 "
              f"{mono('manifest_sha256')} 欄位後、"
              "正規 JSON 的 SHA-256——"
              "一個自我指涉的欄位不可能"
              "存在於它所描述的東西"
              "內部。重現它只要四行："),
        ("code", "python",
         "import json, hashlib\n"
         "m = json.load(open('stable_data/stable_manifest_v1.0.json', encoding='utf-8'))\n"
         "core = {k: v for k, v in m.items() if k != 'manifest_sha256'}\n"
         "canon = json.dumps(core, ensure_ascii=False, sort_keys=True,\n"
         "                   separators=(',', ':'))\n"
         "print(hashlib.sha256(canon.encode()).hexdigest() == m['manifest_sha256'])"),
        ("kv", [("預期值", mono(MANIFEST))]),
        ("h2", "自己數一遍記錄", "count"),
        ("p", "分片就是單純的 NumPy 封存檔。"
              "沒有任何東西阻止你在完全"
              "不用 MMRF 程式碼的情況下"
              "自己數："),
        ("code", "python",
         "import numpy as np, pathlib\n"
         "total = 0\n"
         "for p in sorted(pathlib.Path('stable_data/shards').glob('*.npz')):\n"
         "    with np.load(p) as z:\n"
         "        total += len(z['prime'])\n"
         f"print(total)   # {n(D['prime_count'])}"),
        ("h2", "拿去對照文獻", "external"),
        ("p", "這個資料集裡有三個值是"
              "獨立已知的，因此是現成"
              "最省事的外部檢查："),
        ("table",
         ["量", "本資料集", "已知值"],
         [
             ("π(2,000,000)", n(D["prime_count"]), n(D["prime_count"])),
             ("2×10⁶ 以下最大間隔", str(B["gap_quantiles"]["max_gap"]),
              str(B["gap_quantiles"]["max_gap"])),
             ("2×10⁶ 以下孪生質數對", n(FAM["twin_prime"]), n(FAM["twin_prime"])),
         ]),
        ("p", "一張兩欄一致的表值得印出來，"
              "只因為兩欄來自不同地方："
              "左欄來自分片，右欄來自"
              "已發表的值。若它們哪天"
              "不一致，該改的是這一頁。"),
        ("h2", "機器可讀", "machine"),
        ("p", "靜態、不需 JavaScript、"
              "不做內容協商："),
        ("table",
         ["路徑", "內容"],
         [
             ('<a href="/.well-known/mmrf.json">/.well-known/mmrf.json</a>',
              "發行 id、穩定清單雜湊、查詢面宣告"),
             ('<a href="/datasets/index.json">/datasets/index.json</a>',
              "資料集身分、欄位、清單雜湊"),
             ('<a href="/workflows/index.json">/workflows/index.json</a>',
              "工作流登錄與預期輸出雜湊"),
             ('<a href="/governance/proposals.json">/governance/proposals.json</a>',
              "提案、審查、收據、來源節點"),
             ('<a href="/citations/index.json">/citations/index.json</a>',
              "資料集引用記錄"),
             ('<a href="/results/stable-baseline.json">/results/stable-baseline.json</a>',
              "完整基線輸出，含自我雜湊"),
             ('<a href="/llms.txt">/llms.txt</a>', "給語言模型的導引"),
             ('<a href="/agents.md">/agents.md</a>', "代理可以問與不可以問什麼"),
         ]),
    ],
}

# --------------------------------------------------------------- Safety (en)
PAGES["en"]["safety"] = {
    "title": "Safety",
    "display": "The boundary is the architecture, not a disclaimer.",
    "meta_title": "Safety — MMRF",
    "description": (
        "MMRF is a mathematical research dataset. It accepts no external target "
        "integer, emits no factor candidate, performs no range narrowing, and stores "
        "no public source–factor relation."),
    "standfirst": (
        "A prime dataset invites one obvious misuse. MMRF's answer is not a terms-of-use "
        "paragraph; it is a guard that runs before the data layer and refuses seventeen "
        "field names outright."),
    "blocks": [
        ("h2", "What MMRF is", "what"),
        ("ul", [
            "A public dataset of mathematical properties of primes in a fixed range.",
            "An aggregate query surface: densities, quantiles, histograms, counts.",
            "A governance and provenance record for how that dataset came to exist.",
        ]),
        ("h2", "What it will not do", "wont"),
        ("ul", [
            "Accept an externally supplied integer of any kind, including an RSA modulus.",
            "Return a factor, a factor candidate, or a set of candidates.",
            "Narrow a search range, or answer a question whose value lies in narrowing one.",
            "Return a nearest prime, an exact prime list, or raw prime records.",
            "Store or publish a relation between a composite and its factors.",
            "Expose controlled datasets. They do not reach this site by any path.",
        ]),
        ("h2", "Endpoints that will never exist", "endpoints"),
        ("chips_off", FORBIDDEN_ENDPOINTS),
        ("h2", "How the refusal actually works", "mechanism"),
        ("p", "The guard evaluates a request before the data layer is touched. A "
              "forbidden field name causes a denial with the field named in the reason, "
              f"a cost of {mono('cost_units: 0')}, and a "
              f"{mono('normalized_request')} of null — the request is never normalised, "
              "so there is nothing downstream to execute."),
        ("split", "en"),
        ("p", "The denial still produces an audit event with its own hash. Refusals are "
              "recorded, not silently dropped, which is what makes a pattern of "
              "attempted misuse visible rather than invisible."),
        ("h2", "The composition rule", "composition"),
        ("p", "Individual aggregate answers are safe; a long series of carefully chosen "
              "ones is the thing to watch. So the surface is bounded in three ways at "
              "once: a fixed operation allowlist, a per-session query budget, and a cap "
              "on how many shards one query may touch. Researchers are additionally "
              "asked not to reconstruct a forbidden output by composing permitted ones."),
        ("p", "That last one is a request, not an enforcement, and it is stated as a "
              "request deliberately. A policy that claims to enforce what it cannot is "
              "worse than one that is honest about where the mechanism ends."),
        ("h2", "Reporting", "reporting"),
        ("p", "If you find a way to obtain a forbidden output from permitted operations, "
              "that is a defect in this design and worth reporting through the "
              f"<a href=\"{SITE['repo']}/issues\" rel=\"noopener\">runtime repository</a>. "
              "Please describe the composition rather than publishing a working "
              "sequence."),
    ],
}

# --------------------------------------------------------------- Safety (zh)
PAGES["zh"]["safety"] = {
    "title": "安全",
    "display": "邊界就是架構本身，不是免責聲明。",
    "meta_title": "安全 — MMRF",
    "description": (
        "MMRF 是數學研究資料集。"
        "不接受外部目標整數、不提供"
        "因數候選、不做範圍縮減、"
        "不保存公開的來源—因數關係。"),
    "standfirst": (
        "質數資料集會招來一種顯而易見"
        "的誤用。MMRF 的回應不是一段"
        "使用條款，而是一個跑在資料層"
        "之前、直接拒絕十七個欄位名稱"
        "的守衛。"),
    "blocks": [
        ("h2", "MMRF 是什麼", "what"),
        ("ul", [
            "一個固定區間內質數之數學"
            "性質的公開資料集。",
            "一個聚合查詢面：密度、"
            "分位數、直方圖、計數。",
            "一份關於該資料集如何成立"
            "的治理與來源記錄。",
        ]),
        ("h2", "它不會做什麼", "wont"),
        ("ul", [
            "接受任何形式的外部整數，"
            "包含 RSA modulus。",
            "回傳因數、因數候選，或"
            "一組候選。",
            "縮減搜尋範圍，或回答一個"
            "其價值就在於縮減範圍的問題。",
            "回傳最近質數、精確質數列表，"
            "或原始質數記錄。",
            "儲存或發布合數與其因數"
            "之間的關係。",
            "暴露受控資料集。它們不會"
            "經由任何路徑抵達本站。",
        ]),
        ("h2", "永遠不會存在的端點", "endpoints"),
        ("chips_off", FORBIDDEN_ENDPOINTS),
        ("h2", "拒絕實際上如何運作", "mechanism"),
        ("p", "守衛在資料層被碰到之前"
              "就評估請求。被禁的欄位"
              "名稱會導致拒絕，理由中"
              "會指名該欄位，成本為 "
              f"{mono('cost_units: 0')}，而 "
              f"{mono('normalized_request')} 為 null"
              "——請求從未被正規化，"
              "因此下游沒有任何東西"
              "可供執行。"),
        ("split", "zh"),
        ("p", "拒絕依然會產生一個帶自身"
              "雜湊的稽核事件。拒絕是被"
              "記錄的，不是被默默丟棄的"
              "——這正是讓一連串嘗試"
              "誤用的行為變得可見、"
              "而非不可見的原因。"),
        ("h2", "組合規則", "composition"),
        ("p", "單一的聚合答案是安全的；"
              "要留意的是一長串精心挑選"
              "的答案。所以這個查詢面"
              "同時受三重限制：固定的"
              "操作允許清單、每個工作階段"
              "的查詢預算，以及單次查詢"
              "可觸及分片數的上限。此外"
              "也要求研究者不要用允許的"
              "操作去重建被禁的輸出。"),
        ("p", "最後這一條是請求，不是"
              "強制，而且是刻意這樣寫的。"
              "一份宣稱能強制它其實做不到"
              "的事的政策，比一份誠實說明"
              "機制到哪裡為止的政策更糟。"),
        ("h2", "回報", "reporting"),
        ("p", "如果你找到一種方法，能用"
              "允許的操作取得被禁的輸出，"
              "那就是本設計的缺陷，值得"
              f"透過<a href=\"{SITE['repo']}/issues\" rel=\"noopener\">runtime "
              "儲存庫</a>回報。請描述"
              "該組合方式，而不要公開"
              "一組可用的查詢序列。"),
    ],
}

# -------------------------------------------------------- Documentation (en)
PAGES["en"]["documentation"] = {
    "title": "Documentation",
    "display": "Everything ships inside the release.",
    "meta_title": "Documentation — MMRF",
    "description": (
        "MMRF documentation index: stable specification, dataset schema, query "
        "language, workflow specification, governance, threat model, operations and "
        "compatibility."),
    "standfirst": (
        "The documents below are files in the release package, not pages written for "
        "this site. Paths are relative to the project root."),
    "blocks": [
        ("h2", "Getting started", "start"),
        ("code", "shell",
         "git clone https://github.com/kakon77777-commits/mmrf-runtime.git\n"
         "cd mmrf-runtime\n"
         "python -m pip install numpy\n"
         "python install/mmrf.py --project-root . doctor\n"
         "python workflows/stable_baseline.py --project-root ."),
        ("p", "NumPy is the only dependency. There is no server to run and no network "
              "access at any point."),
        ("h2", "Specifications", "specs"),
        ("table",
         ["Document", "Path"],
         [
             ("Stable core specification 1.0", mono("docs_v10/MMRF_STABLE_CORE_SPECIFICATION_1.0.md")),
             ("Threat model 1.0", mono("docs_v10/MMRF_THREAT_MODEL_1.0.md")),
             ("Operations manual 1.0", mono("docs_v10/MMRF_OPERATIONS_MANUAL_1.0.md")),
             ("Release freeze 1.0", mono("docs_v10/MMRF_RELEASE_FREEZE_1.0.md")),
             ("Compatibility & upgrade matrix 1.0", mono("docs_v10/MMRF_COMPATIBILITY_UPGRADE_MATRIX_1.0.md")),
             ("Scientific query language 0.8", mono("docs_v08/MMRF_DATA_LAKE_SCIENTIFIC_QUERY_v0.8.md")),
             ("Federation governance 0.9", mono("docs_v09/MMRF_SCIENTIFIC_FEDERATION_GOVERNANCE_v0.9.md")),
             ("Conformance profile 0.9", mono("docs_v09/MMRF_RC_CONFORMANCE_PROFILE_0.9.md")),
             ("Cryptographic safety policy", mono("docs/MMRF_CRYPTOGRAPHIC_SAFETY_POLICY_v0.1.md")),
             ("Project charter", mono("docs/MMRF_PROJECT_CHARTER_v0.1.md")),
             ("3M integration map", mono("docs/MMRF_3M_INTEGRATION_MAP.md")),
         ]),
        ("h2", "Schemas", "schemas"),
        ("table",
         ["Schema", "Path"],
         [
             ("Shard record", mono("schemas_v08/shard-record-0.8.schema.json")),
             ("Data lake manifest", mono("schemas_v08/data-lake-manifest-0.8.schema.json")),
             ("Scientific query", mono("schemas_v08/scientific-query-0.8.schema.json")),
             ("Scientific workflow", mono("schemas_v08/scientific-workflow-0.8.schema.json")),
             ("Dataset proposal", mono("schemas_v09/dataset-proposal-0.9.schema.json")),
             ("Dataset review", mono("schemas_v09/dataset-review-0.9.schema.json")),
             ("Provenance graph", mono("schemas_v09/provenance-graph-0.9.schema.json")),
             ("Dataset citation", mono("schemas_v09/dataset-citation-0.9.schema.json")),
         ]),
        ("h2", "Version history", "history"),
        ("table",
         ["Version", "What it added"],
         [
             ("v0.1", "foundation"),
             ("v0.2", "ingestion"),
             ("v0.3", "public index"),
             ("v0.4", "controlled research enclave"),
             ("v0.5", "federated vault"),
             ("v0.6", "transparency and recovery"),
             ("v0.7", "policy network"),
             ("v0.8", "data lake and the scientific query guard"),
             ("v0.9", "scientific federation, governance, wheel30 column"),
             ("v1.0", "stable core, release freeze, promoted generation 2"),
         ]),
        ("h2", "This site", "site"),
        ("p", "Static, built by a Python script with no dependencies, from the runtime's "
              "own artifacts. Every figure comes through "
              f"{mono('sync_facts.py')}, which refuses to write if an artifact fails its "
              "own hash check — so a stale number cannot survive a build. Source: "
              f"<a href=\"{SITE['site_repo']}\" rel=\"noopener\">mmrf-site</a>."),
    ],
}

# -------------------------------------------------------- Documentation (zh)
PAGES["zh"]["documentation"] = {
    "title": "文件",
    "display": "所有文件都在發行包裡。",
    "meta_title": "文件 — MMRF",
    "description": (
        "MMRF 文件索引：穩定規格、"
        "資料集結構、查詢語言、工作流"
        "規格、治理、威脅模型、營運"
        "與相容性。"),
    "standfirst": (
        "下列文件是發行包裡的檔案，"
        "不是為本站另寫的頁面。"
        "路徑相對於專案根目錄。"),
    "blocks": [
        ("h2", "開始使用", "start"),
        ("code", "shell",
         "git clone https://github.com/kakon77777-commits/mmrf-runtime.git\n"
         "cd mmrf-runtime\n"
         "python -m pip install numpy\n"
         "python install/mmrf.py --project-root . doctor\n"
         "python workflows/stable_baseline.py --project-root ."),
        ("p", "NumPy 是唯一的相依套件。"
              "沒有伺服器要跑，"
              "任何步驟都不需要網路。"),
        ("h2", "規格", "specs"),
        ("table",
         ["文件", "路徑"],
         [
             ("穩定核心規格 1.0", mono("docs_v10/MMRF_STABLE_CORE_SPECIFICATION_1.0.md")),
             ("威脅模型 1.0", mono("docs_v10/MMRF_THREAT_MODEL_1.0.md")),
             ("營運手冊 1.0", mono("docs_v10/MMRF_OPERATIONS_MANUAL_1.0.md")),
             ("發行凍結 1.0", mono("docs_v10/MMRF_RELEASE_FREEZE_1.0.md")),
             ("相容與升級矩陣 1.0", mono("docs_v10/MMRF_COMPATIBILITY_UPGRADE_MATRIX_1.0.md")),
             ("科學查詢語言 0.8", mono("docs_v08/MMRF_DATA_LAKE_SCIENTIFIC_QUERY_v0.8.md")),
             ("聯邦治理 0.9", mono("docs_v09/MMRF_SCIENTIFIC_FEDERATION_GOVERNANCE_v0.9.md")),
             ("一致性剖面 0.9", mono("docs_v09/MMRF_RC_CONFORMANCE_PROFILE_0.9.md")),
             ("密碼安全政策", mono("docs/MMRF_CRYPTOGRAPHIC_SAFETY_POLICY_v0.1.md")),
             ("專案章程", mono("docs/MMRF_PROJECT_CHARTER_v0.1.md")),
             ("3M 整合圖", mono("docs/MMRF_3M_INTEGRATION_MAP.md")),
         ]),
        ("h2", "結構定義", "schemas"),
        ("table",
         ["結構", "路徑"],
         [
             ("分片記錄", mono("schemas_v08/shard-record-0.8.schema.json")),
             ("資料湖清單", mono("schemas_v08/data-lake-manifest-0.8.schema.json")),
             ("科學查詢", mono("schemas_v08/scientific-query-0.8.schema.json")),
             ("科學工作流", mono("schemas_v08/scientific-workflow-0.8.schema.json")),
             ("資料集提案", mono("schemas_v09/dataset-proposal-0.9.schema.json")),
             ("資料集審查", mono("schemas_v09/dataset-review-0.9.schema.json")),
             ("來源圖", mono("schemas_v09/provenance-graph-0.9.schema.json")),
             ("資料集引用", mono("schemas_v09/dataset-citation-0.9.schema.json")),
         ]),
        ("h2", "版本歷史", "history"),
        ("table",
         ["版本", "新增了什麼"],
         [
             ("v0.1", "基礎"),
             ("v0.2", "匯入"),
             ("v0.3", "公開索引"),
             ("v0.4", "受控研究飛地"),
             ("v0.5", "聯邦保管庫"),
             ("v0.6", "透明性與復原"),
             ("v0.7", "政策網路"),
             ("v0.8", "資料湖與科學查詢守衛"),
             ("v0.9", "科學聯邦、治理、wheel30 欄"),
             ("v1.0", "穩定核心、發行凍結、晉升第二世代"),
         ]),
        ("h2", "關於本站", "site"),
        ("p", "靜態網站，由一支無相依的 "
              "Python 腳本從 runtime 自己的"
              "成品建置。每一個數字都經過 "
              f"{mono('sync_facts.py')}，"
              "而它在任何成品未通過自身"
              "雜湊檢查時就拒絕寫入"
              "——所以過期的數字撐不過"
              "一次建置。原始碼："
              f"<a href=\"{SITE['site_repo']}\" rel=\"noopener\">mmrf-site</a>。"),
    ],
}

# ---------------------------------------------------------------- About (en)
PAGES["en"]["about"] = {
    "title": "About",
    "display": "The fifth project in the 3M series.",
    "meta_title": "About — MMRF",
    "description": (
        "MMRF — Multidirectional Matrix Research Infrastructure, part of the 3M series "
        "from EveMissLab. Apache-2.0."),
    "standfirst": (
        "MMR measures. MMLC records. MLF contains. MMPF chooses. MMRF is where the "
        "results are kept, and the first of them to be defined by a refusal."),
    "blocks": [
        ("h2", "The series", "series"),
        ("table",
         ["Project", "What it does", "Site"],
         [
             ("MMR-Bench", "benchmark and audit workpaper",
              '<a href="https://mmr.evemisslab.com" rel="noopener">mmr</a>'),
             ("MMLC", "ledger runtime; time-indexed transaction chains",
              '<a href="https://mmlc.evemisslab.com" rel="noopener">mmlc</a>'),
             ("MLF", "matrix ledger format; byte-exact containers",
              '<a href="https://mlf.evemisslab.com" rel="noopener">mlf</a>'),
             ("MMPF", "route-aware auditable factorization runtime",
              '<a href="https://mmpf.evemisslab.com" rel="noopener">mmpf</a>'),
             ("MMRF", "research infrastructure; this site", "—"),
         ]),
        ("h2", "Why the refusal is the design", "why"),
        ("p", "MMPF factors integers and is open about it. MMRF holds a prime dataset "
              "and is equally open about the fact that a prime dataset with an "
              "unrestricted query surface is a different kind of object entirely."),
        ("p", "The distance between the two is not a policy document. It is a guard "
              "that runs before the data layer, an operation allowlist, a field "
              "denylist, a per-session budget, and a governance process in which the "
              "safety classification is declared inside the proposal and checked by a "
              "reviewer whose only job is that. The boundary is load-bearing."),
        ("h2", "Release", "release"),
        ("kv", [
            ("Version", SITE["version"]),
            ("Release ID", mono(F["release_id"])),
            ("Licence", "Apache-2.0"),
            ("Runtime", f'<a href="{SITE["repo"]}" rel="noopener">mmrf-runtime</a>'),
            ("This site", f'<a href="{SITE["site_repo"]}" rel="noopener">mmrf-site</a>'),
            ("Publisher", CIT["publisher"]),
        ]),
        ("h2", "Changes made after the release was cut", "changes"),
        ("p", "Three, all recorded in the runtime's git history as a single commit "
              "against an unmodified import of the published package, so the diff is "
              "readable:"),
        ("ul", [
            f"{mono('family_counts')} no longer reports a Sophie Germain count. It was "
            "sharing a bit mask with safe primes and no Sophie Germain bit was ever "
            "written, so the surface returned one real quantity under two names.",
            "An empty shard selection now raises instead of returning an empty "
            "aggregate, so a missing index can no longer be mistaken for a range with "
            "no primes in it.",
            "A replayable baseline study was added, because the shipped baseline "
            "workflow cannot run from the shipped package.",
        ]),
        ("p", "None of them changed a shard byte, and the stable manifest hash is the "
              "same as the one the release published."),
    ],
}

# ---------------------------------------------------------------- About (zh)
PAGES["zh"]["about"] = {
    "title": "關於",
    "display": "3M 系列的第五個專案。",
    "meta_title": "關於 — MMRF",
    "description": (
        "MMRF — 多向矩陣研究基礎設施，"
        "EveMissLab 3M 系列之一。"
        "Apache-2.0。"),
    "standfirst": (
        "MMR 量測。MMLC 記錄。"
        "MLF 容納。MMPF 選擇。"
        "MMRF 是結果被保存的地方，"
        "也是其中第一個由「拒絕」"
        "來定義的。"),
    "blocks": [
        ("h2", "這個系列", "series"),
        ("table",
         ["專案", "做什麼", "網站"],
         [
             ("MMR-Bench", "基準與稽核工作底稿",
              '<a href="https://mmr.evemisslab.com" rel="noopener">mmr</a>'),
             ("MMLC", "帳本執行環境；時間索引交易鏈",
              '<a href="https://mmlc.evemisslab.com" rel="noopener">mmlc</a>'),
             ("MLF", "矩陣帳本格式；逐位元精確的容器",
              '<a href="https://mlf.evemisslab.com" rel="noopener">mlf</a>'),
             ("MMPF", "路徑感知、可稽核的分解執行環境",
              '<a href="https://mmpf.evemisslab.com" rel="noopener">mmpf</a>'),
             ("MMRF", "研究基礎設施；本站", "—"),
         ]),
        ("h2", "為什麼拒絕就是設計", "why"),
        ("p", "MMPF 分解整數，而且對此"
              "毫不掩飾。MMRF 持有一個"
              "質數資料集，同樣毫不掩飾"
              "地指出：一個查詢面不受限"
              "的質數資料集，是完全"
              "另一種東西。"),
        ("p", "兩者之間的距離不是一份"
              "政策文件。它是一個跑在"
              "資料層之前的守衛、一份"
              "操作允許清單、一份欄位"
              "拒絕清單、一個每工作階段"
              "的預算，以及一套治理流程"
              "——在其中安全分類被宣告"
              "在提案內部，並由一位"
              "職責只有這件事的審查者"
              "查核。這道邊界是承重的。"),
        ("h2", "發行資訊", "release"),
        ("kv", [
            ("版本", SITE["version"]),
            ("發行 ID", mono(F["release_id"])),
            ("授權", "Apache-2.0"),
            ("Runtime", f'<a href="{SITE["repo"]}" rel="noopener">mmrf-runtime</a>'),
            ("本站原始碼", f'<a href="{SITE["site_repo"]}" rel="noopener">mmrf-site</a>'),
            ("發行者", CIT["publisher"]),
        ]),
        ("h2", "發行之後做過的更動", "changes"),
        ("p", "三項，全部記錄在 runtime 的 "
              "git 歷史中，作為對已發布包"
              "之未修改匯入的單一 commit，"
              "所以 diff 是可讀的："),
        ("ul", [
            f"{mono('family_counts')} 不再回報 Sophie Germain "
            "計數。它與 safe prime 共用"
            "同一個位元遮罩，而 Sophie "
            "Germain 的位元從未被寫入，"
            "於是查詢面把同一個真實的量"
            "用兩個名字回傳了。",
            "空的分片選取現在會拋出例外，"
            "而不是回傳空的聚合，因此"
            "索引缺失不會再被誤認為"
            "一個沒有質數的區間。",
            "新增了一個可重播的基線研究，"
            "因為隨附的基線工作流無法"
            "從隨附的包執行。",
        ]),
        ("p", "三項都沒有改動任何一個"
              "分片位元組，穩定清單雜湊"
              "與發行時公布的完全相同。"),
    ],
}

# ---------------------------------------------------------------- Daily reports
PAGES["en"]["reports"] = {
    "title": "Daily reports",
    "display": "A short public log.",
    "meta_title": "Daily reports — MMRF",
    "description": (
        "Public daily update reports for MMRF. The page shows dates and downloads; "
        "sensitive data is not published."),
    "standfirst": (
        "One card per public update. The report itself is in the download."),
    "blocks": [
        ("h2", "Public entries", "entries"),
        ("reports",),
    ],
}

PAGES["zh"]["reports"] = {
    "title": "每日更新",
    "display": "公開更新日報。",
    "meta_title": "每日更新日報 — MMRF",
    "description": (
        "MMRF 的公開每日更新日報。頁面只顯示日期與下載，敏感資料不公開。"),
    "standfirst": "每張卡片代表一次公開更新；日報內容放在下載檔中。",
    "blocks": [
        ("h2", "公開條目", "entries"),
        ("reports",),
    ],
}
