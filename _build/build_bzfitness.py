"""
BZ Fitness — client-ready proposal.

Migrated from Adaline-io/Bz-fitness-proposal. Kuwait commercial & household
fitness-equipment distributor; full website rebuild for a 500+ product catalog.
Accent: electric red-orange (#ff4d2e), from the source proposal.

Run:  python3 _build/build_bzfitness.py
"""

import template as T

PALETTE = "--red:#ff4d2e;--yellow:#ff4d2e;--green:#3dd483;--blue:#5a8eff;"

DATA = {
    "slug": "bz-fitness",
    "client": "BZ Fitness",
    "title": "Project Proposal · BZ Fitness",
    "description": "Project Proposal for BZ Fitness — prepared by Adaline.",
    "palette": PALETTE,

    "nav_title": "BZ Fitness",
    "nav_sub": "Project Proposal",
    "topnav": [("brief", "Brief"), ("build", "Build"), ("process", "Process"),
               ("timeline", "Timeline"), ("investment", "Investment"), ("agency", "Agency")],
    "menu": [("cover", "Cover", "00"), ("brief", "The Brief", "01"),
             ("build", "What We Build", "02"), ("process", "How We Work", "03"),
             ("timeline", "Timeline", "04"), ("investment", "The Investment", "05"),
             ("agency", "The Agency", "06"), ("legal", "The Fine Print", "07")],

    "hero": {
        "tag": "Project Proposal",
        "meta": [("Date", "23 June 2026"), ("Valid", "10 days from issue")],
        "prepared_label": "Prepared for",
        "title_html": "BZ<br/>Fitness.",
        "sub": ["Commercial & Household", "Fitness Equipment", "Kuwait", "Get in. Get Fit."],
        "desc": "A complete website rebuild — built to actually showcase the range, the machines, "
                "and the credibility behind BZ Fitness. Hosting, webmail, SEO foundation, and team "
                "training included.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Get in. Let's go.",
        "cta": "HIT START",
        "cta_subject": "BZ Fitness — website proposal acceptance",
    },

    "sections": [
        {
            "type": "brief", "id": "brief", "kicker": "01 · The Brief",
            "title": "500+ products. One of Kuwait's deepest fitness catalogs. A website that doesn't show any of it.",
            "sub": "BZ Fitness operates at distributor scale — five hundred-plus products across cardio, "
                   "pin-loaded strength, plate-loaded strength, free weights, and accessories. That's not a "
                   "product list, that's a serious operation. The current site treats it like a brochure: "
                   "surface-level category headers, placeholder product links, no detail pages, no spec sheets, "
                   "no inquiry flow. The business is significantly bigger than the website lets on.",
            "cells": [
                {"num": "▸ The Reality", "h": "The catalog is the business. The site hides it.",
                 "p": "500+ products across multiple categories and brand lines. The depth itself is the "
                      "competitive moat against smaller dealers. Right now, a buyer landing on bzfitness.com "
                      "can't browse the range, compare specs, or even see what's actually available."},
                {"num": "▸ The Opportunity", "h": "Kuwait's commercial buyers shortlist online.",
                 "p": "Gym owners, hotel chains, schools, sports clubs, premium residential — they research "
                      "before they call. A site that handles 500+ products cleanly, with proper category "
                      "navigation and inquiry flow, becomes the primary sales channel rather than a phone book."},
                {"num": "▸ The Objective", "h": "Showcase the catalog. Generate the leads.",
                 "p": "Every product on its own detail page with specs and dimensions. Hierarchical category "
                      "nav that scales to the full range. WhatsApp-first inquiry on every single product. Lead "
                      "capture wired to your team in real-time. Designed to compete with global manufacturer "
                      "sites — at distributor scale."},
            ],
            "players_kicker": "▸ Who's Coming to the Site",
            "players": [
                {"tag": "Player 01", "h": "The Commercial Buyer",
                 "p": "Gym chains, hotel groups, sports facilities, school procurement. Buying multiple units, "
                      "comparing on spec and after-sales support. Won't make contact until they've shortlisted "
                      "from your catalog."},
                {"tag": "Player 02", "h": "The Home / Premium User",
                 "p": "High-end residential buyer setting up a home gym. One or two machines, but expects a "
                      "premium digital experience and a clean spec sheet. The customer who refers friends."},
                {"tag": "Player 03", "h": "The Existing Customer",
                 "p": "Already bought equipment, needs service, parts, or to add to their setup. Should find "
                      "support and reach the team in under two taps."},
            ],
        },

        {
            "type": "build", "id": "build", "kicker": "02 · What We Build",
            "title": "One website. Everything around it included.",
            "sub": "The main deliverable is the website rebuild. Hosting, webmail, SEO foundation, and team "
                   "training are bundled in — not sold as add-ons. Tap each tab to see what's inside.",
            "tabs": [
                {
                    "num": "01", "name": "The Website", "h": "The Website Rebuild",
                    "lead": "A fast, modern, mobile-first website built to handle 500+ products without "
                            "breaking a sweat. Next.js for speed and SEO. Hierarchical category navigation "
                            "that scales to the full range. Every product on its own detail page. WhatsApp-first "
                            "inquiry on every single one — every product page becomes a lead-capture surface.",
                    "lists": [
                        {"label": "▸ Sitemap & Information Architecture", "items": [
                            "Home — brand position, range overview, featured machines, trust signals, latest catalog",
                            "About — company story, scale, after-sales philosophy, partnership credentials",
                            "Cardio — Treadmills · Ellipticals · Spin Bikes · Stair Climbers · Air Rowers · Ski Machines",
                            "Strength: Pin Loaded — 10+ product lines (Apex, Echo, Echo Pro, Dynamic, Zenmotion, Nexus, Galaxy Pro, Prestige Pro, Peak Pro, more)",
                            "Strength: Plate Loaded — Lagazy, Lagazy Pro, Vertex, Lightning, plus expansion lines",
                            "Strength: Free Weights — Lumina, Echo Pro, Prestige Pro, Zenmotion, plus expansion",
                            "Accessories — Dumbbells · Plates · Rods · Steppers · Supporting Rods · all variations",
                            "Services & Support — installation, maintenance, parts catalog, warranty terms",
                            "Brochure / Catalog Download — full PDF catalog, gated for lead capture",
                            "Community — BZ Fitness customer community, events, partnerships",
                            "Contact — outlet info, hours, WhatsApp inquiry, embedded map, multi-channel",
                            "Privacy + Terms — standard legal pages, Kuwait data law-compliant"]},
                        {"label": "▸ The 500-Product Catalog System", "items": [
                            "One master product template — image gallery, specs table, dimensions, weight, use-case tags, “Inquire on WhatsApp” CTA",
                            "500+ product detail pages generated from this template + structured data import",
                            "Category landing pages with filter and sort (by use case, by weight class, by price tier)",
                            "Related machines block on every detail page — keeps buyers browsing instead of bouncing",
                            "Search across the full catalog with smart matching (by name, by category, by spec)",
                            "Data import workflow — your team supplies product data once via spreadsheet, system generates pages"]},
                        {"label": "▸ Lead Generation Engine", "items": [
                            "WhatsApp deep-link on every product page — one-tap inquiry with machine name pre-filled",
                            "Inquiry form with vertical-specific routing (commercial vs household vs B2B)",
                            "Catalog download as gated lead capture — name + phone + email before PDF",
                            "“Request a Quote” flow for multi-product inquiries (gym fitouts, hotel orders)",
                            "Lead notifications direct to your team via email + optional WhatsApp webhook"]},
                        {"label": "▸ Performance & Polish", "items": [
                            "Sub-2.5s mobile load on Kuwait 4G — fast enough that buyers don't leave",
                            "WCAG AA accessibility — assistive tech compatible",
                            "Mobile-first responsive — Kuwait B2B research is phone-first",
                            "Schema.org Product markup — every machine appears properly in Google Search",
                            "Arabic-ready architecture — English at launch, Arabic toggle scoped for Phase 2"]},
                    ],
                    "price_label": "One-time investment", "price": "₹75,000",
                    "price_note": "Website build · 500+ products · lead-gen",
                    "meta": [("Duration", "25–30 days"), ("Tech", "Next.js + Vercel"),
                             ("Pages", "12 + 500 products"), ("Support", "30 days included")],
                },
                {
                    "num": "02", "name": "Plus Included", "h": "Everything Else, Bundled In",
                    "lead": "Hosting, professional webmail, SEO foundation, and team training — all included in "
                            "the ₹83,000 total. No surprise renewals in month two. No “oh, that's extra.” Clean.",
                    "lists": [
                        {"label": "▸ Hosting (1 year)", "items": [
                            "Vercel hosting — same infrastructure used by Nike, McDonald's, Twitch",
                            "Global CDN — fast in Kuwait, fast in Riyadh, fast everywhere",
                            "Automatic HTTPS via Let's Encrypt",
                            "99.99% uptime SLA from Vercel",
                            "Renewal from year 2: ₹6,000/year"]},
                        {"label": "▸ Professional Webmail (3 accounts)", "items": [
                            "Google Workspace setup — info@, sales@, support@bzfitness.com",
                            "Custom domain emails on a real business mail platform",
                            "50 GB storage per account, Google Calendar, Drive, Meet included",
                            "Mobile-ready on iOS and Android out of the box",
                            "Subscription billed direct from Google — not marked up by Adaline"]},
                        {"label": "▸ SEO Foundation", "items": [
                            "Google Business Profile setup & optimisation for Kuwait visibility",
                            "On-page SEO across all pages — meta tags, schema, sitemaps",
                            "Keyword targeting for “fitness equipment Kuwait,” “commercial treadmill Kuwait,” etc.",
                            "Google Search Console submitted + verified",
                            "Bing Webmaster Tools setup (matters in GCC)"]},
                        {"label": "▸ Team Training + 30-day Support", "items": [
                            "One 90-minute training session — how to update products, prices, photos",
                            "Recorded session for future team members",
                            "Written quick-reference guide — bookmark and forget",
                            "30 days of post-launch bug fixes and minor content edits at no charge"]},
                    ],
                    "price_label": "Bundled in the total", "price": "₹18,000",
                    "price_note": "Hosting + Webmail + SEO + Training",
                    "meta": [("Hosting", "1 year included"), ("Webmail", "3 accounts setup"),
                             ("SEO", "Full foundation"), ("Training", "90 min + recorded")],
                },
            ],
        },

        {
            "type": "process", "id": "process", "kicker": "03 · How We Work",
            "title": "Four phases. Documented. Scoped. No surprises.",
            "sub": "A website project goes off the rails in the middle when scope creeps and nobody owns the "
                   "calendar. Here's how we keep that from happening.",
            "steps": [
                {"n": "PHASE 01", "h": "Brief",
                 "p": "Discovery call, brand assets handover, product photography audit, content priority list. One week."},
                {"n": "PHASE 02", "h": "Design",
                 "p": "Homepage and product page mockups, design system locked. Two rounds of feedback. Sign-off gate before development."},
                {"n": "PHASE 03", "h": "Build",
                 "p": "Next.js development, product catalog populated, all 12 pages built, all 30+ product detail pages generated."},
                {"n": "PHASE 04", "h": "Launch",
                 "p": "Testing, mobile QA, hosting deployment, webmail go-live, SEO submission, training session, handover."},
            ],
            "principles": [
                {"label": "▸ Content Philosophy", "h": "The machine is the hero.",
                 "p": "Clean product photography, honest spec sheets, dimensions buyers can plan around. No stock "
                      "fitness imagery, no motivational quotes, no fluff. The buyer wants to know: what is it, how "
                      "big is it, how much does it cost. We answer all three."},
                {"label": "▸ Inquiry Philosophy", "h": "WhatsApp first. Email second. Forms last.",
                 "p": "Every product page has a one-tap WhatsApp inquiry button that pre-fills the machine name. "
                      "That's how Kuwait buyers actually contact suppliers. Forms exist but they're not the primary "
                      "path. Email lives in the footer."},
            ],
        },

        {
            "type": "timeline", "id": "timeline", "kicker": "04 · Timeline",
            "title": "Six weeks from kickoff to launch.",
            "sub": "Working days, excludes weekends and public holidays in Kuwait and India. The catalog import "
                   "phase runs alongside development — your team can supply product data while we build, and the "
                   "system generates pages as data arrives.",
            "tracks": [
                {"name": "▸ Website Build", "dur": "25–30 working days",
                 "phases": [
                     {"num": "P1", "name": "Discovery", "dur": "3 days"},
                     {"num": "P2", "name": "Design", "dur": "5 days"},
                     {"num": "P3", "name": "Build", "dur": "10 days"},
                     {"num": "P4", "name": "Catalog Import", "dur": "5 days"},
                     {"num": "P5", "name": "Testing", "dur": "3 days"},
                     {"num": "P6", "name": "Launch", "dur": "2 days"}]},
            ],
            "note": "<strong>Hosting, webmail, SEO setup, and training</strong> are completed alongside the Launch "
                    "phase. The catalog import phase runs in parallel with build — your team provides product data "
                    "via spreadsheet, our system generates the 500+ detail pages from it. Full site live, indexed, "
                    "and team trained by end of week six.",
        },

        {
            "type": "investment", "id": "investment", "kicker": "05 · The Investment",
            "title": "One clean number. Everything bundled.",
            "sub": "Total one-time investment for the full programme. Hosting, webmail, SEO, and training all "
                   "included — not sold separately. Toggle items below to see how the number changes.",
            "hero": {
                "label": "▸ FULL PROGRAMME · ONE-TIME",
                "title": "Website + Hosting + Webmail + SEO & Support",
                "desc": "Complete website rebuild built for 500+ products, one year of hosting, three webmail "
                        "accounts, full SEO foundation, team training session, and 30 days of post-launch support. "
                        "Nothing else billed in year one.",
                "price": "₹93,000",
            },
            "hint": "TOGGLE TO SEE WHAT EACH PIECE COSTS",
            "rows": [
                {"num": "01", "name": "The Website Rebuild",
                 "note": "12 pages + 500+ product detail pages · lead-gen built in",
                 "price": "₹75,000", "price_val": 75000, "recurring_val": 0, "short": "Website"},
                {"num": "02", "name": "Hosting · Year 1",
                 "note": "Vercel global CDN · HTTPS · 99.99% uptime",
                 "price": "₹6,000", "price_val": 6000, "recurring_val": 6000, "short": "Hosting"},
                {"num": "03", "name": "Webmail Setup",
                 "note": "3 Google Workspace accounts · setup only",
                 "price": "₹4,000", "price_val": 4000, "recurring_val": 0, "short": "Webmail"},
                {"num": "04", "name": "SEO Foundation + Training + 30-day Support",
                 "note": "GBP setup · on-page SEO · 90-min training · bug fixes",
                 "price": "₹8,000", "price_val": 8000, "recurring_val": 0, "short": "SEO & Support"},
            ],
            "recur": {"l": "From <strong>Year 2 onward</strong> — hosting renewal only",
                      "r": "₹6,000 / year", "prefix": "Year 2 onward", "unit": "year"},
            "notes": [
                {"label": "▸ Payment Schedule", "items": [
                    "40% deposit on engagement start",
                    "40% at design sign-off (end of week 2)",
                    "20% on launch &amp; handover",
                    "Bank transfer · INR or KWD equivalent at prevailing rate"]},
                {"label": "▸ Things to Note", "items": [
                    "All prices exclude applicable GST",
                    "Google Workspace subscription billed direct by Google (~₹400/account/month)",
                    "Product photography assumed to be provided by BZ Fitness (we can arrange shoot separately if needed)",
                    "Brochure PDF assumed to be ready (we'll present it properly on the site)"]},
            ],
        },

        {
            "type": "agency", "id": "agency", "kicker": "06 · The Agency",
            "title": "Three reasons we're a fit for BZ Fitness.",
            "cells": [
                {"mark": "▸ ONE", "h": "We've done this catalog-heavy build before",
                 "p": "Product catalogs with 30+ SKUs across multiple categories — we know how to make them "
                      "browsable without becoming overwhelming. Spec tables that don't drown the user. Detail "
                      "pages that load fast."},
                {"mark": "▸ TWO", "h": "Kuwait + Gulf is in our existing book",
                 "p": "We're already running active engagements in the GCC — UAE abaya brand, Saudi auto parts "
                      "B2B. We understand the WhatsApp-first inquiry pattern, the Arabic content readiness "
                      "question, the Friday-Saturday weekend reality."},
                {"mark": "▸ THREE", "h": "One studio, no handoffs",
                 "p": "Strategy, design, development, and ongoing support all sit in one team. No “we'll loop in "
                      "the developer” delays. No “the designer's on leave” excuses. Project lead is your single "
                      "point of contact."},
            ],
        },

        {
            "type": "legal", "id": "legal", "kicker": "07 · The Fine Print",
            "title": "Terms of Engagement — tap to expand.",
            "sub": "Standard agency terms governing the engagement between BZ Fitness and Myadaline Communications "
                   "LLP. Plain English. Mutual.",
            "docs": [
                {
                    "id": "acc-terms", "anum": "Document 01",
                    "title": "Terms & Conditions of Engagement",
                    "meta": [("Effective", "On acceptance"), ("Version", "1.0"),
                             ("Valid", "10 days from issue"), ("Jurisdiction", "Calicut, Kerala")],
                    "toc": ["Scope & Acceptance", "The Engagement", "Fees & Payment", "Changes & Revisions",
                            "Deliverables & Acceptance", "Intellectual Property", "Hosting & Third-Party",
                            "Confidentiality", "Warranties", "Liability", "Termination", "Force Majeure",
                            "Disputes", "Notices", "Miscellaneous"],
                    "sections": [
                        {"h": "Scope & Acceptance", "body":
                         "<p>This Proposal sets out the scope of services provided by Myadaline Communications LLP "
                         "(operating as Adaline, the “Agency”) to BZ Fitness (the “Client”). Valid for ten (10) "
                         "days from issue. The engagement commences upon written acceptance, signed engagement "
                         "letter, or receipt of the deposit.</p>"},
                        {"h": "The Engagement", "body":
                         "<p>The Agency will deliver the website rebuild, hosting setup, webmail configuration, SEO "
                         "foundation, and team training as described in Sections 2 and 5 of this Proposal. The Client "
                         "will provide timely access to brand assets, product information, photography, approvals, "
                         "and decisions necessary for delivery.</p>"},
                        {"h": "Fees & Payment Terms", "body":
                         "<p>Total engagement fee: ₹93,000 (Indian Rupees, equivalent KWD at prevailing rate "
                         "acceptable), exclusive of GST.</p><span class=\"lsub\">Payment schedule</span><ul>"
                         "<li>40% deposit on engagement start (₹37,200)</li>"
                         "<li>40% at design sign-off, end of week 2 (₹37,200)</li>"
                         "<li>20% on launch and handover (₹18,600)</li>"
                         "<li>Third-party subscriptions (Google Workspace) billed direct to Client</li></ul>"
                         "<p><strong>Late payment:</strong> 1.5% per month compounded after 15 days from invoice date.</p>"},
                        {"h": "Change Requests & Revisions", "body":
                         "<p>Two rounds of revision included at the design stage. Additional revisions or "
                         "scope-expanding changes require a written Change Order with fee and timeline impact agreed "
                         "before execution. Minor copy edits during the build phase are accommodated without charge.</p>"},
                        {"h": "Deliverables & Acceptance", "body":
                         "<p>Deliverables submitted at each phase per Section 4 timeline. Client provides "
                         "consolidated feedback within five (5) working days. Silence beyond this window = deemed "
                         "acceptance. Final delivery conditional on final payment.</p>"},
                        {"h": "Intellectual Property", "body":
                         "<p>On final payment, the Agency assigns to the Client all IP rights in the approved "
                         "deliverables — website codebase, design files, content. Agency retains: pre-existing tools "
                         "and frameworks; unselected drafts and concepts; the right to feature the work in its "
                         "portfolio (subject to confidentiality). Third-party assets (fonts, hosting, libraries) "
                         "remain governed by their original licence terms.</p>"},
                        {"h": "Hosting & Third-Party Services", "body":
                         "<p>Hosting is provided via Vercel for one (1) year included in the total fee. Renewal at "
                         "₹6,000/year from year 2, paid annually. Google Workspace subscription billed directly to "
                         "Client by Google (Agency does not mark up third-party subscriptions). Domain registration, "
                         "if needed, billed at cost.</p>"},
                        {"h": "Confidentiality", "body":
                         "<p>Each party treats as confidential all non-public information disclosed in connection "
                         "with the engagement — business strategy, pricing, customer information, technical "
                         "specifications. Confidentiality survives termination for three (3) years. Agency portfolio "
                         "rights are limited to publicly visible deliverables.</p>"},
                        {"h": "Warranties & Disclaimers", "body":
                         "<p>The Agency warrants professional performance consistent with industry standards and "
                         "substantial conformity of deliverables to agreed specifications at final acceptance. "
                         "Otherwise, deliverables provided <strong>“as is”</strong>. No warranty of specific "
                         "business outcomes — sales, inquiries, search rankings — as these depend on factors outside "
                         "the Agency's control including market dynamics, competition, and Client's ongoing marketing "
                         "efforts.</p>"},
                        {"h": "Limitation of Liability", "body":
                         "<p>Agency's aggregate liability shall not exceed the total fees paid under this engagement. "
                         "No liability for indirect, incidental, special, or consequential damages — including loss of "
                         "profits, business opportunity, data, or reputation — regardless of foreseeability.</p>"},
                        {"h": "Termination", "body":
                         "<p><strong>For convenience:</strong> either party with 14 days' written notice. Client pays "
                         "for work completed up to effective date plus non-cancellable third-party commitments.</p>"
                         "<p><strong>For cause:</strong> immediate on material breach uncured within 10 days of notice.</p>"
                         "<p><strong>Survival:</strong> payment obligations, confidentiality, IP assignment, and "
                         "provisions that should survive — do.</p>"},
                        {"h": "Force Majeure", "body":
                         "<p>No liability for failure or delay due to events beyond reasonable control — natural "
                         "disasters, pandemic, government action, civil unrest, telecoms failure, third-party service "
                         "outage. Affected party notifies in writing, mitigates, resumes when practicable.</p>"},
                        {"h": "Governing Law & Dispute Resolution", "body":
                         "<p>Governed by laws of India. First attempt: good-faith negotiation between authorised "
                         "representatives within 30 days of dispute notice. Failing that: arbitration under the "
                         "Arbitration and Conciliation Act, 1996, sole arbitrator mutually appointed, seat at Calicut "
                         "(Kozhikode), Kerala, language English. Subject to the above, Calicut courts have exclusive "
                         "jurisdiction.</p>"},
                        {"h": "Notices & Communication", "body":
                         "<p>Formal notices in writing by email. Agency address of record: "
                         "<strong>bettercall@myadaline.com</strong>. Day-to-day communication via agreed channels "
                         "(email, WhatsApp, project workspace) — not subject to formal-notice requirement.</p>"},
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
