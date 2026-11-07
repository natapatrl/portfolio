"""Builds the static site from content.py.

Run from the repo root:  python3 _build/build.py
Folders starting with "_" are not published by GitHub Pages, so this script stays private to the repo.
"""
import json
import os
import random
from html import escape as e

from content import SITE, HOME, ABOUT, CONTACT, PROJECTS

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


def placeholder(label, caption=None, ratio="16/9", cls=""):
    cap = f'<figcaption>{e(caption)}</figcaption>' if caption else ""
    return (f'<figure class="frame {cls}"><div class="ph" style="aspect-ratio:{ratio}" role="img" '
            f'aria-label="Image coming soon: {e(label)}"><span>[ img: {e(label)} ]</span></div>{cap}</figure>')


def ext_link(label, href, cls="link"):
    return f'<a class="{cls}" href="{href}" target="_blank" rel="noopener">{e(label)}</a>'


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
    <img class="brand-mark" src="{p}assets/logo.svg" alt="" width="64" height="44">
    <span class="brand-text"><span class="brand-name">NATAPATR LORSATHIAN</span><span class="brand-role">game designer</span></span>
  </a>
  <nav class="site-nav" aria-label="Main">{nav}</nav>
  <div class="read" aria-hidden="true"><span class="read-label">READ</span><span class="read-cells"></span><span class="read-pct">0%</span></div>
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


def tag_chips(tags):
    out = ""
    for t in tags:
        cls, icon = TAG_STYLE.get(t, ("", []))
        px = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y, r in enumerate(icon) for x, ch in enumerate(r) if ch == "X")
        svg = f'<svg viewBox="0 0 5 5" aria-hidden="true" shape-rendering="crispEdges">{px}</svg>' if px else ""
        out += f'<span class="chip {cls}">{svg}{e(t.replace(" Design", ""))}</span>'
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
        title = pr.get("list_title", pr["title"])
        rows += f"""
  <a class="mission" href="{p}projects/{pr['slug']}/">
    <span class="m-id">{num(i)}</span>
    <span class="m-thumb">{placeholder(pr['hero_ph'])}</span>
    <span class="m-name"><span class="m-title">{e(title)}<span class="slash">/</span></span><span class="m-genre">{e(pr['genre'])}</span>{tag_chips(pr['tags'])}</span>
    {spec_strip(pr)}
  </a>"""
    return f'<nav class="missions" aria-label="Projects">{rows}\n</nav>'


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
    no_html = f'<span class="doc-no">{e(no)}</span>' if no else ""
    sub_html = f'<p class="doc-sub">{e(sub)}</p>' if sub else ""
    return (f'<header class="doc-head {cls}">{no_html}<{tag} class="doc-title">{e(title)}</{tag}>{sub_html}</header>')


def page_head(no, title, sub=None):
    return doc_head(no, title, sub, cls="compact")


def section_head(n, label):
    return f'<h2 class="sec"><span class="sec-no">{e(n)}</span>{e(label)}</h2>'


def build_home():
    p = ""
    f = PROJECTS[0]
    links = ext_link(*f["links"][0])                                          # Steam only on home
    body = f"""
<section class="hero wrap">
  <h1 class="hero-intro">{e(HOME['intro'])}<span class="cursor" aria-hidden="true">_</span></h1>
  <p class="hero-tools">{e(HOME['tools'])}</p>
</section>

<section class="wrap featured" aria-labelledby="featured-title">
  <div class="featured-grid">
    <a class="featured-media" href="{p}projects/{f['slug']}/" tabindex="-1" aria-hidden="true">{placeholder(f['hero_ph'], 'FIG. 01 / ' + f['title'])}</a>
    <div class="featured-body">
      <p class="feat-kicker">/ LATEST PROJECT</p>
      {doc_head(None, f['title'], None, tag="h2", cls="featured-head")}
      {badges(f.get('badges', []))}
      <p class="feat-tag">{e(f.get('tagline', f['blurb']))}</p>
      <div class="links">{links}<a class="link internal" href="{p}projects/{f['slug']}/">Full breakdown</a></div>
    </div>
  </div>
</section>

<section class="quest" aria-label="Design quest">
  <p class="quest-label">{e(HOME['quest_label'])}</p>
  <p class="quest-title">{e(HOME['quest'])}</p>
  <p class="quest-reward">{e(HOME['reward'])}</p>
</section>

<section class="wrap more" aria-labelledby="more-title">
  <h2 class="sec" id="more-title"><span class="sec-no">/ INDEX</span>More projects</h2>
  {mission_list(p, list(enumerate(PROJECTS))[1:])}
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
  <div class="chat" data-chat>
    <div class="chat-head">
      {placeholder('avatar', None, '1/1', 'avatar')}
      <div><p class="chat-name">Nat</p><p class="chat-status">online</p></div>
    </div>
    <div class="chat-log" aria-live="polite">{fallback}</div>
    <div class="chat-options" role="group" aria-label="Reply options"><a class="chat-opt final" href="../projects/">{e(ABOUT['final'])}</a></div>
  </div>
  <script type="application/json" id="chat-data">{data}</script>
</section>
"""
    page("about/index.html", "About", "About Nat - a versatile game designer who enjoys UI/UX and level design the most.",
         body, active="ABOUT")


