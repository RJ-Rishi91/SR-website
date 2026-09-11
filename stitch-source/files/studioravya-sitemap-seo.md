# Studio Ravya — Site Architecture & SEO Map

This is the build spec for Antigravity — every route, its job in the funnel, its target keyword, and its metadata. Build to this before writing any page copy.

**Domain note:** this is currently a subdomain of your personal site (`studioravya.onerishi.in`). For a business you're actively pitching to clients, that's a credibility and SEO problem — a subdomain often gets treated as a separate, weaker property by Google, and a prospective client evaluating your web work will notice you didn't give your own business a real domain. Move this to its own domain (`studioravya.com`, `.in`, `.studio`, whatever's available) before you start driving traffic to it.

**Global nav:** Home · Services (dropdown) · Work · Process · Pricing · Blog · About · [Start a Project] (button, right-aligned, always visible)
**Footer:** Services list · Work · Blog · About · Privacy Policy · Terms · social links

---

## 1. Home — `/`
- **Funnel stage:** entry / brand
- **Target keyword:** brand name only ("Studio Ravya") — this page is for conversion, not acquisition
- **Title tag:** Studio Ravya — Website Design & Development Studio
- **Meta description:** Studio Ravya builds fast, custom websites and digital products for businesses and creators — from landing pages to full web apps. See our work and get a quote.
- **H1:** Websites and digital products, built to grow your business.
- **Primary CTA:** Start a Project → `/contact`
- **Links to:** Services, Work, Pricing, Contact

## 2. Services Hub — `/services`
- **Funnel stage:** TOFU/MOFU (acquisition + qualification)
- **Target keyword:** website design and development services
- **Title tag:** Web Design & Development Services | Studio Ravya
- **Meta description:** Explore Studio Ravya's website and web app services — design, development, e-commerce, landing pages, and custom builds. Get a quote for your project.
- **H1:** Services built around what your business actually needs
- **Primary CTA:** Get a Quote → `/contact`
- **Links to:** each service page, `/pricing`, `/contact`

## 3–7. Individual Service Pages
Each gets its own URL, H1, and keyword — never combine these.

| Page | URL | Target keyword | Title tag |
|---|---|---|---|
| Website Design & Development | `/services/website-design-development` | website design and development services | Website Design & Development Services \| Studio Ravya |
| Landing Pages / Campaign Sites | `/services/landing-pages` | landing page design service | Landing Page Design Services \| Studio Ravya |
| E-commerce Websites | `/services/ecommerce-websites` | ecommerce website development | Ecommerce Website Development \| Studio Ravya |
| Brand & Web Identity | `/services/brand-and-web-identity` | brand identity and website design | Brand & Web Identity Design \| Studio Ravya |
| Custom Web Apps / Tools | `/services/custom-web-apps` | custom web application development | Custom Web App Development \| Studio Ravya |

- **Meta description pattern:** [Service] built around [outcome] — from [step] through [step], designed to [benefit]. See our process and get a quote.
- **Each page links to:** 1–2 relevant case studies, `/pricing`, `/contact`, back to `/services`

## 8. Work Hub — `/work`
- **Target keyword:** web design portfolio / website development portfolio
- **Title tag:** Our Work | Studio Ravya Portfolio
- **Meta description:** See websites, web apps, and digital projects built by Studio Ravya — real projects, real outcomes.
- **H1:** Work we're proud of
- **Links to:** individual case studies, `/contact`

## 9. Individual Case Study Pages — `/work/[project-slug]`
- **Target keyword:** varies per project (e.g. "[industry] website design case study")
- **Structure:** problem → what was built → tools/tech used → outcome
- **Links to:** the relevant service page, `/contact`
- **Content source:** use real completed work — your DevFest Udaipur site/event work, Gazette Collective projects, and any client sites you've shipped. Don't fabricate client results; describe the work and real numbers only where you have them.

## 10. Process — `/process`
- **Target keyword:** web design process
- **Title tag:** Our Process | Studio Ravya
- **Meta description:** How a project with Studio Ravya actually works — from discovery to launch. See the steps, timeline, and what to expect.
- **H1:** How we build
- **Links to:** `/pricing`, `/contact`

## 11. Pricing — `/pricing`
- **Target keyword:** website design pricing
- **Title tag:** Website Design & Development Pricing | Studio Ravya
- **Meta description:** Transparent pricing for website design, development, and custom builds. See package ranges and what's included before you reach out.
- **H1:** Pricing built around scope, not guesswork
- **Links to:** `/contact`, `/faq`

## 12. About — `/about`
- **Target keyword:** Studio Ravya (brand) / web design studio about
- **Title tag:** About Studio Ravya
- **Meta description:** Studio Ravya is a web design and development studio built on clarity, craft, and the idea that technology should feel alive. Meet the studio.
- **H1:** About the studio
- **This is where the sun branding, philosophy, and voice live** — one page, not four.
- **Links to:** `/work`, `/contact`

## 13. Blog Hub — `/blog`
- **Target keyword:** web design blog / website tips
- **Title tag:** Blog | Studio Ravya — Web Design & Business Tips
- **Meta description:** Practical advice on websites, web design costs, and growing your business online — from the team at Studio Ravya.
- **H1:** Ideas on building a better web presence
- **Links to:** individual posts

## 14. Individual Blog Posts — `/blog/[post-slug]`
- **Target keyword:** varies per post — always a real buyer question ("how much does a website cost," "landing page vs website," "how long does a website take to build")
- **Every post links to:** the relevant service page + `/pricing` or `/contact`
- Sample post provided separately (see `studioravya-sample-blog-post.md`)

## 15. Contact / Start a Project — `/contact`
- **Target keyword:** hire a web designer / get a website quote
- **Title tag:** Start a Project | Studio Ravya
- **Meta description:** Tell us about your project and get a response within a few business days. Website design, development, and custom builds for growing businesses.
- **H1:** Let's build something that works
- **Form fields:** Name, Email, Project Type (dropdown), Budget Range (dropdown), Timeline, Message
- **On submit:** redirect to `/thank-you`

## 16. FAQ — `/faq`
- **Target keyword:** website design FAQ + long-tail question phrases
- **Title tag:** FAQ | Studio Ravya
- **H1:** Common questions
- Pull questions straight from what prospects actually ask before hiring — timeline, cost, revisions, ownership of code/design, hosting/maintenance after launch

## 17. Thank You — `/thank-you`
- **Not indexed** (`noindex` — this page has no reason to rank)
- **Title tag:** Thanks — We've Got Your Details
- **H1:** Thanks — we'll be in touch soon
- Use this page to fire your conversion tracking event

## 18. Privacy Policy — `/privacy-policy` and Terms — `/terms-of-service`
- Standard legal pages — required if you're collecting contact-form data or running ads/analytics. Low SEO priority, but their absence is a trust red flag on a real business site.

## 19. 404 — served automatically, not a nav item
- **Title tag:** Page Not Found
- Include nav back to Home, Services, and Contact so a broken link doesn't dead-end a visitor

---

## Internal linking rules (don't skip this)
- Every service page → 1–2 case studies + Pricing + Contact
- Every case study → its service page + Contact
- Every blog post → the service page it's most relevant to
- Pricing → Contact + FAQ
- Home → Services, Work, Pricing, Contact (not Ecosystem/Journal-style pages — cut)
