# -*- coding: utf-8 -*-
"""
Upgraded Static-site generator for harrisonbarrow.com (Slate & Gold Theme)
Run:  python3 build.py
Outputs HTML + sitemap.xml + robots.txt + llms.txt + CNAME + manifest into this folder.
"""
import json
import os
import datetime
import html
import re

from site_data import (SITE, TOWNS, COURTS, CREDENTIALS, PRACTICE_AREAS,
                       RESULTS, REVIEWS, GENERAL_FAQS)

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = SITE["domain"].rstrip("/")
TODAY = datetime.date.today().isoformat()

def url(path):
    if not path.startswith("/"):
        path = "/" + path
    return DOMAIN + path

EMOJIS = {
    "oui-dui": "🚗",
    "drug-crimes": "💊",
    "assault-battery": "🛡️",
    "domestic-violence": "🏡",
    "sex-crimes": "⚠️",
    "gun-firearm-crimes": "🔫",
    "theft-larceny": "💰",
    "white-collar-crimes": "💼",
}

ICONS = {
  "oui-dui": '<path d="M3 13l2-5a3 3 0 0 1 2.8-2h8.4A3 3 0 0 1 19 8l2 5v4a1 1 0 0 1-1 1h-1a1 1 0 0 1-1-1v-1H6v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><circle cx="7.5" cy="14.5" r="1.3"/><circle cx="16.5" cy="14.5" r="1.3"/>',
  "drug-crimes": '<path d="M10 2v6.3L5.4 17A2 2 0 0 0 7.2 20h9.6a2 2 0 0 0 1.8-3L14 8.3V2"/><path d="M8.5 2h7"/><path d="M8 14h8"/>',
  "assault-battery": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v4"/><path d="M12 16h.01"/>',
  "domestic-violence": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M12 18s-3-2.2-3-4.2a1.8 1.8 0 0 1 3-1.3 1.8 1.8 0 0 1 3 1.3c0 2-3 4.2-3 4.2z"/>',
  "sex-crimes": '<path d="m14.5 12.5-8 8a2.1 2.1 0 1 1-3-3l8-8"/><path d="m16 16 6-6"/><path d="m8 8 6-6"/><path d="m9 7 8 8"/><path d="m21 11-8-8"/>',
  "gun-firearm-crimes": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
  "theft-larceny": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
  "white-collar-crimes": '<rect width="18" height="13" x="3" y="7" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
  "scale": '<path d="m16 16 3-8 3 8c-.9.6-1.9 1-3 1s-2.1-.4-3-1Z"/><path d="m2 16 3-8 3 8c-.9.6-1.9 1-3 1s-2.1-.4-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
  "gavel": '<path d="m14.5 12.5-8 8a2.1 2.1 0 1 1-3-3l8-8"/><path d="m16 16 6-6"/><path d="m8 8 6-6"/><path d="m9 7 8 8"/><path d="m21 11-8-8"/>',
  "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 8h2M13 8h2M9 12h2M13 12h2M9 16h2M13 16h2"/>',
  "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
  "shieldcheck": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
  "briefcase": '<rect width="18" height="13" x="3" y="7" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
}

def icon(name):
    inner = ICONS.get(name, ICONS["scale"])
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + inner + '</svg>')


NAV = [
    ("home", "Home", "/"),
    ("harrison-barrow", "Harrison Barrow", "/harrison-barrow/"),
    ("criminal-defense", "Criminal Defense", "/criminal-defense/"),
    ("civil-litigation", "Civil Litigation", "/civil-litigation/"),
    ("results", "Results", "/results/"),
    ("reviews", "Reviews", "/reviews/"),
    ("contact", "Contact", "/contact/"),
]

def header(active):
    nav_items = ""
    for key, label, href in NAV:
        is_active_class = " active" if key == active else ""
        
        if key == "criminal-defense":
            submenu = ""
            for pa in PRACTICE_AREAS:
                submenu += f'<li><a href="/criminal-defense/{pa["slug"]}/" class="dropdown-link">{pa["nav"]}</a></li>'
            
            nav_items += f"""
            <div class="nav-item nav-item-dropdown{is_active_class}">
              <a href="/criminal-defense/" class="nav-link">Criminal Defense</a>
              <ul class="dropdown-menu">
                {submenu}
              </ul>
            </div>"""
        else:
            nav_items += f'<div class="nav-item{is_active_class}"><a href="{href}" class="nav-link">{label}</a></div>'

    return f"""
  <header class="header" id="header">
    <div class="container">
      <a href="/" class="logo" aria-label="Harrison Barrow, Attorney at Law P.C. - home">
        <img class="logo-mark" src="/assets/img/logo-mark-gold.png" alt="" width="42" height="40">
        <span class="logo-text">
          <span class="logo-main">Harrison Barrow</span>
          <span class="logo-sub">Attorney at Law P.C.</span>
        </span>
      </a>
      
      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
      
      <nav class="nav-menu" id="nav-menu">
        {nav_items}
        
        <a href="tel:{SITE['phone_tel']}" class="phone-nav-btn">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="margin-right: 4px;"><path d="M6.62 10.79c1.44 2.82 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          {SITE['phone_display']}
        </a>
      </nav>
    </div>
  </header>"""

def footer():
    return f"""
  <footer class="footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-column">
          <a href="/" class="logo" style="margin-bottom: 1.5rem;">
            <img class="logo-mark" src="/assets/img/logo-mark-gold.png" alt="" width="46" height="44">
            <span class="logo-text">
              <span class="logo-main" style="font-size: 1.25rem;">Harrison Barrow</span>
              <span class="logo-sub" style="font-size: 0.6rem;">Attorney at Law P.C.</span>
            </span>
          </a>
          <p style="font-size: 0.85rem; color: var(--text-light-secondary); line-height: 1.6;">Aggressive representation and thorough trial preparation for criminal defendants, individuals, and businesses across Cape Cod.</p>
        </div>
        
        <div class="footer-column">
          <h4>Office Directory</h4>
          <ul class="footer-links-list">
            <li><a href="/" class="footer-link">Home</a></li>
            <li><a href="/harrison-barrow/" class="footer-link">About Harrison</a></li>
            <li><a href="/criminal-defense/" class="footer-link">Criminal Defense</a></li>
            <li><a href="/civil-litigation/" class="footer-link">Civil Litigation</a></li>
            <li><a href="/results/" class="footer-link">Case Results</a></li>
            <li><a href="/reviews/" class="footer-link">Testimonials</a></li>
          </ul>
        </div>
        
        <div class="footer-column">
          <h4>Hyannis Office</h4>
          <address>
            <p><strong>Harrison Barrow, Attorney at Law</strong><br>
            300 Barnstable Rd.<br>
            Hyannis, MA 02601</p>
            <a href="http://maps.google.com/maps?f=q&amp;hl=en&amp;z=15&amp;q=300%20Barnstable%20Rd.,Hyannis,MA,02601" target="_blank" class="footer-map-link">Get Directions &amp; Map [+]</a>
          </address>
        </div>

        <div class="footer-column">
          <h4>Of Counsel Relationship</h4>
          <p style="font-size: 0.85rem; color: var(--text-light-secondary); line-height: 1.6;">
            Harrison is proud to be <strong>Of Counsel</strong> to <a href="https://princimills.com" target="_blank" rel="noopener" style="color: var(--primary-gold); font-weight:600; text-decoration:underline;">Princi Mills Law PC</a>, a leading civil and criminal litigation firm on Cape Cod. This collaboration allows him to leverage additional trial resources and deliver outstanding results for clients with complex legal needs.
          </p>
        </div>
      </div>
      
      <div class="footer-bottom">
        <div class="footer-bottom-info">
          <p>&copy; {datetime.date.today().year} Harrison Barrow, Attorney at Law P.C. All Rights Reserved.</p>
          <p style="margin-top: 0.25rem;">
            <a href="/privacy-policy/" style="text-decoration: underline; margin-right: 1rem;">Privacy Policy</a>
            <a href="/sitemap.xml" style="text-decoration: underline;">Sitemap</a>
          </p>
        </div>
        <div class="footer-bottom-info" style="font-size: 0.85rem; color: var(--primary-gold);">
          Call Today: <a href="tel:{SITE['phone_tel']}" style="font-weight: 600;">{SITE['phone_display']}</a>
        </div>
      </div>
      
      <p class="footer-disclaimer-text">
        <strong>Disclaimer:</strong> The information on this website is for general information purposes only. Nothing on this site should be taken as legal advice for any individual case or situation. This information is not intended to create, and receipt or viewing does not constitute, an attorney-client relationship.
      </p>
    </div>
  </footer>
  
  <div class="callbar">
    <div class="callbar-inner">
      <a href="tel:{SITE['phone_tel']}" class="callbar-item highlight" style="flex: 1;">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M6.62 10.79c1.44 2.82 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        Call 24/7
      </a>
      <a href="/contact/" class="callbar-item" style="flex: 1;">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
        Consult
      </a>
    </div>
  </div>"""

