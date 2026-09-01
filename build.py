#!/usr/bin/env python3
"""
The Agents Force — static site builder.

Run:  python3 build.py

Everything you'd normally want to change (copy, links, agents, journal posts)
lives in the CONTENT section below. Run the script and it regenerates the HTML
files in this folder. No installs, no npm, no build tools — just Python 3.

styles.css is NOT generated — edit it directly.

Why a build step at all: the header, footer and <head> are shared by every page.
Editing them in one place here beats editing them in four HTML files by hand.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# CONTENT
# =============================================================================

SITE = {
    "domain": "theagentsforce.com",
    "url": "https://theagentsforce.com",
    "name": "The Agents Force",
    "author": "Hari Om Vashishtha",
    "entity": "Unfinished Innovations LLP",
    "year": "2026",
    "og_image": "assets/og-cover.jpg",
}

# Google Analytics 4. Set to "" to strip tracking from every page.
GA_MEASUREMENT_ID = "G-ZM2HP8YTXB"

# Bump this any time styles.css changes. GitHub Pages' CDN and browsers cache
# styles.css hard since the URL never changes on its own — without a version
# bump, a CSS push can go live in the HTML while the stylesheet itself keeps
# serving the old cached copy. Changing this string changes the URL, which
# forces a fresh fetch everywhere.
CSS_VERSION = "3"

LINKS = {
    "thesis":   "https://docs.google.com/document/d/157b6_cHT56PZEqKb5SWV6kdMRtgs3RzCIivMjhwPP6c/edit?usp=sharing",
    "thesis_agent": "https://orgfarm-3a666335d9-dev-ed.develop.my.site.com/NothingElseMatterzDotCom/",
    "mdcp":     "https://github.com/hov8aa/Million-Dollar-Consistency-Partner-MDCP",
    "youtube":  "https://youtube.com/playlist?list=PLhMmOSOqNYXgdHJ0fJVtwaiwgZ601X5uQ&si=Ixzyp-0OKh1JJ1HI",
    "linkedin": "https://www.linkedin.com/in/hov8a/",
    "x":        "https://x.com/hov8a",
    "book":     "https://calendar.app.google/SUfhrngH4TPw91fn6",
    "journal":  "journal.html",
    "project":  "https://3mistakesofmylife.in/",
}

# Salesforce Web-to-Lead. The OID identifies the destination org: if this ever
# points at the wrong org, submissions still return HTTP 200 and the Lead simply
# lands somewhere nobody is watching. Verify after any org change.
#
# reCAPTCHA must be v2 "I'm not a robot" Checkbox. Web-to-Lead does not support
# v3 or Enterprise: v3 returns a score and expects the site owner's server to
# pick a threshold, and there is no server here to put that decision in.
# A v3 key renders as "ERROR for site owner: Invalid key type".
#
# captcha_key must match the API Key Pair nickname in Salesforce exactly,
# including case.
SALESFORCE = {
    "oid": "00DgL000005LHCf",
    "endpoint": "https://webto.salesforce.com/servlet/servlet.WebToLead?encoding=UTF-8",
    "captcha_key": "TheAgentsForce",
    "recaptcha_sitekey": "6LcNHqMtAAAAAMF2PffjhUXDMeGqLrB8YKtGyqMt",
    "return_url": "https://theagentsforce.com/thanks.html",
    "lead_source": "Web",
    # Enterprise hubs first, per ICP. Anyone outside picks "Somewhere else".
    "countries": [
        ("US", "United States"), ("GB", "United Kingdom"), ("CA", "Canada"),
        ("AU", "Australia"), ("IN", "India"), ("AE", "United Arab Emirates"),
        ("SG", "Singapore"), ("DE", "Germany"), ("NL", "Netherlands"),
        ("IE", "Ireland"), ("OTHER", "Somewhere else"),
    ],
}

HIRE = {
    "h2": 'Tell me what&rsquo;s <span class="g">breaking</span>.',
    "lede": "Not a newsletter signup. This goes straight into a Salesforce Lead record "
            "and I read every one myself.",
    "steps": [
        "You describe the system that isn&rsquo;t behaving. Be specific &mdash; vague inputs "
        "get vague replies.",
        "I reply within two working days with what I&rsquo;d want to look at first, whether "
        "or not there is an engagement in it.",
        "If it is a fit, we scope the 5-day Exploratory Sprint. If it is not, I will say so plainly.",
    ],
    "proof": "This form is a live Salesforce <strong>Web-to-Lead</strong> endpoint running on my "
             "own org &mdash; captcha, field mapping and lead routing included. The site is the "
             "first system I am asking you to judge.",
}

HERO = {
    "eyebrow": "Agent Force Optimization R&amp;D",
    # The headline carries the memory. Keep it short enough to survive a phone.
    "h1": 'One agent. One hypothesis. <span class="g">One goal.</span>',
    "sub": "I build Agentforce agents on Salesforce and ship them into real workflows &mdash; "
           "then publish the architecture, the failures, and the numbers.",
}

AGENTS = [
    {
        "title": "Ph.D.-Style Thesis: Agent God Complexes",
        "description": "Reimagining the Hiring Industry in the Age of AI.",
        "icon": "graduation-cap",
        "href": LINKS["thesis"],
        "cta": "Read the thesis",
        "agent_href": LINKS["thesis_agent"],
        "agent_cta": "Try the agent",
    },
    {
        "title": "3MoMLife &mdash; Discipline Agent",
        "description": "Salesforce Agentforce agent built on the 3MistakesOfMyLife.in discipline programme.",
        "icon": "database",
        "href": "journal-agent-001.html",
        "cta": "Read the architecture",
        "agent_href": LINKS["project"],
        "agent_cta": "Try the agent",
    },
    {
        "title": "Hermes &mdash; Million Dollar Consistency Partner",
        "description": "A five-agent pipeline that turns daily working sessions into compounding output.",
        "icon": "workflow",
        "href": LINKS["mdcp"],
        "cta": "View framework on GitHub",
        "badge": "Private agent &mdash; not yet public",
    },
]

PROCESS = {
    "lede": "Four weeks from first call to a result you can defend in a board meeting. "
            "No retainer, no discovery theatre.",
    "steps": [
        {
            "n": "01",
            "kicker": "Exploratory Sprint &middot; 5 days",
            "title": "Map the system before touching it.",
            "body": "I trace your funnel end to end and find where work leaks. You leave with a "
                    "written hypothesis, the assumptions it rests on, and the boundaries we agree "
                    "not to cross.",
        },
        {
            "n": "02",
            "kicker": "Measured Experiment &middot; 3 weeks",
            # Retitled: the original read "One agent. One hypothesis. One number."
            # which is now the hero headline.
            "title": "The number gets agreed before the first line of code.",
            "body": "We build against a single measurable outcome &mdash; pipeline influenced &mdash; "
                    "and the guardrails are documented up front, not patched in after something breaks.",
        },
        {
            "n": "03",
            "kicker": "The verdict",
            "title": "It moved the number, or it did not.",
            "body": "Both are results. Most agent pilots never reach this point because nobody agreed "
                    "what success looked like on day one.",
        },
    ],
    "price": "$2,500",
    "price_note": "for the 5-day Exploratory Sprint &mdash; credited in full against the experiment.",
}

ABOUT = {
    "lede": "I build agents on Salesforce and ship them into real workflows &mdash; then publish the "
            "architecture, the failures, and the numbers. Everything here has been run on my own "
            "operations before it is offered to yours.",
    "facts": [
        ("Salesforce", "Agentforce agents built and deployed on live orgs."),
        ("Method", "Hypothesis, assumptions, boundaries &mdash; written before code."),
        ("Measure", "Pipeline influenced. One number, agreed on day one."),
    ],
}

POSTS = [
    {
        "href": "journal-agent-001.html",
        "edition": "Open Source Humans &mdash; Edition 11",
        "date": "8 March 2026",
        "date_iso": "2026-03-08",
        "read": "7 min read",
        "title": "The Science, Art, &amp; Architecture of My Salesforce Agent #001",
        "excerpt": "Most conversations about agents focus on tools, prompts, and demos &mdash; not "
                   "architecture. A teardown of Agent #001: the topic router, the RAG-backed FAQ "
                   "layer, the boundaries it protects, and why messy data kills agents long before "
                   "prompts do.",
    },
]

ICONS = {
    "graduation-cap":
        '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/>'
        '<path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "database":
        '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/>'
        '<path d="M3 12A9 3 0 0 0 21 12"/>',
    "workflow":
        '<rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/>'
        '<rect width="8" height="8" x="13" y="13" rx="2"/>',
}

NAV = [
    ("Agents", "index.html#agents", False),
    ("How it works", "index.html#how", False),
    ("About me", "index.html#about", False),
    ("Journal", "journal.html", False),
    ("Thesis", LINKS["mdcp"], True),
    ("Hire me", "index.html#hire", False),
]

# =============================================================================
# HELPERS
# =============================================================================


def icon(name):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true" focusable="false">'
        + ICONS[name] + "</svg>"
    )


def is_external(href):
    return href.startswith("http://") or href.startswith("https://")


def esc(href):
    """Escape bare ampersands in URLs so the markup is valid HTML."""
    return href.replace("&amp;", "&").replace("&", "&amp;")


def link_attrs(href):
    """External links open in a new tab; internal ones never do.

    The old Button component defaulted every href to target="_blank", which sent
    people off-site when they clicked an internal link like 'Read the journal'.
    """
    if is_external(href):
        return ' target="_blank" rel="noopener noreferrer"'
    return ""


def btn(href, label, variant="primary", size=None):
    cls = "btn btn-" + variant + (" btn-" + size if size else "")
    return f'<a class="{cls}" href="{esc(href)}"{link_attrs(href)}>{label}</a>'


def analytics():
    """Google tag (gtag.js).

    Placed last in <head> on purpose: it is async, so the browser finds it via
    the preload scanner anyway, and putting it after the stylesheet and font
    preload keeps analytics from competing with them for the first round trip.
    """
    if not GA_MEASUREMENT_ID:
        return ""
    return f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_MEASUREMENT_ID}');
</script>
"""


