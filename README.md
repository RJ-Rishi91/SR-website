# Studio Ravya — Web Design & Digital Product Studio

> Websites and digital products, built to grow your business.

Studio Ravya is a bespoke digital product and web engineering studio platform. Built with **Astro 4**, **Tailwind CSS**, and a **Python FastAPI** backend for dispatches and client lead acquisition.

---

## 🏛 Architecture

- **Frontend:** [Astro 4.16+](https://astro.build) (Static Site Generation for GitHub Pages)
- **Styling:** [Tailwind CSS](https://tailwindcss.com) with bespoke Nocturnal Solar luxury design tokens
- **Typography:** *Newsreader* (editorial serif headlines) + *Plus Jakarta Sans* (high-precision sans UI)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com) + SQLite (`studioravya.db`) running on `localhost:8000`
- **CMS Suite:** Dedicated in-browser admin portal at `/admin` for editorial publishing, markdown editing, post scheduling, image uploads, and client inquiry review
- **Deployment:** GitHub Pages via `.github/workflows/deploy.yml`

---

## 🚀 Quick Start

### 1. Frontend Development

```bash
# Start Astro dev server (default http://localhost:4321)
npm run dev

# Build production static site (output to ./dist)
npm run build

# Preview static build locally
npm run preview
```

### 2. Backend Server (Localhost)

```bash
# Launch the FastAPI backend on http://localhost:8000
./start_backend.sh

# Or run manually with python:
cd backend
source venv/bin/activate
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🌐 Site Structure & Funnel Map

| Route | Page Name | Purpose |
|---|---|---|
| `/` | **Home** | Brand entry, hero aura, 5-service bento grid, case studies, process teaser, conversion CTA |
| `/services` | **Services Hub** | Capability roster & decision alignment matrix ("Which service fits your situation") |
| `/services/website-design-development` | **Service Page** | Flagship website design, deliverables, speed benchmarks, service FAQ |
| `/services/landing-pages` | **Service Page** | High-velocity campaign and product launch pages |
| `/services/ecommerce-websites` | **Service Page** | Custom digital storefronts and lookbook shopping flows |
| `/services/brand-and-web-identity` | **Service Page** | Visual systems, typography scales, chromatic tokens |
| `/services/custom-web-apps` | **Service Page** | Full-stack web software, portals, dashboards & tools |
| `/work` | **Work Hub** | Showcase portfolio of shipped digital flagships |
| `/work/[slug]` | **Case Study Detail** | In-depth case study template (The Challenge, What We Built, Tech Stack, Metrics) |
| `/process` | **Process** | 5-phase delivery framework, milestones, client collaboration inputs |
| `/pricing` | **Pricing** | Scope-based packages ($3K–$15K+), cost drivers breakdown, pricing FAQ |
| `/about` | **About** | Studio manifesto, solar brand heritage, craftsmanship standards |
| `/blog` | **Blog Hub** | Actionable essays on web pricing, conversion design, and technology |
| `/blog/[slug]` | **Article Detail** | Long-form reading layout with live reading progress bar |
| `/contact` | **Start a Project** | Bespoke scoping form connecting to backend API |
| `/faq` | **FAQ** | Comprehensive client questions on contracts, code ownership, and warranties |
| `/thank-you` | **Thank You** | Post-inquiry confirmation screen with next-steps timeline |
| `/privacy-policy` | **Privacy Policy** | Data protection and mutual NDA terms |
| `/terms-of-service` | **Terms of Service** | Commercial terms and 100% intellectual property ownership |
| `/404` | **404 Orbit** | Custom solar orbit error page |
| `/rss.xml` | **RSS Feed** | Automated RSS feed for insights |
| `/sitemap.xml` | **XML Sitemap** | Full SEO sitemap |

---

## 🔐 Admin CMS Portal (`/admin`)

Access the management console at `http://localhost:4321/admin`:

- **Master Password:** `studioravya2026` (configurable in `backend/.env`)
- **Dispatches Dashboard (`/admin/posts`):** View all drafts, scheduled posts, and live articles with search and category filtering.
- **Markdown Editor (`/admin/editor`):** Dual-pane editor with live rendered preview, word counter, image uploader, and date scheduler.
- **Client Inquiries (`/admin/inquiries`):** Inspect leads captured through `/contact` with project type, budget, timeline, and 1-click mailto reply.
- **Calendar (`/admin/calendar`):** Visual schedule of publishing velocity.
- **Settings (`/admin/settings`):** Backend health monitor and GitHub rebuild webhook status.

---

## 📦 GitHub Pages Deployment

The repository includes `.github/workflows/deploy.yml`:
1. Push your repository to GitHub (`main` branch).
2. Go to repository **Settings** → **Pages** → Source: **GitHub Actions**.
3. Every push to `main` automatically compiles Astro into static HTML and deploys to GitHub Pages.
