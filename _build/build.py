"""Builds the static site from content.py.

Run from the repo root:  python3 _build/build.py
Folders starting with "_" are not published by GitHub Pages, so this script stays private to the repo.
"""
import os
import random
from html import escape as e

from content import SITE, HOME, ABOUT, CONTACT, PROJECTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ("https://fonts.googleapis.com/css2?family=Rubik:wght@400;500"
         "&family=Space+Grotesk:wght@400;500;700&family=Tiny5&display=swap")
NAV = [("ABOUT", "about/"), ("PROJECTS", "projects/"), ("CONTACT", "contact/")]


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def email_link(p, cls=""):
    u, d = SITE["email_user"], SITE["email_domain"]
    return (f'<a class="js-email {cls}" data-u="{e(u)}" data-d="{e(d)}" href="{p}contact/">'
            f'{e(u)} [at] {e(d.replace(".", " [dot] "))}</a>')


def placeholder(label, ratio="16/9", cls=""):
    return (f'<div class="ph {cls}" style="aspect-ratio:{ratio}" role="img" aria-label="Image coming soon: {e(label)}">'
            f'<span class="ph-tag">IMG</span><span class="ph-label">{e(label)}</span></div>')


def page(rel_out, title, desc, body, active=None, p=None):
    depth = rel_out.count("/")
    p = p if p is not None else "../" * depth
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
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="logo" href="{p}" aria-label="Home">
    <span class="logo-name">NATAPATR<br>LORSATHIAN</span>
    <span class="logo-role">GAME DESIGNER</span>
  </a>
  <nav class="site-nav" aria-label="Main">{nav}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="footer-links">
    <a href="{SITE['itch']}" target="_blank" rel="noopener">itch.io</a>
    <a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
    {email_link(p)}
  </div>
  <p class="footer-note">&copy; {SITE['name']}</p>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>
"""
    write(rel_out, html)


def project_card(pr, p, featured=False):
    title = pr.get("list_title", pr["title"])
    tags = "".join(f"<li>{e(t)}</li>" for t in pr["tags"])
    return f"""<a class="card" href="{p}projects/{pr['slug']}/">
  {placeholder(pr['hero_ph'])}
  <div class="card-body">
    <p class="card-meta">{e(pr['year'])} &middot; {e(pr['kind'])}</p>
    <h3>{e(title)}</h3>
    <p class="card-roles">{e(pr['roles'])}</p>
    <p>{e(pr['blurb'])}</p>
    <ul class="tags">{tags}</ul>
  </div>
</a>"""


def build_home():
    p = ""
    f = PROJECTS[0]
    awards = "".join(f"<li>{e(a)}</li>" for a in f.get("awards", []))
    buttons = "".join(
        f'<a class="btn{" btn-primary" if i == 0 else ""}" href="{href}" target="_blank" rel="noopener">{e(lbl)}</a>'
        for i, (lbl, href) in enumerate(f["links"]))
    others = "\n".join(project_card(pr, p) for pr in PROJECTS[1:])
    body = f"""
<section class="hero wrap">
  <h1 class="hero-intro">{e(HOME['intro'])}</h1>
  <p class="hero-tools">{e(HOME['tools'])}</p>
</section>

<section class="featured wrap" aria-labelledby="featured-title">
  <p class="kicker">&gt; FEATURED PROJECT_</p>
  <div class="featured-card">
    <a class="featured-media" href="{p}projects/{f['slug']}/" tabindex="-1" aria-hidden="true">{placeholder(f['hero_ph'])}</a>
    <div class="featured-body">
      <p class="card-meta">{e(f['year'])} &middot; {e(f['kind'])} &middot; {e(f['roles'])}</p>
      <h2 id="featured-title">{e(f['title'])}</h2>
      <p>{e(f['blurb'])}</p>
      <ul class="awards">{awards}</ul>
      <div class="btn-row">{buttons}<a class="btn" href="{p}projects/{f['slug']}/">View project</a></div>
    </div>
  </div>
</section>

<section class="quest" aria-label="Design quest">
  <p class="quest-label">{e(HOME['quest_label'])}</p>
  <p class="quest-title">{e(HOME['quest'])}</p>
  <p class="quest-reward">{e(HOME['reward'])}</p>
</section>

<section class="wrap more" aria-labelledby="more-title">
  <p class="kicker" id="more-title">&gt; MORE PROJECTS_</p>
  <div class="grid">
{others}
  </div>
  <p class="center"><a class="btn" href="{p}projects/">All projects</a></p>
</section>
"""
    page("index.html", None, SITE["description"], body, p=p)


def build_about():
    bubbles = "\n".join(
        f'<div class="bubble {side}"><p>{e(text)}</p></div>' for side, text in ABOUT["chat"])
    body = f"""
<section class="wrap narrow">
  <h1 class="page-title">{e(ABOUT['title'])}</h1>
  <div class="chat">
    <div class="chat-head">
      {placeholder('Photo or avatar of Nat', '1/1', 'avatar')}
      <div><p class="chat-name">Nat</p><p class="chat-status">&#9679; online</p></div>
    </div>
{bubbles}
    <div class="bubble them typing" aria-hidden="true"><span></span><span></span><span></span></div>
  </div>
  <p class="center"><a class="btn btn-primary" href="../projects/">See my projects</a> <a class="btn" href="../contact/">Get in touch</a></p>
</section>
"""
    page("about/index.html", "About", "About Nat - a versatile game designer who enjoys UI/UX and level design the most.",
         body, active="ABOUT")


def build_projects():
    p = "../"
    cards = "\n".join(project_card(pr, p) for pr in PROJECTS)
    body = f"""