def head(title, description, page_url, *, og_type="website", extra=""):
    og_image = f'{SITE["url"]}/{SITE["og_image"]}'
    canonical = f'{SITE["url"]}/{page_url}' if page_url != "index.html" else SITE["url"] + "/"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="author" content="{SITE['author']}">
<meta name="theme-color" content="#04101f">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The Agents Force — one agent, one hypothesis, one goal.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<meta name="twitter:creator" content="@hov8a">

<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="fonts/poppins-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css?v={CSS_VERSION}">
{extra}{analytics()}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(active=None):
    items = []
    for label, href, external in NAV:
        cur = ' class="is-active" aria-current="page"' if label == active else ""
        items.append(f'<a href="{esc(href)}"{link_attrs(href)}{cur}>{label}</a>')
    nav = "".join(items)
    return f"""<header class="site-header">
  <a class="brand" href="index.html">
    <span class="brand-name">The <span class="g">Agents</span> Force</span>
    <span class="brand-tag">Connecting the dots</span>
  </a>
  <nav class="site-nav" aria-label="Primary">{nav}</nav>
  {btn('index.html#hire', 'Hire Me', 'primary', 'sm')}
</header>
"""


def footer():
    socials = "".join(
        f'<a href="{esc(href)}" target="_blank" rel="noopener noreferrer">{label}</a>'
        for label, href in [("YouTube", LINKS["youtube"]), ("LinkedIn", LINKS["linkedin"]), ("X", LINKS["x"])]
    )
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="divider-gold"></div>
    <div class="site-footer-row">
      <div class="site-footer-copy">{SITE['domain']} &mdash; a project of {SITE['entity']}. &copy;{SITE['year']}.</div>
      <div class="site-footer-links">{socials}</div>
    </div>
  </div>
