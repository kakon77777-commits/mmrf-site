# -*- coding: utf-8 -*-
"""Builds mmrf.evemisslab.com into dist/.

    python sync_facts.py && python build.py

English at the root, Traditional Chinese under /zh/. Both trees are generated
from the same block list per page in src/content.py; the build fails if a page
is missing from either language, or if the two trees end up different sizes.

The machine-readable layer (/.well-known/mmrf.json and friends) is written from
the same facts.json the HTML uses, so the JSON a crawler reads and the number a
human reads cannot disagree.
"""

from __future__ import annotations

import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import content as C  # noqa: E402

DIST = ROOT / "dist"

FONTS_BASE = (
    "https://fonts.googleapis.com/css2"
    "?family=Chivo:wght@400;500;700"
    "&family=Instrument+Serif:ital@0;1"
    "&family=IBM+Plex+Mono:wght@400;500;600"
)
FONTS_ZH = "&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@400;600"

THEME_BOOT = (
    "<script>(function(){try{var t=localStorage.getItem('mmrf-theme');"
    "if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t);}}"
    "catch(e){}})();</script>"
)

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" fill="#101418"/>
<rect x="4" y="4" width="24" height="24" fill="none" stroke="#3f9a92" stroke-width="2"/>
<rect x="10" y="10" width="5" height="5" fill="#c9a227"/>
<rect x="17" y="10" width="5" height="5" fill="#3f9a92"/>
<rect x="10" y="17" width="5" height="5" fill="#3f9a92"/>
<rect x="17" y="17" width="5" height="5" fill="#b4483f"/>
</svg>
"""


def url_path(lang, slug):
    base = "/" if lang == "en" else "/zh/"
    return base if not slug else f"{base}{slug}/"


def out_file(lang, slug):
    rel = url_path(lang, slug).strip("/")
    return DIST / rel / "index.html" if rel else DIST / "index.html"


# --------------------------------------------------------------------------
# block renderers
# --------------------------------------------------------------------------

def r_h2(text, anchor):
    return f'<h2 class="h2" id="{anchor}">{text}</h2>'


def r_p(text):
    return f'<p class="p">{text}</p>'


def r_ul(items):
    return f'<ul class="list">{"".join(f"<li>{i}</li>" for i in items)}</ul>'


def r_kv(rows):
    cells = "".join(
        f'<div class="kv-row"><dt class="kv-k">{k}</dt><dd class="kv-v">{v}</dd></div>'
        for k, v in rows
    )
    return f'<dl class="kv">{cells}</dl>'


def r_code(tag, text):
    return (f'<div class="code"><div class="code-tag">{tag}</div>'
            f"<pre><code>{html.escape(text)}</code></pre></div>")


def r_table(headers, rows):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows
    )
    return ('<div class="tbl-wrap"><table class="tbl">'
            f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>")


def r_chips(items, off=False):
    cls = "chip chip-off" if off else "chip"
    return ('<ul class="chips">'
            + "".join(f'<li><span class="{cls}">{html.escape(i)}</span></li>'
                      for i in items)
            + "</ul>")


def r_stat4(items):
    cells = "".join(
        f'<div class="stat"><span class="stat-n">{v}</span>'
        f'<span class="stat-l">{l}</span></div>' for v, l in items
    )
    return f'<div class="stat4">{cells}</div>'


def r_cards(items):
    cells = "".join(
        f'<a class="card" href="{h}"><span class="card-t">{t}</span>'
        f'<span class="card-d">{d}</span></a>' for h, t, d in items
    )
    return f'<div class="cards">{cells}</div>'


def r_cite(text, lang):
    ch = C.CHROME[lang]
    return ('<figure class="cite">'
            f'<blockquote class="cite-q">{html.escape(text)}</blockquote>'
            f'<button class="cite-btn" type="button" data-copy="{html.escape(text, quote=True)}" '
            f'data-copied="{ch["copied"]}">{ch["copy"]}</button></figure>')


def r_bars(title, pairs, note):
    top = max(v for _, v in pairs) or 1
    rows = "".join(
        f'<div class="bar-row"><span class="bar-l">{html.escape(str(k))}</span>'
        f'<span class="bar-track"><span class="bar-fill" style="width:{v / top * 100:.2f}%"></span></span>'
        f'<span class="bar-v">{v:,}</span></div>'
        for k, v in pairs
    )
    n = f'<p class="bar-note">{note}</p>' if note else ""
    return (f'<figure class="bars"><figcaption class="bar-title">{title}</figcaption>'
            f'<div class="bar-set">{rows}</div>{n}</figure>')


def r_note(text):
    return f'<aside class="note"><p>{text}</p></aside>'


def r_gate(rows):
    cells = "".join(
        f'<div class="gate-row" data-on="{str(bool(v)).lower()}">'
        f'<span class="gate-k">{html.escape(k)}</span>'
        f'<span class="gate-v">{"true" if v else "false"}</span></div>'
        if isinstance(v, bool) else
        f'<div class="gate-row" data-on="class">'
        f'<span class="gate-k">{html.escape(k)}</span>'
        f'<span class="gate-v">{html.escape(str(v))}</span></div>'
        for k, v in rows
    )
    return f'<div class="gate">{cells}</div>'


CHAIN_LABELS = {
    "en": [("proposal", "proposed against a named base manifest"),
           ("review", "two independent approvals"),
           ("promotion", "receipt issued at threshold"),
           ("manifest", "generation 2 becomes public"),
           ("citation", "citable, with its own hash")],
    "zh": [("提案", "針對具名基底清單提出"),
           ("審查", "兩份獨立核准"),
           ("晉升", "達門檻後簽發收據"),
           ("清單", "第二世代成為公開"),
           ("引用", "可被引用，並有自身雜湊")],
}


def r_chain(lang):
    steps = "".join(
        f'<li class="chain-step"><span class="chain-n">{i + 1}</span>'
        f'<span class="chain-t">{t}</span><span class="chain-d">{d}</span></li>'
        for i, (t, d) in enumerate(CHAIN_LABELS[lang])
    )
    return f'<ol class="chain">{steps}</ol>'


def r_reviews(lang):
    cells = ""
    for r in C.G["reviews"]:
        findings = "".join(f"<li>{html.escape(f)}</li>" for f in r["findings"])
        cells += (
            f'<div class="rev"><div class="rev-head">'
            f'<span class="rev-who">{html.escape(r["reviewer_id"])}</span>'
            f'<span class="rev-dec">{html.escape(r["decision"])}</span></div>'
            f'<ul class="rev-find">{findings}</ul>'
            f'<code class="rev-h">{r["document_sha256"][:24]}…</code></div>'
        )
    return f'<div class="revs">{cells}</div>'


SPLIT_T = {
    "en": {"sent": "sent", "got": "returned", "cost": "cost", "reached": "shards read"},
    "zh": {"sent": "送出", "got": "回傳", "cost": "成本", "reached": "讀取分片"},
}


def r_split(lang):
    t = SPLIT_T[lang]
    return (
        '<div class="split">'
        f'<div class="split-col split-bad"><div class="split-tag">{t["sent"]}</div>'
        f"<pre><code>{html.escape(C.DENIED_QUERY)}</code></pre></div>"
        f'<div class="split-col"><div class="split-tag">{t["got"]}</div>'
        f"<pre><code>{html.escape(C.DENIED_RESPONSE)}</code></pre></div>"
        "</div>"
        f'<div class="split-foot"><span>{t["cost"]}: 0</span>'
        f'<span>{t["reached"]}: 0</span></div>'
    )


PROV_T = {
    "en": ("dataset", "workflow", "output", "environment"),
    "zh": ("資料集", "工作流", "輸出", "環境"),
}


def r_provenance(lang):
    d, w, o, e = PROV_T[lang]
    env = C.B["environment"]
    return (
        '<div class="prov">'
        f'<div class="prov-cell"><span class="prov-k">{d}</span>'
        f'<code class="prov-v">{C.MANIFEST[:20]}…</code></div>'
        f'<div class="prov-cell"><span class="prov-k">{w}</span>'
        f'<code class="prov-v">{C.WF_SHA[:20]}…</code></div>'
        f'<div class="prov-cell"><span class="prov-k">{o}</span>'
        f'<code class="prov-v">{C.OUT_SHA[:20]}…</code></div>'
        f'<div class="prov-cell"><span class="prov-k">{e}</span>'
        f'<code class="prov-v">Python {env["python"]} · NumPy {env["numpy"]}</code></div>'
        "</div>"
    )


def render_blocks(blocks, lang):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h2":
            out.append(r_h2(b[1], b[2]))
        elif kind == "p":
            out.append(r_p(b[1]))
        elif kind == "ul":
            out.append(r_ul(b[1]))
        elif kind == "kv":
            out.append(r_kv(b[1]))
        elif kind == "code":
            out.append(r_code(b[1], b[2]))
        elif kind == "table":
            out.append(r_table(b[1], b[2]))
        elif kind == "chips":
            out.append(r_chips(b[1]))
        elif kind == "chips_off":
            out.append(r_chips(b[1], off=True))
        elif kind == "stat4":
            out.append(r_stat4(b[1]))
        elif kind == "cards":
            out.append(r_cards(b[1]))
        elif kind == "cite":
            out.append(r_cite(b[1], lang))
        elif kind == "bars":
            out.append(r_bars(b[1], b[2], b[3]))
        elif kind == "note":
            out.append(r_note(b[1]))
        elif kind == "gate":
            out.append(r_gate(b[1]))
        elif kind == "chain":
            out.append(r_chain(b[1]))
        elif kind == "reviews":
            out.append(r_reviews(b[1]))
        elif kind == "split":
            out.append(r_split(b[1]))
        elif kind == "provenance":
            out.append(r_provenance(b[1]))
        else:
            raise SystemExit(f"unknown block: {kind}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# hero
# --------------------------------------------------------------------------

HERO_T = {
    "en": {
        "in": "crosses the boundary",
        "out": "never crosses",
        "in_items": ["a density", "a quantile", "a histogram", "a count",
                     "a manifest hash", "an audit event"],
        "out_items": ["a target integer", "an RSA modulus", "a factor",
                      "a factor candidate", "a narrowed range", "a prime list"],
        "guard": "guard",
        "note": "The guard runs before the data layer. A refused request costs nothing, "
                "reads nothing, and is still recorded.",
    },
    "zh": {
        "in": "可跨過邊界",
        "out": "永不跨過",
        "in_items": ["密度", "分位數", "直方圖", "計數", "清單雜湊", "稽核事件"],
        "out_items": ["目標整數", "RSA modulus", "因數",
                      "因數候選", "縮減後的範圍", "質數列表"],
        "guard": "守衛",
        "note": "守衛跑在資料層之前。被拒的請求不花成本、"
                "不讀取任何東西，而且依然被記錄下來。",
    },
}


def render_hero(lang):
    t = HERO_T[lang]
    ins = "".join(f'<li class="bd-item">{html.escape(i)}</li>' for i in t["in_items"])
    outs = "".join(f'<li class="bd-item">{html.escape(i)}</li>' for i in t["out_items"])
    return f"""<section class="bd" aria-label="{t['guard']}">
  <div class="bd-side bd-in">
    <h2 class="bd-h">{t['in']}</h2>
    <ul class="bd-list">{ins}</ul>
  </div>
  <div class="bd-wall" aria-hidden="true"><span class="bd-wall-t">{t['guard']}</span></div>
  <div class="bd-side bd-out">
    <h2 class="bd-h">{t['out']}</h2>
    <ul class="bd-list">{outs}</ul>
  </div>
