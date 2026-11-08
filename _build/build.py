"""Builds the static site from content.py.

Run from the repo root:  python3 _build/build.py
Folders starting with "_" are not published by GitHub Pages, so this script stays private to the repo.
"""
import json
import os
import random
from html import escape as e

from content import SITE, HOME, ABOUT, CONTACT, PROJECTS, DESIGN_LOG, RETRO_PLACEHOLDER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700"
         "&family=IBM+Plex+Sans:wght@400;500&family=Martian+Mono:wdth,wght@75..112.5,300..500"
         "&family=Tiny5&display=swap")
NAV = [("ABOUT", "about/"), ("PROJECTS", "projects/"), ("CONTACT", "contact/")]


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def num(i):
    return f"{i + 1:02d}"


def email_link(p, cls=""):
    u, d = SITE["email_user"], SITE["email_domain"]
    return (f'<a class="js-email {cls}" data-u="{e(u)}" data-d="{e(d)}" href="{p}contact/">'
            f'{e(u)} [at] {e(d.replace(".", " [dot] "))}</a>')


def placeholder(label, caption=None, ratio="16/9", cls="", decorative=False):
    """Image slot. decorative=True for thumbnails inside a link or button whose text already names
    the project, so screen readers don't read the image label as part of the link name."""
    cap = f'<figcaption>{e(caption)}</figcaption>' if caption else ""
    if decorative:
        fig_attr, ph_attr = ' aria-hidden="true"', ""
    else:
        fig_attr, ph_attr = "", f' role="img" aria-label="Image coming soon: {e(label)}"'
    return (f'<figure class="frame {cls}"{fig_attr}><div class="ph" style="aspect-ratio:{ratio}"{ph_attr}>'
            f'<span>[ img: {e(label)} ]</span></div>{cap}</figure>')


def ext_link(label, href, cls="link"):
    return (f'<a class="{cls}" href="{href}" target="_blank" rel="noopener">{e(label)}'
            '<span class="sr-only"> (opens in new tab)</span></a>')


def page(rel_out, title, desc, body, active=None, p=None):
    depth = rel_out.count("/")
    p = p if p is not None else "../" * depth
    home = p or "./"
    canonical = SITE["base_url"] + rel_out.replace("index.html", "")
    nav = "".join(
        f'<a href="{p}{href}"{" class=\"active\" aria-current=\"page\"" if label == active else ""}>{label}</a>'
        for label, href in NAV)
    full_title = f"{title} | {SITE['name']}" if title else f"{SITE['name']} | Game Designer"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{p}assets/style.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="{home}" aria-label="Natapatr Lorsathian, home">
    <img class="brand-mark" src="{p}assets/logo.svg" alt="" width="80" height="45">
    <span class="brand-text"><span class="brand-name">NATAPATR LORSATHIAN</span><span class="brand-role">game designer</span></span>
  </a>
  <nav class="site-nav" aria-label="Main">{nav}</nav>
  <div class="read" aria-hidden="true"><span class="read-label">SCROLL</span><span class="read-cells"></span><span class="read-pct">0%</span></div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="footer-links">
    {ext_link('itch.io', SITE['itch'])}
    {ext_link('LinkedIn', SITE['linkedin'])}
    {email_link(p, 'link')}
  </div>
  <p class="footer-note">&copy; {SITE['name']}</p>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>