</footer>
</body>
</html>
"""


def portrait(sizes, priority=False):
    load = 'loading="eager" fetchpriority="high"' if priority else 'loading="lazy"'
    return (
        '<div class="portrait-ring">'
        f'<img src="assets/portrait-hari.jpg" alt="{SITE["author"]}" '
        f'width="880" height="880" sizes="{sizes}" decoding="async" {load}>'
        "</div>"
    )


def jsonld(obj_lines):
    return '<script type="application/ld+json">\n' + obj_lines + "\n</script>\n"


# =============================================================================
# PAGES
# =============================================================================


def hire_form():
    """Salesforce Web-to-Lead form.

    Deliberately shorter than the snippet Salesforce generates. The generated
    version ships a City field plus Country (~250 options) and State/Province
    (~400 options, mixing Italian provinces, Japanese prefectures and Indian
    states) — roughly 35 KB of markup that nothing downstream routes on.

    `description` is a standard Lead field but is NOT in the generated snippet.
    Web-to-Lead silently discards fields it does not recognise: the Lead still
    saves, the field is just blank. Confirm it maps before trusting it.
    """
    sf = SALESFORCE
    options = "".join(
        f'<option value="{code}">{name}</option>' for code, name in sf["countries"]
    )
    captcha_settings = (
        '{"keyname":"%s","fallback":"true","orgId":"%s","ts":""}'
        % (sf["captcha_key"], sf["oid"])
    )
    return f"""<form class="hire-form" action="{sf['endpoint']}&amp;orgId={sf['oid']}" method="POST">

        <input type="hidden" name="captcha_settings" value='{captcha_settings}'>
        <input type="hidden" name="oid" value="{sf['oid']}">
        <input type="hidden" name="retURL" value="{sf['return_url']}">
        <input type="hidden" id="lead_source" name="lead_source" value="{sf['lead_source']}">

        <div class="field-row">
          <div class="field">
            <label for="first_name">First name</label>
            <input id="first_name" maxlength="40" name="first_name" type="text" autocomplete="given-name" placeholder="Hari">
          </div>
          <div class="field">
            <label for="last_name">Last name</label>
            <input id="last_name" maxlength="80" name="last_name" type="text" autocomplete="family-name" placeholder="Vashishtha" required>
          </div>
        </div>

        <div class="field">
          <label for="email">Work email</label>
          <input id="email" maxlength="80" name="email" type="email" autocomplete="email" placeholder="you@company.com" required>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="company">Company</label>
            <input id="company" maxlength="40" name="company" type="text" autocomplete="organization" placeholder="Acme Consulting" required>
          </div>
          <div class="field">
            <label for="country_code">Country <span class="opt">(optional)</span></label>
            <select id="country_code" name="country_code"><option value="">Select&hellip;</option>{options}</select>
          </div>
        </div>

        <div class="field">
          <label for="description">What is the system doing that it shouldn&rsquo;t?</label>
          <textarea id="description" name="description" maxlength="2000" placeholder="The part of your Salesforce estate you would least like to explain to a new architect."></textarea>
        </div>

        <div class="form-captcha">
          <div class="g-recaptcha" data-sitekey="{sf['recaptcha_sitekey']}"></div>
        </div>

        <div class="form-actions">
          <button class="btn btn-primary btn-lg" type="submit" name="submit">Send it over</button>
          <p class="form-legal">Goes to my Salesforce org. No list, no sequence, no automated follow-up.</p>
        </div>

      </form>"""


def hire_section():
    steps = "".join(
        f'<li><span class="n">{i}</span><span>{text}</span></li>'
        for i, text in enumerate(HIRE["steps"], start=1)
    )
    return f"""
