"""
Roca Fuels — the canonical reference proposal.

Migrated verbatim from Adaline-BC/Rocafuels_proposal (GitHub canonical). This is
the gold-standard instance: every future proposal mirrors this structure, tone,
investment layout, and CTA. Accent: black & white (monochrome) per client.

Run:  python3 _build/build_rocafuel.py
"""

import template as T

# Black & white accent — the four canonical hues collapse to ink / soft-ink.
BW_PALETTE = "--red:#f5f1ea;--yellow:#f5f1ea;--green:#d8d3cc;--blue:#807a72;"

DATA = {
    "slug": "rocafuel",
    "client": "Roca Fuels",
    "title": "Project Proposal · Roca Fuels",
    "description": "Project Proposal for Roca Fuels — prepared by Adaline.",
    "palette": BW_PALETTE,

    "nav_title": "Roca Fuels",
    "nav_sub": "Project Proposal",
    "topnav": [
        ("brief", "Brief"), ("build", "Build"), ("process", "Process"),
        ("timeline", "Timeline"), ("investment", "Investment"), ("agency", "Agency"),
    ],
    "menu": [
        ("cover", "Cover", "00"), ("brief", "The Brief", "01"),
        ("build", "What We Build", "02"), ("process", "How We Work", "03"),
        ("timeline", "Timeline", "04"), ("investment", "The Investment", "05"),
        ("agency", "The Agency", "06"), ("legal", "The Fine Print", "07"),
    ],

    "hero": {
        "tag": "Project Proposal",
        "meta": [("Date", "14 June 2026"), ("Valid", "10 days from issue")],
        "prepared_label": "Prepared for",
        "title_html": "Roca<br/>Fuels.",
        "sub": ["Authorised Dealer", "MRPL", "ONGC Group", "Calicut, Kerala"],
        "desc": "A 36-month brand programme across four connected workstreams. Built as one "
                "identity, not four vendors. Scoped, paced, and measured for the long horizon.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Thank You.",
        "cta": "HIT START",
        "cta_subject": "Roca Fuels — proposal acceptance",
        "next_line": "Or, to commence the engagement, reply to:",
    },

    "sections": [
        # ---------------------------------------------------------------- BRIEF
        {
            "type": "brief", "id": "brief", "kicker": "01 · The Brief",
            "title": "The fuel category competes on price. Roca's move is to compete on identity.",
            "sub": "Drive any 5 km in Calicut and the petrol pumps blur — yellow flags, red "
                   "discount boards, hand-painted offers taped to the canopy. Roca, with the MRPL "
                   "credential as foundation, can step out of that game entirely and build what the "
                   "category rarely attempts: a fuel station that operates as a brand.",
            "cells": [
                {"num": "▸ The Opportunity", "h": "The gap is identity, not price.",
                 "p": "Almost no station in the area competes on brand. MRPL backing, ONGC group "
                      "credentials, BIS-spec fuel, NABL-tested batches — Roca has the credentials "
                      "to step entirely out of the discount-board frame."},
                {"num": "▸ The Goal", "h": "The pump customers drive past three others to reach.",
                 "p": "Measured in recall, repeat visits, and the kind of recognition a discount "
                      "cannot buy. 36-month horizon. Premium positioning, held with discipline, "
                      "compounds."},
                {"num": "▸ The Approach", "h": "Four workstreams, one identity.",
                 "p": "A portfolio website, a monthly content engine, a print brand album, and a "
                      "customer engagement platform — built as one connected system. No "
                      "agency-juggling. No handoff friction."},
            ],
            "players_kicker": "▸ Who We're Speaking To",
            "players": [
                {"tag": "Player 01", "h": "The Local Regular",
                 "p": "Fills twice a week, lives within 5 km, same route, same time of day. Becomes "
                      "loyal passively — by Roca becoming the habit."},
                {"tag": "Player 02", "h": "The Premium Owner",
                 "p": "Newer car, sometimes premium fuel, reads the small print on the pump. Wins on "
                      "credentials told plainly — MRPL, NABL, BIS spec."},
                {"tag": "Player 03", "h": "The Fleet & B2B",
                 "p": "3+ vehicles, credit terms, statement accuracy. Highest LTV per customer when "
                      "won. Near-impossible to poach once locked in."},
            ],
        },

        # ---------------------------------------------------------------- BUILD
        {
            "type": "build", "id": "build", "kicker": "02 · What We Build",
            "title": "Four deliverables. Each scoped. Each priced. Each transparent.",
            "sub": "Take one, take two, take all four. Every deliverable works standalone and "
                   "compounds when stacked. Tap each tab to see what's inside — or use the bundle "
                   "calculator below to mix and match.",
            "tabs": [
                {
                    "num": "01", "name": "Website", "h": "Portfolio Website",
                    "lead": "A fast, modern Next.js website that answers “Are they open? Where? "
                            "What do they sell? Can I trust them?” in under three seconds on a "
                            "mobile network. SEO-engineered for local search.",
                    "lists": [
                        {"label": "▸ Sitemap", "items": [
                            "Home — hero video, MRPL credentials, services snapshot, one-tap directions",
                            "About — origin, MRPL partnership, brand values",
                            "Quality — fuel testing, batch traceability, BIS spec explained",
                            "Services — grades, allied services, B2B / fleet offerings",
                            "Engagement Programme — lucky draw, loyalty, enrolment",
                            "Locate Us — interactive map, hours, per-outlet contact",
                            "Contact + Privacy + Terms"]},
                        {"label": "▸ Performance Targets", "items": [
                            "Sub-2.5s mobile load on 4G",
                            "WCAG AA accessibility compliance",
                            "Schema.org petrol-station rich results on Google",
                            "Top-3 organic ranking on neighbourhood-based searches by month six"]},
                    ],
                    "price_label": "One-time investment", "price": "₹68,500",
                    "price_note": "+ 1 year hosting included",
                    "meta": [("Duration", "16–18 days"), ("Tech", "Next.js + Vercel"),
                             ("Support", "30 days included"), ("Renewal", "From year 2")],
                },
                {
                    "num": "02", "name": "Content Engine", "h": "Monthly Content Engine",
                    "lead": "Eight posts a month. Two a week, alternating reels and static, captured "
                            "in a single monthly shoot day, delivered for review two weeks before "
                            "posting. Restraint, consistency, and craft over volume.",
                    "lists": [
                        {"label": "▸ Reel Concepts (rotating monthly)", "items": [
                            "The 6 AM Open — cinematic timelapse of the station coming alive",
                            "Trace the Drop — fuel journey from refinery to nozzle",
                            "Faces at the Forecourt — honest staff portraits",
                            "30-Second Fuel Fact — designed text-on-screen explainer",
                            "The Walk-Through — architectural tour of operations"]},
                        {"label": "▸ What's Included Monthly", "items": [
                            "Content strategy + calendar planning",
                            "4 cinematic reels + 4 static creatives",
                            "One full shoot day with Motiontape crew",
                            "Caption + hashtag curation, on-brand voice",
                            "Engagement & community management (4-hour response window)",
                            "Monthly reporting dashboard"]},
                    ],
                    "price_label": "Monthly retainer",
                    "price": "₹31,000<span style=\"font-size:18px;color:var(--muted);font-weight:400\">/mo</span>",
                    "price_note": "Per outlet · ongoing",
                    "meta": [("Posts", "8 per month"), ("Shoot day", "1 per month"),
                             ("Response", "4-hour window"), ("Reporting", "Monthly + Quarterly")],
                },
                {
                    "num": "03", "name": "Brand Album", "h": "Brand Album",
                    "lead": "A 16-page printed brand book. Saddle-stitched A5, uncoated premium paper, "
                            "image-led layout. Used for fleet pitches, MRPL partnership reviews, and as "
                            "walk-in collateral that survives the meeting.",
                    "lists": [
                        {"label": "▸ Contents (16 pages)", "items": [
                            "Cover · Origin Note · The MRPL Standard",
                            "The Forecourt (architectural spread) · What We Pump",
                            "The People · Voices of the Drivers",
                            "Identity System · The Roadmap · Back Cover"]},
                        {"label": "▸ Deliverable", "items": [
                            "Print-ready PDF with bleed marks & cropmarks",
                            "InDesign source files on handover",
                            "Editorial copywriting included",
                            "Photography from monthly shoot library",
                            "Production printing quoted separately on request"]},
                    ],
                    "price_label": "One-time deliverable", "price": "₹9,500",
                    "price_note": "16 pages · print-ready PDF",
                    "meta": [("Format", "A5 saddle-stitched"), ("Pages", "16, full colour"),
                             ("Sources", "InDesign included"), ("Printing", "Quoted on request")],
                },
                {
                    "num": "04", "name": "Engagement Engine", "h": "Customer Engagement Engine",
                    "lead": "A weekly lucky draw + loyalty points system that turns every fill-up into "
                            "customer data. QR-based entry at the pump (with cashier tablet backup), "
                            "WhatsApp confirmations, admin dashboard, cryptographic draw with audit log.",
                    "lists": [
                        {"label": "▸ Four Connected Surfaces", "items": [
                            "Customer QR entry form (mobile PWA, under 20 seconds)",
                            "Cashier tablet app — bill verification & fallback entry",
                            "Admin dashboard — customers, entries, draws, analytics, export",
                            "Loyalty engine — Bronze / Silver / Gold tiers, redemption via WhatsApp"]},
                        {"label": "▸ Compliance Built In", "items": [
                            "Positioned as loyalty programme, not lottery — in-kind prizes only",
                            "Published T&Cs, tamper-proof cryptographic draw",
                            "DPDP Act-compliant data handling, consent at entry",
                            "WhatsApp Business API via BSP (AiSensy / Interakt)",
                            "Roca owns 100% of customer data — Adaline is processor only"]},
                    ],
                    "price_label": "One-time build", "price": "₹95,000",
                    "price_note": "+ ₹3,000/mo hosting",
                    "meta": [("Build time", "30–35 days"), ("WhatsApp", "At cost pass-through"),
                             ("Data owner", "Roca Fuels"), ("Support", "30 days included")],
                },
            ],
        },

        # -------------------------------------------------------------- PROCESS
        {
            "type": "process", "id": "process", "kicker": "03 · How We Work",
            "title": "Four phases. Documented. Scoped. No surprise turns.",
            "sub": "A creative engagement falls apart in the middle when nobody knows what phase "
                   "they're in. This is how it runs — written down up-front, signed off at the gates.",
            "steps": [
                {"n": "PHASE 01", "h": "Brief",
                 "p": "Discovery, outlet visit, audience priority, locked brand voice and visual direction."},
                {"n": "PHASE 02", "h": "Plan",
                 "p": "Strategy, calendar, architecture — all written down, all signed off before execution."},
                {"n": "PHASE 03", "h": "Create",
                 "p": "Photography + design + development by the right specialists. One studio, three engines."},
                {"n": "PHASE 04", "h": "Review",
                 "p": "Structured feedback rounds. Notion workspace, shared calendar, dedicated Account Lead."},
            ],
            "principles": [
                {"label": "▸ Visual Direction", "h": "One look, locked across every frame.",
                 "p": "Architectural framing, near-dusk photography, controlled saturation, deep blacks. "
                      "Honesty over shine — no stock, no template effects, no trending presets. The "
                      "system is documented in the brand album and applied across web, social, print, and signage."},
                {"label": "▸ Growth Strategy", "h": "Organic, local, built to compound.",
                 "p": "Google Business Profile as the primary channel (drives more directions-clicks than "
                      "Instagram). Local SEO engineering for neighbourhood-based searches. Two or three "
                      "quarterly creator partnerships in the 10K–100K Calicut range. Response within 4 "
                      "working hours — including the negative ones."},
            ],
        },

        # ------------------------------------------------------------- TIMELINE
        {
            "type": "timeline", "id": "timeline", "kicker": "04 · Timeline",
            "title": "Two parallel tracks. Website in 4 weeks. Full system in 7–8 weeks.",
            "sub": "Tracks A and B share a discovery phase, then run in parallel. The website goes "
                   "live first — brand presence doesn't wait on the deeper system.",
            "tracks": [
                {"name": "▸ Track A — Portfolio Website", "dur": "16–18 working days",
                 "phases": [
                     {"num": "P1", "name": "Discovery", "dur": "2 days"},
                     {"num": "P2", "name": "Design", "dur": "3 days"},
                     {"num": "P3", "name": "Development", "dur": "7 days"},
                     {"num": "P4", "name": "Testing", "dur": "2 days"},
                     {"num": "P5", "name": "Launch", "dur": "2 days"}]},
                {"name": "▸ Track B — Engagement Engine", "dur": "30–35 working days",
                 "phases": [
                     {"num": "E1", "name": "Compliance", "dur": "4 days"},
                     {"num": "E2", "name": "UI / UX", "dur": "5 days"},
                     {"num": "E3", "name": "Backend", "dur": "10 days"},
                     {"num": "E4", "name": "Frontend", "dur": "10 days"},
                     {"num": "E5", "name": "Testing", "dur": "4 days"},
                     {"num": "E6", "name": "Launch", "dur": "2 days"}]},
            ],
            "note": "<strong>Social Media + Brand Album</strong> begin alongside Track A and continue "
                    "as ongoing / one-off. The website goes live around week 4; the engagement system "
                    "around week 7–8.",
        },

        # ----------------------------------------------------------- INVESTMENT
        {
            "type": "investment", "id": "investment", "kicker": "05 · The Investment",
            "title": "Four deliverables. One clear number.",
            "sub": "Total first-month commitment for the full programme. Toggle items below to see "
                   "how the number changes — no upsell traps, no hidden line items.",
            "hero": {
                "label": "▸ FULL PROGRAMME · FIRST MONTH",
                "title": "Website + Album + Engagement + Social Month 1",
                "desc": "All four workstreams launched together. Three one-time builds plus the first "
                        "month of social media retainer and engagement hosting. Subsequent months are "
                        "recurring only.",
                "price": "₹2,07,000",
            },
            "rows": [
                {"num": "01", "name": "Portfolio Website",
                 "note": "One-time · includes 1 yr hosting + 30-day support",
                 "price": "₹68,500", "price_val": 68500, "recurring_val": 0, "short": "Website"},
                {"num": "02", "name": "Social Media Engine · Month 1",
                 "note": "8 posts · monthly shoot · community mgmt",
                 "price": "₹31,000", "price_val": 31000, "recurring_val": 31000, "short": "Social retainer"},
                {"num": "03", "name": "Brand Album",
                 "note": "16-page print-ready PDF + source files",
                 "price": "₹9,500", "price_val": 9500, "recurring_val": 0, "short": "Brand Album"},
                {"num": "04", "name": "Customer Engagement Engine",
                 "note": "Full build + 30-day support + month 1 hosting",
                 "price": "₹98,000", "price_val": 98000, "recurring_val": 3000, "short": "Engagement hosting"},
            ],
            "recur": {"l": "From <strong>Month 2 onward</strong> — social retainer + engagement hosting",
                      "r": "₹34,000 / month"},
            "notes": [
                {"label": "▸ Payment Schedule", "items": [
                    "40% deposit on engagement start",
                    "40% at design / mid-project sign-off",
                    "20% on final delivery &amp; handover",
                    "Monthly retainers invoiced in advance, 7-day terms"]},
                {"label": "▸ Things to Note", "items": [
                    "All prices exclude applicable GST",
                    "WhatsApp messaging billed at cost (~₹0.13 utility / ~₹0.78 marketing per message)",
                    "Prize fund managed directly by Roca — in-kind only, no cash",
                    "Third-party costs (ad spend, paid plugins, print production) at cost, pre-approved"]},
            ],
        },

        # --------------------------------------------------------------- AGENCY
        {
            "type": "agency", "id": "agency", "kicker": "06 · The Agency",
            "title": "Three reasons. They matter for Roca specifically.",
            "cells": [
                {"mark": "▸ ONE", "h": "Co-builders, not vendors",
                 "p": "We sit on the same side of the table as the brands we work with. Roca's growth "
                      "is the metric — not the hours billed. We push back when we disagree, propose "
                      "harder when something feels soft, and stay engaged after launch."},
                {"mark": "▸ TWO", "h": "One studio, three engines",
                 "p": "Brand & consulting, production, and technology — under one roof. No "
                      "agency-versus-developer finger-pointing when something breaks at 9 PM on a Friday."},
                {"mark": "▸ THREE", "h": "Premium positioning specialists",
                 "p": "Holding a premium voice under category pressure — against the discount-shout "
                      "reflex of fuel retail — is hard, and it's specifically what we're built to do."},
            ],
        },

        # ---------------------------------------------------------------- LEGAL
        {
            "type": "legal", "id": "legal", "kicker": "07 · The Fine Print",
            "title": "Privacy Policy & Terms — tap to expand.",
            "sub": "Both documents are full, web-grade legal foundations. Privacy Policy governs "
                   "customer data in the engagement engine. Terms govern the engagement between Roca "
                   "Fuels and Myadaline Communications LLP.",
            "docs": [
                {
                    "id": "acc-privacy", "anum": "Document 01",
                    "title": "Privacy Policy — Roca Fuels Engagement Engine",
                    "meta": [("Effective", "Upon launch"), ("Version", "1.0"),
                             ("Data Fiduciary", "Roca Fuels"), ("Governing Law", "DPDP Act 2023")],
                    "toc": ["Overview & Scope", "Information We Collect", "How We Use Information",
                            "Legal Basis", "Sharing & Disclosure", "Data Retention", "Your Rights",
                            "Data Security", "Cookies", "Children's Privacy", "Changes",
                            "Grievance & Contact"],
                    "sections": [
                        {"h": "Overview & Scope", "body":
                         "<p>This Privacy Policy describes how Roca Fuels (the “Data Fiduciary”) "
                         "collects, uses, stores, and protects personal information of customers "
                         "participating in the Customer Engagement Engine — the QR entry form, lucky "
                         "draw, loyalty rewards, and associated WhatsApp communications. Governed by the "
                         "Digital Personal Data Protection Act, 2023 (“DPDP Act”) and the "
                         "Information Technology Act, 2000.</p>"},
                        {"h": "Information We Collect", "body":
                         "<span class=\"lsub\">Provided directly</span><ul>"
                         "<li>Vehicle registration number — to associate entries and prevent duplicates</li>"
                         "<li>WhatsApp mobile number — for confirmations, points updates, and (with separate consent) marketing</li>"
                         "<li>Fuelling amount — to award loyalty points and verify eligibility</li>"
                         "<li>Optional bill photograph — aids staff verification at entry</li>"
                         "<li>Customer name (optional) — for personalisation only</li></ul>"
                         "<span class=\"lsub\">Collected automatically</span><ul>"
                         "<li>Date, time, and outlet of each entry</li>"
                         "<li>Device and browser information at the QR form</li>"
                         "<li>WhatsApp delivery and read receipts where available</li></ul>"
                         "<p><strong>We do not collect:</strong> identity documents, financial accounts, "
                         "biometric data, government IDs, or location data beyond the outlet of entry.</p>"},
                        {"h": "How We Use Information", "body":
                         "<ul><li>Register and verify lucky-draw entries</li>"
                         "<li>Calculate, credit, and redeem loyalty points</li>"
                         "<li>Send transactional WhatsApp messages (confirmations, balances, results)</li>"
                         "<li>Send marketing WhatsApp messages only with separate explicit consent</li>"
                         "<li>Prevent fraud and ensure draw integrity</li>"
                         "<li>Improve the programme through aggregated, non-identifying analysis</li></ul>"},
                        {"h": "Legal Basis for Processing", "body":
                         "<ul><li><strong>Consent</strong> — for collection and participation; informed, specific, withdrawable</li>"
                         "<li><strong>Separate consent</strong> — for marketing messages, independent of programme consent</li>"
                         "<li><strong>Legitimate interest</strong> — fraud prevention and aggregate analytics</li>"
                         "<li><strong>Legal obligation</strong> — where required by law or court order</li></ul>"},
                        {"h": "Information Sharing & Disclosure", "body":
                         "<p>We do not sell or rent personal information. Information is shared only with:</p><ul>"
                         "<li><strong>Service providers (Data Processors)</strong> — WhatsApp BSP, cloud hosting provider, and Myadaline Communications LLP (Adaline) as platform operator. All bound by data-processing agreements.</li>"
                         "<li><strong>Legal disclosure</strong> — where required by law, regulation, or court order</li>"
                         "<li><strong>Business transfers</strong> — in event of merger or acquisition, with prior notice</li></ul>"},
                        {"h": "Data Retention", "body":
                         "<ul><li><strong>Entry records:</strong> active programme cycle + 12 months (audit / dispute window)</li>"
                         "<li><strong>Loyalty points history:</strong> active membership + 24 months from last transaction</li>"
                         "<li><strong>WhatsApp message logs:</strong> 12 months from dispatch</li>"
                         "<li><strong>Bill photographs:</strong> 90 days post-verification, then deleted</li>"
                         "<li><strong>Anonymised analytics:</strong> may be retained indefinitely (no longer identifies you)</li></ul>"},
                        {"h": "Your Rights & Choices", "body":
                         "<p>Subject to applicable law, you have:</p><ul>"
                         "<li><strong>Right of access</strong> to your information and a summary</li>"
                         "<li><strong>Right of correction</strong> for inaccurate or incomplete data</li>"
                         "<li><strong>Right of erasure</strong>, subject to legal retention</li>"
                         "<li><strong>Right to withdraw consent</strong> at any time, as easily as given</li>"
                         "<li><strong>Right to nominate</strong> someone to exercise rights on your behalf</li>"
                         "<li><strong>Right to grievance redressal</strong> with our Grievance Officer</li></ul>"
                         "<p>Reply to any of our WhatsApp messages with the word <strong>“PRIVACY”</strong> to exercise any of these rights.</p>"},
                        {"h": "Data Security", "body":
                         "<p>Reasonable security measures include TLS encryption in transit, encryption at "
                         "rest for sensitive data, role-based admin access, audit logging of all "
                         "administrative actions, regular backups, and security reviews. Personal-data "
                         "breaches likely to cause significant harm will be notified to affected individuals "
                         "and the Data Protection Board of India per DPDP Act requirements.</p>"},
                        {"h": "Cookies & Tracking Technologies", "body":
                         "<p>The platform uses only minimum cookies necessary for functionality — "
                         "sessions, language preference. No third-party advertising cookies, no cross-site "
                         "tracking, no individual profiling analytics.</p>"},
                        {"h": "Children's Privacy", "body":
                         "<p>The Engagement Engine is intended for individuals aged 18+. We do not knowingly "
                         "collect information from minors. Any inadvertently collected minor data will be "
                         "deleted without delay on becoming aware.</p>"},
                        {"h": "Changes to This Policy", "body":
                         "<p>Material changes will be notified to active participants via WhatsApp and "
                         "reflected in the “Last Updated” date. Continued participation after notice "
                         "constitutes acceptance.</p>"},
                        {"h": "Grievance & Contact", "body":
                         "<p>A designated Grievance Officer will be named by Roca Fuels at launch in "
                         "accordance with the DPDP Act. Contact details published at the entry form and on "
                         "Roca Fuels' website. Platform operator queries: Myadaline Communications LLP, "
                         "bettercall@myadaline.com, +91 90481 91616.</p>"},
                    ],
                },
                {
                    "id": "acc-terms", "anum": "Document 02",
                    "title": "Terms & Conditions of Engagement",
                    "meta": [("Effective", "On acceptance"), ("Version", "2.0"),
                             ("Valid", "10 days from issue"), ("Jurisdiction", "Calicut, Kerala")],
                    "toc": ["Scope & Acceptance", "The Engagement", "Fees & Payment",
                            "Changes & Revisions", "Deliverables & Acceptance", "Intellectual Property",
                            "Data Protection", "Confidentiality", "Third-Party Services", "Warranties",
                            "Liability", "Termination", "Force Majeure", "Disputes", "Notices",
                            "Miscellaneous"],
                    "sections": [
                        {"h": "Scope & Acceptance", "body":
                         "<p>This Proposal sets out the scope of services provided by Myadaline "
                         "Communications LLP (operating as Adaline, the “Agency”) to Roca Fuels "
                         "(the “Client”). Valid for ten (10) days from issue. The engagement "
                         "commences upon written acceptance, signed engagement letter, or receipt of the deposit.</p>"},
                        {"h": "The Engagement", "body":
                         "<p>The Agency will deliver the four workstreams described in Section 2 of this "
                         "Proposal. A project lead and team will be assigned appropriate to scope. The "
                         "Client will provide timely access to information, brand assets, approvals, and "
                         "decisions necessary for delivery.</p>"},
                        {"h": "Fees & Payment Terms", "body":
                         "<p>All fees per Section 5 of this Proposal, exclusive of GST.</p>"
                         "<span class=\"lsub\">Payment schedule</span><ul>"
                         "<li>40% deposit on engagement start</li>"
                         "<li>40% at mid-project / design approval milestone</li>"
                         "<li>20% on final delivery and handover</li>"
                         "<li>Monthly retainers invoiced in advance, payable within 7 days</li>"
                         "<li>Third-party pass-throughs billed at cost with prior approval</li></ul>"
                         "<p><strong>Late payment:</strong> 1.5% per month compounded after 15 days. "
                         "Suspension of services possible until cleared.</p>"},
                        {"h": "Change Requests & Revisions", "body":
                         "<p>Each deliverable includes defined revision rounds per Section 5. Additional "
                         "revisions and scope-expanding changes require a written Change Order with fee and "
                         "timeline impact agreed before execution.</p>"},
                        {"h": "Deliverables & Acceptance", "body":
                         "<p>Deliverables submitted at each stage per Section 4 timeline. Client provides "
                         "consolidated feedback within five (5) working days. Silence beyond this window = "
                         "deemed acceptance. Final delivery conditional on final payment.</p>"},
                        {"h": "Intellectual Property", "body":
                         "<p>On final payment, the Agency assigns to the Client all IP rights in approved "
                         "deliverables (website, brand album, social-media assets, engagement engine "
                         "codebase and config). Agency retains: pre-existing tools and frameworks; "
                         "unselected drafts and concepts; the right to feature work in its portfolio "
                         "(subject to confidentiality). Third-party assets remain governed by their "
                         "original licence terms.</p>"},
                        {"h": "Data Protection & Customer Records", "body":
                         "<p>All personal data collected through the Engagement Engine is the sole property "
                         "of the Client (Data Fiduciary under the DPDP Act, 2023). The Agency operates as "
                         "Data Processor only, processing on documented Client instructions per the Privacy "
                         "Policy. On termination, all personal data is returned or deleted as directed.</p>"},
                        {"h": "Confidentiality", "body":
                         "<p>Each party treats as confidential all non-public information disclosed in "
                         "connection with the engagement — business strategy, financials, customer info, "
                         "technical specifications. Confidentiality survives termination for three (3) years. "
                         "Agency portfolio rights are limited to publicly visible deliverables.</p>"},
                        {"h": "Third-Party Materials & Services", "body":
                         "<p>Deliverables may involve third-party platforms — hosting, WhatsApp BSP, "
                         "payment gateway, stock libraries, plugins. Charges passed through at cost with "
                         "prior approval. Agency makes no warranties on third-party availability, "
                         "performance, or pricing.</p>"},
                        {"h": "Warranties & Disclaimers", "body":
                         "<p>The Agency warrants professional performance consistent with industry standards "
                         "and substantial conformity of deliverables to agreed specifications at final "
                         "acceptance. Otherwise, deliverables provided <strong>“as is”</strong>. No "
                         "warranty of specific business outcomes — follower growth, sales lift, customer "
                         "acquisition — as these depend on factors outside the Agency's control.</p>"},
                        {"h": "Limitation of Liability", "body":
                         "<p>Agency's aggregate liability shall not exceed the total fees paid in the 12 "
                         "months preceding the claim. No liability for indirect, incidental, special, or "
                         "consequential damages — including loss of profits, business opportunity, data, "
                         "or reputation — regardless of foreseeability.</p>"},
                        {"h": "Termination", "body":
                         "<p><strong>For convenience:</strong> either party with 30 days' written notice. "
                         "Client pays for work completed up to effective date plus non-cancellable "
                         "third-party commitments.</p>"
                         "<p><strong>For cause:</strong> immediate on material breach uncured within 15 days of notice.</p>"
                         "<p><strong>Survival:</strong> payment obligations, confidentiality, and provisions that should survive — do.</p>"},
                        {"h": "Force Majeure", "body":
                         "<p>No liability for failure or delay due to events beyond reasonable control — "
                         "natural disasters, pandemic, government action, civil unrest, war, terrorism, "
                         "telecoms failure. Affected party notifies in writing, mitigates, resumes when "
                         "practicable. After 60 consecutive days of force majeure, either party may terminate.</p>"},
                        {"h": "Governing Law & Dispute Resolution", "body":
                         "<p>Governed by laws of India. First attempt: good-faith negotiation between "
                         "authorised representatives within 30 days of dispute notice. Failing that: "
                         "arbitration under the Arbitration and Conciliation Act, 1996, sole arbitrator "
                         "mutually appointed, seat at Calicut (Kozhikode), Kerala, language English. Subject "
                         "to the above, Calicut courts have exclusive jurisdiction.</p>"},
                        {"h": "Notices & Communication", "body":
                         "<p>Formal notices in writing by email. Agency address of record: "
                         "<strong>bettercall@myadaline.com</strong>. Day-to-day communication via agreed "
                         "channels (email, WhatsApp, Notion) — not subject to formal-notice requirement.</p>"},
                        {"h": "Miscellaneous", "body":
                         "<ul><li><strong>Entire agreement:</strong> this Proposal + executed engagement letter is the complete understanding</li>"
                         "<li><strong>Amendment:</strong> in writing, signed by both parties</li>"
                         "<li><strong>Severability:</strong> invalid provisions don't affect the rest</li>"
                         "<li><strong>No waiver:</strong> delay in exercising rights is not a waiver</li>"
                         "<li><strong>Assignment:</strong> requires written consent except in merger / acquisition</li>"
                         "<li><strong>Independent contractor:</strong> no partnership, joint venture, agency, or employment relationship</li>"
                         "<li><strong>Counterparts:</strong> may be executed electronically</li></ul>"},
                    ],
                },
            ],
        },
    ],
}


if __name__ == "__main__":
    print("Built:", T.build(DATA))
