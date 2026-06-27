"""
BZ Fitness — PLACEHOLDER proposal.

Source repo Adaline-io/Bz-fitness-proposal is not in this session's scope, so the
content below is structural scaffolding only — NOT client-ready. It proves the
template generalises and gives the routing a real card. Once the source repo is
in scope, replace the copy/pricing with the migrated content and drop the draft
banner. Accent below is a placeholder pending confirmation (brand rule: ask
before setting a client accent).

Run:  python3 _build/build_bzfitness.py
"""

import template as T

# PLACEHOLDER accent — confirm with the Management before client-ready.
PALETTE = "--red:#ff5c44;--yellow:#ff5c44;--green:#3dd483;--blue:#5a8eff;"

DATA = {
    "slug": "bz-fitness",
    "client": "BZ Fitness",
    "title": "Project Proposal · BZ Fitness",
    "description": "Project Proposal for BZ Fitness — prepared by Adaline.",
    "palette": PALETTE,
    "draft_note": "Draft scaffold &mdash; <strong>placeholder content pending migration</strong> "
                  "from Bz-fitness-proposal. Not client-ready.",

    "nav_title": "BZ Fitness",
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
        "title_html": "BZ<br/>Fitness.",
        "sub": ["Strength & Conditioning", "Placeholder", "Calicut, Kerala"],
        "desc": "Placeholder brief. Real scope, deliverables, and pricing migrate in once "
                "Bz-fitness-proposal is in scope.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Let's Train.",
        "cta": "HIT START",
        "cta_subject": "BZ Fitness — proposal acceptance",
        "next_line": "Or, to commence the engagement, reply to:",
    },

    "sections": [
        {"type": "brief", "id": "brief", "kicker": "01 · The Brief",
         "title": "Placeholder headline. The positioning line goes here.",
         "sub": "Placeholder brief paragraph — set the market context and the move BZ Fitness makes.",
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
             {"num": "01", "name": "Website", "h": "Placeholder Website",
              "lead": "Placeholder lead describing the website deliverable.",
              "lists": [{"label": "▸ Scope", "items": ["Placeholder scope item one",
                                                       "Placeholder scope item two",
                                                       "Placeholder scope item three"]}],
              "price_label": "One-time investment", "price": "₹00,000",
              "price_note": "placeholder",
              "meta": [("Duration", "TBD"), ("Tech", "TBD"), ("Support", "TBD")]},
             {"num": "02", "name": "Content", "h": "Placeholder Content Engine",
              "lead": "Placeholder lead describing the content retainer.",
              "lists": [{"label": "▸ Monthly", "items": ["Placeholder item one",
                                                         "Placeholder item two"]}],
              "price_label": "Monthly retainer", "price": "₹00,000",
              "price_note": "placeholder",
              "meta": [("Posts", "TBD"), ("Response", "TBD")]},
         ]},
        {"type": "process", "id": "process", "kicker": "03 · How We Work",
         "title": "Four phases. Documented. Scoped.",
         "sub": "Placeholder process — identical cadence to the canonical, content TBD.",
         "steps": [
             {"n": "PHASE 01", "h": "Brief", "p": "Placeholder phase description."},
             {"n": "PHASE 02", "h": "Plan", "p": "Placeholder phase description."},
             {"n": "PHASE 03", "h": "Create", "p": "Placeholder phase description."},
             {"n": "PHASE 04", "h": "Review", "p": "Placeholder phase description."},
         ],
         "principles": [
             {"label": "▸ Visual Direction", "h": "Placeholder principle.",
              "p": "Replace with the visual direction for this brand."},
             {"label": "▸ Growth Strategy", "h": "Placeholder principle.",
              "p": "Replace with the growth strategy for this brand."},
         ]},
        {"type": "timeline", "id": "timeline", "kicker": "04 · Timeline",
         "title": "Placeholder timeline. Weeks to live.",
         "sub": "Placeholder schedule — wire in the real tracks on migration.",
         "tracks": [
             {"name": "▸ Track A — Placeholder", "dur": "TBD",
              "phases": [{"num": "P1", "name": "Discovery", "dur": "—"},
                         {"num": "P2", "name": "Design", "dur": "—"},
                         {"num": "P3", "name": "Build", "dur": "—"},
                         {"num": "P4", "name": "Launch", "dur": "—"}]},
         ],
         "note": "<strong>Placeholder note.</strong> Replace with the real parallel-track summary."},
        {"type": "investment", "id": "investment", "kicker": "05 · The Investment",
         "title": "Deliverables. One clear number.",
         "sub": "Placeholder investment. Real figures and split migrate in with the lead details.",
         "hero": {"label": "▸ FULL PROGRAMME · FIRST MONTH",
                  "title": "Placeholder bundle",
                  "desc": "Placeholder description of the full-programme bundle.",
                  "price": "₹0"},
         "rows": [
             {"num": "01", "name": "Placeholder Website", "note": "One-time · placeholder",
              "price": "₹0", "price_val": 0, "recurring_val": 0, "short": "Website"},
             {"num": "02", "name": "Placeholder Retainer · Month 1", "note": "Monthly · placeholder",
              "price": "₹0", "price_val": 0, "recurring_val": 0, "short": "Retainer"},
         ],
         "recur": {"l": "From <strong>Month 2 onward</strong> — placeholder recurring",
                   "r": "₹0 / month"},
         "notes": [
             {"label": "▸ Payment Schedule", "items": ["Placeholder split (e.g. 40 / 40 / 20)",
                                                       "Monthly retainers invoiced in advance"]},
             {"label": "▸ Things to Note", "items": ["All prices exclude applicable GST",
                                                     "Placeholder note two"]},
         ]},
        {"type": "agency", "id": "agency", "kicker": "06 · The Agency",
         "title": "Three reasons. They matter for BZ specifically.",
         "cells": [
             {"mark": "▸ ONE", "h": "Co-builders, not vendors",
              "p": "Placeholder — same agency positioning as canonical."},
             {"mark": "▸ TWO", "h": "One studio, three engines",
              "p": "Placeholder — brand, production, technology under one roof."},
             {"mark": "▸ THREE", "h": "Placeholder differentiator",
              "p": "Replace with the reason that matters specifically for BZ Fitness."},
         ]},
    ],
}


if __name__ == "__main__":
    print("Built:", T.build(DATA))