<section id="hire" class="section section-canvas">
  <div class="wrap hire-grid">
    <div>
      <p class="eyebrow">Hire me</p>
      <h2 class="hire-title">{HIRE['h2']}</h2>
      <p class="hire-lede">{HIRE['lede']}</p>
      <ol class="hire-steps">{steps}</ol>
      <p class="hire-proof">{HIRE['proof']}</p>
    </div>
    <div class="card card-gold card-pad-8">
      {hire_form()}
    </div>
  </div>
</section>
"""


def page_thanks():
    """Web-to-Lead retURL target.

    noindex because it is reachable only after a POST and has no standalone
    value in search. Fires a GA generate_lead event — without this page the
    conversion is invisible, since the form POSTs off-domain to Salesforce.
    """
    noindex = '<meta name="robots" content="noindex, follow">\n'
    return (
        head(
            "Thanks — The Agents Force",
            "Your message reached my Salesforce org.",
            "thanks.html",
            extra=noindex,
        )
        + header()
        + """<main id="main" class="notfound">
  <div>
    <p class="eyebrow">Received</p>
    <h1>It landed.</h1>
    <p style="color: var(--text-muted); max-width: 52ch; margin-bottom: var(--space-8)">
      Your message is now a Lead record in my Salesforce org. I read them myself and
      reply within two working days &mdash; including when the answer is that I am not
      the right person for it.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="journal.html">Read the journal</a>
      <a class="btn btn-secondary" href="index.html">Back to the homepage</a>
    </div>
  </div>
</main>
<script>
  if (typeof gtag === 'function') { gtag('event', 'generate_lead', { method: 'web_to_lead' }); }
</script>
"""
        + footer()
    )


RECAPTCHA_SCRIPT = """<script src="https://www.google.com/recaptcha/api.js" async defer></script>
<script>
  // Salesforce's captcha_settings payload needs a fresh timestamp at submit time.
  function timestamp() {
    var response = document.getElementById("g-recaptcha-response");
    if (response == null || response.value.trim() == "") {
      var elems = JSON.parse(document.getElementsByName("captcha_settings")[0].value);
      elems["ts"] = JSON.stringify(new Date().getTime());
      document.getElementsByName("captcha_settings")[0].value = JSON.stringify(elems);
    }
  }
  setInterval(timestamp, 500);
