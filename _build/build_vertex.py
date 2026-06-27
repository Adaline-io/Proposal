"""
Vertex PRO — client-ready proposal.

Migrated from Adaline-io/vertex-proposal ("Vertex PRO" web development). Saudi /
GCC construction, civil, steel-structure, industrial & fit-out contractor; a
premium one-page digital presence. Re-cast into the canonical Adaline proposal
style. Accent: gold (#c9a862), carried from the source brand.

Vertex prices as a single all-in package (not itemised), so the investment uses
a static layout rather than the toggle bundle calculator.

Run:  python3 _build/build_vertex.py
"""

import template as T

PALETTE = "--red:#c9a862;--yellow:#c9a862;--green:#e4c988;--blue:#5a8eff;"

# Static investment section (no toggle calculator — single package + optional retainer).
INVESTMENT_HTML = """
<section id="investment" class="page" aria-labelledby="invest-title">
  <div class="kicker">04 · The Investment</div>
  <h2 class="sec-title" id="invest-title">Simple, transparent pricing.</h2>
  <p class="sec-sub">No hidden fees. No surprises. Everything you need to launch a premium digital
  presence in one clear number — with an optional retainer if you want us to keep it growing.</p>

  <div class="invest-hero">
    <div>
      <div class="ih-label">&#9656; COMPLETE PACKAGE &#183; ONE-TIME</div>
      <div class="ih-title">Web Design + Dev + Content + Hosting + Email</div>
      <p class="ih-desc">Everything included to get Vertex PRO online — custom design, development,
      professional content, hosting &amp; deployment, and business email. <strong>~ SAR 2,500.</strong></p>
    </div>
    <div class="ih-price">&#8377;63,000</div>
  </div>

  <div class="notes-mini">
    <div class="note-card">
      <div class="nc-label">&#9656; What's Included</div>
      <ul>
        <li>Custom website design &amp; development</li>
        <li>Professional content writing</li>
        <li>Hosting &amp; deployment setup</li>
        <li>Business email configuration</li>
        <li>Responsive mobile design</li>
        <li>Contact form with email alerts</li>
        <li>SEO optimization</li>
        <li>1 round of revisions</li>
      </ul>
    </div>
    <div class="note-card">
      <div class="nc-label">&#9656; Optional Add-On &#183; Content Management</div>
      <ul>
        <li>LinkedIn content strategy</li>
        <li>Regular LinkedIn posts</li>
        <li>Website content updates</li>
        <li>New project additions</li>
        <li>Performance reporting</li>
      </ul>
    </div>
  </div>

  <div class="invest-recur">
    <div class="ir-l">LinkedIn + website content management &mdash; <strong>optional monthly retainer</strong> (~ SAR 800)</div>
    <div class="ir-r">&#8377;20,000 / month</div>
  </div>

  <div class="notes-mini">
    <div class="note-card">
      <div class="nc-label">&#9656; Payment Schedule</div>
      <ul>
        <li>50% deposit on engagement start</li>
        <li>50% on launch &amp; handover</li>
        <li>Bank transfer &#183; INR or SAR equivalent at prevailing rate</li>
      </ul>
    </div>
    <div class="note-card">
      <div class="nc-label">&#9656; Things to Note</div>
      <ul>
        <li>All prices exclude applicable GST</li>
        <li>Final design customised to Vertex PRO's official logo &amp; brand styleguides</li>
        <li>Project imagery &amp; content inputs provided by Vertex PRO</li>
        <li>Proposal valid for 30 days from date of issue</li>
      </ul>
    </div>
  </div>
</section>
"""

