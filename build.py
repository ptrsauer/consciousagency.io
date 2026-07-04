#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["markdown", "jinja2"]
# ///
"""Static site generator for consciousagency.io.

Deliberately minimal (cold-blooded software): markdown in, HTML out.
Everything the site publishes for AI agents (llms.txt, markdown copies,
full-text RSS) is a first-class output of this script, not a plugin.

Usage:
    ./build.py          # build posts/ + pages/ into docs/
    ./build.py --serve  # build, then serve docs/ on localhost:8000
"""

import re
import shutil
import sys
from datetime import date, datetime, timezone
from html import escape
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
SITE = {
    "title": "Conscious Agency",
    "url": "https://consciousagency.io",
    "description": "Research, experiments, and reflections by Peter Sauer.",
    "author": "Peter Sauer",
    "accent": "#059669",
}
MD_EXTENSIONS = ["fenced_code", "tables", "footnotes", "smarty"]


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Parse a minimal `key: value` front matter block. No YAML dependency."""
    meta: dict[str, str] = {}
    if text.startswith("---"):
        head, _, body = text[3:].partition("\n---")
        for line in head.strip().splitlines():
            if ":" in line:
                key, _, value = line.partition(":")
                meta[key.strip()] = value.strip()
        return meta, body.lstrip("\n")
    return meta, text


def load_post(path: Path) -> dict:
    meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
    slug = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    post_date = date.fromisoformat(meta.get("date") or path.stem[:10])
    return {
        "slug": slug,
        "title": meta.get("title", slug),
        "description": meta.get("description", ""),
        "date": post_date,
        "markdown": body,
        "html": markdown.markdown(body, extensions=MD_EXTENSIONS),
        "url": f"{SITE['url']}/posts/{slug}/",
    }


def rfc822(d: date) -> str:
    return datetime(d.year, d.month, d.day, tzinfo=timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S +0000"
    )


def build() -> Path:
    out = ROOT / "docs"
    shutil.rmtree(out, ignore_errors=True)
    (out / "posts").mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html"]),
    )
    env.globals["site"] = SITE

    posts = sorted(
        (load_post(p) for p in (ROOT / "posts").glob("*.md")),
        key=lambda p: p["date"],
        reverse=True,
    )

    # Posts: HTML page + verbatim markdown copy (AI consumability).
    for post in posts:
        page_dir = out / "posts" / post["slug"]
        page_dir.mkdir(parents=True)
        (page_dir / "index.html").write_text(
            env.get_template("post.html").render(post=post), encoding="utf-8"
        )
        (out / "posts" / f"{post['slug']}.md").write_text(
            post["markdown"], encoding="utf-8"
        )

    # Standalone pages (about, ...).
    for page_path in (ROOT / "pages").glob("*.md"):
        meta, body = parse_front_matter(page_path.read_text(encoding="utf-8"))
        page_dir = out / page_path.stem
        page_dir.mkdir(parents=True)
        (page_dir / "index.html").write_text(
            env.get_template("page.html").render(
                title=meta.get("title", page_path.stem),
                content=markdown.markdown(body, extensions=MD_EXTENSIONS),
            ),
            encoding="utf-8",
        )

    # Index.
    (out / "index.html").write_text(
        env.get_template("index.html").render(posts=posts), encoding="utf-8"
    )

    # Static assets.
    shutil.copytree(ROOT / "static", out / "static")

    # RSS 2.0 with full-text content.
    items = "\n".join(
        f"""  <item>
    <title>{escape(p["title"])}</title>
    <link>{p["url"]}</link>
    <guid>{p["url"]}</guid>
    <pubDate>{rfc822(p["date"])}</pubDate>
    <description>{escape(p["html"])}</description>
  </item>"""
        for p in posts
    )
    (out / "feed.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{escape(SITE["title"])}</title>
  <link>{SITE["url"]}</link>
  <description>{escape(SITE["description"])}</description>
{items}
</channel>
</rss>
""",
        encoding="utf-8",
    )

    # Sitemap.
    urls = [SITE["url"] + "/"] + [p["url"] for p in posts]
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
        + "\n</urlset>\n",
        encoding="utf-8",
    )

    # llms.txt: index for agents. llms-full.txt: complete content.
    (out / "llms.txt").write_text(
        f"# {SITE['title']}\n\n> {SITE['description']}\n\n## Posts\n\n"
        + "\n".join(
            f"- [{p['title']}]({SITE['url']}/posts/{p['slug']}.md): {p['description']}"
            for p in posts
        )
        + "\n",
        encoding="utf-8",
    )
    (out / "llms-full.txt").write_text(
        "\n\n---\n\n".join(
            f"# {p['title']}\n({p['date'].isoformat()}, {p['url']})\n\n{p['markdown']}"
            for p in posts
        )
        + "\n",
        encoding="utf-8",
    )

    (out / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n",
        encoding="utf-8",
    )

    # GitHub Pages plumbing: custom domain + no Jekyll processing.
    (out / "CNAME").write_text("consciousagency.io\n", encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")

    print(f"built {len(posts)} post(s) -> {out}")
    return out


if __name__ == "__main__":
    out = build()
    if "--serve" in sys.argv:
        import http.server

        print("serving on http://localhost:8000 (ctrl-c to stop)")
        http.server.test(
            HandlerClass=http.server.SimpleHTTPRequestHandler,
            port=8000,
            directory=str(out),
        )