</script>
"""


def page_index():
    person_ld = jsonld("""{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "The Agents Force",
  "url": "https://theagentsforce.com/",
  "description": "Salesforce Agentforce agents built against one measurable outcome.",
  "founder": { "@type": "Person", "name": "Hari Om Vashishtha", "sameAs": [
    "https://www.linkedin.com/in/hov8a/", "https://x.com/hov8a" ] },
  "parentOrganization": { "@type": "Organization", "name": "Unfinished Innovations LLP" },
  "areaServed": "Worldwide",
  "knowsAbout": ["Salesforce Agentforce", "AI agent architecture", "CRM data architecture"]
}""")

    cards = []
    for i, a in enumerate(AGENTS, start=1):
        badge = f'<p class="agent-badge">{a["badge"]}</p>' if a.get("badge") else ""
        inner = (
            f'<div class="agent-step" aria-hidden="true">{i}</div>'
            f'<div class="agent-icon">{icon(a["icon"])}</div>'
            f'<h3 class="agent-title">{a["title"]}</h3>'
            f'{badge}'
            f'<p class="agent-desc">{a["description"]}</p>'
        )
        actions = []
        if a.get("href"):
            cta = a.get("cta", "Read more")
            actions.append(
                f'<a class="agent-action" href="{esc(a["href"])}"{link_attrs(a["href"])}>{cta} &rarr;</a>'
            )
        if a.get("agent_href"):
            agent_cta = a.get("agent_cta", "Try the agent")
            actions.append(
                f'<a class="agent-action" href="{esc(a["agent_href"])}"{link_attrs(a["agent_href"])}>{agent_cta} &rarr;</a>'
            )
        actions_html = f'<div class="agent-actions">{"".join(actions)}</div>' if actions else ""
        cards.append(f'<div class="agent-card">{inner}{actions_html}</div>')

    steps = "".join(
        f'<div class="card card-plain card-pad-8 process-card">'
        f'<div class="process-n" aria-hidden="true">{s["n"]}</div>'
        f'<div class="process-kicker">{s["kicker"]}</div>'
        f'<h3 class="process-title">{s["title"]}</h3>'
        f'<p class="process-body">{s["body"]}</p></div>'
        for s in PROCESS["steps"]
    )

    facts = "".join(
        f'<div class="about-fact"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in ABOUT["facts"]
    )

    return (
        head(
            "The Agents Force — Salesforce Agentforce agents, built against one measurable outcome",
            "I build Agentforce agents on Salesforce and ship them into real workflows, then publish "
            "the architecture, the failures, and the numbers. Five-day Exploratory Sprint, then one "
            "measured experiment.",
            "index.html",
            extra=person_ld + RECAPTCHA_SCRIPT,
        )
        + header("Agents")
        + f"""<main id="main">

<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">{HERO['eyebrow']}</p>
      <h1>{HERO['h1']}</h1>
      <p class="hero-sub">{HERO['sub']}</p>
      <div class="hero-actions">
        {btn('index.html#hire', 'Hire Me', 'primary')}
        {btn('#agents', 'See the agents', 'secondary')}
      </div>
    </div>
    <div class="hero-portrait">{portrait('(max-width: 760px) 220px, 440px', priority=True)}</div>
  </div>
</section>

<section id="agents" class="section section-page">
  <div class="wrap">
    <div class="section-heading center" style="margin-bottom: var(--space-16)">
      <p class="eyebrow">Live now</p>
      <h2><span class="g">Portfolio</span><br>of Agents</h2>
    </div>
    <div class="agent-grid">{''.join(cards)}</div>
  </div>
</section>

<section id="how" class="section section-canvas">
  <div class="wrap">
    <div class="process-head">
      <div style="max-width:620px">
        <p class="eyebrow">How it works</p>
        <h2>Exploratory Sprint<br><span class="g">&rarr; Measured Experiment</span></h2>
      </div>
      <p class="process-lede">{PROCESS['lede']}</p>
    </div>
    <div class="process-grid">{steps}</div>
    <div style="margin-top: var(--space-10)">
      <div class="card card-gold card-pad-8">
        <div class="offer-row">
          <div class="offer-copy">
            <span class="offer-price">{PROCESS['price']}</span>
            <span>{PROCESS['price_note']}</span>
          </div>
          {btn(LINKS['book'], 'Book the sprint', 'primary', 'lg')}
        </div>
      </div>
    </div>
  </div>
</section>

<section id="about" class="section section-page">
  <div class="wrap about-grid">
    <div class="about-portrait">{portrait('(max-width: 760px) 260px, 320px')}</div>
    <div>
      <p class="eyebrow">About</p>
      <h2>Hari Om <span class="g">Vashishtha</span></h2>
      <p class="about-lede">{ABOUT['lede']}</p>
      <dl class="about-facts">{facts}</dl>
      <div class="about-actions">
        {btn(LINKS['journal'], 'Read the journal', 'secondary')}
        {btn(LINKS['linkedin'], 'LinkedIn', 'ghost')}
      </div>
    </div>
  </div>
