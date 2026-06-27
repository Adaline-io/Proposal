"""
Team-facing root directory (index.html).

Internal, <meta noindex>. One card per client proposal, NEWEST-FIRST (sorted by
`date` descending, then name). Each card links to ./<slug>/. Self-contained:
Adaline wordmark inlined as base64, same brand fonts/colours as the proposals.

Run:  python3 _build/build_index.py
"""

import json
import os

import template as T

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def _load():
    with open(os.path.join(HERE, "clients.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    clients = [c for c in data["clients"] if not c.get("slug", "").startswith("_")]
    # Newest-first: date descending, then name ascending.
    clients.sort(key=lambda c: (c.get("date", ""), ), reverse=True)
    clients.sort(key=lambda c: c.get("name", "").lower())
    clients.sort(key=lambda c: c.get("date", ""), reverse=True)
    return clients


CSS = r"""
:root{
  --paper:#0b0b0b;--paper-2:#141414;--paper-3:#1c1c1c;
  --ink:#f5f1ea;--ink-soft:#d8d3cc;--muted:#807a72;--muted-2:#56524c;
  --line:#262626;--line-2:#363636;
  --display:'Space Grotesk',system-ui,sans-serif;
  --mono:'JetBrains Mono',monospace;--body:'Inter',system-ui,sans-serif;
  --pad:clamp(20px,5vw,48px);--maxw:1080px;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:15.5px;line-height:1.6;-webkit-font-smoothing:antialiased;min-height:100vh}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 var(--pad)}
header{border-bottom:1px solid var(--line);padding:36px 0 28px}
header .top{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;flex-wrap:wrap}
header .wm img{height:30px;width:auto;filter:brightness(0) invert(1) opacity(.9);display:block}
header .badge{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line-2);border-radius:3px;padding:6px 12px}
header h1{font-family:var(--display);font-size:clamp(34px,6vw,64px);font-weight:800;letter-spacing:-.03em;line-height:1;margin:32px 0 14px}
header .sub{font-family:var(--mono);font-size:12.5px;color:var(--muted);letter-spacing:.04em;max-width:620px}
header .sub strong{color:var(--ink-soft);font-weight:600}
.meta-row{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase;margin-top:22px;display:flex;gap:18px;flex-wrap:wrap}
.meta-row span strong{color:var(--ink)}
main{padding:40px 0 80px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.card{position:relative;display:flex;flex-direction:column;background:var(--paper-2);border:1px solid var(--line);border-radius:6px;padding:26px 24px;text-decoration:none;color:inherit;transition:border-color .2s,transform .2s,background .2s;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--accent,#f5f1ea)}
.card:hover{border-color:var(--line-2);transform:translateY(-3px);background:var(--paper-3)}
.card .ct{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:18px}
.card .num{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.12em}
.card .status{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;padding:4px 9px;border-radius:3px;font-weight:700}
.card .status.ready{background:rgba(61,212,131,.14);color:#7fe3ab;border:1px solid rgba(61,212,131,.3)}
.card .status.draft{background:rgba(128,122,114,.14);color:var(--muted);border:1px solid var(--line-2)}
.card h2{font-family:var(--display);font-size:26px;font-weight:700;letter-spacing:-.02em;margin:0 0 8px;line-height:1.1}
.card p{font-size:13.5px;color:var(--muted);margin:0 0 20px;line-height:1.5;flex:1}
.card .foot{display:flex;justify-content:space-between;align-items:center;font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.06em;border-top:1px solid var(--line);padding-top:14px}
.card .foot .open{color:var(--ink-soft);display:inline-flex;align-items:center;gap:6px;transition:gap .2s}
.card:hover .foot .open{gap:10px;color:var(--ink)}
.card .swatch{display:inline-flex;align-items:center;gap:7px}
.card .swatch i{width:11px;height:11px;border-radius:50%;background:var(--accent,#f5f1ea);display:inline-block;border:1px solid rgba(255,255,255,.15)}
footer{border-top:1px solid var(--line);padding:28px 0 48px;font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.06em;line-height:1.8}
footer strong{color:var(--ink-soft)}
@media(max-width:520px){.grid{grid-template-columns:1fr}}
"""


def _card(i, c):
    status = c.get("status", "draft")
    status_label = "Client-ready" if status == "ready" else "Draft"
    return (
        '<a class="card" href="./%s/" style="--accent:%s">'
        '<div class="ct"><span class="num">%02d</span>'
        '<span class="status %s">%s</span></div>'
        '<h2>%s</h2><p>%s</p>'
        '<div class="foot"><span class="swatch"><i></i>%s</span>'
        '<span class="open">Open &rarr;</span></div></a>'
        % (T.e(c["slug"]), T.e(c.get("accent", "#f5f1ea")), i + 1,
           T.e(status), T.e(status_label),
           T.e(c["name"]), T.e(c.get("tagline", "")),
           T.e(c.get("date", "—")))
    )


def render():
    clients = _load()
    wm = T._data_uri("wordmark.png")
    cards = "".join(_card(i, c) for i, c in enumerate(clients))
    ready = sum(1 for c in clients if c.get("status") == "ready")
    draft = sum(1 for c in clients if c.get("status") == "draft")
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="theme-color" content="#0b0b0b">\n'
        '<meta name="robots" content="noindex,nofollow">\n'
        '<title>Adaline · Proposals (Internal)</title>\n'
        '<meta name="description" content="Internal proposal directory — Adaline.">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
        '&family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700;800'
        '&display=swap" rel="stylesheet">\n'
        '<style>%s</style>\n</head>\n<body>\n'
        '<header><div class="wrap"><div class="top">'
        '<div class="wm"><img src="%s" alt="Adaline"></div>'
        '<div class="badge">Internal · Team-facing</div></div>'
        '<h1>Proposals.</h1>'
        '<div class="sub">The consolidated home for every Adaline client proposal. '
        'Pick a client to open their proposal. <strong>This directory is internal '
        '(noindex)</strong> — client links are the per-client pages only.</div>'
        '<div class="meta-row"><span><strong>%d</strong> total</span>'
        '<span><strong>%d</strong> client-ready</span>'
        '<span><strong>%d</strong> draft</span>'
        '<span>Ordered newest-first</span></div>'
        '</div></header>\n'
        '<main><div class="wrap"><div class="grid">%s</div></div></main>\n'
        '<footer><div class="wrap">'
        '<strong>%s</strong> &middot; %s<br/>'
        '%s &middot; WhatsApp %s &middot; %s'
        '</div></footer>\n</body>\n</html>\n'
        % (CSS, wm, len(clients), ready, draft, cards,
           T.CONTACT["legal_name"], T.CONTACT["place"],
           T.CONTACT["email"], T.CONTACT["whatsapp"], T.CONTACT["gstin"])
    )


def build():
    out = os.path.join(REPO, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render())
    return out


if __name__ == "__main__":
    print("Built:", build())