</section>
<p class="bd-note">{t['note']}</p>"""


# --------------------------------------------------------------------------
# shell
# --------------------------------------------------------------------------

def render_page(lang, slug):
    page = C.PAGES[lang][slug]
    ch = C.CHROME[lang]
    other = "zh" if lang == "en" else "en"
    here = C.SITE["origin"] + url_path(lang, slug)
    there = url_path(other, slug)

    nav = "".join(
        '<a class="bar-link" href="{h}"{c}>{l}</a>'.format(
            h=url_path(lang, s), l=label,
            c=' aria-current="page"' if s == slug else "")
        for s, label in ch["nav"]
    )

    items = [(b[2], b[1]) for b in page["blocks"] if b[0] == "h2"]
    if items:
        links = "".join(
            f'<li><a class="toc-link" data-toc-link href="#{a}">{l}</a></li>'
            for a, l in items
        )
        toc = (f'<nav class="toc" aria-label="{ch["on_this_page"]}">'
               f'<h2 class="toc-title">{ch["on_this_page"]}</h2>'
               f'<ul class="toc-list">{links}</ul></nav>')
    else:
        toc = '<div class="toc"></div>'

    hero = render_hero(lang) if page.get("hero") == "boundary" else ""
    fonts = FONTS_BASE + (FONTS_ZH if lang == "zh" else "") + "&display=swap"

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "MMRF Public Prime Lake",
        "version": C.SITE["version"],
        "url": here,
        "description": page["description"],
        "inLanguage": ch["lang"],
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "creator": {"@type": "Organization", "name": "EveMissLab", "url": C.SITE["lab"]},
        "identifier": C.CIT["citation_id"],
        "isAccessibleForFree": True,
        "variableMeasured": ["prime density", "prime gaps", "residue distribution",
                             "prime families"],
    }

    return f"""<!doctype html>
