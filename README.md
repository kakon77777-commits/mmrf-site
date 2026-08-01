# mmrf-site

Source for [mmrf.evemisslab.com](https://mmrf.evemisslab.com) — the public site
for MMRF, the Multidirectional Matrix Research Infrastructure.

## Build

```bash
python sync_facts.py    # pull figures out of ../mmrf-runtime's artifacts
python build.py         # render dist/
npx wrangler deploy     # publish
```

No dependencies beyond the Python standard library. English at the root,
Traditional Chinese under `/zh/`; the build fails if a page is missing from
either tree, or if the two trees come out different sizes.

## Why sync_facts.py exists

Every count, hash, density and governance record on the site is read from the
runtime's own artifacts at build time. `sync_facts.py` verifies the stable
manifest and the baseline output against their own recorded hashes before
writing anything, and refuses to write if either fails — so a figure on the page
cannot quietly drift away from the artifact it claims to describe.

## Machine-readable layer

Generated from the same facts as the HTML, so a crawler and a reader cannot be
told different things:

- `/.well-known/mmrf.json`
- `/datasets/index.json`
- `/workflows/index.json`
- `/governance/proposals.json`
- `/citations/index.json`
- `/results/stable-baseline.json`
- `/llms.txt`, `/agents.md`

## Licence

Apache-2.0.
