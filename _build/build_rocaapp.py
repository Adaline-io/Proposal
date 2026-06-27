"""
ROCA Group — Business Feasibility Study (the "Roca app" proposal).

Migrated from Adaline-BC/Roca-Proposal. NOTE: this is a different client from
Roca Fuels — "ROCA Group", a B2B auto-parts distributor in Saudi Arabia. This is
Phase 0 (a feasibility study) before the B2B platform / app build. Re-cast into
the canonical Adaline proposal style. Accent: gold (#d4a853), from the source.
Currency: AED. Investment uses a static layout (single fee + milestone schedule).

Run:  python3 _build/build_rocaapp.py
"""

import template as T

PALETTE = "--red:#d4a853;--yellow:#d4a853;--green:#f0d48a;--blue:#3b82f6;"

INVESTMENT_HTML = """
<section id="investment" class="page" aria-labelledby="invest-title">
  <div class="kicker">05 · The Investment</div>
  <h2 class="sec-title" id="invest-title">Pricing &amp; payment.</h2>
  <p class="sec-sub">One fee for the complete study — all twelve deliverables, the full report, the
  deck, the canvas, and every piece of raw data. Billed in three milestones across the six weeks.</p>

  <div class="invest-hero">
    <div>
      <div class="ih-label">&#9656; BUSINESS FEASIBILITY STUDY &#183; ALL 12 DELIVERABLES</div>
      <div class="ih-title">60&ndash;80 page report + deck + canvas + all raw data</div>
      <p class="ih-desc">Duration: 6 weeks. Everything Roca needs to validate the platform before a
      single line of code is written.</p>
    </div>
    <div class="ih-price">AED 13,000</div>
  </div>

  <div class="notes-mini">
    <div class="note-card">
      <div class="nc-label">&#9656; Payment Schedule</div>
      <ul>
        <li><strong>AED 6,500</strong> &mdash; signing + kickoff (before work begins)</li>
        <li><strong>AED 3,250</strong> &mdash; research + survey complete (end of Week 4)</li>
        <li><strong>AED 3,250</strong> &mdash; final report + presentation delivered (Week 6)</li>
        <li>International wire transfer &#183; wire charges borne by Client &#183; FEMA-compliant billing</li>
      </ul>
    </div>
    <div class="note-card">
      <div class="nc-label">&#9656; Study + App Together &mdash; Credited</div>
      <ul>
        <li>Proceed with both the study and app development, and the full study fee is credited toward Phase 1.</li>
        <li>Effectively, the study becomes free when you commit to the full build.</li>
        <li>It pays for itself the first time it prevents a wrong decision.</li>
      </ul>
    </div>
  </div>

  <div class="invest-recur">
    <div class="ir-l">Study &rarr; App together &mdash; <strong>the AED 13,000 study fee is credited to Phase 1</strong></div>
    <div class="ir-r">AED 13,000 credited</div>
  </div>

  <div class="kicker" style="margin-top:48px">&#9656; How This Connects to the App Build</div>
  <div class="proc">
    <div class="pstep"><div class="pn">PHASE 0</div><h4>Feasibility Study</h4><p>This proposal. Creates the strategic foundation for every decision that follows.</p></div>
    <div class="pstep"><div class="pn">PHASE 1</div><h4>App Development</h4><p>Buyer app + admin + rep portal. The feature priority matrix decides what gets built first.</p></div>
    <div class="pstep"><div class="pn">PHASE 2</div><h4>Enhancements</h4><p>BNPL, AI, analytics. Market gap analysis identifies the highest-demand features.</p></div>
    <div class="pstep"><div class="pn">PHASE 3</div><h4>Expansion</h4><p>UAE, Bahrain. The study enables resource-efficient expansion into new markets.</p></div>
  </div>
</section>
"""