<section class="wrap">
  <h1 class="page-title">GAME PROJECTS</h1>
  <div class="grid">
{cards}
  </div>
</section>
"""
    page("projects/index.html", "Projects", "Game design projects by Natapatr (Nat) Lorsathian.", body,
         active="PROJECTS")


def build_project(i, pr):
    p = "../../"
    stats = "".join(f'<div class="stat"><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in pr["stats"])
    links = "".join(
        f'<a class="btn{" btn-primary" if j == 0 else ""}" href="{href}" target="_blank" rel="noopener">{e(lbl)}</a>'
        for j, (lbl, href) in enumerate(pr["links"]))
    links = f'<div class="btn-row">{links}</div>' if links else ""
    awards = "".join(f"<li>{e(a)}</li>" for a in pr.get("awards", []))
    awards = f'<ul class="awards">{awards}</ul>' if awards else ""
    overview = "".join(f"<p>{e(t)}</p>" for t in pr["overview"])
    history = "".join(f"<li>{e(t)}</li>" for t in pr["history"])
    sections = ""
    for n, (heading, paras, ph) in enumerate(pr["sections"]):
        text = "".join(f"<p>{e(t)}</p>" for t in paras)
        sections += f"""
  <section class="split{" flip" if n % 2 else ""}">
    <div><h3>&gt; {e(heading)}</h3>{text}</div>
    {placeholder(ph)}
  </section>"""
    if sections:
        sections = f'<h2 class="section-title">About the project</h2>{sections}'
    gallery = ""
    if pr["gallery_ph"]:
        gallery = '<div class="gallery">' + "".join(placeholder(g) for g in pr["gallery_ph"]) + "</div>"
    prev_pr = PROJECTS[i - 1]
    next_pr = PROJECTS[(i + 1) % len(PROJECTS)]
    body = f"""
<article class="wrap project">
  <p><a class="back" href="{p}projects/">&lt; All projects</a></p>
  <header class="project-head">
    <p class="kicker">{e(pr['subtitle'])}</p>
    <h1 class="page-title">{e(pr['title'])}</h1>
    <p class="card-roles">{e(pr['year'])} &middot; {e(pr['kind'])} &middot; {e(pr['roles'])}</p>
  </header>
  {placeholder(pr['hero_ph'], '16/9', 'hero-ph')}
  <dl class="stats">{stats}</dl>
  {links}
  {awards}
  <div class="two-col">
    <section><h2 class="section-title">&gt; Overview_</h2>{overview}</section>
    <section class="log"><h2 class="section-title">{e(pr['history_title'])}</h2><ul class="quest-log">{history}</ul></section>
  </div>
  {sections}
  {gallery}
  <nav class="pager" aria-label="More projects">
    <a href="{p}projects/{prev_pr['slug']}/">&lt; {e(prev_pr['title'])}</a>
    <a href="{p}projects/{next_pr['slug']}/">{e(next_pr['title'])} &gt;</a>
  </nav>
</article>
"""
    page(f"projects/{pr['slug']}/index.html", pr["title"],
         f"{pr['title']} - {pr['blurb']}", body, active="PROJECTS")


def build_contact():
    lines = "".join(f"<p>{e(t)}</p>" for t in CONTACT["lines"])
    body = f"""
<section class="wrap narrow">
  <p class="kicker">&gt; {e(CONTACT['heading'])}_</p>
  <div class="terminal">{lines}</div>
  <h1 class="page-title">CONTACT ME</h1>
  <dl class="contact-list">
    <div><dt>Email</dt><dd>{email_link('../', 'big')}</dd></div>
    <div><dt>LinkedIn</dt><dd><a href="{SITE['linkedin']}" target="_blank" rel="noopener">{e(SITE['linkedin_label'])}</a></dd></div>
    <div><dt>itch.io</dt><dd><a href="{SITE['itch']}" target="_blank" rel="noopener">twonah.itch.io</a></dd></div>
  </dl>
</section>
"""
    page("contact/index.html", "Contact", "Contact Nat for game design roles and a tailored resume.", body,
         active="CONTACT")


def build_404():
    body = """
<section class="wrap narrow center">
  <p class="kicker">&gt; ERROR 404_</p>
  <h1 class="page-title">LEVEL NOT FOUND</h1>
  <p>This room doesn't exist (yet). Respawn at the start?</p>
  <p><a class="btn btn-primary" href="/portfolio/">Back to home</a></p>
</section>
"""
    page("404.html", "Not found", "Page not found.", body, p="/portfolio/")


def build_assets():
    rnd = random.Random(7)
    # Dithered pixel edge: dense at the bottom, sparse at the top (used above the quest band).
    w, h, s = 480, 48, 8
    rects = []
    for y in range(0, h, s):
        density = (y + s) / h
        for x in range(0, w, s):
            if y == h - s or rnd.random() < density ** 1.6:
                rects.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
           f'shape-rendering="crispEdges" fill="#000">{"".join(rects)}</svg>')
    write("assets/pixel-edge.svg", svg)
    write("assets/favicon.svg",
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">'
          '<rect width="16" height="16" fill="#162354"/>'
          '<path fill="#9ef5d6" d="M3 3h2v10H3zM11 3h2v10h-2zM5 5h2v2H5zM7 7h2v2H7zM9 9h2v2H9z"/></svg>')
    with open(os.path.join(os.path.dirname(__file__), "style.css"), encoding="utf-8") as f:
        write("assets/style.css", f.read())
    with open(os.path.join(os.path.dirname(__file__), "site.js"), encoding="utf-8") as f:
        write("assets/site.js", f.read())


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
