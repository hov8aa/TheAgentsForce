# Working in this repo

Read this before changing anything. Applies to humans and to AI assistants
operating through the GitHub API.

## build.py is the source of truth

These files are **generated output**. Never edit them directly:

- `index.html`
- `journal.html`
- `journal-agent-001.html`
- `thanks.html`
- `404.html`
- `sitemap.xml`
- `robots.txt`

They are produced by `build.py`. Editing them works until the next rebuild, then
the change disappears with no error.

`styles.css` is **hand-maintained** and is not generated. Edit it directly.

## The workflow

```
# 1. edit build.py (or styles.css)
# 2. regenerate
python build.py
# 3. commit the generator AND its output together
git add -A && git commit && git push
```

Any commit that changes generated HTML must also change `build.py` in the same
commit. If it doesn't, something has gone wrong.

## Where to make common changes

| To change | Edit |
|---|---|
| Header nav links | `NAV` |
| Header CTA button | `header()` |
| Hero copy and buttons | `HERO`, `page_index()` |
| Agent cards | `AGENTS` |
| Pricing, sprint steps | `PROCESS` |
| About copy | `ABOUT` |
| Journal post list | `POSTS` |
| Hire form fields, org ID | `SALESFORCE`, `hire_form()` |
| Hire section copy | `HIRE` |
| Anything in `styles.css` | `styles.css` directly, then bump `CSS_VERSION` |

Bump `CSS_VERSION` whenever `styles.css` changes, or the CDN will serve a stale
stylesheet against new markup.

## Why this file exists

On 2026-08-28, three commits (`9ec6015`, `33215f1`, `fcf09c8`) changed the header
CTA from "Work with me" to "Hire Me" across four HTML files in 114 seconds,
without touching `build.py`. The generator kept emitting the old labels for three
days. A rebuild would have reverted the change silently.

Nothing in the repo indicated that `build.py` was the source of truth, and nothing
checked afterwards. `.github/workflows/build-check.yml` now fails any push where
the generated files disagree with `build.py`. This file is the other half: the
rule stated where anyone working here will actually see it.

Note that commits made through the GitHub API are attributed to the repo owner
regardless of who or what authored them. The commit log cannot tell you whether a
change was made by a person or an assistant. Do not rely on it for that.