"""
    write(rel_out, html)


TAG_STYLE = {
    # tag: (css class, 5x5 pixel icon rows)
    "Gameplay Design": ("t-gameplay", [".X...", "XXX..", ".X.X.", "...X.", "....."]),   # d-pad + button
    "Level Design": ("t-level", ["....X", "...XX", "..XXX", ".XXXX", "XXXXX"]),          # stairs
    "UX/UI Design": ("t-ux", ["X....", "XX...", "XXX..", "XX...", "..X.."]),             # cursor
}


def tag_chips(tags, full=False, label=None, link=None):
    """Discipline chips. With a label they become a labelled list (home profile window); with
    link (the path to the site root) each chip opens the Projects page filtered to it (#level).
    Inside project links they stay plain spans."""
    item = "li" if label else "span"
    out = ""
    for t in tags:
        cls, icon = TAG_STYLE.get(t, ("", []))
        px = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y, r in enumerate(icon) for x, ch in enumerate(r) if ch == "X")
        svg = f'<svg viewBox="0 0 5 5" aria-hidden="true" shape-rendering="crispEdges">{px}</svg>' if px else ""
        text = e(t if full else t.replace(" Design", ""))
        if link is not None:
            out += (f'<{item}><a class="chip chip-link {cls}" href="{link}projects/#{cls[2:]}" '
                    f'aria-label="{text} projects">{svg}{text}</a></{item}>')
        else:
            out += f'<{item} class="chip {cls}">{svg}{text}</{item}>'
    if label:
        return f'<ul class="chips" aria-label="{e(label)}">{out}</ul>'
    return f'<span class="chips">{out}</span>'


def stat(pr, key):
    return dict(pr["stats"]).get(key, "")


def spec_strip(pr):
    """Year / team / engine as a compact HUD readout instead of a sentence."""
    team = stat(pr, "Team size")
    engine = stat(pr, "Engine").replace("Unreal Fortnite (UEFN)", "UEFN")
    cells = [("YEAR", pr["year"]), ("TEAM", team), ("ENGINE", engine)]
    return ('<span class="m-spec">' + "".join(
        f'<span><b>{e(k)}</b>{e(v)}</span>' for k, v in cells) + "</span>")


def mission_list(p, projects):
    rows = ""
    for i, pr in projects:
        title = pr["title"]
        rows += f"""
  <a class="mission" href="{p}projects/{pr['slug']}/" data-tags="{e(' '.join(TAG_STYLE[t][0] for t in pr['tags']))}">
    <span class="m-id" aria-hidden="true">{num(i)}</span>
    <span class="m-thumb">{placeholder(pr['hero_ph'], decorative=True)}</span>
    <span class="m-name"><span class="m-title">{e(title)}<span class="slash" aria-hidden="true">/</span></span><span class="m-genre">{e(pr['genre'])}</span>{tag_chips(pr['tags'])}</span>
    {spec_strip(pr)}
  </a>"""
    return f'<nav class="missions" aria-label="Projects">{rows}\n</nav>'


def pick_cards(p, slugs):
    """Compact cards for the home page picks (the Projects page has the full rows)."""
    cards = ""
    for slug in slugs:
        i, pr = next((i, pr) for i, pr in enumerate(PROJECTS) if pr["slug"] == slug)
        cards += f"""
  <a class="card" href="{p}projects/{slug}/">
    {placeholder(pr['hero_ph'], None, '16/9', decorative=True)}
    <span class="card-head"><span class="m-title">{e(pr['title'])}<span class="slash" aria-hidden="true">/</span></span><span class="card-id" aria-hidden="true">{num(i)}</span></span>
    <span class="m-genre">{e(pr['genre'])}</span>{tag_chips(pr['tags'])}
  </a>"""
    return f'<div class="cards">{cards}\n</div>'


def filter_bar():
    opts = [("all", "All", len(PROJECTS))] + [
        (cls, t.replace(" Design", ""), sum(t in pr["tags"] for pr in PROJECTS)) for t, (cls, _) in TAG_STYLE.items()]
    btns = "".join(
        f'<button type="button" class="filter{" " + cls if cls != "all" else ""}" data-filter="{cls}" '
        f'aria-pressed="{"true" if cls == "all" else "false"}">{e(label)}<span class="count">{n:02d}</span></button>'
        for cls, label, n in opts)
    return (f'<div class="filters" role="group" aria-label="Filter projects by discipline">'
            f'<span class="filters-label" aria-hidden="true">FILTER /</span>{btns}'
            f'<span class="filter-status" aria-live="polite"></span></div>')


BADGE_ICON = {
    "award": ["XXXXX", "XXXXX", ".XXX.", "..X..", ".XXX."],   # trophy
    "status": [".....", ".XXX.", ".XXX.", ".XXX.", "....."],  # status light
}


def badges(items):
    out = ""
    for kind, label in items:
        px = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y, r in enumerate(BADGE_ICON[kind])
                     for x, ch in enumerate(r) if ch == "X")
        out += (f'<span class="badge b-{kind}"><svg viewBox="0 0 5 5" aria-hidden="true" '
                f'shape-rendering="crispEdges">{px}</svg>{e(label)}</span>')
    return f'<div class="badges">{out}</div>'


def doc_head(no, title, sub=None, tag="h1", cls=""):
    """Datasheet heading: dim number and title share a baseline; the sub-line sits on its own row
    under the title, so it never pushes the title out of line."""
    no_html = f'<span class="doc-no" aria-hidden="true">{e(no)}</span>' if no else ""
    sub_html = f'<p class="doc-sub">{e(sub)}</p>' if sub else ""
    return (f'<header class="doc-head {cls}">{no_html}<{tag} class="doc-title">{e(title)}</{tag}>{sub_html}</header>')


def page_head(no, title, sub=None):
    return doc_head(no, title, sub, cls="compact")


def section_head(n, label, tag="h2"):
    return f'<{tag} class="sec"><span class="sec-no" aria-hidden="true">{e(n)}</span>{e(label)}</{tag}>'


def window(title, inner, tag=None, attrs="", cls="", heading=None):
    """Content window: sharp frame, mint corner brackets, title bar with decorative lights.
    A tag (e.g. NEW) sits with the title on the left, away from the lights, so it doesn't
    read as a clickable control."""
    tg = f'<span class="window-tag">{e(tag)}</span>' if tag else ""
    t = heading or "span"   # e.g. "h2" where the window title is the section's heading
    return (f'<div class="window {cls}"{attrs}><div class="window-bar"><{t} class="window-title">{e(title)}{tg}</{t}>'
            f'<span class="window-lights" aria-hidden="true"><i></i><i></i><i></i></span></div>'
            f'<div class="window-body">{inner}\n    </div></div>')


def build_home():
    p = ""
    f = PROJECTS[0]
    links = ext_link(*f["links"][0])                                          # Steam only on home
    tools = "".join(f'<li class="chip t-tool">{e(t)}</li>' for t in HOME["tools"])
    body = f"""
<section class="hero wrap">
  {window(HOME['profile_title'], f"""
      <p class="hud-label" aria-hidden="true"><span class="hud-text">{e(HOME['player_label'])}</span></p>
      <h1 class="hero-intro out">{e(HOME['player'])}<span class="sr-only">, game designer</span><span class="cursor" aria-hidden="true">_</span></h1>
      <p class="hero-bio out">{e(HOME['bio'])}</p>
      <p class="hud-label" aria-hidden="true"><span class="hud-text">{e(HOME['class_label'])}</span></p>
      <div class="out class-chips">{tag_chips(HOME['classes'], full=True, label="Disciplines", link=p)}</div>
      <p class="hud-label" aria-hidden="true"><span class="hud-text">{e(HOME['loadout_label'])}</span></p>
      <ul class="chips tools out" aria-label="Tools I work in">{tools}</ul>""", attrs=' data-console')}
</section>

<a class="scroll-cue" href="#quest" tabindex="-1" aria-hidden="true"><span>SCROLL</span><svg viewBox="0 0 5 3" shape-rendering="crispEdges"><rect x="0" y="0" width="1" height="1"/><rect x="4" y="0" width="1" height="1"/><rect x="1" y="1" width="1" height="1"/><rect x="3" y="1" width="1" height="1"/><rect x="2" y="2" width="1" height="1"/></svg></a>

<section class="wrap featured" id="latest" aria-label="Latest project">
  {window(HOME['latest_title'], f"""
    <div class="featured-grid">
      <a class="featured-media" href="{p}projects/{f['slug']}/" tabindex="-1" aria-hidden="true">{placeholder(f['hero_ph'], 'FIG. 01 / ' + f['title'])}</a>
      <div class="featured-body">
        {doc_head(None, f['title'], None, tag="h2", cls="featured-head")}
        {badges(f.get('badges', []))}
        <p class="feat-tag">{e(f.get('tagline', f['blurb']))}</p>
        <div class="links">{links}<a class="link internal" href="{p}projects/{f['slug']}/">Full breakdown</a></div>
      </div>
    </div>""", tag=HOME["latest_tag"])}
</section>

<section class="quest" id="quest" aria-label="Design quest" data-rip>
  <span class="quest-seam" aria-hidden="true"></span>
  <div class="quest-band">
    <p class="quest-label">{e(HOME['quest_label'])}</p>
    <p class="quest-title">{e(HOME['quest'])}</p>
    <p class="quest-reward">{e(HOME['reward'])}</p>
  </div>
</section>

<section class="wrap more" aria-labelledby="more-title">
  <h2 class="sec" id="more-title"><span class="sec-no" aria-hidden="true">/ PICKS</span>More projects</h2>
  {pick_cards(p, HOME['picks'])}
  <div class="links more-all"><a class="link internal" href="{p}projects/">All {len(PROJECTS)} projects</a></div>
</section>
"""
    page("index.html", None, SITE["description"], body, p=p)


def build_about():
    # Full transcript as plain HTML (what visitors without JavaScript see); site.js replaces it
    # with the interactive version using the JSON script below.
    fallback = "".join(f'<div class="bubble them"><p>{e(t)}</p></div>' for t in ABOUT["intro"])
    for t in ABOUT["topics"]:
        fallback += f'<div class="bubble me"><p>{e(t["q"])}</p></div>'
        fallback += "".join(f'<div class="bubble them"><p>{e(a)}</p></div>' for a in t["a"])
    data = json.dumps({"intro": ABOUT["intro"], "topics": ABOUT["topics"],
                       "final": ABOUT["final"], "finalHref": "../projects/"}).replace("</", "<\\/")
    body = f"""
<section class="wrap section-page">
  {page_head('01', ABOUT['title'])}
  <div class="window chat-window"><div class="window-bar"><span class="window-title">MESSAGES</span><span class="window-lights" aria-hidden="true"><i></i><i></i><i></i></span></div>
  <div class="chat" data-chat>
    <div class="chat-head">
      {placeholder('avatar', None, '1/1', 'avatar')}
      <div><p class="chat-name">Nat</p><p class="chat-status">online</p></div>
    </div>
    <div class="chat-log" aria-live="polite">{fallback}</div>
    <div class="chat-options" role="group" aria-label="Reply options"><a class="chat-opt final" href="../projects/">{e(ABOUT['final'])}</a></div>
  </div></div>
  <script type="application/json" id="chat-data">{data}</script>
</section>
"""
    page("about/index.html", "About", "About Nat - a versatile game designer who enjoys UI/UX and level design the most.",
         body, active="ABOUT")


def build_projects():
    body = f"""
<section class="wrap">
  {page_head('02', 'Game projects')}
  {window("PROJECT INDEX", filter_bar() + mission_list('../', list(enumerate(PROJECTS))), cls="list-window")}
</section>
"""
    page("projects/index.html", "Projects", "Game design projects by Natapatr (Nat) Lorsathian.", body,
         active="PROJECTS")


def pdr(problem, decision, result):
    rows = [("01", "PROBLEM", problem, ""), ("02", "DECISION", decision, " dec"), ("03", "RESULT", result, "")]
    return '<dl class="pdr">' + "".join(
        f'<div class="{c.strip()}"><dt><b>{n}</b>{lbl}</dt><dd>{e(t)}</dd></div>' for n, lbl, t, c in rows) + "</dl>"


def design_log(pr):
    """Tabbed DESIGN LOG window: Overview (contributions + highlight menu), one tab per highlight
    (image beside problem / decision / result), Retrospective. Above 900px all panes share one grid
    cell, so the window keeps the same size on every tab; on smaller screens each tab sizes itself."""
    log = DESIGN_LOG.get(pr["slug"], {"highlights": []})
    hls = log["highlights"]
    contrib = "".join(f"<li>{e(t)}</li>" for t in pr["history"])
    hls = [tuple(h) for h in hls]
    menu = "".join(
        f'<button type="button" class="dl-open" data-go="{k + 1}"><span class="dl-thumb">{placeholder(img, decorative=True)}</span>'
        f'<span class="dl-mtext"><span class="dl-mno">{k + 1:02d}</span><span class="dl-mtitle">{e(t)}</span>'
        f'<span class="dl-mteaser">{e(prob)}</span></span><span class="dl-go" aria-hidden="true">OPEN &rarr;</span></button>'
        for k, (t, img, prob, _d, _r) in enumerate(hls))
    menu_html = f'<div><h3 class="dl-h">HIGHLIGHTS</h3><div class="dl-menu">{menu}</div></div>' if hls else ""
    tabs = [("OVERVIEW", f'''<div class="dl-overview"><div><h3 class="dl-h">{e(pr['history_title'].upper())}</h3>
      <ul class="plus-list">{contrib}</ul></div>{menu_html}</div>''')]
    for k, (t, img, prob, dec, res) in enumerate(hls):
        tabs.append((f"{k + 1:02d} {t}", f'<div class="hl-grid">{placeholder(img, f"FIG. {k + 1:02d} / {t.title()}")}'
                     f'<div>{pdr(prob, dec, res)}</div></div>'))
    tabs.append(("RETROSPECTIVE", f'<p class="retro">{e(log.get("retrospective", RETRO_PLACEHOLDER))}</p>'))
    n = len(tabs)
    tl = "".join(
        f'<button type="button" class="dl-tab" role="tab" id="dl-t{i}" aria-controls="dl-p{i}" '
        f'aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">'
        f'<span class="dl-pip{" seen" if i == 0 else ""}" aria-hidden="true"></span>{e(t)}</button>'
        for i, (t, _) in enumerate(tabs))
    panes = "".join(
        f'<div class="dl-pane{" on" if i == 0 else ""}" role="tabpanel" id="dl-p{i}" aria-labelledby="dl-t{i}" tabindex="0">'
        f'<div class="dl-content">{c}</div>'
        f'<div class="dl-step"><button type="button" class="dl-prev"{" disabled" if i == 0 else ""}><span aria-hidden="true">&larr; </span>Prev</button>'
        f'<span class="dl-count">{i + 1:02d} / {n:02d}</span>'
        f'<button type="button" class="dl-next"{" disabled" if i == n - 1 else ""}>Next<span aria-hidden="true"> &rarr;</span></button></div></div>'
        for i, (_, c) in enumerate(tabs))
    return (f'<div class="window dl" data-log><div class="window-bar"><h2 class="window-title">DESIGN LOG</h2>'
            f'<span class="window-lights" aria-hidden="true"><i></i><i></i><i></i></span></div>'
            f'<div class="dl-tabs" role="tablist" aria-label="Design log">{tl}</div><div class="dl-panes">{panes}</div></div>')


def build_project(i, pr):
    p = "../../"
    rows = "".join(f'<div class="row"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in pr["stats"])
    role_rows = f'<div class="row"><dt>Roles</dt><dd>{e(pr["roles"].replace(" | ", " / "))}</dd></div>'
    spec = f"""<dl class="readout">
      <div class="grp">SPECS</div>{rows}
      <div class="grp">ROLE</div>{role_rows}
    </dl>"""
    links = "".join(ext_link(lbl, href) for lbl, href in pr["links"])
    links = f'<div class="links">{links}</div>' if links else ""
    trophy = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y, r in enumerate(BADGE_ICON["award"])
                     for x, ch in enumerate(r) if ch == "X")
    trophy = f'<svg viewBox="0 0 5 5" aria-hidden="true" shape-rendering="crispEdges">{trophy}</svg>'
    awards = "".join(f"<li>{trophy}{e(a)}</li>" for a in pr.get("awards", []))
    awards = f'<div class="file-awards"><h3 class="grp">AWARDS</h3><ul>{awards}</ul></div>' if awards else ""
    overview = "".join(f"<p>{e(t)}</p>" for t in pr["overview"])
    history = "".join(f"<li>{e(t)}</li>" for t in pr["history"])
    n = 2
    sections = ""
    for k, (heading, paras, ph) in enumerate(pr["sections"]):
        n += 1
        text = "".join(f"<p>{e(t)}</p>" for t in paras)
        sections += f"""
  <section class="split{" flip" if k % 2 else ""}">
    <div>{section_head(f"{n}.0", heading)}<div class="prose">{text}</div></div>
    {placeholder(ph, f"FIG. {num(k + 1)} / {heading}")}
  </section>"""
    gallery = ""
    if pr["gallery_ph"]:
        gallery = '<div class="gallery">' + "".join(
            placeholder(g, f"FIG. {num(len(pr['sections']) + j + 1)} / {g}") for j, g in enumerate(pr["gallery_ph"])) + "</div>"
    prev_pr = PROJECTS[i - 1]
    next_pr = PROJECTS[(i + 1) % len(PROJECTS)]
    body = f"""
<article class="wrap project">
  <nav class="proj-nav" aria-label="Project navigation">
    <a class="back link internal" href="{p}projects/"><span class="pn-full">All projects</span><span class="pn-short">Projects</span></a>
    <span class="proj-step">
      <a class="link internal prev" href="{p}projects/{prev_pr['slug']}/" aria-label="Previous project: {e(prev_pr['title'])}"><span class="pn-full">{num(i - 1 if i else len(PROJECTS) - 1)} / {e(prev_pr['title'])}</span><span class="pn-short">Prev</span></a>
      <span class="proj-count" aria-hidden="true">{num(i)}<b>/</b>{len(PROJECTS):02d}</span>
      <a class="link internal" href="{p}projects/{next_pr['slug']}/" aria-label="Next project: {e(next_pr['title'])}"><span class="pn-full">{num((i + 1) % len(PROJECTS))} / {e(next_pr['title'])}</span><span class="pn-short">Next</span></a>
    </span>
  </nav>
  {doc_head(num(i), pr['title'], f"{pr['subtitle']} / {pr['year']} / {pr['kind']}", cls="page-head")}
  {window("PROJECT FILE", f"""
    <div class="file-grid">
      <div class="file-main">
        {placeholder(pr['hero_ph'], 'FIG. 00 / ' + pr['title'], '16/9', 'hero-ph')}
        <p class="file-pitch">{e(pr['blurb'])}</p>
      </div>
      <div class="file-side">
        {spec}
        {awards}
        {links}
      </div>
    </div>""", cls="file-window", heading="h2")}
  {design_log(pr)}
</article>
"""
    page(f"projects/{pr['slug']}/index.html", pr["title"],
         f"{pr['title']} - {pr['blurb']}", body, active="PROJECTS")


def build_contact():
    lines = "".join(f"<p>{e(t)}</p>" for t in CONTACT["lines"])
    body = f"""
<section class="wrap section-page">
  {page_head('03', 'Contact me')}
  {window("COMMS", f"""
    <div class="contact-grid"><div>
    {section_head('/ RESUME', CONTACT['heading'])}
    <div class="note prose">{lines}</div>
    </div><div>
    {section_head('/ CHANNELS', 'Reach me at')}
    <dl class="readout contact">
      <div class="row"><dt>Email</dt><dd>{email_link('../')}</dd></div>
      <div class="row"><dt>LinkedIn</dt><dd>{ext_link(SITE['linkedin_label'], SITE['linkedin'], '')}</dd></div>
      <div class="row"><dt>itch.io</dt><dd>{ext_link('twonah.itch.io', SITE['itch'], '')}</dd></div>
    </dl>
    </div></div>""", cls="contact-window")}
</section>
"""
    page("contact/index.html", "Contact", "Contact Nat for game design roles and a tailored resume.", body,
         active="CONTACT")


def build_404():
    body = """
<section class="wrap section-page">
  <h1 class="sec"><span class="sec-no" aria-hidden="true">/ 404</span>Level not found</h1>
  <div class="prose"><p>This room doesn't exist (yet). Respawn at the start?</p></div>
  <div class="links"><a class="link internal" href="/portfolio/">Back to home</a></div>
</section>
"""
    page("404.html", "Not found", "Page not found.", body, p="/portfolio/")


LOGO_CELL = 5   # px per logo cell in the top bar


def nl_logo():
    """Pixel NL plate (logo concept 6a, 2026-11-07). One grid: the letters, the corner cuts and
    the "/" are all whole cells. Letters are 5 cells tall with 1-cell strokes; the "/" (the site's
    link flair) sits in the L's empty top-right corner. Corners are deliberately uneven: top-left
    loses one cell, bottom-right a two-step cut, the other two stay square. The letters and "/"
    are real holes, so the header shows through. Mint gradient plus a top sheen."""
    n = ["X....X", "XX...X", "X.X..X", "X..X.X", "X...XX"]
    l = ["X....", "X....", "X....", "X....", "XXXXX"]
    glyph = [a + "." + c for a, c in zip(n, l)]
    pad = 2
    w, h = len(glyph[0]) + pad * 2, len(glyph) + pad * 2      # 16 x 9 cells
    holes = {(x + pad, y + pad) for y, row in enumerate(glyph) for x, c in enumerate(row) if c == "X"}
    holes |= {(13, 2), (12, 3), (11, 4)}                       # the "/"
    holes |= {(0, 0)}                                          # top-left: one cell
    holes |= {(w - 1, h - 1), (w - 2, h - 1), (w - 1, h - 2)}  # bottom-right: two steps
    cells = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>'
                    for y in range(h) for x in range(w) if (x, y) not in holes)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w * LOGO_CELL}" '
            f'height="{h * LOGO_CELL}" shape-rendering="crispEdges">'
            f'<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{w}" y2="{h}">'
            '<stop offset="0" stop-color="#d6fff1"/><stop offset=".55" stop-color="#9ef5d6"/>'
            '<stop offset="1" stop-color="#5fd9b3"/></linearGradient>'
            '<linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/>'
            '<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="c">{cells}</clipPath></defs>'
            f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="url(#g)"/>'
            f'<rect width="{w}" height="5" fill="url(#s)"/></g></svg>')


def tear_edge(seed, cell, depth, width=480, loose=5, fill="#000"):
    """A band edge 'ripped' into pixels: solid along the top, then a stepped contour of whole cells
    (each column 0..depth-1 cells deep, changing by at most one step), with a few loose cells
    breaking away below. Draw it under a solid band; flip it for the other side."""
    rnd = random.Random(seed)
    cols = width // cell
    rects, h = [], 1
    for x in range(cols):
        h = max(0, min(depth - 1, h + rnd.choice((-1, 0, 0, 1))))
        if h:
            rects.append(f'<rect x="{x * cell}" y="0" width="{cell}" height="{h * cell}"/>')
    for _ in range(loose):
        x = rnd.randrange(cols)
        rects.append(f'<rect x="{x * cell}" y="{(depth - 1) * cell}" width="{cell}" height="{cell}"/>')
    hgt = depth * cell
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{hgt}" viewBox="0 0 {width} {hgt}" '
            f'shape-rendering="crispEdges" fill="{fill}">{"".join(rects)}</svg>'), hgt


# Pixel size (px), max depth (cells), loose cells per tile, tile width (px) of the quest band rip.
QUEST_EDGE = {"cell": 24, "depth": 2, "loose": 3, "width": 960}


def build_assets():
    # Design-quest band edges: different seeds top and bottom so the rip doesn't look mirrored.
    for side, seed in (("top", 11), ("bottom", 23)):
        svg, _ = tear_edge(seed, QUEST_EDGE["cell"], QUEST_EDGE["depth"], QUEST_EDGE["width"], QUEST_EDGE["loose"])
        write(f"assets/quest-edge-{side}.svg", svg)
    logo = nl_logo()
    write("assets/logo.svg", logo)
    write("assets/favicon.svg", logo)
    here = os.path.dirname(__file__)
    for name in ("style.css", "site.js"):
        with open(os.path.join(here, name), encoding="utf-8") as f:
            write(f"assets/{name}", f.read())


def build_sitemap():
    urls = ["", "about/", "projects/", "contact/"] + [f"projects/{pr['slug']}/" for pr in PROJECTS]
    items = "".join(f"<url><loc>{SITE['base_url']}{u}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n'
                         f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>\n')


if __name__ == "__main__":
    build_assets()
    build_home()
    build_about()
    build_projects()
    for i, pr in enumerate(PROJECTS):
        build_project(i, pr)
    build_contact()
    build_404()
    build_sitemap()
    print("Built", 6 + len(PROJECTS), "pages")
