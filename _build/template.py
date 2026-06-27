"""
Adaline proposal builder — the canonical reusable template.

Distilled from Adaline-BC/Rocafuels_proposal (the GitHub canonical, NOT the old
Vercel version). Renders a single self-contained static HTML proposal: all CSS,
JS, fonts-by-link and brand assets (base64) inlined. No frameworks, no external
deps, no analytics/tracking. Vanilla JS only.

A proposal is described as a plain Python dict (see build_rocafuel.py for the
canonical reference instance). Future proposals are pure data — same structure,
same tone, same investment layout, same CTA, per-client accent.

Brand system (do not break):
  paper #0b0b0b · ink #f5f1ea · Space Grotesk (display) / Inter (body) /
  JetBrains Mono (utility). Per-client accent via the palette block. Voice is
  "the Management" — never internal names in client-facing copy. Close every
  proposal with the three Adaline signs (+ o x) + wordmark + contact.
"""

import base64
import html
import os

ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Contact block — constant across every Adaline proposal.
CONTACT = {
    "email": "bettercall@myadaline.com",
    "whatsapp": "+91 90481 91616",
    "gstin": "GSTIN 32ABYFM6787D1ZN",
    "place": "Calicut, Kerala",
    "legal_name": "Myadaline Communications LLP",
}