# ---------------------------------------------------------------------------
# Schema & Infrastructure
# ---------------------------------------------------------------------------
def site_nodes():
    firm_id = DOMAIN + "/#firm"
    person_id = DOMAIN + "/#harrison"
    web_id = DOMAIN + "/#website"
    locations = []
    for o in SITE["offices"]:
        locations.append({
            "@type": "Place", "name": o["name"],
            "address": {"@type": "PostalAddress", "streetAddress": o["street"],
                        "addressLocality": o["city"], "addressRegion": o["state"],
                        "postalCode": o["zip"], "addressCountry": "US"},
            "geo": {"@type": "GeoCoordinates", "latitude": o["lat"], "longitude": o["lng"]},
        })
    reviews = [{
        "@type": "Review",
        "author": {"@type": "Person", "name": r[2]},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": r[1],
    } for r in REVIEWS]
    
    firm = {
        "@type": ["LegalService", "Attorney", "LocalBusiness"],
        "@id": firm_id,
        "name": SITE["name"],
        "alternateName": "Harrison Barrow Law",
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/assets/img/logo.png",
        "image": DOMAIN + "/assets/img/og-image.jpg",
        "telephone": SITE["phone_display"],
        "priceRange": "Free consultation",
        "description": "Cape Cod criminal defense and civil litigation firm handling OUI, drug, assault, domestic violence, business litigation, and property disputes.",
        "address": {"@type": "PostalAddress", "streetAddress": SITE["offices"][0]["street"],
                    "addressLocality": SITE["offices"][0]["city"], "addressRegion": "MA",
                    "postalCode": SITE["offices"][0]["zip"], "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["offices"][0]["lat"], "longitude": SITE["offices"][0]["lng"]},
        "location": locations,
        "areaServed": [{"@type": "AdministrativeArea", "name": "Cape Cod, Massachusetts"},
                       {"@type": "AdministrativeArea", "name": "Barnstable County, Massachusetts"},
                       {"@type": "State", "name": "Massachusetts"}],
        "knowsAbout": [pa["nav"] for pa in PRACTICE_AREAS] + ["Criminal defense", "Civil litigation"],
        "founder": {"@id": person_id},
        "employee": {"@id": person_id},
        "sameAs": list(SITE["social"].values()),
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0",
                            "reviewCount": str(len(REVIEWS)), "bestRating": "5"},
        "review": reviews,
    }
    
    person = {
        "@type": "Person",
        "@id": person_id,
        "name": "Harrison Barrow",
        "jobTitle": "Attorney",
        "image": DOMAIN + "/assets/img/harrison-barrow.jpg",
        "url": DOMAIN + "/harrison-barrow/",
        "worksFor": {"@id": firm_id},
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": "Harvard University Extension School"},
            {"@type": "CollegeOrUniversity", "name": "Chicago-Kent College of Law"},
            {"@type": "CollegeOrUniversity", "name": "National Criminal Defense College"},
        ],
        "memberOf": [
            {"@type": "Organization", "name": "Massachusetts Association of Criminal Defense Lawyers"},
            {"@type": "Organization", "name": "National Association of Criminal Defense Lawyers"},
            {"@type": "Organization", "name": "Massachusetts Bar Association"},
            {"@type": "Organization", "name": "Barnstable Bar Advocates"},
        ],
        "award": ["Top 100 Trial Lawyers, The National Trial Lawyers",
                  "Top 40 Under 40, The National Trial Lawyers",
                  "Avvo 10.0 Superb Rating",
                  "First Justice's Pro Bono Publico Award"],
        "knowsAbout": [pa["nav"] for pa in PRACTICE_AREAS] + ["Criminal defense", "Civil litigation"],
    }
    
    website = {
        "@type": "WebSite", "@id": web_id, "url": DOMAIN + "/",
        "name": SITE["name"], "publisher": {"@id": firm_id}, "inLanguage": "en-US",
    }
    return [firm, person, website]

def webpage_node(path, title, desc):
    return {
        "@type": "WebPage", "@id": url(path) + "#webpage", "url": url(path),
        "name": title, "description": desc,
        "isPartOf": {"@id": DOMAIN + "/#website"},
        "about": {"@id": DOMAIN + "/#firm"},
        "inLanguage": "en-US",
    }

def breadcrumb_node(crumbs):
    items = []
    for i, (name, p) in enumerate(crumbs, 1):
        it = {"@type": "ListItem", "position": i, "name": name}
        if p:
            it["item"] = url(p)
        items.append(it)
    return {"@type": "BreadcrumbList", "itemListElement": items}

def faq_node(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}

def service_node(pa):
    return {
        "@type": "Service", "serviceType": pa["nav"],
        "name": pa["h1"], "description": pa["seo_desc"],
        "provider": {"@id": DOMAIN + "/#firm"},
        "areaServed": {"@type": "AdministrativeArea", "name": "Cape Cod, Massachusetts"},
        "url": url(f"/criminal-defense/{pa['slug']}/"),
    }

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def breadcrumbs_html(crumbs):
    lis = ""
    for name, p in crumbs:
        if p:
            lis += f'<li><a href="{p}">{name}</a></li>'
        else:
            lis += f'<li><span aria-current="page">{name}</span></li>'
    return f'<div class="breadcrumbs"><ol style="display:flex; list-style:none; padding:0; margin:0; justify-content:center; align-items:center; gap:0.5rem;">{lis}</ol></div>'

def faq_block(faqs, heading="Frequently Asked Questions", intro=None):
    items = ""
    for i, (q, a) in enumerate(faqs):
        pid = f"faq-{abs(hash(q)) % 100000}-{i}"
        items += f"""
        <div style="border-bottom: 1px solid var(--border-gold-30); padding: 1.5rem 0;">
          <h3 style="font-size: 1.2rem; color: var(--primary-gold); margin-bottom: 0.75rem;">{q}</h3>
          <div style="color: var(--text-light-secondary); font-size: 0.95rem;">{a}</div>
        </div>"""
    intro_html = f'<p style="text-align:center; font-size:1.1rem; color:var(--text-light-secondary); margin-bottom:3rem;">{intro}</p>' if intro else ""
    return f"""
<section class="section section-dark">
  <div class="container" style="max-width: 800px;">
    <div style="text-align: center; margin-bottom: 3rem;">
      <span class="hero-tagline">FAQ</span>
      <h2 style="color: var(--primary-gold); margin-bottom: 1rem;">{heading}</h2>
      {intro_html}
    </div>
    <div style="display: flex; flex-direction: column; gap: 0.5rem;">
      {items}
    </div>
  </div>
</section>"""

def cta_band():
    return f"""
<section class="section section-dark" style="border-top: 1px solid var(--border-gold-30); border-bottom: 1px solid var(--border-gold-30); background-color: var(--bg-dark-tertiary);">
  <div class="container" style="text-align: center; max-width: 800px;">
    <span class="hero-tagline">Consultation</span>
    <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Let's Talk About Your Case Today</h2>
    <p style="color: var(--text-light-secondary); font-size: 1.1rem; margin-bottom: 2.5rem;">Your first consultation is free and completely confidential. Tell me what happened, and I'll tell you honestly where you stand and what your options are.</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn btn-gold">Schedule Free Review</a>
      <a href="tel:{SITE['phone_tel']}" class="btn btn-outline">Call {SITE['phone_display']}</a>
    </div>
  </div>
</section>"""

def aside_block(active_slug=None):
    lis = ""
    for pa in PRACTICE_AREAS:
        cur = ' style="color: var(--accent-gold); font-weight:600;"' if pa["slug"] == active_slug else ""
        lis += f'<li style="margin-bottom: 0.75rem;"><a href="/criminal-defense/{pa["slug"]}/"{cur}>{pa["nav"]}</a></li>'
    return f"""
        <div class="sidebar-card">
          <h4 class="sidebar-title">Defense Areas</h4>
          <ul style="list-style: none; padding: 0; margin-bottom: 2rem;">
            {lis}
          </ul>
          
          <h4 class="sidebar-title">Need Representation?</h4>
          <p style="font-size: 0.9rem; color: var(--text-light-secondary); margin-bottom: 1.5rem;">Get a trial lawyer who is ready to fight in court. Schedule your free evaluation.</p>
          <a href="/contact/" class="btn btn-gold" style="display: block; text-align: center; width: 100%;">Get Help Now</a>
        </div>"""

def page_hero(crumbs, eyebrow, h1, lead):
    crumbs_html = breadcrumbs_html(crumbs)
    return f"""
  <section class="subpage-hero">
    <div class="container">
      <div class="reveal">
        {crumbs_html}
        <h1>{h1}</h1>
        {f'<p class="hero-description" style="margin-top: 1rem; margin-bottom: 0; font-size: 1.1rem; max-width: 800px; margin-left: auto; margin-right: auto;">{lead}</p>' if lead else ""}
      </div>
    </div>
  </section>"""

