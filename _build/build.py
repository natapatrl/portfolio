"""Builds the static site from content.py.

Run from the repo root:  python3 _build/build.py
Folders starting with "_" are not published by GitHub Pages, so this script stays private to the repo.
"""
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
  <a class="logo" href="{home}" aria-label="Home">
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


def mission_list(p, projects):
    rows = ""
    for i, pr in projects:
        title = pr.get("list_title", pr["title"])
        rows += f"""
  <a class="mission" href="{p}projects/{pr['slug']}/">
    <span class="m-id">{num(i)}</span>
    <span class="m-name"><span class="m-title">{e(title)}<span class="slash">/</span></span><small>{e(pr['blurb'])}</small></span>
    <span class="m-meta"><span>{e(pr['year'])}</span><span>{e(pr['kind'])}</span><span>{e(' / '.join(pr['tags']))}</span></span>
  </a>"""
    return f'<nav class="missions" aria-label="Projects">{rows}\n</nav>'


def section_head(n, label):
    return f'<h2 class="sec"><span class="sec-no">{e(n)}</span>{e(label)}</h2>'


def build_home():
    p = ""
    f = PROJECTS[0]
    awards = "".join(f"<li>{e(a)}</li>" for a in f.get("awards", []))
    links = "".join(ext_link(lbl, href) for lbl, href in f["links"])
    body = f"""
<section class="hero wrap">
  <h1 class="hero-intro">{e(HOME['intro'])}<span class="cursor" aria-hidden="true">_</span></h1>
  <p class="hero-tools">{e(HOME['tools'])}</p>
</section>

<section class="wrap featured" aria-labelledby="featured-title">
  {section_head('/ FEATURED', 'Latest project')}
  <div class="featured-grid">
    <a class="featured-media" href="{p}projects/{f['slug']}/" tabindex="-1" aria-hidden="true">{placeholder(f['hero_ph'], 'FIG. 01 / ' + f['title'])}</a>
    <div class="featured-body">
      <div class="doc-head">
        <span class="doc-no">01</span>
        <div><h3 class="doc-title" id="featured-title">{e(f['title'])}</h3>
        <p class="doc-sub">{e(f['subtitle'])} / {e(f['roles'])}</p></div>
      </div>
      <div class="prose"><p>{e(f['blurb'])}</p></div>
      <ul class="plus-list awards">{awards}</ul>
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
    bubbles = "\n".join(
        f'<div class="bubble {side}"><p>{e(text)}</p></div>' for side, text in ABOUT["chat"])
    body = f"""
<section class="wrap narrow">
  {section_head('/ ABOUT', ABOUT['title'])}
  <div class="chat">
    <div class="chat-head">
      {placeholder('avatar', None, '1/1', 'avatar')}
      <div><p class="chat-name">Nat</p><p class="chat-status">&gt; online_</p></div>
    </div>
{bubbles}
    <div class="bubble them typing" aria-hidden="true"><span></span><span></span><span></span></div>
  </div>
  <div class="links"><a class="link internal" href="../projects/">See my projects</a><a class="link internal" href="../contact/">Get in touch</a></div>
</section>
"""
    page("about/index.html", "About", "About Nat - a versatile game designer who enjoys UI/UX and level design the most.",
         body, active="ABOUT")


def build_projects():
    body = f"""
<section class="wrap">
  <div class="doc-head page-head">
    <span class="doc-no">{len(PROJECTS):02d}</span>
    <div><h1 class="doc-title">Game projects</h1><p class="doc-sub">Gameplay / Level / UX/UI design, 2024 to now</p></div>
  </div>
  {mission_list('../', list(enumerate(PROJECTS)))}
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
  <header class="doc-head page-head">
    <span class="doc-no">{num(i)}</span>
    <div><h1 class="doc-title">{e(pr['title'])}</h1>
    <p class="doc-sub">{e(pr['subtitle'])} / {e(pr['year'])} / {e(pr['kind'])}</p></div>
  </header>
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
<section class="wrap narrow">
  {section_head('/ RESUME', CONTACT['heading'])}
  <div class="note prose">{lines}</div>
  {section_head('/ CONTACT', 'Contact me')}
  <dl class="readout contact">
    <div class="row"><dt>Email</dt><dd>{email_link('../')}</dd></div>
    <div class="row"><dt>LinkedIn</dt><dd>{ext_link(SITE['linkedin_label'], SITE['linkedin'], '')}</dd></div>
    <div class="row"><dt>itch.io</dt><dd>{ext_link('twonah.itch.io', SITE['itch'], '')}</dd></div>
  </dl>
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


def build_assets():
    rnd = random.Random(7)
    w, h, s = 480, 48, 8
    rects = []
    for y in range(0, h, s):
        density = (y + s) / h
        for x in range(0, w, s):
            if y == h - s or rnd.random() < density ** 1.6:
                rects.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}"/>')
    write("assets/pixel-edge.svg",
          f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
          f'shape-rendering="crispEdges" fill="#000">{"".join(rects)}</svg>')
    write("assets/favicon.svg",
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">'
          '<rect width="16" height="16" fill="#162354"/>'
          '<path fill="#9ef5d6" d="M3 3h2v10H3zM11 3h2v10h-2zM5 5h2v2H5zM7 7h2v2H7zM9 9h2v2H9z"/></svg>')
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