<html lang="{ch['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page['meta_title'])}</title>
<meta name="description" content="{html.escape(page['description'])}">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{C.SITE['origin'] + url_path('en', slug)}">
<link rel="alternate" hreflang="zh-Hant" href="{C.SITE['origin'] + url_path('zh', slug)}">
<link rel="alternate" hreflang="x-default" href="{C.SITE['origin'] + url_path('en', slug)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MMRF">
<meta property="og:title" content="{html.escape(page['meta_title'])}">
<meta property="og:description" content="{html.escape(page['description'])}">
<meta property="og:url" content="{here}">
<meta property="og:locale" content="{'zh_TW' if lang == 'zh' else 'en_US'}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f4f2ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#101418" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="/assets/styles.css">
{THEME_BOOT}
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{ch['skip']}</a>

<header class="bar">
  <div class="bar-in">
    <a class="bar-mark" href="{url_path(lang, '')}">MMRF
      <span class="bar-ver">{C.SITE['version']}</span></a>
    <nav class="bar-nav" aria-label="MMRF">{nav}</nav>
    <div class="bar-tools">
      <a class="bar-btn" href="{there}" hreflang="{'zh-Hant' if other == 'zh' else 'en'}" title="{ch['lang_switch_title']}">{ch['lang_switch']}</a>
      <button class="bar-btn" type="button" data-theme-toggle aria-label="{ch['theme']}">&#9681;</button>
    </div>
  </div>