</section>
{hire_section()}
</main>
"""
        + footer()
    )


def page_journal():
    items = []
    for p in POSTS:
        items.append(f"""<a class="journal-card card card-plain card-pad-8 card-interactive" href="{p['href']}">
  <div class="journal-card-grid">
    <div>
      <div class="journal-meta">
        <span>{p['edition']}</span>
        <time class="dim" datetime="{p['date_iso']}">{p['date']}</time>
        <span class="dim">{p['read']}</span>
      </div>
      <h2 class="journal-title">{p['title']}</h2>
      <p class="journal-excerpt">{p['excerpt']}</p>
    </div>
    <div class="journal-arrow" aria-hidden="true">&rarr;</div>
  </div>
</a>""")

    return (
        head(
            "Journal — The Agents Force",
            "Architecture teardowns, failures, and the numbers behind each agent — written while the "
            "work is still in progress.",
            "journal.html",
        )
        + header("Journal")
        + f"""<main id="main" class="section section-page">
  <div class="wrap">
    <div class="journal-intro">
      <p class="eyebrow">Journal</p>
      <h1>Field notes from<br><span class="g">building in the open.</span></h1>
      <p>Architecture teardowns, failures, and the numbers behind each agent &mdash; written while the
      work is still in progress.</p>
    </div>
    <div class="journal-list">{''.join(items)}</div>
  </div>
</main>
"""
        + footer()
    )


ARTICLE_BODY = """
<p>Everyone is building AI agents right now. New tools appear every week &mdash; copilots, autonomous
assistants, multi-agent systems. The vocabulary is expanding faster than most of us can properly
evaluate it.</p>

<p>This is a breakdown of the science, art, and architecture of Agent #001: the conversational
interface behind my project, <a href="https://3mistakesofmylife.in/" target="_blank" rel="noopener noreferrer">3MistakesOfMyLife.in</a>.</p>

<h2>Start with the word &ldquo;science&rdquo;</h2>
<p>Science is the disciplined process of observing reality, identifying patterns, forming hypotheses,
testing them against the world, and refining understanding based on evidence. In simple terms: a
structured method for interacting with reality.</p>
<p>We are entering an era where artificial intelligence participates in that interaction. Agents are
not just software &mdash; they are systems designed to engage humans through the most fundamental
human mechanism there is: conversation. And conversation is not casual. It is highly structured.</p>

<blockquote>A conversation is a very scientific event involving many forces of nature to yield maximum
benefits for all involved parties, depending upon the match in frequencies, intents, and uncovered
assumptions.</blockquote>

<p>Every conversation carries invisible forces: intentions, attention, language, emotional states,
assumptions, mental models. When they align, conversations create clarity. When they do not, they
produce confusion and wasted effort.</p>
<p>Most of us are not disciplined, and most of us do not practise much self-awareness. Without those
two things, conversations become reactive instead of constructive: assumptions stay hidden,
intentions stay unclear, decisions become inconsistent. In a world increasingly shaped by intelligent
systems, that gap matters more, not less.</p>

<h2>A note from the beginning</h2>
<p>About a year ago a mentor told me that a great many Agentforce agents were being deployed, and a
great many of them were failing &mdash; not because the technology was weak, but because the
architecture behind them was. The industry, he said, is going to need critical thinkers who can
design these systems properly.</p>
<p>So I started learning the ABCs of Agentforce. I am a slow learner, but persistent. Today I have my
first agent running. Is it impressive? Not really &mdash; it is barely up to the mark compared to the
best out there. That is fine. I am not a specialist yet. I am working on it, four hours a day.</p>

<h2>The project behind the agent</h2>
<p>3 Mistakes of My Life is a discipline programme for kids, built in collaboration with parents. The
premise is simple: if the next generation grows up in a world shaped by AI, they will need stronger
foundations in discipline, reflection, self-awareness, and structured thinking. Those are not
developed through lectures &mdash; they come from guided conversations and deliberate practice.</p>
<p>Parents participate alongside their kids. Mentors guide the parents. Discipline becomes a
measurable practice rather than a vague concept. Agent #001 is the first conversational interface
into that system.</p>

<h2>Current architecture</h2>
<p>Agent #001 is extremely basic. It performs one primary function: it explains the project. There is
no persuasion layer, no onboarding automation, no behavioural coaching, no lifecycle engagement. It
introduces the project and answers questions from a structured knowledge library, through a small set
of conversational topics.</p>