DATA = {
    "slug": "roca-app",
    "client": "ROCA Group",
    "title": "Business Feasibility Study · ROCA Group",
    "description": "Business Feasibility Study for ROCA Group — B2B Auto Parts Platform, Saudi Arabia. Prepared by Adaline.",
    "palette": PALETTE,

    "nav_title": "ROCA Group",
    "nav_sub": "Business Feasibility Study",
    "topnav": [("brief", "Why"), ("deliverables", "Deliverables"), ("timeline", "Execution"),
               ("outcomes", "Outcomes"), ("investment", "Investment"), ("agency", "Adaline")],
    "menu": [("cover", "Cover", "00"), ("brief", "Why This Study", "01"),
             ("deliverables", "Deliverables", "02"), ("timeline", "Execution", "03"),
             ("outcomes", "What You Get", "04"), ("investment", "The Investment", "05"),
             ("agency", "Why Adaline", "06"), ("legal", "Terms", "07")],

    "hero": {
        "tag": "Business Feasibility Study · ADL-ROCA-FS-001",
        "meta": [("Date", "April 2026"), ("Valid", "30 days from issue")],
        "prepared_label": "Prepared for",
        "title_html": "ROCA<br/>Group.",
        "sub": ["B2B Auto Parts Platform", "Business Feasibility Study", "Saudi Arabia"],
        "desc": "A comprehensive market study, validation, and strategic blueprint — before a single "
                "line of code is written. The proof that comes before the platform.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Build the Proof.",
        "cta": "HIT START",
        "cta_subject": "ROCA Group — feasibility study acceptance",
    },

    "sections": [
        {
            "type": "brief", "id": "brief", "kicker": "01 · The Foundation",
            "title": "Why this study matters.",
            "sub": "Roca is planning a significant investment in a B2B e-commerce platform for auto parts "
                   "distribution across Saudi Arabia. Building an app without this study is like constructing "
                   "a building without soil testing — it might stand, but you're betting 150K AED on “might.” "
                   "This study removes the guesswork.",
            "cells": [
                {"num": "▸ Market Demand", "h": "Is the demand real?",
                 "p": "Is there enough market demand to justify this platform? What does your actual buyer "
                      "want from a B2B ordering experience?"},
                {"num": "▸ Competitive Gaps", "h": "Where are the gaps?",
                 "p": "What are your competitors doing digitally, and where are the gaps you can exploit?"},
                {"num": "▸ Operational Impact", "h": "Can it cut overhead?",
                 "p": "Can you realistically reduce your 160+ employee overhead with this platform?"},
                {"num": "▸ Business Model", "h": "Is the model right?",
                 "p": "What's the right business model — and is the product-market fit real? What are the "
                      "growth drivers and blockers?"},
            ],
        },

        {
            "type": "brief", "id": "deliverables", "kicker": "02 · The Deliverables",
            "title": "Twelve deliverables. Deep and actionable.",
            "sub": "Not a surface-level market overview — a deep, actionable study with twelve specific "
                   "outputs, each documented, cited, and visualised.",
            "cells": [
                {"num": "01", "h": "Industry Research",
                 "p": "Complete landscape of auto parts distribution in Saudi Arabia. Market size, growth "
                      "trends, digital adoption rates, regulatory environment, supply chain dynamics."},
                {"num": "02", "h": "Micro & Macro Market Analysis",
                 "p": "GDP, SME growth, Vision 2030 impact, B2B e-commerce penetration, fleet growth, and "
                      "automotive aftermarket trends in Riyadh, Jeddah, and Dammam."},
                {"num": "03", "h": "Target Market Survey",
                 "p": "Direct research with 30–50 actual and potential buyers. Phone interviews + digital "
                      "survey covering ordering habits, digital readiness, and pain points."},
                {"num": "04", "h": "Competitor Benchmarking",
                 "p": "Map every competitor offering B2B auto parts digitally in Saudi. Apps, features, "
                      "pricing, user reviews, market positioning."},
                {"num": "05", "h": "Segmentation Analysis",
                 "p": "Break the buyer base into segments — garages, fleet companies, resellers, retail "
                      "shops, government procurement. Size, behaviour, value, priority ranking."},
                {"num": "06", "h": "Product-Market Fit",
                 "p": "Does the proposed B2B app solve a real, urgent problem? Validation through survey "
                      "data, competitor gaps, and buyer behaviour analysis."},
                {"num": "07", "h": "Business Model Validation",
                 "p": "Revenue streams, unit economics, cost structure, pricing sensitivity, break-even "
                      "analysis. Is this commercially viable at scale?"},
                {"num": "08", "h": "Market Size & Demand",
                 "p": "Historical performance, emerging trends, and a 5-year future demand projection for "
                      "B2B auto parts e-commerce in Saudi Arabia."},
                {"num": "09", "h": "Force Field Analysis",
                 "p": "Growth drivers (Vision 2030, digital adoption, fleet expansion) vs barriers "
                      "(resistance to digital, cash-based culture, competitor lock-in). Mapped and weighted."},
                {"num": "10", "h": "Critical Success Factors",
                 "p": "The 8–10 things that must go right for this platform to succeed. Ranked by impact and "
                      "difficulty, each with a mitigation strategy."},
                {"num": "11", "h": "Gap & Opportunity Mapping",
                 "p": "Unmet buyer needs, underperforming competitor areas, geographic gaps, service gaps — "
                      "each mapped to a platform feature opportunity."},
                {"num": "12", "h": "Business Model Canvas",
                 "p": "A complete one-page strategic canvas: value proposition, customer segments, channels, "
                      "revenue streams, key partners, resources, activities, cost structure."},
            ],
        },

        {
            "type": "timeline", "id": "timeline", "kicker": "03 · Execution",
            "title": "A structured six-week engagement.",
            "sub": "Weekly progress updates via video call, with WhatsApp for daily coordination. Each phase "
                   "ends with a concrete output you can hold.",
            "tracks": [
                {"name": "▸ 6-Week Engagement", "dur": "6 weeks",
                 "phases": [
                     {"num": "W1", "name": "Discover", "dur": "Week 1"},
                     {"num": "W2–3", "name": "Research", "dur": "Weeks 2–3"},
                     {"num": "W3–4", "name": "Survey", "dur": "Weeks 3–4"},
                     {"num": "W4–5", "name": "Analyze", "dur": "Weeks 4–5"},
                     {"num": "W5–6", "name": "Blueprint", "dur": "Weeks 5–6"},
                     {"num": "W6", "name": "Present", "dur": "Week 6"}]},
            ],
            "note": "<strong>Discover</strong> — kickoff with Roca leadership, operations and data handover. "
                    "<strong>Research &amp; Survey</strong> — industry + competitor audit, regulatory scan "
                    "(ZATCA, e-commerce, data laws), and a 30–50 respondent buyer survey with 10–15 key-account "
                    "interviews. <strong>Analyze &amp; Blueprint</strong> — segmentation, product-market fit, "
                    "force-field mapping, and the Business Model Canvas. <strong>Present</strong> — full "
                    "walk-through to leadership, with every file, dataset, and the strategic blueprint handed over.",
        },

        {
            "type": "brief", "id": "outcomes", "kicker": "04 · What You Get",
            "title": "What Roca walks away with.",
            "sub": "This study becomes the foundation for everything that follows — app development, marketing "
                   "strategy, pricing decisions, investor conversations, and market expansion.",
            "cells": [
                {"num": "▸ Report", "h": "60–80 Page Feasibility Report",
                 "p": "All twelve deliverables documented, cited, and visualised with charts and frameworks."},
                {"num": "▸ Deck", "h": "Presentation Deck (40–45 slides)",
                 "p": "Findings summarised for a board or investor presentation."},
                {"num": "▸ Canvas", "h": "Business Model Canvas",
                 "p": "A one-page blueprint of your business — a living map to test new ideas without guessing."},
                {"num": "▸ Matrix", "h": "Feature Priority Matrix",
                 "p": "Every proposed app feature ranked by market demand, competitive advantage, and "
                      "development complexity."},
                {"num": "▸ Data", "h": "Raw Survey Data",
                 "p": "From 30–50 actual buyers — Roca keeps this for future reference."},
                {"num": "▸ Benchmark", "h": "Competitor Benchmark Report",
                 "p": "Top competitors analysed to identify their advantages and where Roca is currently lagging."},
            ],
        },

        {"type": "raw", "id": "investment", "html": INVESTMENT_HTML},

        {
            "type": "agency", "id": "agency", "kicker": "06 · Our Edge",
            "title": "Why Adaline for this study.",
            "cells": [
                {"mark": "▸ ONE", "h": "Same team builds the app",
                 "p": "The study directly informs the development. No handoff gaps, no lost context — the "
                      "people who research the market are the people who build the platform."},
                {"mark": "▸ TWO", "h": "Primary research",
                 "p": "We actually call your buyers. We survey real people. Most agencies just pull secondary "
                      "data from Google — we go to the source."},
                {"mark": "▸ THREE", "h": "Actionable, not academic",
                 "p": "Every finding comes with a “so what” and a “now what.” No 100-page documents that sit "
                      "in a drawer."},
                {"mark": "▸ FOUR", "h": "Gulf market experience",
                 "p": "We serve clients across UAE, Qatar, and Saudi. We understand the business culture, the "
                      "buying behaviour, and the regulatory environment."},
                {"mark": "▸ FIVE", "h": "One partner, full journey",
                 "p": "Study → Strategy → Development → Launch → Growth. Adaline stays with you through every phase."},
            ],
        },

        {
            "type": "legal", "id": "legal", "kicker": "07 · The Fine Print",
            "title": "Terms & Conditions — tap to expand.",
            "sub": "Standard terms governing the engagement between ROCA Group and Myadaline Communications LLP.",
            "docs": [
                {
                    "id": "acc-terms", "anum": "Document 01",
                    "title": "Terms & Conditions of Engagement",
                    "meta": [("Effective", "On acceptance"), ("Version", "1.0"),
                             ("Valid", "30 days from issue"), ("Governing Law", "Laws of India")],
                    "toc": ["Payment & Billing", "Client Responsibilities", "Intellectual Property",
                            "Confidentiality & Termination", "Disputes", "Governing Law"],
                    "sections": [
                        {"h": "Payment & Billing", "body":
                         "<ul><li>All fees quoted in AED. Wire transfer charges borne by Client.</li>"
                         "<li>50% advance required before work begins.</li>"
                         "<li>Milestone payments due within 7 days of delivery.</li>"
                         "<li>Late payment beyond 15 days: work pauses, 2% monthly late fee.</li></ul>"},
                        {"h": "Client Responsibilities", "body":
                         "<ul><li>Provide access to internal data within the first week.</li>"
                         "<li>Designate one SPOC for approvals and coordination.</li>"
                         "<li>Facilitate introductions to 10–15 key buyers.</li>"
                         "<li>Respond to deliverables within 5 business days. No response = deemed approved.</li></ul>"},
                        {"h": "Intellectual Property", "body":
                         "<ul><li>All deliverables become Roca's property upon full payment.</li>"
                         "<li>Adaline retains the right to reference the engagement without proprietary data.</li>"
                         "<li>Pre-existing frameworks remain Adaline's property with perpetual licence to the Client.</li></ul>"},
                        {"h": "Confidentiality & Termination", "body":
                         "<ul><li>All shared data is strictly confidential. Survives termination for 2 years.</li>"
                         "<li>Either party may terminate with 15 days' written notice. Client pays for completed work.</li></ul>"},
                        {"h": "Disputes", "body":
                         "<p>Disputes resolved first by good-faith negotiation (15 days), then arbitration under "
                         "the Indian Arbitration and Conciliation Act, 1996.</p>"},
                        {"h": "Governing Law", "body":
                         "<p>Governed by the laws of India. This proposal is valid for 30 days from the date of issue.</p>"},
                    ],
                },
            ],
        },
    ],
}


if __name__ == "__main__":
    print("Built:", T.build(DATA))