DATA = {
    "slug": "vertex",
    "client": "Vertex PRO",
    "title": "Project Proposal · Vertex PRO",
    "description": "Web Development Proposal for Vertex PRO — prepared by Adaline.",
    "palette": PALETTE,

    "nav_title": "Vertex PRO",
    "nav_sub": "Web Development Proposal",
    "topnav": [("brief", "Brief"), ("build", "Scope"), ("timeline", "Timeline"),
               ("investment", "Investment"), ("agency", "Agency")],
    "menu": [("cover", "Cover", "00"), ("brief", "The Brief", "01"),
             ("build", "What We Build", "02"), ("timeline", "Timeline", "03"),
             ("investment", "The Investment", "04"), ("agency", "The Agency", "05")],

    "hero": {
        "tag": "Web Development Proposal",
        "meta": [("Date", "May 2026"), ("Valid", "30 days from issue")],
        "prepared_label": "Prepared for",
        "title_html": "Vertex<br/>PRO.",
        "sub": ["Web Design & Development", "Construction & Industrial", "Saudi Arabia & GCC"],
        "desc": "A premium digital presence that reflects the quality of the work — from luxury "
                "Dior retail fit-outs to large-scale industrial projects. Design, development, "
                "content, hosting, and business email, delivered end-to-end.",
        "byline_html": "Proposal by<br/><strong>Adaline · The Agency</strong>",
    },

    "close": {
        "thanks": "Let's Build.",
        "cta": "HIT START",
        "cta_subject": "Vertex PRO — web development proposal acceptance",
    },

    "sections": [
        {
            "type": "brief", "id": "brief", "kicker": "01 · The Brief",
            "title": "Premium work. The digital presence should match it.",
            "sub": "Vertex PRO delivers at the top of the market — luxury Dior retail fit-outs, steel "
                   "structure erection, civil works, industrial machinery installations, HVAC, and interior "
                   "fitouts across Saudi Arabia and the GCC. The website should carry that same weight: "
                   "modern, fast, and built to win the brief.",
            "cells": [
                {"num": "▸ The Reality", "h": "The portfolio is world-class. The presence isn't yet.",
                 "p": "From Dior flagship retail to large-scale steel and industrial projects, the work "
                      "speaks for itself. A premium digital presence makes that credibility visible to every "
                      "prospect before the first call."},
                {"num": "▸ The Audience", "h": "GCC clients shortlist online first.",
                 "p": "Developers, retail groups, and industrial principals across Saudi Arabia and the Gulf "
                      "research and shortlist contractors digitally. A credible, fast, well-structured site "
                      "is the first proof of quality."},
                {"num": "▸ The Objective", "h": "Showcase the work. Generate the enquiry.",
                 "p": "A modern, responsive site that showcases the portfolio, services, and credibility — "
                      "with a working contact flow wired to the sales team. Designed from Vertex PRO's own "
                      "logo and brand styleguides."},
            ],
            "players_kicker": "▸ Projects We'll Feature",
            "players": [
                {"tag": "Industrial", "h": "Steel Structure Erection", "p": "Saudi Arabia — large-scale structural steel."},
                {"tag": "Retail", "h": "Dior Flagship Store", "p": "Riyadh, KSA — luxury retail fit-out."},
                {"tag": "Retail", "h": "Magrabi Optical", "p": "KSA — premium retail rollout."},
                {"tag": "Commercial", "h": "Industrial Complex", "p": "Saudi Arabia — commercial build & fit-out."},
                {"tag": "Civil", "h": "Foundation Works", "p": "Saudi Arabia — civil & groundworks."},
                {"tag": "+", "h": "More projects", "p": "Added with detailed cards, category filters, and lightbox viewing as the portfolio grows."},
            ],
        },

        {
            "type": "build", "id": "build", "kicker": "02 · What We Build",
            "title": "A complete end-to-end web solution. No hidden costs.",
            "sub": "From design to deployment, everything is included in one package. Tap each tab to see "
                   "what's inside.",
            "tabs": [
                {
                    "num": "01", "name": "Website", "h": "Website Design & Development",
                    "lead": "A custom-designed, responsive website built with modern web technologies — "
                            "tailored to Vertex PRO's existing logo and brand styleguides, fast across every "
                            "device and region.",
                    "lists": [
                        {"label": "▸ Design & Build", "items": [
                            "Custom design tailored to your existing logo and brand styleguides",
                            "Responsive across all devices (mobile, tablet, desktop)",
                            "Hero section with parallax scrolling effects",
                            "About section with animated stat counters",
                            "Services showcase (6 service categories)",
                            "Project portfolio — installations, steel structure, industrial, and more",
                            "Client logo marquee (customer scroll bars)",
                            "Contact form with direct sales-team integration",
                            "Navigation with smooth scrolling",
                            "SEO optimization & meta tags"]},
                        {"label": "▸ Performance", "items": [
                            "Mobile-first responsive design",
                            "Fast load times (under 2 seconds)",
                            "Cross-browser & device tested",
                            "Horizontal-scroll project gallery with lightbox"]},
                    ],
                    "price_label": "In the complete package", "price": "Included",
                    "price_note": "Custom design · modern stack",
                    "meta": [("Stack", "Modern web technologies"), ("Responsive", "Mobile-first"),
                             ("Speed", "Under 2s load"), ("Revisions", "1 round included")],
                },
                {
                    "num": "02", "name": "Content", "h": "Content Creation",
                    "lead": "Professional copy that speaks to your target audience — written for both humans "
                            "and search engines, across every section of the site.",
                    "lists": [
                        {"label": "▸ Copy Deliverables", "items": [
                            "Hero headline & subtext",
                            "About section — company story & mission",
                            "6× service descriptions with features",
                            "Project descriptions & categorization",
                            "Contact section copy",
                            "SEO meta descriptions"]},
                    ],
                    "price_label": "In the complete package", "price": "Included",
                    "price_note": "Every section, written for you",
                    "meta": [("Scope", "Full site copy"), ("SEO", "Meta descriptions"),
                             ("Tone", "Premium, on-brand")],
                },
                {
                    "num": "03", "name": "Hosting", "h": "Hosting & Deployment",
                    "lead": "Reliable, fast hosting with everything configured — so the site loads quickly "
                            "across Saudi Arabia, the GCC, and beyond.",
                    "lists": [
                        {"label": "▸ Infrastructure", "items": [
                            "Domain transfer, configuration & DNS setup",
                            "SSL certificate (HTTPS)",
                            "CDN for global fast loading",
                            "Production deployment & optimization",
                            "Performance monitoring"]},
                    ],
                    "price_label": "In the complete package", "price": "Included",
                    "price_note": "SSL · CDN · monitoring",
                    "meta": [("SSL", "HTTPS included"), ("CDN", "Global edge"),
                             ("Deploy", "Production-optimised")],
                },
                {
                    "num": "04", "name": "Email", "h": "Business Email",
                    "lead": "Professional email that matches your domain — for credible client "
                            "communication and brand consistency.",
                    "lists": [
                        {"label": "▸ Setup", "items": [
                            "Custom domain email (e.g. info@vertexpro.sa)",
                            "Email client setup & configuration",
                            "Spam protection & security",
                            "Setup guidance & onboarding"]},
                    ],
                    "price_label": "In the complete package", "price": "Included",
                    "price_note": "Domain email, configured",
                    "meta": [("Domain", "info@vertexpro.sa"), ("Security", "Spam protection"),
                             ("Onboarding", "Guided setup")],
                },
            ],
        },

        {
            "type": "timeline", "id": "timeline", "kicker": "03 · Timeline",
            "title": "From kickoff to launch in approximately 10 days.",
            "sub": "A tight, focused schedule. Discovery to deployment in two working weeks, with a "
                   "revision round built in before launch.",
            "tracks": [
                {"name": "▸ Design to Launch", "dur": "≈ 10 working days",
                 "phases": [
                     {"num": "D1", "name": "Discovery & Kickoff", "dur": "1 day"},
                     {"num": "D2–4", "name": "Design & Content", "dur": "3 days"},
                     {"num": "D5–7", "name": "Development", "dur": "3 days"},
                     {"num": "D8–9", "name": "Testing & Revisions", "dur": "2 days"},
                     {"num": "D10", "name": "Deployment & Handover", "dur": "1 day"}]},
            ],
            "note": "<strong>Day 1</strong> aligns on brand guidelines, content inputs, imagery, and sitemap. "
                    "<strong>Days 2–7</strong> cover high-fidelity design, all page content, and the responsive "
                    "build with animations, contact form, and SEO. <strong>Days 8–10</strong> handle "
                    "cross-browser testing, revisions, domain/hosting/email setup, SSL, and launch — with "
                    "handover documentation provided.",
        },

        {"type": "raw", "id": "investment", "html": INVESTMENT_HTML},

        {
            "type": "agency", "id": "agency", "kicker": "05 · The Agency",
            "title": "Four reasons to build with us.",
            "cells": [
                {"mark": "▸ ONE", "h": "Design-first approach",
                 "p": "Every pixel is intentional. We obsess over the details so the website feels premium "
                      "and polished — a match for the calibre of the work it represents."},
                {"mark": "▸ TWO", "h": "Performance focused",
                 "p": "Lightning-fast load times, smooth animations, and optimisation for every device and "
                      "connection speed across the region."},
                {"mark": "▸ THREE", "h": "Transparent process",
                 "p": "Regular updates, clear timelines, and no surprises. You always know exactly where the "
                      "project stands."},
                {"mark": "▸ FOUR", "h": "Modern tech stack",
                 "p": "Built with current technologies for reliability, speed, and easy future updates as the "
                      "portfolio and business grow."},
            ],
        },
    ],
}


if __name__ == "__main__":
    print("Built:", T.build(DATA))
