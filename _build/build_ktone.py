"""
K Tone — client-ready proposal.

Built from the K Tone proposal brief (client-supplied PDF) + pricing given
directly by the Management. Car audio & stereo specialists — installation,
DSP tuning/programming, custom-fabricated enclosures for custom builds, parts
at competitive pricing, sound damping cheaper than the market. Calicut, Kerala.

Investment is a mixed one-time + monthly bundle (Landing Page + Branding as
one-time builds; Marketing & Strategy + Content Development as ongoing
retainers) — uses the toggle bundle calculator, same shape as the Roca Fuels
canonical. Accent: deep teal (#1f9e8f), placeholder pending Management sign-off
since K Tone has no fixed brand colour on file yet.

Run:  python3 _build/build_ktone.py
"""

import template as T

PALETTE = "--red:#1f9e8f;--yellow:#1f9e8f;--green:#5ad1c4;--blue:#5a8eff;"

DATA = {
    "slug": "ktone",
    "client": "K Tone",
    "title": "Project Proposal · K Tone",
    "description": "Project Proposal for K Tone — prepared by Adaline.",
    "palette": PALETTE,

    "nav_title": "K Tone",
    "nav_sub": "Project Proposal",
    "topnav": [("brief", "Brief"), ("build", "Build"), ("process", "Process"),
               ("timeline", "Timeline"), ("investment", "Investment"), ("agency", "Agency")],
    "menu": [("cover", "Cover", "00"), ("brief", "The Brief", "01"),
             ("build", "What We Build", "02"), ("process", "How We Work", "03"),
             ("timeline", "Timeline", "04"), ("investment", "The Investment", "05"),
             ("agency", "The Agency", "06"), ("legal", "The Fine Print", "07")],

    "hero": {
        "tag": "Project Proposal",
        "meta": [("Date", "1 July 2026"), ("Valid", "10 days from issue")],
        "prepared_label": "Prepared for",
        "title_html": "K<br/>Tone.",
        "sub": ["Car Audio & Tuning", "Custom Builds", "Calicut, Kerala"],
        "desc": "A brand visibility and lead-generation programme — positioning, a landing page "
                "built to convert, and a content engine that finally shows the work behind the "
                "sound. Built as one connected system, not three separate vendors.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Let's Tune It.",
        "cta": "HIT START",
        "cta_subject": "K Tone — proposal acceptance",
    },

    "sections": [
        {
            "type": "brief", "id": "brief", "kicker": "01 · The Brief",
            "title": "Everyone sells car speakers. K Tone tunes them, builds the shell, and "
                     "prices it fairly — none of which shows up online yet.",
            "sub": "K Tone doesn't compete on stocking the same stereo boxes as everyone else — the "
                   "edge is in the install: custom-fabricated enclosures for the build, DSP tuning "
                   "programmed to the cabin, and sound damping priced below the market. That's a "
                   "specialist's business. Right now, none of it is visible past word of mouth.",
            "cells": [
                {"num": "▸ The Reality", "h": "The install is the differentiator. The internet doesn't know it.",
                 "p": "Custom shell fabrication, DSP-programmed tuning, and damping priced under the "
                      "competition — this is specialist work most car audio dealers in Kerala don't "
                      "even attempt. It's invisible to anyone who hasn't already walked in."},
                {"num": "▸ The Opportunity", "h": "Car audio buyers research before they show up.",
                 "p": "Enthusiasts building a custom system, everyday owners chasing better sound, "
                      "resellers comparing part pricing — all of them shortlist online first. A page "
                      "and social presence that actually shows the tuning and the builds becomes the "
                      "first sale."},
                {"num": "▸ The Objective", "h": "Make the craft visible. Turn visibility into inquiries.",
                 "p": "Brand positioning that states the specialism plainly, a landing page built to "
                      "capture the inquiry, and a content engine that shows the builds as they happen "
                      "— connected as one system, not three separate vendors."},
            ],
            "players_kicker": "▸ Who We're Speaking To",
            "players": [
                {"tag": "Player 01", "h": "The Build Enthusiast",
                 "p": "Wants a fully custom system — enclosure fabricated to spec, tuning dialled to "
                      "the cabin. Researches heavily, compares installers on craft, not price."},
                {"tag": "Player 02", "h": "The Everyday Upgrade",
                 "p": "Stock system sounds thin, wants it fixed without overspending. Price-sensitive, "
                      "needs the value made obvious — parts, damping, labour."},
                {"tag": "Player 03", "h": "The Reseller & Referral",
                 "p": "Compares part pricing across dealers, refers installers to their own customers. "
                      "Wins repeat business once trust and pricing are proven."},
            ],
        },

        {
            "type": "build", "id": "build", "kicker": "02 · What We Build",
            "title": "Four deliverables. Priced individually, built as one system.",
            "sub": "Landing page, brand positioning, ongoing marketing strategy, and social content "
                   "production — each scoped and priced on its own, but designed to compound when run "
                   "together. Tap each tab to see what's inside.",
            "tabs": [
                {
                    "num": "01", "name": "Landing Page", "h": "Landing Page Development",
                    "lead": "A high-converting, mobile-first landing page built to answer the only "
                            "question that matters to a car audio buyer: can these people actually do "
                            "what I need, and how do I reach them. Every section built around the inquiry.",
                    "lists": [
                        {"label": "▸ Page Structure", "items": [
                            "Hero — the work, stated plainly: installs, tuning, custom builds",
                            "Services — stereo install, DSP tuning & programming, custom enclosure "
                            "fabrication, sound damping, parts & brands",
                            "Work Showcase — completed builds, before/after, damping jobs",
                            "Pricing Philosophy — how K Tone prices fairly against the market",
                            "Inquiry / Contact — WhatsApp-first lead capture, one tap",
                            "Location & Hours"]},
                        {"label": "▸ Conversion & Build", "items": [
                            "Lead capture and inquiry generation wired to WhatsApp + form",
                            "UI/UX wireframe and content structure built for mobile-first traffic",
                            "Service-focused copywriting — plain, specific, no jargon",
                            "Mobile-first responsive design, fast on 4G"]},
                    ],
                    "price_label": "One-time investment", "price": "₹56,000",
                    "price_note": "+ hosting & AMC billed separately (annual)",
                    "meta": [("Duration", "12–15 days"), ("Tech", "Modern responsive build"),
                             ("Hosting", "Billed separately, annual"), ("Support", "Included at launch")],
                },
                {
                    "num": "02", "name": "Branding", "h": "Brand & Services Marketing",
                    "lead": "Before a single ad runs, K Tone needs a clear position: what it does, "
                            "who it's for, and why it's priced the way it is. This workstream builds "
                            "that foundation — the messaging every future page, post, and pitch pulls from.",
                    "lists": [
                        {"label": "▸ Strategy Deliverables", "items": [
                            "Brand positioning and messaging strategy",
                            "Service communication framework — install, tuning, custom builds, parts, "
                            "damping, explained in plain language",
                            "Content pillars and communication guidelines",
                            "Digital marketing recommendations for visibility and lead generation"]},
                        {"label": "▸ Deliverable Format", "items": [
                            "Marketing strategy document, ready to brief any future vendor or hire",
                            "Messaging framework applied across the landing page and social content"]},
                    ],
                    "price_label": "One-time investment", "price": "₹35,000",
                    "price_note": "Strategy document + messaging framework",
                    "meta": [("Duration", "10–12 days"), ("Format", "Strategy document"),
                             ("Applies to", "Web + social"), ("Revisions", "1 round included")],
                },
                {
                    "num": "03", "name": "Marketing & Strategy", "h": "Marketing & Strategy — Monthly",
                    "lead": "Positioning only works if someone's running it. This is the ongoing "
                            "campaign planning and digital marketing execution that turns the landing "
                            "page into an inquiry pipeline — ad spend and platform costs billed "
                            "separately, at cost.",
                    "lists": [
                        {"label": "▸ Included Monthly", "items": [
                            "Marketing campaign planning and execution oversight",
                            "Digital marketing recommendations reviewed and adjusted monthly",
                            "Lead generation tracking against the landing page inquiry flow",
                            "Monthly performance and visibility recommendations"]},
                        {"label": "▸ Note", "items": [
                            "Ad spend (Meta, Google) billed separately, at cost, pre-approved"]},
                    ],
                    "price_label": "Monthly retainer",
                    "price": "₹12,000<span style=\"font-size:18px;color:var(--muted);font-weight:400\">/mo</span>",
                    "price_note": "Ad spend billed separately, at cost",
                    "meta": [("Focus", "Lead generation"), ("Reporting", "Monthly"),
                             ("Ad spend", "At cost, separate"), ("Reviews", "Monthly check-in")],
                },
                {
                    "num": "04", "name": "Content", "h": "Social Media Content Development",
                    "lead": "Professional photo and video production that finally shows the work — "
                            "the builds, the tuning, the shell fabrication — across Instagram, "
                            "Facebook, and LinkedIn. Planned on a monthly calendar, not posted on impulse.",
                    "lists": [
                        {"label": "▸ Monthly Production", "items": [
                            "Creative direction and content planning",
                            "Professional photo and video production of live builds",
                            "Brand films, reels, and short-form content",
                            "Service showcase videos — install, tuning, damping, custom shells",
                            "Social media creatives for ongoing visibility"]},
                        {"label": "▸ Platforms", "items": [
                            "Content optimised for Instagram, Facebook, LinkedIn, and other relevant "
                            "platforms",
                            "Monthly content calendar delivered ahead of posting"]},
                    ],
                    "price_label": "Monthly retainer",
                    "price": "₹27,000<span style=\"font-size:18px;color:var(--muted);font-weight:400\">/mo</span>",
                    "price_note": "Shoot day + edit + calendar, monthly",
                    "meta": [("Shoot day", "1 per month"), ("Deliverables", "Reels + statics + films"),
                             ("Calendar", "Delivered monthly"), ("Platforms", "IG · FB · LinkedIn")],
                },
            ],
        },

        {
            "type": "process", "id": "process", "kicker": "03 · How We Work",
            "title": "Four phases, each signed off before the next begins.",
            "sub": "A branding-plus-content engagement drifts when nobody owns the calendar. Here's "
                   "the structure that keeps position, page, and content moving together.",
            "steps": [
                {"n": "PHASE 01", "h": "Brief",
                 "p": "Discovery call, service and pricing audit, competitor scan, brand voice direction locked."},
                {"n": "PHASE 02", "h": "Plan",
                 "p": "Positioning and messaging strategy, landing page wireframe, content calendar "
                      "structure — signed off before build."},
                {"n": "PHASE 03", "h": "Create",
                 "p": "Landing page development, brand documents finalised, first content shoot scheduled."},
                {"n": "PHASE 04", "h": "Launch & Run",
                 "p": "Page live, campaign planning begins, monthly content production starts on calendar."},
            ],
            "principles": [
                {"label": "▸ Content Philosophy", "h": "The build is the content.",
                 "p": "Real installs, real tuning sessions, real fabrication — not stock car-audio "
                      "photography. The work is the proof; the camera just needs to show up."},
                {"label": "▸ Inquiry Philosophy", "h": "WhatsApp first. Page second. Ads last.",
                 "p": "Every page and post routes to a one-tap WhatsApp inquiry — that's how K Tone's "
                      "customers actually reach an installer. Ad spend amplifies once the page and "
                      "content are proven, not before."},
            ],
        },

        {
            "type": "timeline", "id": "timeline", "kicker": "04 · Timeline",
            "title": "Live in three weeks. Content running from month one.",
            "sub": "Landing page and branding run in parallel from kickoff. Marketing & Strategy and "
                   "Social Content begin as an ongoing monthly engagement alongside launch.",
            "tracks": [
                {"name": "▸ Track A — Landing Page", "dur": "12–15 working days",
                 "phases": [
                     {"num": "P1", "name": "Discovery", "dur": "2 days"},
                     {"num": "P2", "name": "Design", "dur": "3 days"},
                     {"num": "P3", "name": "Development", "dur": "5 days"},
                     {"num": "P4", "name": "Testing", "dur": "2 days"},
                     {"num": "P5", "name": "Launch", "dur": "1 day"}]},
                {"name": "▸ Track B — Branding", "dur": "10–12 working days",
                 "phases": [
                     {"num": "B1", "name": "Discovery & Audit", "dur": "3 days"},
                     {"num": "B2", "name": "Positioning & Messaging", "dur": "4 days"},
                     {"num": "B3", "name": "Pillars & Guidelines", "dur": "3 days"},
                     {"num": "B4", "name": "Sign-off", "dur": "1 day"}]},
            ],
            "note": "<strong>Marketing & Strategy</strong> and <strong>Social Media Content</strong> "
                    "begin as ongoing monthly engagements from kickoff — the first shoot and campaign "
                    "plan are scheduled inside week one, so content is already in motion by the time "
                    "the page goes live.",
        },

        {
            "type": "investment", "id": "investment", "kicker": "05 · The Investment",
            "title": "Four deliverables. One clear number.",
            "sub": "Total first-month commitment across the full programme. Toggle items below to see "
                   "how the number changes — ad spend and hosting/AMC are never bundled in, always "
                   "billed separately at cost.",
            "hero": {
                "label": "▸ FULL PROGRAMME · FIRST MONTH",
                "title": "Landing Page + Branding + Strategy + Content Month 1",
                "desc": "Both one-time builds plus the first month of marketing strategy and content "
                        "production. Subsequent months are recurring only.",
                "price": "₹1,30,000",
            },
            "rows": [
                {"num": "01", "name": "Landing Page Development",
                 "note": "One-time · hosting & AMC billed separately",
                 "price": "₹56,000", "price_val": 56000, "recurring_val": 0, "short": "Landing Page"},
                {"num": "02", "name": "Branding",
                 "note": "One-time · strategy document + messaging framework",
                 "price": "₹35,000", "price_val": 35000, "recurring_val": 0, "short": "Branding"},
                {"num": "03", "name": "Marketing & Strategy",
                 "note": "Monthly · campaign planning + lead tracking · ad spend at cost",
                 "price": "₹12,000", "price_val": 12000, "recurring_val": 12000, "short": "Marketing & Strategy"},
                {"num": "04", "name": "SM Content Development",
                 "note": "Monthly · shoot day + edit + content calendar",
                 "price": "₹27,000", "price_val": 27000, "recurring_val": 27000, "short": "Content Development"},
            ],
            "recur": {"l": "From <strong>Month 2 onward</strong> — marketing strategy + content development",
                      "r": "₹39,000 / month"},
            "notes": [
                {"label": "▸ Payment Schedule", "items": [
                    "40% deposit on engagement start",
                    "40% at design &amp; positioning sign-off",
                    "20% on landing page launch &amp; handover",
                    "Monthly retainers invoiced in advance, 7-day terms"]},
                {"label": "▸ Things to Note", "items": [
                    "All prices exclude applicable GST",
                    "Hosting &amp; AMC billed separately, annually, quoted on request",
                    "Ad spend (Meta, Google, etc.) billed at cost, pre-approved",
                    "Landing page content assumes product &amp; build photography access from K Tone"]},
            ],
        },

        {
            "type": "agency", "id": "agency", "kicker": "06 · The Agency",
            "title": "Three reasons we're a fit for K Tone.",
            "cells": [
                {"mark": "▸ ONE", "h": "We translate technical craft into plain language",
                 "p": "DSP tuning and custom fabrication are hard to explain to a buyer who just wants "
                      "better sound. We've done this translation before — spec-heavy work made simple "
                      "without dumbing it down."},
                {"mark": "▸ TWO", "h": "One studio, no handoffs",
                 "p": "Positioning, the landing page, and the monthly content shoot all sit with the "
                      "same team. No brief lost between a branding agency and a separate content vendor."},
                {"mark": "▸ THREE", "h": "Calicut, on the ground",
                 "p": "Based in Calicut, working across Kerala's local business landscape — we "
                      "understand the WhatsApp-first inquiry pattern and the word-of-mouth trust car "
                      "audio buyers actually run on."},
            ],
        },

        {
            "type": "legal", "id": "legal", "kicker": "07 · The Fine Print",
            "title": "Terms of Engagement — tap to expand.",
            "sub": "Standard agency terms governing the engagement between K Tone and Myadaline "
                   "Communications LLP. Plain English. Mutual.",
            "docs": [
                {
                    "id": "acc-terms", "anum": "Document 01",
                    "title": "Terms & Conditions of Engagement",
                    "meta": [("Effective", "On acceptance"), ("Version", "1.0"),
                             ("Valid", "10 days from issue"), ("Jurisdiction", "Calicut, Kerala")],
                    "toc": ["Scope & Acceptance", "The Engagement", "Fees & Payment", "Changes & Revisions",
                            "Deliverables & Acceptance", "Intellectual Property", "Confidentiality",
                            "Warranties", "Liability", "Termination", "Force Majeure", "Disputes",
                            "Notices", "Miscellaneous"],
                    "sections": [
                        {"h": "Scope & Acceptance", "body":
                         "<p>This Proposal sets out the scope of services provided by Myadaline "
                         "Communications LLP (operating as Adaline, the “Agency”) to K Tone (the "
                         "“Client”). Valid for ten (10) days from issue. The engagement commences upon "
                         "written acceptance, signed engagement letter, or receipt of the deposit.</p>"},
                        {"h": "The Engagement", "body":
                         "<p>The Agency will deliver the landing page, brand &amp; services marketing "
                         "strategy, and the ongoing marketing and content workstreams described in "
                         "Section 2 of this Proposal. The Client will provide timely access to brand "
                         "assets, build/service photography, approvals, and decisions necessary for "
                         "delivery.</p>"},
                        {"h": "Fees & Payment Terms", "body":
                         "<p>Full first-month engagement fee: ₹1,30,000, exclusive of GST. Recurring fee "
                         "from Month 2: ₹39,000/month.</p><span class=\"lsub\">Payment schedule</span><ul>"
                         "<li>40% deposit on engagement start</li>"
                         "<li>40% at design &amp; positioning sign-off</li>"
                         "<li>20% on landing page launch and handover</li>"
                         "<li>Monthly retainers invoiced in advance, payable within 7 days</li>"
                         "<li>Ad spend and hosting/AMC billed separately, at cost, with prior approval</li></ul>"
                         "<p><strong>Late payment:</strong> 1.5% per month compounded after 15 days from "
                         "invoice date.</p>"},
                        {"h": "Change Requests & Revisions", "body":
                         "<p>One round of revision included on the branding strategy document and the "
                         "landing page design. Additional revisions or scope-expanding changes require a "
                         "written Change Order with fee and timeline impact agreed before execution.</p>"},
                        {"h": "Deliverables & Acceptance", "body":
                         "<p>Deliverables submitted at each phase per Section 4 timeline. Client provides "
                         "consolidated feedback within five (5) working days. Silence beyond this window = "
                         "deemed acceptance. Final landing page delivery conditional on final payment of "
                         "that milestone.</p>"},
                        {"h": "Intellectual Property", "body":
                         "<p>On payment of each respective milestone, the Agency assigns to the Client all "
                         "IP rights in the approved deliverables — landing page codebase, brand strategy "
                         "document, and delivered social content assets. Agency retains: pre-existing tools "
                         "and frameworks; unselected drafts and concepts; the right to feature the work in "
                         "its portfolio (subject to confidentiality). Third-party assets (fonts, hosting, "
                         "stock libraries) remain governed by their original licence terms.</p>"},
                        {"h": "Confidentiality", "body":
                         "<p>Each party treats as confidential all non-public information disclosed in "
                         "connection with the engagement — business strategy, pricing, customer "
                         "information, supplier relationships. Confidentiality survives termination for "
                         "three (3) years. Agency portfolio rights are limited to publicly visible "
                         "deliverables.</p>"},
                        {"h": "Warranties & Disclaimers", "body":
                         "<p>The Agency warrants professional performance consistent with industry "
                         "standards and substantial conformity of deliverables to agreed specifications at "
                         "final acceptance. Otherwise, deliverables provided <strong>“as is”</strong>. No "
                         "warranty of specific business outcomes — inquiries, sales, follower growth — as "
                         "these depend on factors outside the Agency's control.</p>"},
                        {"h": "Limitation of Liability", "body":
                         "<p>Agency's aggregate liability shall not exceed the total fees paid in the 3 "
                         "months preceding the claim. No liability for indirect, incidental, special, or "
                         "consequential damages — including loss of profits, business opportunity, data, "
                         "or reputation — regardless of foreseeability.</p>"},
                        {"h": "Termination", "body":
                         "<p><strong>For convenience:</strong> either party with 14 days' written notice. "
                         "Client pays for work completed up to effective date plus non-cancellable "
                         "third-party commitments.</p>"
                         "<p><strong>For cause:</strong> immediate on material breach uncured within 10 "
                         "days of notice.</p>"
                         "<p><strong>Survival:</strong> payment obligations, confidentiality, IP "
                         "assignment, and provisions that should survive — do.</p>"},
                        {"h": "Force Majeure", "body":
                         "<p>No liability for failure or delay due to events beyond reasonable control — "
                         "natural disasters, government action, civil unrest, telecoms failure, "
                         "third-party service outage. Affected party notifies in writing, mitigates, "
                         "resumes when practicable.</p>"},
                        {"h": "Governing Law & Dispute Resolution", "body":
                         "<p>Governed by laws of India. First attempt: good-faith negotiation between "
                         "authorised representatives within 30 days of dispute notice. Failing that: "
                         "arbitration under the Arbitration and Conciliation Act, 1996, sole arbitrator "
                         "mutually appointed, seat at Calicut (Kozhikode), Kerala, language English. "
                         "Subject to the above, Calicut courts have exclusive jurisdiction.</p>"},
                        {"h": "Notices & Communication", "body":
                         "<p>Formal notices in writing by email. Agency address of record: "
                         "<strong>bettercall@myadaline.com</strong>. Day-to-day communication via agreed "
                         "channels (email, WhatsApp) — not subject to formal-notice requirement.</p>"},
                        {"h": "Miscellaneous", "body":
                         "<ul><li><strong>Entire agreement:</strong> this Proposal + executed engagement "
                         "letter is the complete understanding</li>"
                         "<li><strong>Amendment:</strong> in writing, signed by both parties</li>"
                         "<li><strong>Severability:</strong> invalid provisions don't affect the rest</li>"
                         "<li><strong>No waiver:</strong> delay in exercising rights is not a waiver</li>"
                         "<li><strong>Assignment:</strong> requires written consent except in merger / "
                         "acquisition</li>"
                         "<li><strong>Independent contractor:</strong> no partnership, joint venture, "
                         "agency, or employment relationship</li>"
                         "<li><strong>Counterparts:</strong> may be executed electronically</li></ul>"},
                    ],
                },
            ],
        },
    ],
}


if __name__ == "__main__":
    print("Built:", T.build(DATA))