# --------------------------------------------------------------------------- #
#  Assets
# --------------------------------------------------------------------------- #
def _data_uri(filename):
    with open(os.path.join(ASSET_DIR, filename), "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    return "data:image/png;base64," + b64


def _assets():
    return {
        "plus": _data_uri("sign-plus.png"),
        "circle": _data_uri("sign-circle.png"),
        "cross": _data_uri("sign-cross.png"),
        "wordmark": _data_uri("wordmark.png"),
    }


def e(s):
    """Escape plain text for HTML."""
    return html.escape(str(s), quote=True)


# --------------------------------------------------------------------------- #
#  CSS — verbatim canonical, with per-client tokens __PALETTE__ / __BODYGLOW__
# --------------------------------------------------------------------------- #
CSS = r"""
:root{
  --paper:#0b0b0b;--paper-2:#141414;--paper-3:#1c1c1c;--paper-4:#242424;
  --ink:#f5f1ea;--ink-soft:#d8d3cc;--muted:#807a72;--muted-2:#56524c;
  --line:#262626;--line-2:#363636;
  __PALETTE__
  --cream:#f5f1ea;
  --display:'Space Grotesk',system-ui,sans-serif;
  --mono:'JetBrains Mono','Space Mono',monospace;
  --body:'Inter','Space Grotesk',system-ui,sans-serif;
  --pad:clamp(20px,5vw,48px);--maxw:1080px;
  --nav-h:54px;
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html{scroll-behavior:smooth;scroll-padding-top:var(--nav-h)}
body{margin:0;background:__BODYGLOW__,var(--paper);color:var(--ink);font-family:var(--body);font-size:15.5px;line-height:1.65;-webkit-font-smoothing:antialiased;min-height:100vh;overflow-x:hidden}
::selection{background:var(--yellow);color:var(--paper)}
:focus-visible{outline:2px solid var(--yellow);outline-offset:2px;border-radius:2px}
button:focus-visible{outline-offset:4px}

/* SCROLL PROGRESS */
.scroll-progress{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,var(--yellow),var(--green));width:0%;z-index:60;transition:width .1s ease}

/* TOPNAV */
.topnav{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(11,11,11,.85);backdrop-filter:blur(16px) saturate(150%);-webkit-backdrop-filter:blur(16px) saturate(150%);border-bottom:1px solid var(--line);height:var(--nav-h);display:flex;align-items:center;justify-content:space-between;padding:0 var(--pad);font-family:var(--mono);font-size:11.5px;letter-spacing:.04em}
.topnav .ntag{color:var(--ink);font-weight:600;letter-spacing:.08em;text-transform:uppercase;display:flex;align-items:center;gap:10px;min-width:0;flex:1}
.topnav .ntag .ntag-main{flex-shrink:0}
.topnav .ntag .sep{color:var(--muted-2);flex-shrink:0}
.topnav .ntag .small{color:var(--muted);font-weight:400;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.topnav .nlinks{display:flex;gap:22px}
.topnav .nlinks a{color:var(--muted);text-decoration:none;transition:color .15s;padding:8px 0;position:relative}
.topnav .nlinks a:hover{color:var(--ink-soft)}
.topnav .nlinks a.active{color:var(--ink)}
.topnav .nlinks a.active::after{content:"";position:absolute;left:0;right:0;bottom:-2px;height:2px;background:var(--yellow);border-radius:1px}
.menu-toggle{display:none;background:none;border:1px solid var(--line);color:var(--ink);width:36px;height:32px;cursor:pointer;border-radius:3px;flex-direction:column;justify-content:center;align-items:center;gap:4px;flex-shrink:0;transition:border-color .2s,background .2s}
.menu-toggle:hover{border-color:var(--line-2);background:var(--paper-2)}
.menu-toggle span{display:block;width:14px;height:1.5px;background:var(--ink);transition:transform .25s,opacity .15s}
body.menu-open .menu-toggle span:nth-child(1){transform:translateY(5.5px) rotate(45deg)}
body.menu-open .menu-toggle span:nth-child(2){opacity:0}
body.menu-open .menu-toggle span:nth-child(3){transform:translateY(-5.5px) rotate(-45deg)}
@media(max-width:780px){
  .topnav .nlinks{display:none}
  .menu-toggle{display:flex}
}

/* MOBILE MENU */
.mobile-menu{position:fixed;top:0;right:0;width:280px;max-width:85vw;height:100vh;background:var(--paper-2);border-left:1px solid var(--line);z-index:55;padding:calc(var(--nav-h) + 24px) 28px 28px;transform:translateX(100%);transition:transform .3s cubic-bezier(.4,0,.2,1);overflow-y:auto;display:flex;flex-direction:column;gap:4px}
body.menu-open .mobile-menu{transform:translateX(0)}
.mobile-menu a{font-family:var(--display);font-size:18px;font-weight:600;color:var(--ink-soft);text-decoration:none;padding:14px 0;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;transition:color .15s}
.mobile-menu a:hover,.mobile-menu a.active{color:var(--ink)}
.mobile-menu a .mm-num{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.1em}
.mobile-menu a.active .mm-num{color:var(--yellow)}
.menu-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.6);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);z-index:54;opacity:0;pointer-events:none;transition:opacity .25s}
body.menu-open .menu-backdrop{opacity:1;pointer-events:auto}

/* PAGE */
.page{max-width:var(--maxw);margin:0 auto;padding:0 var(--pad)}
section{padding:84px 0;border-top:1px solid var(--line);position:relative;scroll-margin-top:calc(var(--nav-h) + 12px)}
section:first-of-type{border-top:none;padding-top:calc(var(--nav-h) + 24px)}
@media(max-width:680px){section{padding:56px 0}section:first-of-type{padding-top:calc(var(--nav-h) + 12px)}}
.kicker{font-family:var(--mono);font-size:11px;letter-spacing:.16em;color:var(--muted);text-transform:uppercase;margin-bottom:18px;display:flex;align-items:center;gap:12px}
.kicker::before{content:"";width:24px;height:1px;background:var(--muted)}
h1,h2,h3,h4{font-family:var(--display);font-weight:700;letter-spacing:-.015em;margin:0}
h2.sec-title{font-size:clamp(26px,4.2vw,42px);line-height:1.1;color:var(--ink);max-width:680px;margin-bottom:18px}
.sec-sub{color:var(--muted);font-size:15px;line-height:1.6;max-width:600px;margin:0 0 36px}
@media(max-width:680px){.sec-sub{font-size:14px;margin-bottom:28px}}

/* HERO */
.hero{padding:0;min-height:calc(100vh - var(--nav-h));display:flex;flex-direction:column;justify-content:space-between;border-top:none}
.hero-head{padding:36px 0 0;display:flex;justify-content:space-between;align-items:flex-start;gap:24px;border-bottom:1px solid var(--line);padding-bottom:24px}
.hero-head .tag{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.hero-head .meta{font-family:var(--mono);font-size:11px;text-align:right;line-height:1.7}
.hero-head .meta .ml{color:var(--muted);letter-spacing:.1em;text-transform:uppercase}
.hero-head .meta .mv{color:var(--ink);font-weight:600}
@media(max-width:680px){.hero-head{padding-top:24px}.hero-head .meta{font-size:10.5px}}
@media(max-width:480px){.hero-head{flex-direction:column;align-items:flex-start;gap:14px}.hero-head .meta{text-align:left;font-size:10.5px}.hero-head .meta div{display:flex;gap:8px}}
.hero-mid{flex:1;display:flex;align-items:center;padding:48px 0}
@media(max-width:680px){.hero-mid{padding:36px 0}}
.hero-mid .label{font-family:var(--mono);font-size:12px;letter-spacing:.18em;color:var(--muted);text-transform:uppercase;margin-bottom:16px}
.hero-mid h1{font-family:var(--display);font-size:clamp(60px,13vw,160px);font-weight:800;line-height:.88;letter-spacing:-.03em;color:var(--ink);margin:0}
.hero-mid .sub{font-family:var(--mono);font-size:12.5px;letter-spacing:.05em;color:var(--ink-soft);margin-top:28px;display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center}
.hero-mid .sub .dot{width:4px;height:4px;background:var(--muted);border-radius:50%;flex-shrink:0}
@media(max-width:480px){.hero-mid .sub{font-size:11px;gap:5px 12px}}
.hero-foot{padding:24px 0 40px;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;border-top:1px solid var(--line)}
.hero-foot .desc{font-size:14px;color:var(--ink-soft);max-width:520px;line-height:1.55}
.hero-foot .byline{font-family:var(--mono);font-size:10.5px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;text-align:right;line-height:1.7;flex-shrink:0}
.hero-foot .byline strong{color:var(--ink-soft)}
@media(max-width:680px){.hero-foot{flex-direction:column;align-items:flex-start;padding-bottom:32px}.hero-foot .byline{text-align:left}}

/* BRIEF */
.brief-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:4px;overflow:hidden;margin-bottom:48px}
@media(max-width:780px){.brief-grid{grid-template-columns:1fr}}
.brief-cell{background:var(--paper);padding:30px 26px;transition:background .2s}
.brief-cell:hover{background:var(--paper-2)}
@media(max-width:480px){.brief-cell{padding:24px 22px}}
.brief-cell .bnum{font-family:var(--mono);font-size:11px;letter-spacing:.16em;color:var(--muted);text-transform:uppercase;margin-bottom:14px}
.brief-cell h3{font-size:21px;font-weight:700;color:var(--ink);margin-bottom:10px;line-height:1.2}
.brief-cell p{font-size:14px;color:var(--ink-soft);margin:0;line-height:1.6}
.players{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media(max-width:780px){.players{grid-template-columns:1fr}}
.player{background:var(--paper-2);border:1px solid var(--line);border-radius:4px;padding:24px;transition:border-color .2s,transform .2s}
.player:hover{border-color:var(--line-2);transform:translateY(-2px)}
.player .tag{font-family:var(--mono);font-size:10.5px;color:var(--yellow);letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:8px}
.player .tag::before{content:"";width:6px;height:6px;background:var(--yellow);border-radius:50%}
.player h4{font-size:18px;color:var(--ink);margin-bottom:8px}
.player p{font-size:13.5px;color:var(--muted);line-height:1.55;margin:0}

/* TABBED BUILD */
.tabbed{margin-top:8px}
.tabnav{display:flex;gap:0;border-bottom:1px solid var(--line);overflow-x:auto;-ms-overflow-style:none;scrollbar-width:none;position:relative}
.tabnav::-webkit-scrollbar{display:none}
.tabnav::after{content:"";position:sticky;right:0;width:30px;height:100%;background:linear-gradient(90deg,transparent,var(--paper));pointer-events:none;display:none}
@media(max-width:680px){.tabnav::after{display:block}}
.tab-btn{flex:1;min-width:130px;background:none;border:none;border-bottom:2px solid transparent;padding:18px 14px;cursor:pointer;font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:left;transition:color .2s,border-color .2s,background .15s}
.tab-btn:hover{color:var(--ink-soft);background:var(--paper-2)}
.tab-btn.active{color:var(--ink);border-bottom-color:var(--yellow)}
.tab-btn .num{display:block;font-size:10px;color:var(--muted);margin-bottom:6px;letter-spacing:.16em}
.tab-btn.active .num{color:var(--yellow)}
.tab-btn .name{display:block;font-weight:600}
@media(max-width:480px){.tab-btn{min-width:120px;padding:14px 12px}.tab-btn .name{font-size:11px}}
.tab-panel{display:none;padding:36px 0;animation:fadein .35s ease}
.tab-panel.active{display:block}
@keyframes fadein{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.panel-grid{display:grid;grid-template-columns:1fr 320px;gap:40px;align-items:start}
@media(max-width:880px){.panel-grid{grid-template-columns:1fr;gap:24px}}
.panel-main h3{font-size:26px;color:var(--ink);margin-bottom:10px;letter-spacing:-.015em}
.panel-main .lead{color:var(--ink-soft);font-size:15px;line-height:1.6;margin-bottom:24px;max-width:560px}
.panel-main .l-sub{font-family:var(--mono);font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.14em;margin:24px 0 10px;display:block}
.panel-main ul{margin:0;padding-left:0;list-style:none}
.panel-main ul li{font-size:14px;color:var(--ink-soft);padding:8px 0;border-bottom:1px solid var(--line);display:flex;gap:12px}
.panel-main ul li::before{content:"+";color:var(--green);font-family:var(--mono);font-size:12px;flex-shrink:0;font-weight:700}
.panel-main ul li:last-child{border-bottom:none}
.panel-side{background:var(--paper-2);border:1px solid var(--line);border-radius:4px;padding:24px;position:sticky;top:calc(var(--nav-h) + 16px)}
@media(max-width:880px){.panel-side{position:static;display:grid;grid-template-columns:auto 1fr;gap:20px 24px;align-items:center;padding:20px}}
@media(max-width:480px){.panel-side{grid-template-columns:1fr}}
.panel-side .ps-label{font-family:var(--mono);font-size:10.5px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase;margin-bottom:8px}
.panel-side .ps-price{font-family:var(--display);font-size:34px;font-weight:800;color:var(--ink);letter-spacing:-.02em;line-height:1;margin-bottom:6px}
.panel-side .ps-note{font-size:12px;color:var(--muted);margin-bottom:18px;font-family:var(--mono);letter-spacing:.04em}
@media(max-width:880px){.panel-side .ps-note{margin-bottom:0}.panel-side > div:first-child{border-right:1px solid var(--line);padding-right:24px}}
@media(max-width:480px){.panel-side > div:first-child{border-right:none;border-bottom:1px solid var(--line);padding-right:0;padding-bottom:16px}}
.panel-side .ps-meta{font-size:12.5px;color:var(--ink-soft);line-height:1.6;padding-top:18px;border-top:1px solid var(--line)}
@media(max-width:880px){.panel-side .ps-meta{padding-top:0;border-top:none}}
.panel-side .ps-meta div{display:flex;justify-content:space-between;padding:4px 0;gap:12px}
.panel-side .ps-meta span{color:var(--muted)}

/* PROCESS */
.proc{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:36px}
@media(max-width:780px){.proc{grid-template-columns:1fr 1fr}}
@media(max-width:460px){.proc{grid-template-columns:1fr}}
.pstep{background:var(--paper-2);border:1px solid var(--line);border-radius:4px;padding:22px;transition:border-color .2s,transform .2s}
.pstep:hover{border-color:var(--line-2);transform:translateY(-2px)}
.pstep .pn{font-family:var(--mono);font-size:11px;color:var(--yellow);letter-spacing:.14em;margin-bottom:14px}
.pstep h4{font-size:18px;color:var(--ink);margin-bottom:8px}
.pstep p{font-size:13.5px;color:var(--muted);margin:0;line-height:1.55}
.principles{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:4px;overflow:hidden}
@media(max-width:680px){.principles{grid-template-columns:1fr}}
.principle{background:var(--paper);padding:24px}
.principle .label{font-family:var(--mono);font-size:10.5px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase;margin-bottom:8px}
.principle h4{font-size:18px;color:var(--ink);margin-bottom:8px;line-height:1.2}
.principle p{font-size:13.5px;color:var(--ink-soft);margin:0;line-height:1.55}

/* TIMELINE */
.tline{margin-top:16px}
.track{margin-bottom:32px}
.track .tl-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--line);gap:16px;flex-wrap:wrap}
.track .tl-head .tname{font-family:var(--mono);font-size:11px;color:var(--yellow);letter-spacing:.14em;text-transform:uppercase}
.track .tl-head .tdur{font-family:var(--mono);font-size:12px;color:var(--ink);font-weight:600}
.track .phases{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px}
.phase-pill{background:var(--paper-2);border:1px solid var(--line);border-radius:3px;padding:14px 16px;transition:border-color .2s,background .2s,transform .2s;cursor:default}
.phase-pill:hover{border-color:var(--yellow);background:var(--paper-3);transform:translateY(-2px)}
.phase-pill .pp-num{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:.1em;margin-bottom:4px}
.phase-pill .pp-name{font-size:13.5px;color:var(--ink);font-weight:600;line-height:1.25;margin-bottom:4px}
.phase-pill .pp-dur{font-family:var(--mono);font-size:11px;color:var(--green)}
.tline-note{margin-top:18px;padding:18px 22px;background:var(--paper-2);border-left:3px solid var(--yellow);border-radius:0 3px 3px 0;font-size:13.5px;color:var(--ink-soft);line-height:1.6}

/* INVESTMENT — with bundle calculator */
.invest-hero{background:var(--cream);color:var(--paper);border-radius:4px;padding:40px;display:grid;grid-template-columns:1fr auto;gap:32px;align-items:center;margin-bottom:24px}
@media(max-width:680px){.invest-hero{grid-template-columns:1fr;text-align:left;padding:28px}}
.invest-hero .ih-label{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted-2);margin-bottom:10px}
.invest-hero .ih-title{font-family:var(--display);font-size:clamp(20px,2.5vw,24px);font-weight:700;color:var(--paper);margin-bottom:8px;letter-spacing:-.01em;line-height:1.2}
.invest-hero .ih-desc{font-size:13.5px;color:#3a3a3a;line-height:1.55;max-width:480px;margin:0}
.invest-hero .ih-price{font-family:var(--display);font-size:clamp(34px,5vw,46px);font-weight:800;color:var(--paper);letter-spacing:-.02em;line-height:1;white-space:nowrap;transition:opacity .25s}
.invest-hero .ih-price.recalc{opacity:.4}

.bundle-hint{font-family:var(--mono);font-size:11px;color:var(--muted);text-align:center;margin:12px 0 16px;letter-spacing:.04em;display:flex;align-items:center;gap:10px;justify-content:center}
.bundle-hint::before,.bundle-hint::after{content:"";flex:1;height:1px;background:var(--line);max-width:80px}

.invest-table{background:var(--paper-2);border:1px solid var(--line);border-radius:4px;overflow:hidden}
.invest-row{display:grid;grid-template-columns:auto auto 1fr auto;gap:16px;padding:18px 24px;border-bottom:1px solid var(--line);align-items:center;transition:background .15s,opacity .25s}
.invest-row:last-child{border-bottom:none}
.invest-row.disabled{opacity:.4}
.invest-row.disabled .ir-price{text-decoration:line-through;color:var(--muted)}
@media(max-width:480px){.invest-row{padding:14px 16px;gap:10px}.invest-row .ir-info .ir-name{font-size:14px}.invest-row .ir-info .ir-note{font-size:11.5px}.invest-row .ir-price{font-size:16px}.invest-row .ir-num{font-size:10px;min-width:18px}}
.invest-row .ir-num{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.1em;min-width:24px}
.ir-toggle{display:flex;align-items:center;cursor:pointer;position:relative}
.ir-toggle input{position:absolute;opacity:0;pointer-events:none}
.ir-check{display:block;width:22px;height:22px;border:1.5px solid var(--line-2);border-radius:3px;background:var(--paper);transition:all .2s;position:relative;flex-shrink:0;pointer-events:none}
.ir-toggle:hover .ir-check{border-color:var(--muted)}
.ir-toggle input:checked + .ir-check{background:var(--yellow);border-color:var(--yellow)}
.ir-toggle input:checked + .ir-check::after{content:"";position:absolute;left:6px;top:2px;width:6px;height:11px;border:solid var(--paper);border-width:0 2.5px 2.5px 0;transform:rotate(45deg)}
.invest-row .ir-info .ir-name{font-size:15px;color:var(--ink);font-weight:600;margin-bottom:2px}
.invest-row .ir-info .ir-note{font-size:12.5px;color:var(--muted);font-family:var(--mono)}
.invest-row .ir-price{font-family:var(--display);font-size:18px;color:var(--ink);font-weight:700;white-space:nowrap;transition:color .2s}

.invest-recur{margin-top:24px;padding:20px 24px;background:var(--paper-3);border:1px solid var(--line);border-radius:4px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;font-family:var(--mono);font-size:13px}
@media(max-width:560px){.invest-recur{grid-template-columns:1fr;gap:8px}}
.invest-recur .ir-l{color:var(--ink-soft);line-height:1.55}
.invest-recur .ir-l strong{color:var(--ink);font-weight:700}
.invest-recur .ir-r{color:var(--yellow);font-weight:700;font-size:15px;white-space:nowrap}

.notes-mini{margin-top:24px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:680px){.notes-mini{grid-template-columns:1fr}}
.note-card{background:var(--paper-2);border:1px solid var(--line);border-radius:4px;padding:20px}
.note-card .nc-label{font-family:var(--mono);font-size:10.5px;color:var(--yellow);letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px}
.note-card ul{margin:0;padding-left:18px;font-size:13px;color:var(--ink-soft);line-height:1.55}
.note-card ul li{margin-bottom:6px}

/* AGENCY */
.agency-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:4px;overflow:hidden}
@media(max-width:780px){.agency-grid{grid-template-columns:1fr}}
.agency-cell{background:var(--paper);padding:30px 26px;transition:background .2s}
.agency-cell:hover{background:var(--paper-2)}
.agency-cell .acmark{font-family:var(--mono);font-size:11px;color:var(--green);letter-spacing:.14em;margin-bottom:14px}
.agency-cell h4{font-size:18px;color:var(--ink);margin-bottom:10px}
.agency-cell p{font-size:13.5px;color:var(--ink-soft);margin:0;line-height:1.6}

/* ACCORDION */
.acc{margin-top:8px}
.acc-item{border:1px solid var(--line);border-radius:4px;background:var(--paper-2);margin-bottom:12px;overflow:hidden;transition:border-color .2s}
.acc-item.open{border-color:var(--line-2)}
.acc-btn{width:100%;text-align:left;background:none;border:none;padding:22px 26px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:18px;font-family:inherit;color:var(--ink);transition:background .15s}
.acc-btn:hover{background:var(--paper-3)}
@media(max-width:480px){.acc-btn{padding:18px 20px}}
.acc-btn .lab{display:flex;flex-direction:column;gap:4px;min-width:0}
.acc-btn .lab .anum{font-family:var(--mono);font-size:10.5px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase}
.acc-btn .lab .atit{font-size:17px;color:var(--ink);font-weight:700;letter-spacing:-.005em;font-family:var(--display);line-height:1.2}
@media(max-width:480px){.acc-btn .lab .atit{font-size:15px}}
.acc-btn .icon{font-family:var(--mono);font-size:18px;color:var(--yellow);transition:transform .25s;flex-shrink:0;width:24px;height:24px;display:flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:3px}
.acc-item.open .acc-btn .icon{transform:rotate(45deg);background:var(--yellow);color:var(--paper);border-color:var(--yellow)}
.acc-body{display:none;padding:0 26px 28px;border-top:1px solid var(--line);counter-reset:asec}
@media(max-width:480px){.acc-body{padding:0 20px 22px}}
.acc-item.open .acc-body{display:block;animation:fadein .25s ease}
.acc-meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:18px 0 24px;overflow:hidden}
.acc-meta-cell{background:var(--paper-2);padding:12px 16px;font-family:var(--mono);font-size:11px}
.acc-meta-cell .am-l{color:var(--muted);text-transform:uppercase;letter-spacing:.1em;font-size:9.5px;margin-bottom:3px}
.acc-meta-cell .am-v{color:var(--ink);font-weight:700}
.acc-toc{padding:18px 22px;background:var(--paper-3);border:1px solid var(--line);border-radius:3px;margin-bottom:22px}
.acc-toc-lbl{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px}
.acc-toc ol{margin:0;padding-left:0;list-style:none;columns:2;column-gap:24px;font-size:13px;counter-reset:li}
@media(max-width:680px){.acc-toc ol{columns:1}}
.acc-toc ol li{padding:4px 0;color:var(--ink-soft);display:flex;gap:8px}
.acc-toc ol li::before{content:counter(li,decimal-leading-zero);counter-increment:li;font-family:var(--mono);color:var(--muted);font-size:10px;flex-shrink:0;letter-spacing:.04em;padding-top:2px}
.acc-section{margin-bottom:26px;counter-increment:asec}
.acc-section h5{font-family:var(--display);font-size:16px;font-weight:700;color:var(--ink);margin:0 0 6px;display:flex;align-items:baseline;gap:12px;letter-spacing:-.005em}
.acc-section h5::before{content:counter(asec,decimal-leading-zero);font-family:var(--mono);font-size:10px;color:var(--muted);font-weight:400;letter-spacing:.04em}
.acc-section .l-div{height:1px;background:var(--line);margin:10px 0 14px}
.acc-section p{font-size:13.5px;color:var(--ink-soft);line-height:1.65;margin:0 0 10px}
.acc-section p:last-child{margin-bottom:0}
.acc-section ul{margin:6px 0 12px;padding-left:20px}
.acc-section ul li{font-size:13px;color:var(--ink-soft);margin-bottom:6px;line-height:1.55}
.acc-section strong{color:var(--ink);font-weight:700}
.acc-section .lsub{display:block;font-family:var(--mono);font-size:10.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin:14px 0 4px}

/* CLOSE */
.close{padding:90px 0 60px;text-align:center;border-top:1px solid var(--line)}
@media(max-width:480px){.close{padding:60px 0 40px}}
.close .signs{display:flex;justify-content:center;gap:36px;margin-bottom:36px}
@media(max-width:480px){.close .signs{gap:24px;margin-bottom:24px}.close .signs img{width:32px;height:32px}}
.close .signs img{width:40px;height:40px;opacity:.55;filter:brightness(0) invert(1)}
.close h2.thanks{font-family:var(--display);font-size:clamp(48px,9vw,96px);font-weight:800;letter-spacing:-.025em;line-height:.95;color:var(--ink);margin:0 0 28px}
.close .cta-start{display:inline-flex;align-items:center;gap:14px;background:var(--yellow);color:var(--paper);padding:18px 36px;border-radius:4px;font-family:var(--mono);font-size:15px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;text-decoration:none;border:none;cursor:pointer;transition:transform .15s,box-shadow .2s;margin-bottom:36px}
.close .cta-start:hover{transform:translateY(-2px);box-shadow:0 10px 34px rgba(245,241,234,.18)}
.close .cta-start .arr{font-size:18px;transition:transform .2s}
.close .cta-start:hover .arr{transform:translateX(5px)}
.close .next-line{font-family:var(--mono);font-size:13px;color:var(--ink-soft);letter-spacing:.04em;margin-bottom:8px}
.close .next-em{display:inline-flex;align-items:center;gap:10px;background:none;color:var(--ink-soft);padding:10px 18px;border-radius:3px;font-family:var(--mono);font-size:13px;font-weight:700;letter-spacing:.04em;margin-top:6px;border:1px solid var(--line-2);cursor:pointer;transition:transform .15s,border-color .2s,color .2s}
.close .next-em:hover{transform:translateY(-1px);border-color:var(--ink-soft);color:var(--ink)}
.close .next-em .copy-ic{display:inline-block;width:14px;height:14px;border:1.5px solid currentColor;border-radius:2px;position:relative;flex-shrink:0}
.close .next-em .copy-ic::before{content:"";position:absolute;left:2px;top:-3px;width:9px;height:11px;border:1.5px solid currentColor;border-radius:2px;background:var(--paper)}

.foot-block{margin-top:60px;padding:30px;background:var(--paper-2);border:1px solid var(--line);border-radius:4px;display:grid;grid-template-columns:auto auto 1fr auto;gap:24px 32px;align-items:center;text-align:left}
@media(max-width:780px){.foot-block{grid-template-columns:1fr;gap:18px;text-align:left;padding:24px}}
.foot-block .fb-wm img{height:32px;width:auto;filter:brightness(0) invert(1) opacity(.85);display:block}
.foot-block .fb-sep{width:1px;height:48px;background:var(--line)}
@media(max-width:780px){.foot-block .fb-sep{width:100%;height:1px}}
.foot-block .fb-tag{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.12em;text-transform:uppercase;line-height:1.7}
.foot-block .fb-tag strong{color:var(--ink-soft)}
.foot-block .fb-contact{font-family:var(--mono);font-size:12px;line-height:1.7;color:var(--ink-soft);text-align:right}
@media(max-width:780px){.foot-block .fb-contact{text-align:left}}
.foot-block .fb-contact .fbc-em{color:var(--ink);font-weight:700;font-size:13px;margin-bottom:4px}
.foot-block .fb-contact .fbc-fade{color:var(--muted);font-size:11px;margin-top:8px}

/* BACK TO TOP */
.btt{position:fixed;bottom:24px;right:24px;width:44px;height:44px;background:var(--yellow);color:var(--paper);border:none;border-radius:50%;cursor:pointer;font-family:var(--mono);font-size:18px;font-weight:700;opacity:0;pointer-events:none;transition:opacity .25s,transform .2s;z-index:48;box-shadow:0 8px 28px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center}
.btt.visible{opacity:1;pointer-events:auto}
.btt:hover{transform:translateY(-3px)}
.btt::before{content:"";width:10px;height:10px;border:solid var(--paper);border-width:2.5px 2.5px 0 0;transform:rotate(-45deg);margin-top:4px}
@media(max-width:480px){.btt{bottom:16px;right:16px;width:40px;height:40px}}

/* DRAFT BANNER — placeholder proposals only (never client-ready) */
.draft-banner{position:sticky;top:var(--nav-h);z-index:45;background:repeating-linear-gradient(45deg,#1c1c1c,#1c1c1c 14px,#141414 14px,#141414 28px);border-bottom:1px solid var(--line-2);color:var(--ink-soft);font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;text-align:center;padding:10px var(--pad);line-height:1.5}
.draft-banner strong{color:var(--ink);font-weight:700}

/* TOAST */
.toast-wrap{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);z-index:90;pointer-events:none}
.toast{background:var(--ink);color:var(--paper);padding:10px 18px;border-radius:3px;font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.04em;opacity:0;transform:translateY(10px);transition:opacity .25s,transform .25s;display:flex;align-items:center;gap:10px}
.toast.show{opacity:1;transform:translateY(0)}

/* PRINT — clean PDF export */
@media print{
  .topnav,.scroll-progress,.menu-toggle,.mobile-menu,.menu-backdrop,.btt,.toast-wrap{display:none !important}
  body{background:#fff;color:#000;font-size:11pt}
  section{padding:18pt 0;break-inside:avoid;page-break-inside:avoid;border-color:#ccc}
  section:first-of-type{padding-top:0}
  .hero-mid h1{font-size:60pt;color:#000}
  h2.sec-title{font-size:20pt;color:#000}
  .hero-mid .label,.kicker,.sec-sub,.brief-cell p,.player p{color:#333}
  .panel-side{position:static;break-inside:avoid;background:#f8f8f8;border-color:#ccc;color:#000}
  .panel-side .ps-price{color:#000}
  .invest-hero{break-inside:avoid;background:#f0f0f0;color:#000}
  .invest-table,.note-card,.pstep,.player,.brief-cell,.agency-cell,.phase-pill,.tline-note,.principle{background:#fafafa;color:#000;border-color:#ccc}
  .acc-item{break-inside:avoid;background:#fff;border-color:#ccc}
  .acc-body{display:block !important}
  .acc-btn .icon{display:none}
  .tab-panel{display:block !important;break-before:page}
  .tab-btn{display:none}
  .close{background:#fff;page-break-before:always}
  .close h2.thanks{color:#000}
  .close .cta-start{display:none}
  .foot-block{background:#fafafa;color:#000;border-color:#ccc}
  a{color:#000;text-decoration:none}
  *{box-shadow:none !important;text-shadow:none !important}
}
"""

JS = r"""
(function(){
  // ============ TABS ============
  document.querySelectorAll('.tabbed').forEach(group=>{
    const btns=group.querySelectorAll('.tab-btn');
    const panels=group.querySelectorAll('.tab-panel');
    btns.forEach((btn,i)=>{
      btn.setAttribute('role','tab');
      btn.setAttribute('aria-selected', btn.classList.contains('active')?'true':'false');
      btn.setAttribute('tabindex', btn.classList.contains('active')?'0':'-1');
      btn.addEventListener('click',()=>activate(i));
      btn.addEventListener('keydown',ev=>{
        if(ev.key==='ArrowRight'){ ev.preventDefault(); activate((i+1)%btns.length); btns[(i+1)%btns.length].focus(); }
        if(ev.key==='ArrowLeft'){ ev.preventDefault(); const p=(i-1+btns.length)%btns.length; activate(p); btns[p].focus(); }
        if(ev.key==='Home'){ ev.preventDefault(); activate(0); btns[0].focus(); }
        if(ev.key==='End'){ ev.preventDefault(); const l=btns.length-1; activate(l); btns[l].focus(); }
      });
    });
    function activate(i){
      btns.forEach(b=>{b.classList.remove('active'); b.setAttribute('aria-selected','false'); b.setAttribute('tabindex','-1');});
      panels.forEach(p=>p.classList.remove('active'));
      btns[i].classList.add('active'); btns[i].setAttribute('aria-selected','true'); btns[i].setAttribute('tabindex','0');
      if(panels[i]) panels[i].classList.add('active');
    }
  });

  // ============ ACCORDION ============
  document.querySelectorAll('.acc-btn').forEach(btn=>{
    btn.setAttribute('aria-expanded','false');
    btn.addEventListener('click',()=>{
      const item=btn.parentElement;
      const open=item.classList.toggle('open');
      btn.setAttribute('aria-expanded', open?'true':'false');
    });
  });

  // ============ SCROLL PROGRESS ============
  const sp=document.querySelector('.scroll-progress');
  function updateProgress(){
    const h=document.documentElement;
    const max=h.scrollHeight-h.clientHeight;
    const pct=max>0?(h.scrollTop/max)*100:0;
    if(sp) sp.style.width=pct+'%';
  }
  let scrollTick=false;
  window.addEventListener('scroll',()=>{
    if(!scrollTick){
      requestAnimationFrame(()=>{ updateProgress(); scrollTick=false; });
      scrollTick=true;
    }
  },{passive:true});
  updateProgress();

  // ============ ACTIVE NAV ============
  const sections=document.querySelectorAll('section[id]');
  const navLinks=document.querySelectorAll('.topnav .nlinks a, .mobile-menu a');
  function setActiveNav(id){
    navLinks.forEach(a=>{
      a.classList.toggle('active', a.getAttribute('href')==='#'+id);
    });
  }
  const activeObs=new IntersectionObserver(entries=>{
    entries.forEach(en=>{
      if(en.isIntersecting && en.intersectionRatio>0.25){
        setActiveNav(en.target.id);
      }
    });
  },{threshold:[0.25,0.5],rootMargin:'-80px 0px -40% 0px'});
  sections.forEach(s=>activeObs.observe(s));

  // ============ REVEAL ON SCROLL ============
  const revObs=new IntersectionObserver(es=>es.forEach(en=>{
    if(en.isIntersecting){en.target.style.opacity='1';en.target.style.transform='translateY(0)';revObs.unobserve(en.target)}
  }),{threshold:0.08});
  document.querySelectorAll('section').forEach(s=>{
    s.style.opacity='0';s.style.transform='translateY(14px)';s.style.transition='opacity .55s ease,transform .55s ease';
    revObs.observe(s);
  });

  // ============ MOBILE MENU ============
  const menuBtn=document.querySelector('.menu-toggle');
  const menuBackdrop=document.querySelector('.menu-backdrop');
  const mobileMenu=document.querySelector('.mobile-menu');
  function closeMenu(){ document.body.classList.remove('menu-open'); if(menuBtn) menuBtn.setAttribute('aria-expanded','false'); }
  function openMenu(){ document.body.classList.add('menu-open'); if(menuBtn) menuBtn.setAttribute('aria-expanded','true'); }
  if(menuBtn){
    menuBtn.setAttribute('aria-expanded','false');
    menuBtn.addEventListener('click',()=>{
      if(document.body.classList.contains('menu-open')) closeMenu(); else openMenu();
    });
  }
  if(menuBackdrop) menuBackdrop.addEventListener('click',closeMenu);
  if(mobileMenu) mobileMenu.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
  document.addEventListener('keydown',ev=>{ if(ev.key==='Escape') closeMenu(); });

  // ============ INVESTMENT BUNDLE CALCULATOR ============
  const toggles=document.querySelectorAll('.ir-toggle input');
  const totalEl=document.querySelector('.ih-price');
  const titleEl=document.querySelector('.ih-title');
  const labelEl=document.querySelector('.ih-label');
  const recurEl=document.querySelector('.invest-recur .ir-r');
  const recurLEl=document.querySelector('.invest-recur .ir-l');
  const fullTitle=titleEl?titleEl.getAttribute('data-full')||titleEl.textContent:'';

  function fmt(n){
    // Indian-format with commas: 207000 -> "2,07,000"
    const s=String(n);
    if(s.length<=3) return s;
    const last3=s.slice(-3);
    const rest=s.slice(0,-3);
    return rest.replace(/\B(?=(\d{2})+(?!\d))/g,',')+','+last3;
  }

  function recalc(){
    if(!totalEl) return;
    let total=0,recur=0,count=0;
    const all=toggles.length;
    toggles.forEach(t=>{
      const row=t.closest('.invest-row');
      if(t.checked){
        total+=parseInt(t.dataset.price,10);
        recur+=parseInt(t.dataset.recurring||'0',10);
        count++;
        row.classList.remove('disabled');
      }else{
        row.classList.add('disabled');
      }
    });
    totalEl.classList.add('recalc');
    setTimeout(()=>{
      totalEl.textContent='₹'+fmt(total);
      totalEl.classList.remove('recalc');
    },120);

    if(titleEl){
      const names=Array.from(toggles).filter(t=>t.checked).map(t=>t.dataset.short);
      if(count===all) titleEl.textContent=fullTitle;
      else if(count===0) titleEl.textContent='No deliverables selected';
      else titleEl.textContent=names.join(' + ');
    }
    if(labelEl){
      labelEl.textContent=count===all?'▸ FULL PROGRAMME · FIRST MONTH':'▸ CUSTOM SELECTION · '+count+' OF '+all;
    }
    if(recurEl){
      recurEl.textContent='₹'+fmt(recur)+' / month';
    }
    if(recurLEl){
      const r=Array.from(toggles).filter(t=>t.checked && parseInt(t.dataset.recurring||'0',10)>0).map(t=>t.dataset.short);
      recurLEl.innerHTML='From <strong>Month 2 onward</strong> — '+(r.length?r.join(' + ').toLowerCase():'no recurring items selected');
    }
  }
  toggles.forEach(t=>t.addEventListener('change',recalc));
  recalc();

  // ============ COPY EMAIL ============
  const copyBtn=document.querySelector('.next-em');
  const toast=document.querySelector('.toast');
  function showToast(msg){
    if(!toast) return;
    toast.textContent='';
    const dot=document.createElement('span');
    dot.style.cssText='width:8px;height:8px;border-radius:50%;background:var(--green);display:inline-block;margin-right:8px;flex-shrink:0';
    toast.appendChild(dot);
    toast.appendChild(document.createTextNode(msg));
    toast.classList.add('show');
    clearTimeout(showToast._t);
    showToast._t=setTimeout(()=>toast.classList.remove('show'),2200);
  }
  if(copyBtn){
    copyBtn.addEventListener('click',async ()=>{
      const email=copyBtn.getAttribute('data-email');
      try{
        await navigator.clipboard.writeText(email);
        showToast('Email copied to clipboard');
      }catch(err){
        const ta=document.createElement('textarea');
        ta.value=email; document.body.appendChild(ta); ta.select();
        try{ document.execCommand('copy'); showToast('Email copied'); }catch(e){ showToast('Tap-hold to copy: '+email); }
        document.body.removeChild(ta);
      }
    });
  }

  // ============ BACK TO TOP ============
  const btt=document.querySelector('.btt');
  function updateBtt(){
    if(!btt) return;
    if(window.scrollY>600) btt.classList.add('visible'); else btt.classList.remove('visible');
  }
  if(btt){
    window.addEventListener('scroll',updateBtt,{passive:true});
    btt.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
    updateBtt();
  }

})();
"""


# --------------------------------------------------------------------------- #
#  Section renderers
# --------------------------------------------------------------------------- #
def _li_list(items):
    return "".join("<li>%s</li>" % it for it in items)


def _brief(s):
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    if s.get("sub"):
        out.append('<p class="sec-sub">%s</p>' % e(s["sub"]))
    out.append('<div class="brief-grid">')
    for c in s["cells"]:
        out.append('<div class="brief-cell"><div class="bnum">%s</div><h3>%s</h3><p>%s</p></div>'
                   % (e(c["num"]), e(c["h"]), e(c["p"])))
    out.append('</div>')
    if s.get("players"):
        out.append('<div class="kicker" style="margin-top:48px">%s</div>' % e(s["players_kicker"]))
        out.append('<div class="players">')
        for p in s["players"]:
            out.append('<div class="player"><div class="tag">%s</div><h4>%s</h4><p>%s</p></div>'
                       % (e(p["tag"]), e(p["h"]), e(p["p"])))
        out.append('</div>')
    out.append('</section>')
    return "".join(out)


def _build(s):
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    if s.get("sub"):
        out.append('<p class="sec-sub">%s</p>' % e(s["sub"]))
    out.append('<div class="tabbed"><div class="tabnav" role="tablist" aria-label="Deliverables">')
    for i, t in enumerate(s["tabs"]):
        out.append('<button class="tab-btn%s"><span class="num">%s</span><span class="name">%s</span></button>'
                   % (" active" if i == 0 else "", e(t["num"]), e(t["name"])))
    out.append('</div>')
    for i, t in enumerate(s["tabs"]):
        out.append('<div class="tab-panel%s" role="tabpanel"><div class="panel-grid"><div class="panel-main">'
                   % (" active" if i == 0 else ""))
        out.append('<h3>%s</h3>' % e(t["h"]))
        out.append('<p class="lead">%s</p>' % e(t["lead"]))
        for grp in t["lists"]:
            out.append('<span class="l-sub">%s</span><ul>%s</ul>'
                       % (e(grp["label"]), _li_list([e(x) for x in grp["items"]])))
        out.append('</div><aside class="panel-side"><div>')
        out.append('<div class="ps-label">%s</div>' % e(t["price_label"]))
        out.append('<div class="ps-price">%s</div>' % t["price"])  # raw: may contain <span>
        out.append('<div class="ps-note">%s</div></div><div class="ps-meta">' % e(t["price_note"]))
        for k, v in t["meta"]:
            out.append('<div><span>%s</span><strong>%s</strong></div>' % (e(k), e(v)))
        out.append('</div></aside></div></div>')
    out.append('</div></section>')
    return "".join(out)


def _process(s):
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    if s.get("sub"):
        out.append('<p class="sec-sub">%s</p>' % e(s["sub"]))
    out.append('<div class="proc">')
    for st in s["steps"]:
        out.append('<div class="pstep"><div class="pn">%s</div><h4>%s</h4><p>%s</p></div>'
                   % (e(st["n"]), e(st["h"]), e(st["p"])))
    out.append('</div><div class="principles">')
    for pr in s["principles"]:
        out.append('<div class="principle"><div class="label">%s</div><h4>%s</h4><p>%s</p></div>'
                   % (e(pr["label"]), e(pr["h"]), e(pr["p"])))
    out.append('</div></section>')
    return "".join(out)


def _timeline(s):
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    if s.get("sub"):
        out.append('<p class="sec-sub">%s</p>' % e(s["sub"]))
    out.append('<div class="tline">')
    for tr in s["tracks"]:
        out.append('<div class="track"><div class="tl-head"><div class="tname">%s</div><div class="tdur">%s</div></div><div class="phases">'
                   % (e(tr["name"]), e(tr["dur"])))
        for ph in tr["phases"]:
            out.append('<div class="phase-pill"><div class="pp-num">%s</div><div class="pp-name">%s</div><div class="pp-dur">%s</div></div>'
                       % (e(ph["num"]), e(ph["name"]), e(ph["dur"])))
        out.append('</div></div>')
    if s.get("note"):
        out.append('<div class="tline-note">%s</div>' % s["note"])  # raw: allows <strong>
    out.append('</div></section>')
    return "".join(out)


def _investment(s):
    h = s["hero"]
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    if s.get("sub"):
        out.append('<p class="sec-sub">%s</p>' % e(s["sub"]))
    out.append('<div class="invest-hero"><div><div class="ih-label">%s</div>'
               '<div class="ih-title" data-full="%s">%s</div><p class="ih-desc">%s</p></div>'
               '<div class="ih-price">%s</div></div>'
               % (e(h["label"]), e(h["title"]), e(h["title"]), e(h["desc"]), e(h["price"])))
    out.append('<div class="bundle-hint">%s</div>' % e(s.get("hint", "TOGGLE TO CUSTOMISE THE BUNDLE")))
    out.append('<div class="invest-table">')
    for r in s["rows"]:
        out.append(
            '<div class="invest-row"><div class="ir-num">%s</div>'
            '<label class="ir-toggle" aria-label="Toggle %s">'
            '<input type="checkbox"%s data-price="%d" data-recurring="%d" data-short="%s">'
            '<span class="ir-check"></span></label>'
            '<div class="ir-info"><div class="ir-name">%s</div><div class="ir-note">%s</div></div>'
            '<div class="ir-price">%s</div></div>'
            % (e(r["num"]), e(r["name"]), " checked" if r.get("checked", True) else "",
               r["price_val"], r.get("recurring_val", 0), e(r["short"]),
               e(r["name"]), e(r["note"]), e(r["price"])))
    out.append('</div>')
    rc = s["recur"]
    out.append('<div class="invest-recur"><div class="ir-l">%s</div><div class="ir-r">%s</div></div>'
               % (rc["l"], e(rc["r"])))  # l raw: allows <strong>
    out.append('<div class="notes-mini">')
    for nc in s["notes"]:
        out.append('<div class="note-card"><div class="nc-label">%s</div><ul>%s</ul></div>'
                   % (e(nc["label"]), _li_list([x for x in nc["items"]])))  # items raw: allow inline tags
    out.append('</div></section>')
    return "".join(out)


def _agency(s):
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    out.append('<div class="agency-grid">')
    for c in s["cells"]:
        out.append('<div class="agency-cell"><div class="acmark">%s</div><h4>%s</h4><p>%s</p></div>'
                   % (e(c["mark"]), e(c["h"]), e(c["p"])))
    out.append('</div></section>')
    return "".join(out)


def _legal(s):
    out = ['<section id="%s" class="page" aria-labelledby="%s-title">' % (s["id"], s["id"])]
    out.append('<div class="kicker">%s</div>' % e(s["kicker"]))
    out.append('<h2 class="sec-title" id="%s-title">%s</h2>' % (s["id"], e(s["title"])))
    if s.get("sub"):
        out.append('<p class="sec-sub">%s</p>' % e(s["sub"]))
    out.append('<div class="acc">')
    for d in s["docs"]:
        out.append('<div class="acc-item"><button class="acc-btn" aria-controls="%s">'
                   '<div class="lab"><span class="anum">%s</span><span class="atit">%s</span></div>'
                   '<span class="icon">+</span></button><div class="acc-body" id="%s">'
                   % (e(d["id"]), e(d["anum"]), e(d["title"]), e(d["id"])))
        out.append('<div class="acc-meta">')
        for k, v in d["meta"]:
            out.append('<div class="acc-meta-cell"><div class="am-l">%s</div><div class="am-v">%s</div></div>'
                       % (e(k), e(v)))
        out.append('</div>')
        out.append('<div class="acc-toc"><div class="acc-toc-lbl">&#9656; Contents</div><ol>%s</ol></div>'
                   % _li_list([e(x) for x in d["toc"]]))
        for sec in d["sections"]:
            out.append('<div class="acc-section"><h5>%s</h5><div class="l-div"></div>%s</div>'
                       % (e(sec["h"]), sec["body"]))  # body raw HTML
        out.append('</div></div>')
    out.append('</div></section>')
    return "".join(out)


def _raw(s):
    return s["html"]


_RENDERERS = {
    "brief": _brief, "build": _build, "process": _process, "timeline": _timeline,
    "investment": _investment, "agency": _agency, "legal": _legal, "raw": _raw,
}


# --------------------------------------------------------------------------- #
#  Top-level render
# --------------------------------------------------------------------------- #
def _hero(d):
    h = d["hero"]
    meta = "".join('<div><span class="ml">%s</span> <span class="mv">%s</span></div>'
                   % (e(k), e(v)) for k, v in h["meta"])
    sub = '<span class="dot"></span>'.join("<span>%s</span>" % e(x) for x in h["sub"])
    return (
        '<section class="hero page" id="cover" aria-label="Cover">'
        '<div class="hero-head"><div class="tag">%s</div><div class="meta">%s</div></div>'
        '<div class="hero-mid"><div><div class="label">%s</div><h1>%s</h1>'
        '<div class="sub">%s</div></div></div>'
        '<div class="hero-foot"><div class="desc">%s</div><div class="byline">%s</div></div>'
        '</section>'
        % (e(h["tag"]), meta, e(h["prepared_label"]), h["title_html"], sub,
           e(h["desc"]), h["byline_html"])
    )


def _nav(d):
    top = "".join('<a href="#%s">%s</a>' % (e(i), e(l)) for i, l in d["topnav"])
    menu = "".join('<a href="#%s"><span>%s</span><span class="mm-num">%s</span></a>'
                   % (e(i), e(l), e(n)) for i, l, n in d["menu"])
    nav = (
        '<nav class="topnav" aria-label="Primary"><div class="ntag">'
        '<span class="ntag-main">%s</span><span class="sep">/</span>'
        '<span class="small">%s</span></div><div class="nlinks">%s</div>'
        '<button class="menu-toggle" aria-label="Open navigation menu">'
        '<span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span>'
        '</button></nav>'
        % (e(d["nav_title"]), e(d["nav_sub"]), top)
    )
    menu_panel = (
        '<div class="menu-backdrop" aria-hidden="true"></div>'
        '<aside class="mobile-menu" aria-label="Mobile navigation">%s</aside>' % menu
    )
    return nav + menu_panel


def _close(d, A):
    c = d["close"]
    email = CONTACT["email"]
    subject = c.get("cta_subject", "Proposal acceptance — %s" % d["client"])
    mailto = "mailto:%s?subject=%s" % (email, e(subject).replace(" ", "%20"))
    signs = (
        '<img src="%s" alt="" aria-hidden="true">'
        '<img src="%s" alt="" aria-hidden="true">'
        '<img src="%s" alt="" aria-hidden="true">'
        % (A["plus"], A["circle"], A["cross"])
    )
    return (
        '<section class="close page" aria-label="Close">'
        '<div class="signs">%s</div>'
        '<h2 class="thanks">%s</h2>'
        '<a class="cta-start" href="%s">%s <span class="arr">&rarr;</span></a>'
        '<div class="next-line">%s</div>'
        '<button class="next-em" data-email="%s" aria-label="Copy email address to clipboard">%s'
        '<span class="copy-ic" aria-hidden="true"></span></button>'
        '<div class="foot-block">'
        '<div class="fb-wm"><img src="%s" alt="Adaline"></div>'
        '<div class="fb-sep" aria-hidden="true"></div>'
        '<div class="fb-tag">Proposal prepared by<br/><strong>%s</strong></div>'
        '<div class="fb-contact"><div class="fbc-em">%s</div><div>%s</div>'
        '<div class="fbc-fade">%s &#183; %s</div></div>'
        '</div></section>'
        % (signs, e(c.get("thanks", "Thank You.")), mailto, e(c.get("cta", "HIT START")),
           e(c.get("next_line", "To commence the engagement, reply to:")),
           e(email), e(email), A["wordmark"], e(CONTACT["legal_name"]),
           e(email), e(CONTACT["whatsapp"]), e(CONTACT["gstin"]), e(CONTACT["place"]))
    )


def render(d):
    """Render a proposal dict into a single self-contained HTML string."""
    A = _assets()
    css = (CSS.replace("__PALETTE__", d["palette"])
              .replace("__BODYGLOW__", d.get("body_glow", _default_glow(d))))
    body = []
    if d.get("draft_note"):
        body.append('<div class="draft-banner">%s</div>' % d["draft_note"])
    body.append(_hero(d))
    for s in d["sections"]:
        body.append(_RENDERERS[s["type"]](s))
    body.append(_close(d, A))

    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="theme-color" content="#0b0b0b">\n'
        '<title>%s</title>\n'
        '<meta name="description" content="%s">\n'
        '<meta name="robots" content="noindex">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
        '&family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700;800'
        '&display=swap" rel="stylesheet">\n'
        '<style>%s</style>\n</head>\n<body>\n'
        '<div class="scroll-progress" aria-hidden="true"></div>\n'
        '%s\n<main>\n%s\n</main>\n'
        '<button class="btt" aria-label="Back to top"></button>\n'
        '<div class="toast-wrap"><div class="toast" role="status" aria-live="polite"></div></div>\n'
        '<script>%s</script>\n</body>\n</html>\n'
        % (e(d["title"]), e(d["description"]), css, _nav(d), "\n".join(body), JS)
    )


def _default_glow(d):
    return ("radial-gradient(ellipse 80% 50% at 50% 0%,rgba(245,241,234,.04),transparent 60%),"
            "radial-gradient(ellipse 60% 40% at 90% 100%,rgba(245,241,234,.02),transparent 50%)")


def build(d, repo_root=None):
    """Render the proposal and write it to <repo_root>/<slug>/index.html."""
    if repo_root is None:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(repo_root, d["slug"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(render(d))
    return out_path