</header>

<main id="main">
  <div class="shell">
    <div class="mast">
      <p class="mast-eyebrow">{html.escape(page['title'])}</p>
      <h1 class="mast-display">{html.escape(page['display'])}</h1>
      <p class="mast-stand">{page['standfirst']}</p>
    </div>
    {hero}
  </div>

  <div class="shell body">
    <div class="body-grid">
      {toc}
      <div class="flow">
{render_blocks(page['blocks'], lang)}
      </div>
    </div>
  </div>
</main>

<footer class="foot">
  <div class="shell foot-grid">
    <p class="foot-note">{ch['footer_note']}</p>
    <div class="foot-meta">
      <span class="foot-line">MMRF {C.SITE['version']} &middot; {ch['footer_release']}</span>
      <span class="foot-line">{C.SITE['licence']}</span>
      <span class="foot-line"><a href="{C.SITE['repo']}" rel="noopener">{ch['repo_link']}</a></span>
      <span class="foot-line"><a href="{C.SITE['lab']}" rel="noopener">{ch['footer_lab']}</a></span>
    </div>
  </div>
</footer>

<script src="/assets/app.js" defer></script>
</body>
</html>
"""


def render_404():
    ch = C.CHROME["en"]
    fonts = FONTS_BASE + "&display=swap"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Not found — MMRF</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="/assets/styles.css">
{THEME_BOOT}
</head>
<body>
<header class="bar"><div class="bar-in">
  <a class="bar-mark" href="/">MMRF <span class="bar-ver">{C.SITE['version']}</span></a>
</div></header>
<main class="shell gone">
  <p class="mast-eyebrow">404</p>
  <h1 class="mast-display">Nothing is registered at this address.</h1>
  <p class="mast-stand">Which is the same answer this dataset gives to most questions.
    Start from the <a href="/">overview</a>, or read the
    <a href="/safety/">boundary</a>.</p>
</main>
<footer class="foot"><div class="shell foot-grid">
  <p class="foot-note">{ch['footer_note']}</p>
</div></footer>
</body>
</html>
"""


