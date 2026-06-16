# Kitab al-Huda Site — AGENTS.md

Static landing page for **kitab-al-huda.github.io** (GitHub Pages).

## Quick facts

- **No build system** — pure HTML/CSS/JS, no package.json, no bundler
- All JS is inlined in `<script>` tags in `index.html`
- CSS in `assets/style.css`
- Only two real pages: `index.html` (RTL Arabic) and `privacy.html`
- Screenshots in `assets/screenshots/` (update via `scripts/generate-screenshots.py`)
- Sitemap: `sitemap.xml` — update when adding/removing pages

## Development

Open `index.html` directly in a browser — no server needed.