# ---------------------------------------------------------------------------
# Shell Render
# ---------------------------------------------------------------------------
def render(path, title, desc, body, nav_key=None, extra_nodes=None, og_image=None, page_hero=None, noindex=False):
    graph = site_nodes() + [webpage_node(path, title, desc)]
    if extra_nodes:
        graph += extra_nodes
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    
    canon = url(path)
    robots = ("noindex, follow" if noindex else
              "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")
    
    ogimg = og_image or "/assets/img/og-image.jpg"
    if not ogimg.startswith("http"):
        ogimg = DOMAIN + ogimg
        
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script>document.documentElement.classList.add('js');</script>
  <title>{title}</title>
  <meta name="description" content="{html.escape(desc, quote=True)}">
  <link rel="canonical" href="{canon}">
  <meta name="robots" content="{robots}">
  <meta name="author" content="Harrison Barrow, Attorney at Law, P.C.">
  <meta name="geo.region" content="US-MA">
  <meta name="geo.placename" content="Hyannis, Cape Cod, Massachusetts">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE['name']}">
  <meta property="og:title" content="{html.escape(title, quote=True)}">
  <meta property="og:description" content="{html.escape(desc, quote=True)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{ogimg}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title, quote=True)}">
  <meta name="twitter:description" content="{html.escape(desc, quote=True)}">
  <meta name="twitter:image" content="{ogimg}">
  <meta name="theme-color" content="#0b132b">
  
  <link rel="icon" href="/assets/img/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  
  <link rel="stylesheet" href="/assets/style.css">
  <script type="application/ld+json">
{ld}
  </script>
</head>
<body class="dark-theme">
<a class="skip-link" href="#main">Skip to content</a>
{header(nav_key)}
<main id="main">"""

    tail = f"""</main>
{footer()}
<script src="/assets/script.js"></script>
</body>
</html>"""
    
    out = head + (page_hero or "") + body + tail
    write_file(path, out)

def write_file(path, content):
    if path == "/":
        fp = os.path.join(ROOT, "index.html")
    elif path.endswith("/"):
        fp = os.path.join(ROOT, path.strip("/"), "index.html")
    else:
        fp = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    return fp

# ---------------------------------------------------------------------------
# Page Builders
# ---------------------------------------------------------------------------
def home_body():
    # Practice areas items
    practice_cards = ""
    for pa in PRACTICE_AREAS:
        emoji = icon(pa["slug"])
        practice_cards += f"""
      <div class="card practice-card reveal">
        <div class="card-icon">{emoji}</div>
        <h3>{pa["nav"]}</h3>
        <p>{pa["blurb"]}</p>
        <a href="/criminal-defense/{pa["slug"]}/" class="card-link">Learn More &rarr;</a>
      </div>"""
      
    # Results items
    results_slides = ""
    for verdict, charge, tag, desc in RESULTS[:3]:
        results_slides += f"""
        <div class="results-slide">
          <div class="result-card">
            <div class="result-verdict">{verdict}</div>
            <div class="result-charge">{charge}</div>
            <p class="result-desc">{desc}</p>
            <div class="result-meta">
              <span>Court Case Outcome</span>
              <span>{tag}</span>
            </div>
          </div>
        </div>"""
        
    # Review items
    review_slides = ""
    for title, body, who in REVIEWS:
      review_slides += f"""
        <div class="testimonial-slide">
          <div class="testimonial-quote">“{body}”</div>
          <div class="testimonial-author">{who}</div>
          <div class="testimonial-position">Verified Client Review &bull; Avvo</div>
        </div>"""
        
    return f"""
<section class="hero">
  <div class="container">
    <div class="hero-content reveal">
      <span class="hero-tagline">{SITE['name']}</span>
      <h1>Protecting your future when the stakes are highest</h1>
      <p class="hero-description">For over 15 years, Harrison Barrow has represented clients across Cape Cod and Massachusetts. He defends individuals accused of criminal offenses and advocates for clients in high-stakes civil disputes.</p>
      <div class="hero-actions">
        <a href="/contact/" class="btn btn-gold">Free Consultation</a>
        <a href="tel:{SITE['phone_tel']}" class="btn btn-outline">Call Today: {SITE['phone_display']}</a>
      </div>
      <div class="hero-badges">
        <div class="badge-item">
          <span class="badge-num">Proven</span>
          <span class="badge-label">Trial Experience</span>
        </div>
        <div class="badge-item">
          <span class="badge-num">15+</span>
          <span class="badge-label">Years of Representation</span>
        </div>
        <div class="badge-item">
          <span class="badge-num">Avvo 10.0</span>
          <span class="badge-label">Superb Rating</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 4rem auto;" class="reveal">
      <span class="hero-tagline" style="color: var(--dark-gold);">Advantage</span>
      <h2 style="color: var(--text-dark-primary); margin-bottom: 1.5rem;">Small-Firm Attention. Big-Firm Results.</h2>
      <p style="color: var(--text-dark-secondary); font-size: 1.1rem;">When you are accused of a crime or involved in a business dispute, you deserve a lawyer who knows your name, answers your phone calls, and prepares every case as if it is going to trial.</p>
    </div>
    <div class="grid grid-4">
      <div class="card reveal" style="background-color: var(--bg-light-secondary); border-color: rgba(0,0,0,0.05); color: var(--text-dark-primary);">
        <div class=\"card-icon\" style=\"color: var(--dark-gold);\">{icon('shieldcheck')}</div>
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; text-transform: uppercase;">Trial-Tested Advocate</h3>
        <p style="color: var(--text-dark-secondary); font-size: 0.9rem; margin-bottom: 0;">Strong record of success representing clients in trials. We don't back down from a fight.</p>
      </div>
      <div class="card reveal" style="background-color: var(--bg-light-secondary); border-color: rgba(0,0,0,0.05); color: var(--text-dark-primary);">
        <div class=\"card-icon\" style=\"color: var(--dark-gold);\">{icon('briefcase')}</div>
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; text-transform: uppercase;">Direct Access</h3>
        <p style="color: var(--text-dark-secondary); font-size: 0.9rem; margin-bottom: 0;">You work directly with Harrison himself. You will not be passed off to a rotating cast of paralegals or associates.</p>
      </div>
      <div class="card reveal" style="background-color: var(--bg-light-secondary); border-color: rgba(0,0,0,0.05); color: var(--text-dark-primary);">
        <div class=\"card-icon\" style=\"color: var(--dark-gold);\">{icon('pin')}</div>
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; text-transform: uppercase;">Local Roots</h3>
        <p style="color: var(--text-dark-secondary); font-size: 0.9rem; margin-bottom: 0;">Office in Hyannis. We know the local Cape Cod courts, clerks, and prosecutors inside and out.</p>
      </div>
      <div class="card reveal" style="background-color: var(--bg-light-secondary); border-color: rgba(0,0,0,0.05); color: var(--text-dark-primary);">
        <div class=\"card-icon\" style=\"color: var(--dark-gold);\">{icon('scale')}</div>
        <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; text-transform: uppercase;">Exclusivity & Focus</h3>
        <p style="color: var(--text-dark-secondary); font-size: 0.9rem; margin-bottom: 0;">Specialized in criminal defense and civil litigation. We prepare every case as if it is going to trial.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 4rem auto;" class="reveal">
      <span class="hero-tagline">Our Services</span>
      <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Core Practice Areas</h2>
      <p style="color: var(--text-light-secondary); font-size: 1.1rem;">Aggressive representation and thorough trial preparation for criminal defendants, individuals, and businesses across Cape Cod.</p>
    </div>
    <div class="grid grid-2" style="margin-bottom: 4rem;">
      <div class="card practice-card reveal" style="background-color: var(--bg-dark-secondary);">
        <div class=\"card-icon\">{icon('gavel')}</div>\1
        <p>Facing a criminal charge can threaten your reputation, license, and freedom. We handle OUI/DUI, domestic violence, drug offenses, sex crimes, firearm charges, theft, and white collar crimes.</p>
        <a href="/criminal-defense/" class="card-link">Explore Criminal Defense &rarr;</a>
      </div>
      <div class="card practice-card reveal" style="background-color: var(--bg-dark-secondary);">
        <div class=\"card-icon\">{icon('building')}</div>\1
        <p>Resolving payment disputes, construction defects, change order issues, mechanic's liens, breach of contract, partnership conflicts, and deceptive business practices (M.G.L. c. 93A).</p>
        <a href="/civil-litigation/" class="card-link">Explore Civil Litigation &rarr;</a>
      </div>
    </div>
    
    <div style="text-align: center; margin-bottom: 2rem;">
      <h3 style="color: var(--primary-gold); margin-bottom: 2rem; font-size: 1.5rem; text-transform: uppercase;">Criminal Defense Areas</h3>
    </div>
    <div class="grid grid-3">
      {practice_cards}
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <div class="content-two-columns">
      <div class="reveal">
        <img src="/assets/img/harrison-barrow.jpg" alt="Attorney Harrison Barrow" style="width: 100%; border-radius: 4px; border: 1px solid var(--border-gold-30); box-shadow: var(--shadow-lg);">
      </div>
      <div class="reveal">
        <span class="hero-tagline" style="color: var(--dark-gold);">Meet Your Advocate</span>
        <h2 style="color: var(--text-dark-primary); margin-bottom: 1.5rem;">Harrison Barrow</h2>
        <p style="color: var(--text-dark-secondary);">Harrison Barrow is a third-generation attorney and second-generation Massachusetts trial lawyer. Recognized as a <strong>Top 100 Trial Lawyer</strong> and <strong>Top 40 Under 40</strong> by The National Trial Lawyers, with a perfect <strong>Avvo 10.0</strong> &ldquo;Superb&rdquo; rating, he has built a strong record of success representing clients in the District and Superior courts throughout Cape Cod and the Commonwealth.</p>
        <p style="color: var(--text-dark-secondary);">He trained at the National Criminal Defense College, clerked for the Cook County Homicide Task Force in Chicago, and has earned a reputation for thorough preparation and trial advocacy.</p>
        <a href="/harrison-barrow/" class="btn btn-gold">Learn More About Harrison</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 4rem auto;" class="reveal">
      <span class="hero-tagline">Track Record</span>
      <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Proven Victories</h2>
      <p style="color: var(--text-light-secondary); font-size: 1.1rem;">A representative sample of criminal trial acquittals, dismissals, and reduced charges. Prior results do not guarantee similar outcomes, and this list is not exhaustive of all cases handled or won.</p>
    </div>
    
    <div class="slider-container results-slider reveal">
      <div class="slider-track results-slider-track">
        {results_slides}
      </div>
      <div class="slider-controls">
        <button class="slider-btn slider-prev" aria-label="Previous slide">&larr;</button>
        <button class="slider-btn slider-next" aria-label="Next slide">&rarr;</button>
      </div>
    </div>
    
    <div style="text-align: center; margin-top: 3rem;">
      <a href="/results/" class="btn btn-outline">View Case Results Directory</a>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 4rem auto;" class="reveal">
      <span class="hero-tagline" style="color: var(--dark-gold);">Testimonials</span>
      <h2 style="color: var(--text-dark-primary); margin-bottom: 1.5rem;">What Our Clients Say</h2>
    </div>
    
    <div class="slider-container testimonials-slider reveal">
      <div class="slider-track">
        {review_slides}
      </div>
    </div>
    
    <div style="text-align: center; margin-top: 3rem;">
      <a href="/reviews/" class="btn btn-outline-dark">Read More Reviews</a>
    </div>
  </div>