def render_sitemap():
    urls = []
    for lang in ("en", "zh"):
        for slug in C.SLUGS:
            loc = C.SITE["origin"] + url_path(lang, slug)
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{h}" '
                f'href="{C.SITE["origin"] + url_path(l, slug)}"/>'
                for h, l in (("en", "en"), ("zh-Hant", "zh"), ("x-default", "en"))
            )
            urls.append(f"<url><loc>{loc}</loc>"
                        f"<lastmod>{C.SITE['updated']}</lastmod>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(urls) + "</urlset>\n")


# --------------------------------------------------------------------------
# machine-readable layer
# --------------------------------------------------------------------------

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def write_machine_layer():
    origin = C.SITE["origin"]

    write_json(DIST / ".well-known" / "mmrf.json", {
        "schema": "mmrf-public-site-1.0",
        "release_id": C.F["release_id"],
        "stable_manifest_sha256": C.MANIFEST,
        "query_surface": "aggregate-only",
        "target_conditioned_queries": False,
        "rsa_target_endpoint": False,
        "factor_candidate_endpoint": False,
        "range_narrowing_endpoint": False,
        "site": origin,
        "runtime_repository": C.SITE["repo"],
        "licence": C.SITE["licence"],
    })

    write_json(DIST / "datasets" / "index.json", {
        "schema": "mmrf-site-datasets-1.0",
        "datasets": [{
            **C.D,
            "citation_id": C.CIT["citation_id"],
            "documentation": f"{origin}/datasets/",
        }],
    })

    write_json(DIST / "workflows" / "index.json", {
        "schema": "mmrf-site-workflows-1.0",
        "workflows": [
            {
                "workflow_id": "stable-baseline",
                "workflow_version": "1.0.0",
                "workflow_sha256": C.WF_SHA,
                "dataset_manifest_sha256": C.MANIFEST,
                "expected_output_sha256": C.OUT_SHA,
                "replayable_from_release": True,
                "safety_classification": "L0_PUBLIC_MATH",
                "result": f"{origin}/results/stable-baseline.json",
            },
            {
                "workflow_id": "prime-distribution-baseline",
                "dataset_manifest_sha256": C.MANIFEST,
                "replayable_from_release": False,
                "reason": ("the data-lake index and generation-1 lake shards are not "
                           "part of the v1.0 package"),
                "safety_classification": "L0_PUBLIC_MATH",
            },
        ],
    })

    write_json(DIST / "governance" / "proposals.json", {
        "schema": "mmrf-site-governance-1.0",
        **C.G,
    })

    write_json(DIST / "citations" / "index.json", {
        "schema": "mmrf-site-citations-1.0",
        "citations": [C.CIT],
    })

    write_json(DIST / "results" / "stable-baseline.json", C.B)

    (DIST / "llms.txt").write_text(f"""# MMRF

> Multidirectional Matrix Research Infrastructure. A public dataset of
> mathematical properties of the {C.D['prime_count']:,} primes below
> {C.D['limit_exclusive']:,}, with an aggregate-only query surface.

MMRF answers aggregate questions about a fixed range of primes: densities,
gap quantiles and histograms, residue distributions, prime family counts.

It does not accept an externally supplied integer of any kind, does not return
factors or factor candidates, does not narrow search ranges, and does not store
relations between composites and their factors. These are enforced by a guard
that runs before the data layer, not by a usage policy. Do not ask this site,
or its data, to help factor a number — there is no path that answers.

## Facts

- Release: {C.F['release_id']}
- Dataset: {C.D['dataset_id']}, generation {C.D['generation']}
- Records: {C.D['prime_count']:,} primes in {C.D['shard_count']} immutable shards
- Range: [0, {C.D['limit_exclusive']:,})
- Stable manifest sha256: {C.MANIFEST}
- Baseline output sha256: {C.OUT_SHA}
- Licence: Apache-2.0

## Machine-readable

- {origin}/.well-known/mmrf.json
- {origin}/datasets/index.json
- {origin}/workflows/index.json
- {origin}/governance/proposals.json
- {origin}/citations/index.json
- {origin}/results/stable-baseline.json

## Pages

- {origin}/ — overview
- {origin}/research/ — measured aggregates with replay instructions
- {origin}/datasets/ — schema, columns, provenance, citation
- {origin}/workflows/ — workflow registry and expected hashes
- {origin}/governance/ — proposal, reviews, promotion receipt
- {origin}/verification/ — reproduce every hash yourself
- {origin}/safety/ — the refusal boundary and how it is enforced
- {origin}/documentation/ — specifications and schemas
- {origin}/about/ — the 3M series

Traditional Chinese: same paths under {origin}/zh/
""", encoding="utf-8")

    (DIST / "agents.md").write_text(f"""# Notes for agents

MMRF is a static, public mathematical dataset. Everything here can be read
without authentication and without executing anything.

## You may

- Read any page, and any JSON under `/datasets/`, `/workflows/`,
  `/governance/`, `/citations/`, `/results/` and `/.well-known/`.
- Cite the dataset using the record at `/citations/index.json`.
- Reproduce every published figure by cloning {C.SITE['repo']} and running
  `python workflows/stable_baseline.py --project-root .`. Expected output
  sha256: `{C.OUT_SHA}`.
- Verify the dataset independently: the shards are plain NumPy `.npz` archives
  and the manifest hash is the SHA-256 of the manifest's canonical JSON with
  the `manifest_sha256` field removed.

## You may not, and asking differently will not help

- Supply a target integer, an RSA modulus, or any number to be analysed.
  Seventeen field names are refused before a request is parsed further.
- Request a factor, a factor candidate, a narrowed search range, a nearest
  prime, or a raw prime list.
- Compose permitted aggregate queries in order to reconstruct any of the above.

There is no endpoint for these and no configuration that enables one. The
refusal is a guard ahead of the data layer, so a refused request never reads a
shard. Refusals are recorded as hashed audit events.

## If you are summarising this project

The accurate one-line description is: a public prime dataset defined as much by
the questions it refuses as by the ones it answers. It is not a factorization
service, and it is not a step toward one.
""", encoding="utf-8")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    counts = {}
    for lang in ("en", "zh"):
        n = 0
        for slug in C.SLUGS:
            if slug not in C.PAGES[lang]:
                raise SystemExit(f"missing page: {lang}/{slug or 'index'}")
            target = out_file(lang, slug)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_page(lang, slug), encoding="utf-8")
            n += 1
        counts[lang] = n

    if counts["en"] != counts["zh"]:
        raise SystemExit(f"language trees differ in size: {counts}")

    assets = DIST / "assets"
    assets.mkdir()
    for name in ("styles.css", "app.js"):
        shutil.copyfile(ROOT / "src" / "assets" / name, assets / name)

    (DIST / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (DIST / "404.html").write_text(render_404(), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(render_sitemap(), encoding="utf-8")
    (DIST / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {C.SITE['origin']}/sitemap.xml\n",
        encoding="utf-8")

    write_machine_layer()

    print(f"built {counts['en']} + {counts['zh']} pages into {DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
