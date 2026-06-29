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

## TODO — Play Store goes live

When the app is published on Google Play, update `index.html` (around line 390):

1. `class="btn btn-lg btn-muted"` → `class="btn btn-lg btn-gold"`
2. `href="#"` → `href="https://play.google.com/store/apps/details?id=com.alfred.kitabalhuda"`
3. Badge text: `📱 قيد النشر` → `📱 متاح على Google Play`
4. Caption text: `سيتم النشر قريباً في المتجر` → `متوفر الآن على Google Play`
