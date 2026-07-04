# consciousagency.io

Source for [consciousagency.io](https://consciousagency.io) — research, experiments, and reflections by Peter Sauer.

Built with a deliberately minimal static site generator: [`build.py`](build.py), ~200 lines of Python, two dependencies (`markdown`, `jinja2`). No framework, no npm, nothing that needs updating next year. The generated site ships zero JavaScript.

## How it works

```
posts/YYYY-MM-DD-slug.md   →  docs/posts/slug/index.html  (+ verbatim .md copy)
pages/about.md             →  docs/about/index.html
templates/*.html           →  Jinja2 layouts
static/                    →  copied as-is
```

`docs/` is committed and served directly by GitHub Pages (deploy from branch, no CI).

Every build also produces, as first-class outputs for AI agents: `llms.txt`, `llms-full.txt`, full-text `feed.xml`, `sitemap.xml`, and a raw markdown copy of every post next to its HTML.

## Publish workflow

```bash
./build.py            # rebuild docs/
./build.py --serve    # preview on localhost:8000
./test_build.py       # sanity checks on the output
git add -A && git commit -m "post: <title>" && git push   # = publish
```

Drafts live outside this repo until they are ready (and in `drafts/`, which the build ignores).

Note: GitHub Pages serves with `Cache-Control: max-age=600`, so a pushed change can take up to 10 minutes to appear for a URL you visited recently. A hard reload on that URL bypasses it.

## Domain setup (Cloudflare)

DNS for the apex domain points at GitHub Pages:

```
A  consciousagency.io  185.199.108.153   (DNS only, no proxy)
A  consciousagency.io  185.199.109.153
A  consciousagency.io  185.199.110.153
A  consciousagency.io  185.199.111.153
```

`docs/CNAME` pins the custom domain; HTTPS is provisioned by GitHub after DNS resolves.