</section>

<section class="section section-dark" id="evaluate-form">
  <div class="container">
    <div class="content-two-columns">
      <div class="reveal">
        <span class="hero-tagline">Consultation</span>
        <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Request a Free Case Evaluation</h2>
        <p style="color: var(--text-light-secondary);">Charged with a crime or facing a business dispute? Don't wait. Early investigation and legal representation can change the course of your case.</p>
        <p style="color: var(--text-light-secondary);">Fill out the form to tell us about your situation, or call us directly at <a href="tel:{SITE['phone_tel']}" style="font-weight: 600; color: var(--accent-gold);">{SITE['phone_display']}</a>. We are available 24/7 for urgent matters.</p>
        <div style="margin-top: 2rem;">
          <p style="margin-bottom: 0.5rem;">⚖️ <strong>100% Confidential</strong></p>
          <p style="margin-bottom: 0.5rem;">⚖️ <strong>No-Obligation Assessment</strong></p>
          <p style="margin-bottom: 0.5rem;">⚖️ <strong>Of Counsel to Princi Mills Law PC</strong></p>
        </div>
      </div>
      <div class="reveal">
        <div class="sidebar-card">
          <form action="https://formspree.io/f/xjgznjbe" method="POST" class="validated-form">
            <input type="hidden" name="_next" value="https://harrisonbarrow.com/thank-you/">
            <div class="form-group">
              <label class="form-label" for="home-name">Your Name</label>
              <input type="text" id="home-name" name="name" class="form-input" required placeholder="Name">
            </div>
            <div class="form-group">
              <label class="form-label" for="home-phone">Phone Number</label>
              <input type="tel" id="home-phone" name="phone" class="form-input" required placeholder="Phone">
            </div>
            <div class="form-group">
              <label class="form-label" for="home-email">Email Address</label>
              <input type="email" id="home-email" name="email" class="form-input" required placeholder="Email">
            </div>
            <div class="form-group">
              <label class="form-label" for="home-area">Practice Area</label>
              <select id="home-area" name="practice_area" class="form-input" style="background-color: var(--bg-dark-tertiary); color: var(--text-light-secondary);">
                <option value="oui_dui">OUI / DUI Defense</option>
                <option value="domestic_violence">Domestic Violence</option>
                <option value="assault_battery">Assault &amp; Battery</option>
                <option value="civil_litigation">Civil Litigation &amp; Disputes</option>
                <option value="other_criminal">Other Criminal Charge</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label" for="home-message">Message Details</label>
              <textarea id="home-message" name="message" class="form-input" required placeholder="Briefly describe what happened..."></textarea>
            </div>
            <button type="submit" class="btn btn-gold" style="width: 100%;">Submit Case Request</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>"""

def bio_body():
    creds_list = ""
    for c in CREDENTIALS:
        creds_list += f"""
      <div class="card reveal" style="padding: 1.5rem; display: flex; align-items: center; gap: 1rem; background-color: var(--bg-light-secondary); border-color: rgba(0,0,0,0.08); color: var(--text-dark-primary);">
        <span style="color: var(--dark-gold); font-size: 1.25rem;">⚖️</span>
        <p style="margin-bottom: 0; font-size: 0.95rem; line-height: 1.4; color: var(--text-dark-secondary);">{c}</p>
      </div>"""
      
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="content-two-columns">
      <div class="reveal">
        <img src="/assets/img/harrison-barrow.jpg" alt="Attorney Harrison Barrow" style="width: 100%; border-radius: 4px; border: 1px solid var(--border-gold-30); box-shadow: var(--shadow-lg);">
      </div>
      <div class="reveal">
        <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Cape Cod Criminal Defense &amp; Civil Trial Attorney</h2>
        <p style="font-size: 1.1rem; color: var(--text-light-secondary); line-height: 1.6; margin-bottom: 2rem;">
          Harrison Barrow is a trial attorney based in <strong>Hyannis, Massachusetts</strong>, serving Cape Cod and the Commonwealth. A third-generation lawyer and second-generation Massachusetts criminal defense advocate, he represents clients in complex criminal charges and civil litigation. In addition to his independent practice, Harrison is proud to serve <strong>Of Counsel to Princi Mills Law PC</strong>, collaborating with their experienced legal team to deliver expanded trial advocacy resources and stellar representation across Cape Cod.
        </p>
        <p>
          He earned his undergraduate degree from <strong>Harvard University Extension School</strong> (Bachelor of Liberal Arts in Social Sciences, with a focus on Psychology), then his Juris Doctor from <strong>Chicago-Kent College of Law</strong> as a merit scholar, with a certificate in criminal litigation. While at Chicago-Kent he attended the Summer Program in Law at Cambridge University and served as an associate editor of the Chicago-Kent Journal of International and Comparative Law. He clerked for the Cook County Public Defender's Office, Homicide Task Force, in Chicago.
        </p>
        <p>
          Harrison's practice extends beyond criminal defense to include civil litigation, representing business owners, contractors, and individuals in complex payment, breach of contract, and construction disputes. He is also panel certified to represent children and parents in complex child and family law cases. He is an active member of several professional organizations including the Barnstable Bar Advocates, Massachusetts Bar Association, National Association of Criminal Defense Lawyers, and Massachusetts Association of Criminal Defense Lawyers.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 4rem auto;" class="reveal">
      <span class="hero-tagline" style="color: var(--dark-gold);">Recognition &amp; Credentials</span>
      <h2 style="color: var(--text-dark-primary);">Professional Credentials</h2>
    </div>
    <div class="grid grid-3">
      {creds_list}
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container" style="max-width: 800px;">
    <div class="reveal">
      <h2 style="color: var(--primary-gold); margin-bottom: 2rem; text-align: center;">Education, Training &amp; Admissions</h2>
      
      <div style="margin-bottom: 2.5rem;">
        <h3 style="color: var(--accent-gold); font-size: 1.35rem; border-bottom: 1px solid var(--border-gold-30); padding-bottom: 0.5rem; margin-bottom: 1rem;">Education</h3>
        <ul style="list-style: square; padding-left: 1.5rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-light-secondary);">
          <li><strong>Juris Doctor:</strong> Chicago-Kent College of Law (Merit Scholar; Certificate in Criminal Litigation; Chicago-Kent Journal of International and Comparative Law Associate Editor)</li>
          <li><strong>Bachelor of Liberal Arts</strong>, Social Sciences (Psychology focus), Harvard University Extension School</li>
          <li><strong>Cambridge University Summer Law Program:</strong> Certificate of Completion (Cambridge, England)</li>
        </ul>
      </div>
      
      <div style="margin-bottom: 2.5rem;">
        <h3 style="color: var(--accent-gold); font-size: 1.35rem; border-bottom: 1px solid var(--border-gold-30); padding-bottom: 0.5rem; margin-bottom: 1rem;">Court Admissions</h3>
        <ul style="list-style: square; padding-left: 1.5rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-light-secondary);">
          <li>Commonwealth of Massachusetts (All District and Superior Courts)</li>
          <li>U.S. District Court, District of Massachusetts</li>
        </ul>
      </div>
      
      <div>
        <h3 style="color: var(--accent-gold); font-size: 1.35rem; border-bottom: 1px solid var(--border-gold-30); padding-bottom: 0.5rem; margin-bottom: 1rem;">Specialized Legal Training</h3>
        <ul style="list-style: square; padding-left: 1.5rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-light-secondary);">
          <li><strong>National Criminal Defense College (NCDC):</strong> Graduate (Trial Practice Institute)</li>
          <li>Committee for Public Counsel Services (CPCS) panel certifications: Criminal Defense, Children and Family Law (CAFL)</li>
        </ul>
      </div>
      
    </div>
  </div>
</section>
{cta_band()}"""

