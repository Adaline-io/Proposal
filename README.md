# Adaline · Proposals

The consolidated home for every Adaline client proposal — one repo, team-facing
directory plus client-facing pages, replacing the old repo-per-proposal sprawl.

Built and maintained by **Adaline** (Myadaline Communications LLP, Calicut).

## What's here

- **`index.html`** — internal, team-facing directory (`noindex`). One card per
  proposal, newest-first, linking to each client page. Don't send this to clients.
- **`<client-slug>/index.html`** — the client-facing proposal. A single
  self-contained static HTML file: all CSS, JS, and brand assets inlined, no
  frameworks, no external dependencies, no tracking. This is the link a client gets.
- **`_build/`** — the Python build system (standard library only): the reusable
  `template.py`, one `build_<client>.py` data file per proposal, the `clients.json`
  registry, and the brand `assets/`.

## Build

```bash
python3 _build/build_all.py
```

No dependencies to install. Output is committed to the repo and deployed to
GitHub Pages on push to `main` (see `.github/workflows/pages.yml`).

## Proposals

| Client      | Page                  | Status        |
|-------------|-----------------------|---------------|
| Roca Fuels  | `./rocafuel/`         | Client-ready  |
| BZ Fitness  | `./bz-fitness/`       | Draft         |
| Vertex      | `./vertex/`           | Draft         |

See **[CLAUDE.md](./CLAUDE.md)** for the operational brief: architecture, the
brand system, how to add a proposal, and the canonical style source.

---

**Contact:** bettercall@myadaline.com · WhatsApp +91 90481 91616 · GSTIN 32ABYFM6787D1ZN