<div class="blueprint">
  <p class="bp-title">Inside Agent #001: <span class="g">a blueprint for AI agent architecture</span></p>
  <p class="bp-lede">Where a message goes, and what it touches on the way.</p>

  <div class="bp-section">
    <p class="bp-label">The conversational routing engine</p>
    <div class="bp-flow">
      <div class="bp-step">
        <div class="bp-marker"><span class="bp-num">1</span><span class="bp-line"></span></div>
        <div class="bp-body"><p class="bp-name">User message</p>
        <p class="bp-desc">Every interaction enters through the website.</p></div>
      </div>
      <div class="bp-step">
        <div class="bp-marker"><span class="bp-num">2</span><span class="bp-line"></span></div>
        <div class="bp-body"><p class="bp-name">Clarity filters</p>
        <p class="bp-desc">Handles ambiguous questions, and redirects off-topic inquiries.</p></div>
      </div>
      <div class="bp-step">
        <div class="bp-marker"><span class="bp-num">3</span><span class="bp-line"></span></div>
        <div class="bp-body"><p class="bp-name">The Topic Selector router</p>
        <p class="bp-desc">Identifies intent and routes the query from every user message.</p></div>
      </div>
      <div class="bp-step">
        <div class="bp-marker"><span class="bp-num">4</span><span class="bp-line"></span></div>
        <div class="bp-body"><p class="bp-name">RAG-grounded Project FAQs</p>
        <p class="bp-desc">Answers pulled from structured knowledge, not generated from scratch.</p></div>
      </div>
    </div>
  </div>

  <div class="bp-section">
    <p class="bp-label">Three layers, kept separate</p>
    <div class="bp-layers">
      <div class="bp-layer"><p class="bp-name">The experience layer</p>
      <p class="bp-desc">Frontend interface for user interactions via the website.</p></div>
      <div class="bp-layer"><p class="bp-name">The conversation layer</p>
      <p class="bp-desc">The &ldquo;brain&rdquo; (Agent #001) interpreting intent and managing information flow.</p></div>
      <div class="bp-layer"><p class="bp-name">The data layer</p>
      <p class="bp-desc">Foundational Salesforce environment for structured records and interaction histories.</p></div>
    </div>
  </div>

  <div class="bp-section">
    <p class="bp-label">Where it is, and where it goes next</p>
    <table class="bp-table">
      <thead><tr><th scope="col">Functional phase</th><th scope="col">Architecture components</th><th scope="col">Agent capability</th></tr></thead>
      <tbody>
        <tr>
          <th scope="row">Current &mdash; awareness</th>
          <td data-label="Architecture components">Knowledge library &amp; Topic Selector</td>
          <td data-label="Agent capability">Explaining project philosophy and answering FAQs</td>
        </tr>
        <tr>
          <th scope="row">Next &mdash; operational</th>
          <td data-label="Architecture components">Logging &amp; mentor registration</td>
          <td data-label="Agent capability">Tracking interaction data and capturing structured mentor leads</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<h3>Topic Selector</h3>
<p>Every user message passes through the Topic Selector first. Its job is to understand intent and
route the conversation to the correct topic &mdash; the conversation router.</p>

<h3>Project FAQs</h3>
<p>Questions about the programme activate Project FAQs, which retrieves from the knowledge library
using retrieval-augmented generation. Instead of generating blindly, the agent references
documentation drawn from the live site. Responses stay grounded in the actual project.</p>

<h3>Off Topic</h3>
<p>Anything outside scope gets a gentle redirect &mdash; &ldquo;I&rsquo;m here to help with the
discipline program. Would you like to know how it works?&rdquo; This protects the boundaries of the
system.</p>

<h2>The architectural principle</h2>
<blockquote>Agents should sit between experience and data &mdash; not replace either.</blockquote>
<p>Experience happens on the website. The agent acts as a conversation layer. Structured records
eventually live in a Salesforce data layer. Keeping those layers separate lets the system evolve
without breaking the conversation interface.</p>

<h2>What is missing</h2>
<p>Right now the agent supports exactly one stage: awareness. Everything else is still to be built.</p>
<ul>
  <li>Parent onboarding</li><li>Mentor registration</li><li>Mentor-family matching</li>
  <li>Discipline session logging</li><li>Behavioural progress tracking</li><li>Referral loops</li>
  <li>Payment systems</li>
</ul>
<p>The business architecture exists conceptually. The operational layers are under construction.</p>

<h2>Data before intelligence</h2>
<p>One thing is already clear: agents do not fail because of prompts. They fail because the underlying
data architecture is messy. Most CRM environments struggle with inconsistent objects, incomplete
fields, and fragmented interaction histories. Introduce an agent into that and it simply amplifies the
chaos.</p>
<p>Before expanding an agent&rsquo;s intelligence, the system has to define clean data structures,
traceable interaction records, and clear ownership of information. Only then does the agent become
useful.</p>

<h2>The next iteration</h2>
<p><strong>Conversation logging.</strong> Conversations are currently stored nowhere. Logging them
tells us what users ask, where conversations break, and whether the agent is improving.</p>
<p><strong>Mentor registration.</strong> Collecting name, email, location, and background inside the
conversation itself &mdash; the first structured dataset for the mentor ecosystem.</p>

<h2>A note to system integrators</h2>
<p>The questions in this project show up inside almost every Salesforce implementation today. How do
we structure data so agents can reason correctly? How do we design conversational systems that
actually support business workflows? How do we move from experimentation to measurable outcomes?</p>
<p>If you are a Salesforce system integrator exploring Agentforce, I would genuinely like to hear how
you are approaching these problems. I am building this in public, and I will keep documenting the
architecture as it evolves.</p>
"""


def page_article():
    p = POSTS[0]
    article_ld = jsonld("""{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "The Science, Art, & Architecture of My Salesforce Agent #001",
  "datePublished": "2026-03-08",
  "author": { "@type": "Person", "name": "Hari Om Vashishtha", "url": "https://theagentsforce.com/" },
  "publisher": { "@type": "Organization", "name": "The Agents Force" },
  "mainEntityOfPage": "https://theagentsforce.com/journal-agent-001.html",
  "image": "https://theagentsforce.com/assets/og-cover.jpg"
}""")

    return (
        head(
            "The Science, Art & Architecture of My Salesforce Agent #001",
            "A teardown of Agent #001: the topic selector, the RAG-grounded FAQ layer, the boundaries "
            "it protects, and why messy data kills agents long before prompts do.",
            "journal-agent-001.html",
            og_type="article",
            extra=article_ld,
        )
        + header("Journal")
        + f"""<main id="main" class="article">
  <div class="article-wrap">
    <a class="article-back" href="journal.html">&larr; Journal</a>
    <div class="article-meta">
      <span>{p['edition']}</span>
      <time class="dim" datetime="{p['date_iso']}">{p['date']}</time>
      <span class="dim">{p['read']}</span>
    </div>
    <h1>The Science, Art, &amp; Architecture of My Salesforce <span class="g">Agent #001</span></h1>
    <div style="margin: var(--space-8) 0"><div class="divider-gold"></div></div>
    {ARTICLE_BODY}
    <div style="margin: var(--space-12) 0 var(--space-8)"><div class="divider-gold"></div></div>
    <p>Agent #001 is just getting started.</p>
    <div class="article-links">
      <a href="{LINKS['book']}" target="_blank" rel="noopener noreferrer">Book a conversation</a>
      <a href="https://nothingelsematterz.com/2026/03/the-science-art-architecture-of-my-salesforce-agent-001-behind-3mistakesofmylife-in/" target="_blank" rel="noopener noreferrer">Original post</a>
    </div>
  </div>
</main>
"""
        + footer()
    )


def page_404():
    return (
        head("Page not found — The Agents Force", "That page does not exist.", "404.html")
        + header()
        + """<main id="main" class="notfound">
  <div>
    <h1>That page doesn&rsquo;t exist.</h1>
    <p style="color: var(--text-muted); margin-bottom: var(--space-8)">
      The link may be out of date, or the page may have moved.</p>
    <a class="btn btn-primary" href="index.html">Back to the homepage</a>
  </div>
</main>
"""
        + footer()
    )


# =============================================================================
# BUILD
# =============================================================================


def main():
    pages = {
        "index.html": page_index(),
        "journal.html": page_journal(),
        "journal-agent-001.html": page_article(),
        "thanks.html": page_thanks(),
        "404.html": page_404(),
    }
    for name, content in pages.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  {name:28s} {len(content.encode()) / 1024:6.1f} KB")

    css_path = os.path.join(HERE, "styles.css")
    print(f"  {'styles.css':28s} {os.path.getsize(css_path) / 1024:6.1f} KB (hand-maintained, not generated)")

    # sitemap + robots
    urls = ["", "journal.html", "journal-agent-001.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{SITE['url']}/{u}</loc></url>")
    sm.append("</urlset>")
    open(os.path.join(HERE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    open(os.path.join(HERE, "robots.txt"), "w").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    print("  sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