def criminal_defense_body():
    cards = ""
    for pa in PRACTICE_AREAS:
        emoji = icon(pa["slug"])
        cards += f"""
      <div class="card practice-card reveal" style="background-color: var(--bg-dark-secondary);">
        <div class="card-icon">{emoji}</div>
        <h3>{pa["nav"]}</h3>
        <p>{pa["blurb"]}</p>
        <a href="/criminal-defense/{pa["slug"]}/" class="card-link">Explore Charges &rarr;</a>
      </div>"""
      
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="content-two-columns" style="margin-bottom: 4rem;">
      <div class="reveal">
        <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Boutique Representation. Aggressive Defense.</h2>
        <p style="font-size: 1.1rem; color: var(--text-light-secondary); line-height: 1.6;">
          If you have been charged with a crime, or are currently under investigation, the actions you take now will affect your record, your family, and your freedom. In Massachusetts, prosecutors build their cases early, and the Registry of Motor Vehicles moves quickly to suspend licenses after arrests. 
        </p>
        <p>
          At Harrison Barrow, Attorney at Law P.C., we provide dedicated, local defense across Cape Cod. We prepare every case as if it is going to trial, giving us maximum leverage to secure dismissals, reductions, and not-guilty verdicts.
        </p>
      </div>
      <div class="reveal">
        <div class="sidebar-card">
          <h4 class="sidebar-title">Our Philosophy</h4>
          <p style="font-size: 0.9rem; color: var(--text-light-secondary); margin-bottom: 1rem;">⚖️ <strong>Investigation First</strong>: We review all police reports, breathalyzer calibration logs, and witness statements to find errors.</p>
          <p style="font-size: 0.9rem; color: var(--text-light-secondary); margin-bottom: 1rem;">⚖️ <strong>Trial Preparedness</strong>: We do not push for quick plea deals. We prepare to defend your rights in front of a jury.</p>
          <p style="font-size: 0.9rem; color: var(--text-light-secondary); margin-bottom: 0;">⚖️ <strong>Avvo 10.0 &ldquo;Superb&rdquo; Rating</strong>: Top legal rating, recognized by peers and clients.</p>
        </div>
      </div>
    </div>
    
    <div style="margin-top: 5rem;">
      <h2 style="color: var(--primary-gold); margin-bottom: 3rem; text-align: center;">Defense Practice Areas</h2>
      <div class="grid grid-3">
        {cards}
      </div>
    </div>
  </div>
</section>
{cta_band()}"""

def practice_body(pa):
    sections_html = ""
    for heading, html_content in pa["sections"]:
        sections_html += f"""
        <div style="margin-bottom: 3rem; border-bottom: 1px solid var(--border-gold-30); padding-bottom: 2rem;">
          <h3 style="color: var(--primary-gold); margin-bottom: 1rem;">{heading}</h3>
          <div style="color: var(--text-light-secondary); font-size: 1rem; line-height: 1.7;">{html_content}</div>
        </div>"""
        
    sidebar_aside = aside_block(pa["slug"])
    
    statute_block = f"""
        <div class="sidebar-card" style="border-color: var(--primary-gold);">
          <span class="hero-tagline" style="font-size: 0.75rem;">{pa["statute_tag"]}</span>
          <p style="font-size: 0.9rem; color: var(--text-light-secondary); line-height: 1.6; margin-top: 0.5rem; margin-bottom: 0;">
            {pa["statute_html"]}
          </p>
        </div>"""
        
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="content-two-columns">
      
      <div class="reveal">
        <div style="margin-bottom: 3rem; font-size: 1.1rem; color: var(--text-light-secondary); line-height: 1.7;">
          {pa["intro"]}
        </div>
        
        {sections_html}
      </div>
      
      <div class="reveal">
        {statute_block}
        {sidebar_aside}
      </div>
      
    </div>
  </div>
</section>
{faq_block(pa["faqs"], f"FAQ: {pa['nav']}", f"Common questions and answers regarding {pa['nav'].lower()} charges in Massachusetts.")}
{cta_band()}"""

def civil_litigation_body():
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="content-two-columns">
      
      <!-- Left Side: Practice Details -->
      <div class="reveal">
        <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Resolving Complex Business &amp; Property Disputes</h2>
        <p style="font-size: 1.1rem; color: var(--text-light-secondary); margin-bottom: 2rem;">
          When business deals break down, construction projects fail, or contracts are breached, the financial stakes can be devastating. Navigating civil litigation in Massachusetts requires more than just filling out paperwork. It requires a trial attorney who understands how to build a case, present complex evidence, and argue persuasively before judges and juries.
        </p>
        
        <p>
          At Harrison Barrow, Attorney at Law, P.C., we bring our rich trial legacy and courtroom trial experience to civil disputes. We represent contractors, homeowners, business owners, and individuals throughout Cape Cod in District and Superior courts.
        </p>
        
        <!-- Detailed Civil Sections -->
        <div style="margin-top: 3rem; display: flex; flex-direction: column; gap: 3rem;">
          
          <!-- Section 1: Construction Disputes -->
          <div style="border-bottom: 1px solid var(--border-gold-30); padding-bottom: 2rem;">
            <h3 style="color: var(--primary-gold); margin-bottom: 1rem;">Construction Disputes</h3>
            <p>
              Cape Cod's active residential and commercial building industry frequently generates disputes over payments, workmanship, and project delays. We represent all sides in these conflicts:
            </p>
            <ul style="list-style: square; padding-left: 1.25rem; color: var(--text-light-secondary); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
              <li><strong>Mechanic's Liens:</strong> Drafting, filing, and enforcing liens to secure payment for contractors, subcontractors, and material suppliers under M.G.L. c. 254.</li>
              <li><strong>Payment Disputes &amp; Non-Performance:</strong> Seeking damages for unpaid work, or defending claims of non-payment.</li>
              <li><strong>Construction Defects:</strong> Representing property owners seeking damages for poor workmanship, structural defects, and code violations, or defending contractors against exaggerated claims.</li>
              <li><strong>Change Order &amp; Delay Claims:</strong> Resolving conflicts over scope-of-work modifications and cost overruns.</li>
            </ul>
          </div>

          <!-- Section 2: Business Litigation -->
          <div style="border-bottom: 1px solid var(--border-gold-30); padding-bottom: 2rem;">
            <h3 style="color: var(--primary-gold); margin-bottom: 1rem;">Business Litigation</h3>
            <p>
              Operating a business involves constant legal risk. When disputes threaten your company's survival, we step in to resolve them efficiently, through mediation or in court:
            </p>
            <ul style="list-style: square; padding-left: 1.25rem; color: var(--text-light-secondary); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
              <li><strong>Partnership &amp; Shareholder Disputes:</strong> Resolving internal conflicts over business assets, control, and division of profits, including breach of fiduciary duty claims.</li>
              <li><strong>Tortious Interference:</strong> Seeking damages when a competitor unlawfully interferes with your business contracts or relationships.</li>
              <li><strong>Fraud &amp; Deceptive Practices:</strong> Representing businesses in disputes involving consumer protection claims (M.G.L. c. 93A) and unfair competition.</li>
            </ul>
          </div>

          <!-- Section 3: Breach of Contract -->
          <div style="border-bottom: 1px solid var(--border-gold-30); padding-bottom: 2rem;">
            <h3 style="color: var(--primary-gold); margin-bottom: 1rem;">Breach of Contract</h3>
            <p>
              Contracts are the foundation of all commercial transactions. When one party fails to live up to their obligations, we act quickly to enforce the agreement:
            </p>
            <ul style="list-style: square; padding-left: 1.25rem; color: var(--text-light-secondary); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
              <li><strong>Vendor &amp; Supplier Disputes:</strong> Enforcing supply agreements, commercial purchase agreements, and distributor contracts.</li>
              <li><strong>Commercial Lease Disputes:</strong> Representing landlords or commercial tenants in lease violations, non-payment, and eviction actions.</li>
              <li><strong>Collections &amp; Debt Recovery:</strong> Pursuing unpaid commercial accounts and invoices, securing attachments, and enforcing judgements.</li>
            </ul>
          </div>

          <!-- Section 4: M.G.L. c. 93A Consumer Protection -->
          <div style="border-bottom: 1px solid var(--border-gold-30); padding-bottom: 2rem;">
            <h3 style="color: var(--primary-gold); margin-bottom: 1rem;">M.G.L. c. 93A Consumer Protection</h3>
            <p>
              Massachusetts General Laws Chapter 93A prohibits unfair methods of competition and deceptive business practices. This powerful statute provides remedies for both individuals and businesses. Because a 93A violation can carry double or treble damages and mandatory attorney's fees, these cases have very high stakes:
            </p>
            <ul style="list-style: square; padding-left: 1.25rem; color: var(--text-light-secondary); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
              <li><strong>Consumer Actions (Section 9):</strong> Representing individuals defrauded or subjected to deceptive practices by businesses, ranging from home improvement contractors to auto dealers.</li>
              <li><strong>Business-to-Business Litigation (Section 11):</strong> Pursuing claims where a commercial partner has acted in bad faith, engaged in deceptive billing, or breached an agreement with unfair intent.</li>
              <li><strong>Defense of 93A Claims:</strong> Defending businesses against bad-faith or exaggerated 93A demand letters, helping negotiate pre-litigation settlements to avoid multiple damage liability.</li>
            </ul>
          </div>

          <!-- Section 5: Personal Injury Litigation -->
          <div>
            <h3 style="color: var(--primary-gold); margin-bottom: 1rem;">Personal Injury</h3>
            <p>
              When negligence causes serious physical or financial harm, you deserve trial-ready advocacy to hold the responsible parties and insurance companies accountable. We handle personal injury claims across Cape Cod:
            </p>
            <ul style="list-style: square; padding-left: 1.25rem; color: var(--text-light-secondary); display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
              <li><strong>Motor Vehicle Accidents:</strong> Representing drivers, passengers, and pedestrians injured in car, truck, or motorcycle collisions on Cape Cod roads.</li>
              <li><strong>Premises Liability:</strong> Pursuing claims for injuries sustained due to unsafe property conditions, slip-and-falls, or inadequate maintenance.</li>
              <li><strong>Serious Injury &amp; Wrongful Death:</strong> Providing compassionate, aggressive trial advocacy to secure full compensation for medical bills, lost wages, and pain and suffering.</li>
            </ul>
          </div>
          
        </div>
      </div>
      
      <!-- Right Side: Sidebar -->
      <div class="reveal">
        
        <!-- Contact Card -->
        <div class="sidebar-card">
          <h4 class="sidebar-title">Dispute Evaluation</h4>
          <p style="font-size: 0.9rem; color: var(--text-light-secondary); margin-bottom: 1.5rem;">Have a contract breach or payment issue? Tell us about your dispute.</p>
          <form action="https://formspree.io/f/xjgznjbe" method="POST" class="validated-form">
            <input type="hidden" name="_next" value="https://harrisonbarrow.com/thank-you/">
            <input type="hidden" name="practice_area" value="civil_litigation">
            <div class="form-group">
              <label class="form-label" for="side-name">Your Name</label>
              <input type="text" id="side-name" name="name" class="form-input" required placeholder="Name">
            </div>
            <div class="form-group">
              <label class="form-label" for="side-phone">Phone Number</label>
              <input type="tel" id="side-phone" name="phone" class="form-input" required placeholder="Phone">
            </div>
            <div class="form-group">
              <label class="form-label" for="side-amount">Disputed Amount ($)</label>
              <input type="text" id="side-amount" name="disputed_amount" class="form-input" placeholder="e.g. $50,000">
            </div>
            <div class="form-group">
              <label class="form-label" for="side-details">Dispute Details</label>
              <textarea id="side-details" name="message" class="form-input" required placeholder="Describe the dispute or contract terms..."></textarea>
            </div>
            <button type="submit" class="btn btn-gold" style="width: 100%;">Evaluate My Case</button>
          </form>
        </div>
        
        <!-- Core Credentials -->
        <div class="sidebar-card">
          <h4 class="sidebar-title">Our Advantage</h4>
          <div class="sidebar-links" style="font-size: 0.9rem; color: var(--text-light-secondary);">
            <p style="margin-bottom: 0.75rem;">⚖️ <strong>Trial-Ready Approach</strong>: We prepare every civil case for trial, which gives us maximum leverage during settlement negotiations.</p>
            <p style="margin-bottom: 0.75rem;">⚖️ <strong>Clear Communication</strong>: We keep you informed at every stage, detailing the costs, risks, and potential benefits of litigation.</p>
            <p>⚖️ <strong>Of Counsel, Princi Mills Law PC</strong>: Added trial resources for complex civil and business matters.</p>
          </div>
        </div>
        
      </div>
      
    </div>
  </div>