def build_projects():
    body = f"""
<section class="wrap section-page">
  {page_head('02', 'Game projects')}
  <div class="frame-box list-box">
  {mission_list('../', list(enumerate(PROJECTS)))}
  </div>
</section>
"""
    page("projects/index.html", "Projects", "Game design projects by Natapatr (Nat) Lorsathian.", body,
         active="PROJECTS")


def build_project(i, pr):
    p = "../../"
    rows = "".join(f'<div class="row"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in pr["stats"])
    role_rows = (f'<div class="row"><dt>Roles</dt><dd>{e(pr["roles"].replace(" | ", " / "))}</dd></div>'
                 f'<div class="row"><dt>Disciplines</dt><dd>{e(" / ".join(pr["tags"]))}</dd></div>')
    spec = f"""<dl class="readout">
      <div class="grp">SPECS</div>{rows}
      <div class="grp">ROLE</div>{role_rows}
    </dl>"""
    links = "".join(ext_link(lbl, href) for lbl, href in pr["links"])
    links = f'<div class="links">{links}</div>' if links else ""
    awards = "".join(f"<li>{e(a)}</li>" for a in pr.get("awards", []))
    awards = f'{section_head("/", "Awards")}<ul class="plus-list awards">{awards}</ul>' if awards else ""
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
  <a class="back link internal" href="{p}projects/">All projects</a>
  {doc_head(num(i), pr['title'], f"{pr['subtitle']} / {pr['year']} / {pr['kind']}", cls="page-head")}
  {placeholder(pr['hero_ph'], 'FIG. 00 / ' + pr['title'], '16/9', 'hero-ph')}
  <div class="two-col">
    <div>
      {section_head('1.0', 'Overview')}
      <div class="prose">{overview}</div>
      {section_head('2.0', pr['history_title'])}
      <ul class="plus-list">{history}</ul>
    </div>
    <aside>
      {spec}
      {links}
      {awards}
    </aside>
  </div>
  {sections}
  {gallery}
  <nav class="pager" aria-label="More projects">
    <a class="link internal prev" href="{p}projects/{prev_pr['slug']}/">{num(i - 1 if i else len(PROJECTS) - 1)} / {e(prev_pr['title'])}</a>
    <a class="link internal" href="{p}projects/{next_pr['slug']}/">{num((i + 1) % len(PROJECTS))} / {e(next_pr['title'])}</a>
  </nav>
</article>
"""
    page(f"projects/{pr['slug']}/index.html", pr["title"],
         f"{pr['title']} - {pr['blurb']}", body, active="PROJECTS")


def build_contact():
    lines = "".join(f"<p>{e(t)}</p>" for t in CONTACT["lines"])
    body = f"""
<section class="wrap section-page">
  {page_head('03', 'Contact me')}
  <div class="frame-box">
    {section_head('/ RESUME', CONTACT['heading'])}
    <div class="note prose">{lines}</div>
    {section_head('/ CHANNELS', 'Reach me at')}
    <dl class="readout contact">
      <div class="row"><dt>Email</dt><dd>{email_link('../')}</dd></div>
      <div class="row"><dt>LinkedIn</dt><dd>{ext_link(SITE['linkedin_label'], SITE['linkedin'], '')}</dd></div>
      <div class="row"><dt>itch.io</dt><dd>{ext_link('twonah.itch.io', SITE['itch'], '')}</dd></div>
    </dl>
  </div>
</section>
"""
    page("contact/index.html", "Contact", "Contact Nat for game design roles and a tailored resume.", body,
         active="CONTACT")


def build_404():
    body = """
<section class="wrap narrow">
  <h2 class="sec"><span class="sec-no">/ 404</span>Level not found</h2>
  <div class="prose"><p>This room doesn't exist (yet). Respawn at the start?</p></div>
  <div class="links"><a class="link internal" href="/portfolio/">Back to home</a></div>
</section>
"""
    page("404.html", "Not found", "Page not found.", body, p="/portfolio/")


def nl_logo():
    """Pixel NL knocked out of a mint gradient badge. Every element sits on one 1-unit grid
    (the same size as the letter pixels): a few badge cells at the top-right corner are missing
    and two drift off to the right."""
    n = ["X...X", "XX..X", "XX..X", "X.X.X", "X..XX", "X..XX", "X...X"]
    l = ["X...", "X...", "X...", "X...", "X...", "X...", "XXXX"]
    glyph = [a + "." + c for a, c in zip(n, l)]
    bw, bh = len(glyph[0]) + 4, len(glyph) + 4          # badge 14 x 11 cells
    holes = [(13, 0), (12, 0), (13, 1), (11, 0), (13, 3)]   # cells missing from the badge
    drift = [(14, 1, 0.7), (15, 0, 0.4)]               # loose cells that broke away
    vw = bw + 2
    hole_rects = "".join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="#000"/>' for x, y in holes)
    px = "".join(f'<rect x="{x + 2}" y="{y + 2}" width="1" height="1"/>'
                 for y, row in enumerate(glyph) for x, c in enumerate(row) if c == "X")
    loose = "".join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="url(#g)" opacity="{o}"/>' for x, y, o in drift)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {bh}" width="{vw * 4}" height="{bh * 4}" '
            'shape-rendering="crispEdges">'
            f'<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{bw}" y2="{bh}">'
            '<stop offset="0" stop-color="#d6fff1"/><stop offset=".55" stop-color="#9ef5d6"/>'
            '<stop offset="1" stop-color="#5fd9b3"/></linearGradient>'
            '<linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/>'
            '<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="{bw}" height="{bh}">'
            f'<rect width="{bw}" height="{bh}" fill="#fff"/>{hole_rects}</mask></defs>'
            f'<g mask="url(#m)"><rect width="{bw}" height="{bh}" fill="url(#g)"/>'
            f'<rect width="{bw}" height="6" fill="url(#s)"/></g>'
            f'<g fill="#0b1338">{px}</g>{loose}</svg>')


def tear_edge(seed, cell, depth, width=480, loose=5, fill="#000"):
    """A band edge 'ripped' into pixels: solid along the top, then a stepped contour of whole cells
    (each column 0..depth-1 cells deep, changing by at most one step), with a few loose cells
    breaking away below. Draw it under a solid band; flip it for the other side."""
    rnd = random.Random(seed)
    cols = width // cell
    rects, h = [], 1
    for x in range(cols):
        h = max(1, min(depth - 1, h + rnd.choice((-1, 0, 0, 1))))
        rects.append(f'<rect x="{x * cell}" y="0" width="{cell}" height="{h * cell}"/>')
    for _ in range(loose):
        x, y = rnd.randrange(cols), rnd.randrange(depth - 1, depth + 1)
        rects.append(f'<rect x="{x * cell}" y="{y * cell}" width="{cell}" height="{cell}"/>')
    hgt = (depth + 1) * cell
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{hgt}" viewBox="0 0 {width} {hgt}" '
            f'shape-rendering="crispEdges" fill="{fill}">{"".join(rects)}</svg>'), hgt


# Pixel size (px), max depth (cells), loose cells per tile, tile width (px) of the quest band rip.
QUEST_EDGE = {"cell": 14, "depth": 4, "loose": 5, "width": 980}


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
