"""
Vertex — PLACEHOLDER proposal ("vertex web development").

Source repo Adaline-io/vertex-proposal is not in this session's scope, so the
content below is structural scaffolding only — NOT client-ready. Replace with the
migrated content once the source repo is in scope, and drop the draft banner.
Accent below is a placeholder pending confirmation.

Run:  python3 _build/build_vertex.py
"""

import template as T

# PLACEHOLDER accent — confirm with the Management before client-ready.
PALETTE = "--red:#ff5c44;--yellow:#5a8eff;--green:#3dd483;--blue:#5a8eff;"

DATA = {
    "slug": "vertex",
    "client": "Vertex",
    "title": "Project Proposal · Vertex",
    "description": "Project Proposal for Vertex — prepared by Adaline.",
    "palette": PALETTE,
    "draft_note": "Draft scaffold &mdash; <strong>placeholder content pending migration</strong> "
                  "from vertex-proposal. Not client-ready.",

    "nav_title": "Vertex",
    "nav_sub": "Project Proposal",
    "topnav": [("brief", "Brief"), ("build", "Build"), ("process", "Process"),
               ("timeline", "Timeline"), ("investment", "Investment"), ("agency", "Agency")],
    "menu": [("cover", "Cover", "00"), ("brief", "The Brief", "01"),
             ("build", "What We Build", "02"), ("process", "How We Work", "03"),
             ("timeline", "Timeline", "04"), ("investment", "The Investment", "05"),
             ("agency", "The Agency", "06")],

    "hero": {
        "tag": "Project Proposal · DRAFT",
        "meta": [("Date", "TBD"), ("Valid", "10 days from issue")],
        "prepared_label": "Prepared for",
        "title_html": "Vertex.",
        "sub": ["Web Development", "Placeholder", "Calicut, Kerala"],
        "desc": "Placeholder brief. Real scope, deliverables, and pricing migrate in once "
                "vertex-proposal is in scope.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Let's Ship.",
        "cta": "HIT START",
        "cta_subject": "Vertex — proposal acceptance",
        "next_line": "Or, to commence the engagement, reply to:",
    },

    "sections": [
        {"type": "brief", "id": "brief", "kicker": "01 · The Brief",
         "title": "Placeholder headline. The positioning line goes here.",
         "sub": "Placeholder brief paragraph — set the market context and the move Vertex makes.",
         "cells": [
             {"num": "▸ The Opportunity", "h": "Placeholder opportunity.",
              "p": "Replace with the real opportunity once content is migrated."},
             {"num": "▸ The Goal", "h": "Placeholder goal.",
              "p": "Replace with the real goal and time horizon."},
             {"num": "▸ The Approach", "h": "Placeholder approach.",
              "p": "Replace with the connected workstreams for this engagement."},
         ]},
        {"type": "build", "id": "build", "kicker": "02 · What We Build",
         "title": "Deliverables. Each scoped. Each priced.",
         "sub": "Placeholder deliverables. Swap in the real tabs and pricing on migration.",
         "tabs": [
             {"num": "01", "name": "Website", "h": "Placeholder Web Build",
              "lead": "Placeholder lead describing the web development deliverable.",
              "lists": [{"label": "▸ Scope", "items": ["Placeholder scope item one",
                                                       "Placeholder scope item two",
                                                       "Placeholder scope item three"]}],
              "price_label": "One-time investment", "price": "₹00,000",
              "price_note": "placeholder",
              "meta": [("Duration", "TBD"), ("Tech", "TBD"), ("Support", "TBD")]},
             {"num": "02", "name": "Care Plan", "h": "Placeholder Care Plan",
              "lead": "Placeholder lead describing the ongoing maintenance retainer.",
              "lists": [{"label": "▸ Monthly", "items": ["Placeholder item one",
                                                         "Placeholder item two"]}],
              "price_label": "Monthly retainer", "price": "₹00,000",
              "price_note": "placeholder",
              "meta": [("SLA", "TBD"), ("Response", "TBD")]},
         ]},
        {"type": "process", "id": "process", "kicker": "03 · How We Work",
         "title": "Four phases. Documented. Scoped.",
         "sub": "Placeholder process — identical cadence to the canonical, content TBD.",
         "steps": [
             {"n": "PHASE 01", "h": "Brief", "p": "Placeholder phase description."},
             {"n": "PHASE 02", "h": "Plan", "p": "Placeholder phase description."},
             {"n": "PHASE 03", "h": "Build", "p": "Placeholder phase description."},
             {"n": "PHASE 04", "h": "Ship", "p": "Placeholder phase description."},
         ],
         "principles": [
             {"label": "▸ Engineering", "h": "Placeholder principle.",
              "p": "Replace with the engineering approach for this build."},
             {"label": "▸ Performance", "h": "Placeholder principle.",
              "p": "Replace with the performance / SEO strategy for this build."},
         ]},
        {"type": "timeline", "id": "timeline", "kicker": "04 · Timeline",
         "title": "Placeholder timeline. Weeks to live.",
         "sub": "Placeholder schedule — wire in the real tracks on migration.",
         "tracks": [
             {"name": "▸ Track A — Placeholder", "dur": "TBD",
              "phases": [{"num": "P1", "name": "Discovery", "dur": "—"},
                         {"num": "P2", "name": "Design", "dur": "—"},
                         {"num": "P3", "name": "Development", "dur": "—"},
                         {"num": "P4", "name": "Launch", "dur": "—"}]},
         ],
         "note": "<strong>Placeholder note.</strong> Replace with the real track summary."},
        {"type": "investment", "id": "investment", "kicker": "05 · The Investment",
         "title": "Deliverables. One clear number.",
         "sub": "Placeholder investment. Real figures and split migrate in with the lead details.",
         "hero": {"label": "▸ FULL PROGRAMME · FIRST MONTH",
                  "title": "Placeholder bundle",
                  "desc": "Placeholder description of the full-programme bundle.",
                  "price": "₹0"},
         "rows": [
             {"num": "01", "name": "Placeholder Web Build", "note": "One-time · placeholder",
              "price": "₹0", "price_val": 0, "recurring_val": 0, "short": "Web build"},
             {"num": "02", "name": "Placeholder Care Plan · Month 1", "note": "Monthly · placeholder",
              "price": "₹0", "price_val": 0, "recurring_val": 0, "short": "Care plan"},
         ],
         "recur": {"l": "From <strong>Month 2 onward</strong> — placeholder recurring",
                   "r": "₹0 / month"},
         "notes": [
             {"label": "▸ Payment Schedule", "items": ["Placeholder split (e.g. 50 / 50)",
                                                       "Monthly care plan invoiced in advance"]},
             {"label": "▸ Things to Note", "items": ["All prices exclude applicable GST",
                                                     "Placeholder note two"]},
         ]},
        {"type": "agency", "id": "agency", "kicker": "06 · The Agency",
         "title": "Three reasons. They matter for Vertex specifically.",
         "cells": [
             {"mark": "▸ ONE", "h": "Co-builders, not vendors",
              "p": "Placeholder — same agency positioning as canonical."},
             {"mark": "▸ TWO", "h": "One studio, three engines",
              "p": "Placeholder — brand, production, technology under one roof."},
             {"mark": "▸ THREE", "h": "Placeholder differentiator",
              "p": "Replace with the reason that matters specifically for Vertex."},
         ]},
    ],
}


if __name__ == "__main__":
    print("Built:", T.build(DATA))