</section>
{cta_band()}"""

def results_body():
    cards = ""
    for verdict, charge, tag, desc in RESULTS:
        # Simplify tag to slug for data-filter checking
        slug_tag = tag.lower().replace(" ", "-")
        cards += f"""
      <div class="result-card reveal" data-category="{slug_tag}">
        <div class="result-verdict">{verdict}</div>
        <div class="result-charge">{charge}</div>
        <p class="result-desc">{desc}</p>
        <div class="result-meta">
          <span>Court Case Outcome</span>
          <span>{tag}</span>
        </div>
      </div>"""
      
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="reveal" style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
      <h2 style="color: var(--primary-gold); margin-bottom: 1rem;">Proven Victories in Court</h2>
      <p style="color: var(--text-light-secondary); font-size: 1.1rem;">
        Below is a representative selection of real court outcomes achieved for clients in Massachusetts District and Superior courts. This list is illustrative and does not represent all cases handled or won.
      </p>
    </div>

    <!-- Interactive category buttons -->
    <div class="filter-container reveal">
      <button class="filter-btn active" data-filter="all">All Cases</button>
      <button class="filter-btn" data-filter="oui">OUI / DUI</button>
      <button class="filter-btn" data-filter="domestic">Domestic Violence</button>
      <button class="filter-btn" data-filter="assault">Assault</button>
      <button class="filter-btn" data-filter="sex-crimes">Sex Crimes</button>
      <button class="filter-btn" data-filter="theft">Theft</button>
      <button class="filter-btn" data-filter="property">Property</button>
    </div>

    <div class="grid grid-3 results-grid reveal" style="align-items: stretch; margin-bottom: 3.5rem;">
      {cards}
    </div>
    
    <div class="callout reveal" style="border-left: 3px solid var(--accent-red); background-color: var(--bg-dark-secondary); padding: 1.5rem; border-radius: 4px;">
      <p style="margin-bottom: 0; font-size: 0.85rem; color: var(--text-light-secondary); line-height: 1.6;">
        <strong>Disclaimer:</strong> Prior results do not guarantee a similar outcome. Every case is unique and depends entirely on its own facts, laws, and evidence. The case summaries above represent a selection of highlighted outcomes and are not an exhaustive list of all case victories or representation.
      </p>
    </div>
  </div>
</section>
{cta_band()}"""

def reviews_body():
    cards = ""
    for title, body, who in REVIEWS:
        cards += f"""
      <div class="card reveal" style="background-color: var(--bg-dark-secondary); display: flex; flex-direction: column;">
        <span style="color: var(--accent-gold); font-size: 1.25rem; margin-bottom: 1rem;">★★★★★</span>
        <h3 style="font-size: 1.2rem; margin-bottom: 0.75rem; color: var(--primary-gold); text-transform: uppercase;">"{title}"</h3>
        <p style="color: var(--text-light-secondary); font-size: 0.95rem; line-height: 1.6; flex-grow: 1; margin-bottom: 1.5rem;">“{body}”</p>
        <div style="border-top: 1px solid var(--border-gold-30); padding-top: 0.75rem; font-size: 0.85rem; color: var(--primary-gold); font-weight: 500;">
          {who} &bull; Verified Client
        </div>
      </div>"""
      
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="reveal" style="text-align: center; max-width: 800px; margin: 0 auto 4rem auto;">
      <h2 style="color: var(--primary-gold); margin-bottom: 1rem;">Client Testimonials &amp; Reviews</h2>
      <p style="color: var(--text-light-secondary); font-size: 1.1rem;">
        Authentic reviews and testimonials from people Harrison has represented in court.
      </p>
    </div>
    
    <div class="grid grid-3" style="margin-bottom: 4rem;">
      {cards}
    </div>
    
    <div class="reveal" style="text-align: center; border-top: 1px solid var(--border-gold-30); padding-top: 3rem;">
      <p style="color: var(--text-light-secondary); margin-bottom: 1.5rem;">We value client feedback. You can read more verified peer and client ratings on our public directories:</p>
      <div class="hero-actions">
        <a href="{SITE['social']['Avvo']}" target="_blank" rel="noopener" class="btn btn-outline">Read Avvo Reviews</a>
        <a href="{SITE['social']['Google']}" target="_blank" rel="noopener" class="btn btn-outline">Read Google Reviews</a>
      </div>
    </div>
  </div>
</section>
{cta_band()}"""

def contact_body():
    return f"""
