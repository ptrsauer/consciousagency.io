#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["markdown", "jinja2"]
# ///
"""Sanity checks on the generated site. Run after build.py."""

from pathlib import Path

from build import build

out = build()
posts = sorted((Path(__file__).parent / "posts").glob("*.md"))

checks = {
    "index exists": (out / "index.html").exists(),
    "feed exists and is rss": (out / "feed.xml").read_text().startswith('<?xml'),
    "sitemap exists": (out / "sitemap.xml").exists(),
    "llms.txt exists": (out / "llms.txt").exists(),
    "llms-full.txt exists": (out / "llms-full.txt").exists(),
    "robots.txt exists": (out / "robots.txt").exists(),
    "CNAME pins domain": (out / "CNAME").read_text().strip() == "consciousagency.io",
    ".nojekyll present": (out / ".nojekyll").exists(),
    "css copied": (out / "static" / "style.css").exists(),
    "about page built": (out / "about" / "index.html").exists(),
}

# One HTML page + one markdown copy per post.
for p in posts:
    slug = p.stem[11:]  # strip YYYY-MM-DD-
    checks[f"post html: {slug}"] = (out / "posts" / slug / "index.html").exists()
    checks[f"post md copy: {slug}"] = (out / "posts" / f"{slug}.md").exists()

# Every post appears in feed, llms.txt and index.
index_html = (out / "index.html").read_text()
feed = (out / "feed.xml").read_text()
llms = (out / "llms.txt").read_text()
for p in posts:
    slug = p.stem[11:]
    checks[f"{slug} in index"] = slug in index_html
    checks[f"{slug} in feed"] = slug in feed
    checks[f"{slug} in llms.txt"] = f"{slug}.md" in llms

# efficient-web budget: no page heavier than 50 KB, zero <script src=...>.
for html in out.rglob("*.html"):
    kb = html.stat().st_size / 1024
    checks[f"{html.relative_to(out)} < 50 KB ({kb:.1f})"] = kb < 50
    checks[f"{html.relative_to(out)} has no external js"] = "<script src" not in html.read_text()

failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL"), name)
print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed")
raise SystemExit(1 if failed else 0)
