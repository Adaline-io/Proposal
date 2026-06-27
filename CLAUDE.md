# CLAUDE.md — Adaline Proposals

Operational brief for this repo. Read this before touching anything.

**Owner:** Adaline (Myadaline Communications LLP, Calicut).
**What this is:** the single consolidated home for **every** Adaline client
proposal. Team-facing directory at the root, client-facing proposal pages per
client folder. Replaces the old one-repo-per-proposal sprawl.

---

## Architecture

```
/
├── index.html              # TEAM-FACING directory (internal, noindex). Cards, newest-first.
├── <client-slug>/index.html# CLIENT-FACING proposal — one self-contained static file.
├── .nojekyll               # serve underscored dirs as-is; no Jekyll processing
├── .github/workflows/pages.yml   # GitHub Pages deploy (rebuilds, verifies sync, deploys)
└── _build/                 # the build system (Python, stdlib only)
    ├── template.py         # the canonical reusable builder (CSS/JS/render). Edit with care.
    ├── build_<client>.py   # one per client — pure DATA dict, calls template.build()
    ├── build_index.py      # renders the root team directory from clients.json
    ├── build_all.py        # builds every proposal + the index
    ├── clients.json        # registry that drives the root directory (newest-first)
    └── assets/             # Adaline wordmark + three signs (+ ○ ×), PNG, embedded as base64
```

**Routing model (mirrors Adaline-io/Onboarding):**
- Root `index.html` = internal directory. `<meta noindex>`. One card per proposal,
  **newest-first**, each linking to `./<client-slug>/`. Never send a client the root.
- `<client-slug>/index.html` = the page you send the client. Self-contained.

---

## Build

Pure Python standard library — no pip install, no node, no frameworks.

```bash
python3 _build/build_all.py          # build everything
python3 _build/build_rocafuel.py     # build one proposal
python3 _build/build_index.py        # rebuild the root directory only
```

Output HTML is committed to the repo (proposals are pre-built static). CI re-runs
the builder and **fails if committed output drifts** from the source data — so
always rebuild and commit after editing a `build_*.py` or `template.py`.

---

## Add a new proposal

When a lead closes, the Management sends: client name, project, total, deposit,
accent colour, payment split, custom sections.

1. Copy `_build/build_rocafuel.py` to `_build/build_<slug>.py`. It's the gold
   reference — keep its section order and tone.
2. Fill in the `DATA` dict: hero, brief, build tabs, process, timeline,
   investment (with the bundle calculator rows), agency, optional legal.
3. Set the per-client `palette` (see Accent below). **Ask before choosing an
   accent** — it's a brand decision.
4. Register it: add `"build_<slug>"` to `CLIENT_MODULES` in `build_all.py` and a
   card entry to `clients.json` (newest-first is by `date` descending).
5. `python3 _build/build_all.py`, eyeball the output, commit.
6. Open a PR and **ask the Management to review before it's treated as
   client-ready.** Nothing ships to a client unreviewed.

---

## Brand system (do not break)

- **Single-file static HTML** per proposal. All CSS/JS/assets inlined (assets as
  base64). No frameworks, no external deps, **no analytics / tracking pixels**.
  Vanilla JS only. The one external link is Google Fonts (same as canonical).
- **Dark theme:** `#0b0b0b` paper, `#f5f1ea` ink.
- **Fonts:** Space Grotesk (display), Inter (body), JetBrains Mono (utility).
- **Accent:** per client, via the `palette` token in each `build_*.py`. The four
  hue vars (`--red --yellow --green --blue`) collapse to the accent; `--yellow`
  is the primary interactive accent. **Roca Fuels = black & white** (monochrome:
  hues set to ink / soft-ink). Ask the Management before setting any accent.
- **Voice = "the Management".** Never put internal names in client-facing copy.
- **Primary CTA = gaming language:** `HIT START →` closes every proposal (mailto).
- **Period-style display headlines.** Vary sentence rhythm — avoid back-to-back
  matched-pair "X. Y." lines.
- **Close every proposal** with the three Adaline signs (+ ○ ×) + wordmark +
  contact: `bettercall@myadaline.com` / WhatsApp `+91 90481 91616` /
  `GSTIN 32ABYFM6787D1ZN`. (Centralised in `template.py` `CONTACT` and `_close()`.)

---

## Canonical style source

`Adaline-BC/Rocafuels_proposal` (the GitHub one) is the canonical reference. The
**old Vercel version (roca-proposal-engine.vercel.app) is outdated — ignore it.**
`template.py` was distilled directly from the canonical: section structure, copy
tone, the investment/bundle-calculator layout, the legal accordion, the close.

### Open reconciliation note
The canonical Roca close ends with *"Thank You." → copy-email*, with **no**
`HIT START →` button. The brand brief lists `HIT START →` as the close CTA, so the
template adds it as the primary CTA above the copy-email affordance. If the
Management prefers the pure-canonical close, remove `.cta-start` from `_close()`.

---

## Status of the entries

| Slug         | Source repo                     | Accent | Status |
|--------------|----------------------------------|--------|--------|
| `rocafuel`   | Adaline-BC/Rocafuels_proposal    | B&W (`#f5f1ea`) | **Migrated** — verbatim, monochrome |
| `bz-fitness` | Adaline-io/Bz-fitness-proposal   | Red-orange (`#ff4d2e`) | **Migrated** — Kuwait fitness catalog |
| `vertex`     | Adaline-io/vertex-proposal       | Gold (`#c9a862`) | **Migrated** — Vertex PRO web build (static investment) |
| `roca-app`   | Adaline-BC/Roca-Proposal         | Gold (`#d4a853`) | **Migrated** — ROCA Group feasibility study (AED, static investment) |

All four are migrated from their real source repos (fetched over public HTTPS;
the four reference repos are outside this session's GitHub MCP scope). **They
still need a Management review before being sent to a client** — confirm the
two per-client accents flagged above (Vertex / roca-app both gold) and the copy.
The `draft_note` banner mechanism remains in `template.py` for any future
placeholder.

---

## Deploy

GitHub Pages via `.github/workflows/pages.yml` on push to `main`. It rebuilds,
verifies the committed output matches, then deploys the whole repo (root + client
folders). `.nojekyll` keeps `_build/` from being processed.