<section class="section section-dark">
  <div class="container">
    <div class="content-two-columns">
      
      <div class="reveal">
        <h2 style="color: var(--primary-gold); margin-bottom: 1.5rem;">Speak to an Attorney Today</h2>
        <p style="font-size: 1.1rem; color: var(--text-light-secondary); line-height: 1.6; margin-bottom: 2rem;">
          Your first consultation is free, confidential, and carries no obligation. Let's discuss your charges, business dispute, or contract terms, and find your legal options.
        </p>
        
        <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 2.5rem;">
          <div style="display: flex; gap: 1rem; align-items: start;">
            <span style="font-size: 1.5rem; color: var(--accent-gold); line-height: 1;">📞</span>
            <div>
              <h4 style="margin-bottom: 0.25rem; font-size: 1.1rem; color: var(--primary-gold);">Call 24/7</h4>
              <p style="margin-bottom: 0; color: var(--text-light-secondary);"><a href="tel:{SITE['phone_tel']}" style="font-weight: 600; font-size: 1.15rem;">{SITE['phone_display']}</a></p>
            </div>
          </div>
          
          <div style="display: flex; gap: 1rem; align-items: start;">
            <span style="font-size: 1.5rem; color: var(--accent-gold); line-height: 1;">📍</span>
            <div>
              <h4 style="margin-bottom: 0.25rem; font-size: 1.1rem; color: var(--primary-gold);">Hyannis Office</h4>
              <p style="margin-bottom: 0; color: var(--text-light-secondary);">300 Barnstable Rd., Hyannis, MA 02601</p>
            </div>
          </div>
          
          <div style="display: flex; gap: 1rem; align-items: start;">
            <span style="font-size: 1.5rem; color: var(--accent-gold); line-height: 1;">⚖️</span>
            <div>
              <h4 style="margin-bottom: 0.25rem; font-size: 1.1rem; color: var(--primary-gold);">Of Counsel</h4>
              <p style="margin-bottom: 0; color: var(--text-light-secondary);">Proudly Of Counsel to <a href="https://princimills.com" target="_blank" rel="noopener" style="color: var(--accent-gold); text-decoration: underline;">Princi Mills Law PC</a></p>
            </div>
          </div>
        </div>
        
        <div class="sidebar-card" style="background-color: var(--bg-dark-tertiary);">
          <p style="font-size: 0.95rem; margin-bottom: 0; line-height: 1.6; color: var(--text-light-secondary);">
            <strong>Confidentiality Warning:</strong> Submitting case details through this form does not create an attorney-client relationship. Please do not send sensitive, highly confidential details until we have completed a conflict-of-interest check.
          </p>
        </div>
      </div>
      
      <div class="reveal">
        <div class="sidebar-card">
          <h3 class="sidebar-title">Request Consult</h3>
          <form action="https://formspree.io/f/xjgznjbe" method="POST" class="validated-form">
            <input type="hidden" name="_next" value="https://harrisonbarrow.com/thank-you/">
            <div class="form-group">
              <label class="form-label" for="contact-name">Full Name</label>
              <input type="text" id="contact-name" name="name" class="form-input" required placeholder="Name">
            </div>
            <div class="form-group">
              <label class="form-label" for="contact-phone">Phone Number</label>
              <input type="tel" id="contact-phone" name="phone" class="form-input" required placeholder="Phone">
            </div>
            <div class="form-group">
              <label class="form-label" for="contact-email">Email Address</label>
              <input type="email" id="contact-email" name="email" class="form-input" required placeholder="Email">
            </div>
            <div class="form-group">
              <label class="form-label" for="contact-area">Case Category</label>
              <select id="contact-area" name="practice_area" class="form-input" style="background-color: var(--bg-dark-tertiary); color: var(--text-light-secondary);">
                <option value="oui_dui">OUI / DUI Defense</option>
                <option value="domestic_violence">Domestic Violence</option>
                <option value="assault_battery">Assault &amp; Battery</option>
                <option value="civil_litigation">Civil Litigation &amp; Disputes</option>
                <option value="other_criminal">Other Criminal Case</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label" for="contact-details">Case / Dispute Details</label>
              <textarea id="contact-details" name="message" class="form-input" required placeholder="Describe your case or dispute..."></textarea>
            </div>
            <button type="submit" class="btn btn-gold" style="width: 100%;">Submit Case Request</button>
          </form>
        </div>
      </div>
      
    </div>
  </div>
</section>"""

def thankyou_body():
    return f"""
<section class="section section-dark" style="min-height: 70vh; display: flex; align-items: center; text-align: center;">
  <div class="container" style="max-width: 600px;">
    <div class="reveal">
      <span style="font-size: 4rem; color: var(--primary-gold); display: block; margin-bottom: 1.5rem;">⚖️</span>
      <h1 style="color: var(--primary-gold); margin-bottom: 1rem;">Thank You</h1>
      <p style="font-size: 1.15rem; color: var(--text-light-secondary); line-height: 1.6; margin-bottom: 2.5rem;">
        Your consultation request has been received. Harrison will review your details and contact you shortly. If this is an urgent matter or you have just been arrested, please call us directly.
      </p>
      <div class="hero-actions" style="justify-content: center;">
        <a href="/" class="btn btn-gold">Back to Homepage</a>
        <a href="tel:{SITE['phone_tel']}" class="btn btn-outline">Call Now: {SITE['phone_display']}</a>
      </div>
    </div>
  </div>
</section>"""

def privacy_body():
    return f"""
<section class="section section-dark">
  <div class="container" style="max-width: 800px; line-height: 1.8;">
    <div class="reveal">
      <p style="font-style: italic; color: var(--primary-gold); margin-bottom: 2rem;">Last Updated: {datetime.date.today().strftime('%B %Y')}</p>
      
      <p>Harrison Barrow, Attorney at Law P.C. ("we," "us," or "our") operates the website harrisonbarrow.com. This Privacy Policy describes how we collect, use, and protect your personal information when you use our website, particularly through our case evaluation forms.</p>
      
      <h3 style="color: var(--primary-gold); margin-top: 2rem; margin-bottom: 1rem; text-transform: uppercase;">1. Information We Collect</h3>
      <p>When you contact us using our online forms, we collect the personal information you submit, which may include your name, phone number, email address, case area, and details about your case or dispute. We do not use third-party tracking pixels or cookies to build advertising profiles.</p>
      
      <h3 style="color: var(--primary-gold); margin-top: 2rem; margin-bottom: 1rem; text-transform: uppercase;">2. How We Use Your Information</h3>
      <p>We use the information you submit solely to respond to your inquiry and to evaluate whether we can assist you with your legal needs. We do not sell, rent, or lease your personal details to third parties.</p>
      
      <h3 style="color: var(--primary-gold); margin-top: 2rem; margin-bottom: 1rem; text-transform: uppercase;">3. Data Retention and Security</h3>
      <p>We store form submissions securely via our form processor (Formspree) which enforces data encryption. Only authorized firm personnel have access to submissions. However, no internet transmission is 100% secure, so please do not send highly sensitive data before we formally agree to represent you.</p>
      
      <h3 style="color: var(--primary-gold); margin-top: 2rem; margin-bottom: 1rem; text-transform: uppercase;">4. Contact Us</h3>
      <p>If you have any questions about this policy, please contact us at {SITE['phone_display']} or at our office in Hyannis, MA.</p>
    </div>
  </div>
</section>"""

def notfound_body():
    return f"""
<section class="section section-dark" style="min-height: 70vh; display: flex; align-items: center; text-align: center;">
  <div class="container" style="max-width: 600px;">
    <div class="reveal">
      <span style="font-size: 4rem; color: var(--primary-gold); display: block; margin-bottom: 1.5rem;">⚠️</span>
      <h1 style="color: var(--primary-gold); margin-bottom: 1rem;">Page Not Found (404)</h1>
      <p style="font-size: 1.15rem; color: var(--text-light-secondary); line-height: 1.6; margin-bottom: 2.5rem;">
        The page you are looking for does not exist or has been moved. Use the buttons below to find what you need.
      </p>
      <div class="hero-actions" style="justify-content: center;">
        <a href="/" class="btn btn-gold">Back to Homepage</a>
        <a href="/criminal-defense/" class="btn btn-outline">Practice Areas</a>
      </div>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------------------
# Infrastructure Generation
# ---------------------------------------------------------------------------
def build_infra():
    # Sitemap
    urls = [
        ("/", "1.0", "weekly"),
        ("/harrison-barrow/", "0.9", "monthly"),
        ("/criminal-defense/", "0.9", "monthly"),
        ("/civil-litigation/", "0.9", "monthly"),
        ("/results/", "0.8", "monthly"),
        ("/reviews/", "0.8", "monthly"),
        ("/contact/", "0.9", "monthly"),
        ("/privacy-policy/", "0.3", "yearly")
    ]
    for pa in PRACTICE_AREAS:
        urls.append((f"/criminal-defense/{pa['slug']}/", "0.8", "monthly"))
        
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p, pr, cf in urls:
        sm += ["  <url>", f"    <loc>{url(p)}</loc>", f"    <lastmod>{TODAY}</lastmod>",
               f"    <changefreq>{cf}</changefreq>", f"    <priority>{pr}</priority>", "  </url>"]
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm))

    # Robots.txt
    ai_bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User",
               "Claude-SearchBot", "anthropic-ai", "Google-Extended", "PerplexityBot",
               "Perplexity-User", "Applebot", "Applebot-Extended", "Amazonbot",
               "meta-externalagent", "Bingbot", "CCBot", "Google-CloudVertexBot"]
    lines = ["# robots.txt for harrisonbarrow.com",
             "# Search engines and AI assistants are welcome to crawl and cite this site.",
             "", "User-agent: *", "Allow: /", ""]
    for b in ai_bots:
        lines += [f"User-agent: {b}", "Allow: /", ""]
    lines += [f"Sitemap: {DOMAIN}/sitemap.xml", ""]
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(lines))

    # LLMs.txt
    L = [f"# {SITE['name']}", "",
         f"> Cape Cod trial attorney based in Hyannis, Massachusetts, and Of Counsel at Princi Mills Law PC. Harrison Barrow represents clients in Criminal Defense "
         f"(OUI/DUI, domestic violence, drug offenses, assault, sex crimes, firearm charges, "
         f"theft, and white collar crimes) and Civil Litigation (construction disputes, "
         f"mechanic's liens, payment disputes, breach of contract, partnership conflicts, and M.G.L. c. 93A). "
         f"Third-generation attorney with proven trial experience. Free consultation: {SITE['phone_display']}.", "",
         "## Key facts",
         f"- Attorney: Harrison Barrow, a third-generation trial lawyer and second-generation MA criminal defense lawyer. He is Of Counsel at Princi Mills Law PC, holds a perfect Avvo 10.0 Superb rating, and is recognized among the Top 100 Trial Lawyers and Top 40 Under 40 (The National Trial Lawyers).",
         f"- Focus Areas: Criminal Defense, Civil Litigation & Business Disputes.",
         f"- Phone: {SITE['phone_display']}",
         f"- Office: 300 Barnstable Road, Hyannis, MA 02601 (Of Counsel at Princi Mills Law PC).",
         f"- Service area: Cape Cod, Barnstable County, and all 14 Massachusetts counties.", "",
         "## Practice areas"]
    for pa in PRACTICE_AREAS:
        L.append(f"- [{pa['nav']}]({url('/criminal-defense/'+pa['slug']+'/')}): {pa['blurb']}")
    L.append(f"- [Civil Litigation]({url('/civil-litigation/')}): Commercial contract breaches, business litigation, mechanic's liens / construction disputes, M.G.L. c. 93A consumer protection claims (both prosecution and defense), and personal injury.")
    L += ["", "## Key pages",
          f"- [Harrison Barrow Biography]({url('/harrison-barrow/')}): Education, training, court admissions, and awards.",
          f"- [Case Results]({url('/results/')}): Authentic outcomes (dismissals, not-guilty verdicts, and civil resolutions).",
          f"- [Client Reviews]({url('/reviews/')}): Verified client testimonials.",
          f"- [Contact]({url('/contact/')}): 24/7 client evaluation lines and office maps.", "",
          "## Disclaimers",
          "- Prior results do not guarantee a similar outcome.",
          "- This site is attorney advertising; contacting the firm does not create an attorney-client relationship.", ""]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(L))

    # CNAME
    open(os.path.join(ROOT, "CNAME"), "w").write(DOMAIN.split("//")[1] + "\n")

# ---------------------------------------------------------------------------
# Main Builder Entry
# ---------------------------------------------------------------------------
def main():
    print("Building site files...")
    
    # 1. Homepage
    render("/", "Cape Cod Criminal Defense & Civil Litigation | Harrison Barrow, Attorney at Law P.C.",
           "Harrison Barrow, Attorney at Law, P.C. is a premier Cape Cod law firm focused on aggressive representation and trial preparation. Office in Hyannis, MA. Call (508) 945-1400 for a free consult.",
           home_body(), nav_key="home")
           
    # 2. Biography Bio Page
    render("/harrison-barrow/", "Harrison Barrow | Criminal Defense & Civil Litigation Attorney",
           "Meet attorney Harrison Barrow, a third-generation trial lawyer on Cape Cod with a proven record of courtroom success. Learn about his background, education, and credentials.",
           bio_body(), nav_key="harrison-barrow")
           
    # 3. About redirect
    about_redirect_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=/harrison-barrow/">
  <title>Redirecting...</title>
  <link rel="canonical" href="https://harrisonbarrow.com/harrison-barrow/">
  <script>
    window.location.replace("/harrison-barrow/");
  </script>
</head>
<body>
  <p>If you are not redirected automatically, please click <a href="/harrison-barrow/">here</a>.</p>
</body>
</html>"""
    write_file("/about/", about_redirect_html)
    
    # 4. Criminal defense hub
    render("/criminal-defense/", "Cape Cod Criminal Defense Hub | Harrison Barrow, Attorney at Law P.C.",
           "Facing criminal charges on Cape Cod? Protect your rights with trial attorney Harrison Barrow. 15+ years experience, proven results. Free consultation.",
           criminal_defense_body(), nav_key="criminal-defense",
           page_hero=page_hero([("Home", "/"), ("Criminal Defense", None)], "Criminal Defense",
                               "Criminal Defense Overview", "Boutique criminal-defense representation with small-firm attention and a trial-tested record, serving Cape Cod and the Commonwealth of Massachusetts."))
                               
    # 5. Criminal defense subpages
    for pa in PRACTICE_AREAS:
        crumbs = [("Home", "/"), ("Criminal Defense", "/criminal-defense/"), (pa["nav"], None)]
        lead = f"Trial-tested defense for {pa['nav'].lower()} charges in the Barnstable, Orleans, and Falmouth courts and across Massachusetts."
        render(f"/criminal-defense/{pa['slug']}/", pa["seo_title"], pa["seo_desc"],
               practice_body(pa), nav_key="criminal-defense",
               page_hero=page_hero(crumbs, "Criminal Defense", pa["h1"], lead),
               extra_nodes=[service_node(pa), faq_node(pa["faqs"]),
                            breadcrumb_node([("Home", "/"), ("Criminal Defense", "/criminal-defense/"),
                                             (pa["nav"], f"/criminal-defense/{pa['slug']}/")])])
                            
    # 6. Civil litigation
    render("/civil-litigation/", "Cape Cod Civil Litigation, 93A, & Personal Injury | Harrison Barrow",
           "Cape Cod civil litigation trial lawyer. Harrison Barrow handles construction disputes, business litigation, contract breaches, 93A consumer claims, and personal injury. Call (508) 945-1400 for a consult.",
           civil_litigation_body(), nav_key="civil-litigation",
           page_hero=page_hero([("Home", "/"), ("Civil Litigation", None)], "Civil Litigation",
                               "Civil Litigation & Trial Law", "Resolving Complex Business & Property Disputes"))
                               
    # 7. Case Results
    render("/results/", "Cape Cod Criminal Case Results | Harrison Barrow, Attorney at Law",
           "View criminal case outcomes and trial victories achieved by Harrison Barrow on Cape Cod. Dismissals and Not Guilty verdicts for OUI, drug charges, assault, and felonies.",
           results_body(), nav_key="results",
           page_hero=page_hero([("Home", "/"), ("Results", None)], "Case Results",
                               "Proven Case Outcomes", "A sample of dismissals, not-guilty verdicts, and reduced charges. Every case is unique, but these show our courtroom preparedness."))
                               
    # 8. Testimonials
    render("/reviews/", "Client Testimonials & Reviews | Harrison Barrow, Attorney at Law",
           "Read reviews and testimonials from clients represented by Harrison Barrow on Cape Cod. Avvo 10.0 Superb-rated Cape Cod trial attorney with a record of dismissals and not-guilty verdicts.",
           reviews_body(), nav_key="reviews",
           page_hero=page_hero([("Home", "/"), ("Reviews", None)], "Client Reviews",
                               "What Clients Say", "Real testimonials from clients Harrison has defended in Massachusetts courts."))
                               
    # 9. Contact
    render("/contact/", "Contact Our Cape Cod Law Firm | Hyannis, MA Office",
           "Contact Harrison Barrow, Attorney at Law P.C. for a free case evaluation on Cape Cod. Call (508) 945-1400. Office in Hyannis, MA.",
           contact_body(), nav_key="contact",
           page_hero=page_hero([("Home", "/"), ("Contact", None)], "Contact",
                               "Get In Touch", "We are available 24/7 for urgent consultations. Call, text, or submit a request online."))
                               
    # 10. Thank you
    render("/thank-you/", "Thank You | Harrison Barrow, Attorney at Law",
           "Thank you for contacting Harrison Barrow, Attorney at Law. Your message has been received.",
           thankyou_body(), nav_key=None, noindex=True)
           
    # 11. Privacy Policy
    render("/privacy-policy/", "Privacy Policy | Harrison Barrow, Attorney at Law P.C.",
           "Read the privacy policy of Harrison Barrow, Attorney at Law P.C. Learn how we handle your personal data.",
           privacy_body(), nav_key=None,
           page_hero=page_hero([("Home", "/"), ("Privacy Policy", None)], "Privacy Policy",
                               "Privacy Policy", "How we handle lead information collected on this website."))
                               
    # 12. 404 Page
    render("/404.html", "Page Not Found (404) | Harrison Barrow, Attorney at Law P.C.",
           "The page you are looking for does not exist or has been moved.",
           notfound_body(), nav_key=None, noindex=True)
           
    # 13. System files (sitemap, robots, llms)
    build_infra()
    print("Build complete.")

if __name__ == "__main__":
    main()
