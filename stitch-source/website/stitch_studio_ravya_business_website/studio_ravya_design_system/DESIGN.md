---
name: Studio Ravya Design System
colors:
  surface: '#17130e'
  surface-dim: '#17130e'
  surface-bright: '#3e3833'
  surface-container-lowest: '#110d09'
  surface-container-low: '#1f1b16'
  surface-container: '#231f1a'
  surface-container-high: '#2e2924'
  surface-container-highest: '#39342f'
  on-surface: '#ebe1d9'
  on-surface-variant: '#d7c3ae'
  inverse-surface: '#ebe1d9'
  inverse-on-surface: '#352f2b'
  outline: '#9f8e7a'
  outline-variant: '#524534'
  surface-tint: '#ffb955'
  primary: '#ffc880'
  on-primary: '#452b00'
  primary-container: '#f5a623'
  on-primary-container: '#644000'
  inverse-primary: '#835500'
  secondary: '#ffb787'
  on-secondary: '#502400'
  secondary-container: '#e07312'
  on-secondary-container: '#461f00'
  tertiary: '#ffc5b1'
  on-tertiary: '#5c1900'
  tertiary-container: '#ff9d7b'
  on-tertiary-container: '#832800'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb4'
  primary-fixed-dim: '#ffb955'
  on-primary-fixed: '#291800'
  on-primary-fixed-variant: '#633f00'
  secondary-fixed: '#ffdcc7'
  secondary-fixed-dim: '#ffb787'
  on-secondary-fixed: '#311300'
  on-secondary-fixed-variant: '#723600'
  tertiary-fixed: '#ffdbcf'
  tertiary-fixed-dim: '#ffb59c'
  on-tertiary-fixed: '#390c00'
  on-tertiary-fixed-variant: '#822800'
  background: '#17130e'
  on-background: '#ebe1d9'
  surface-variant: '#39342f'
typography:
  display-xl:
    fontFamily: Newsreader
    fontSize: 72px
    fontWeight: '400'
    lineHeight: 80px
    letterSpacing: -0.02em
  display-xl-mobile:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: -0.01em
  display-lg:
    fontFamily: Newsreader
    fontSize: 56px
    fontWeight: '400'
    lineHeight: 64px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '500'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
    letterSpacing: 0em
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
    letterSpacing: 0em
  headline-sm:
    fontFamily: Newsreader
    fontSize: 22px
    fontWeight: '500'
    lineHeight: 30px
    letterSpacing: 0em
  body-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.04em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.12em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 4rem
  margin-mobile: 1.25rem
  space-xs: 0.375rem
  space-sm: 0.75rem
  space-md: 1.25rem
  space-lg: 2.25rem
  space-xl: 4rem
---

## Brand & Style

This design system embodies an editorial, high-craft digital boutique aesthetic combining deep nocturnal warmth with radiant luminescent solar accents. It targets visionary founders, high-growth enterprise leaders, and ambitious brand stewards seeking flagship-grade digital artifacts rather than commodity websites.

The visual style synthesizes **Refined Editorial Luxury** with **Subtle Luminous Skeuomorphism**:
- Deep obsidian and charcoal ground the experience, providing architectural weight and prestige.
- Solar glows, radiant aureoles, and metallic gold accents punctuate high-priority interactive touchpoints.
- Precision linework, razor-thin golden keylines, and celestial sun-ray motifs introduce mathematical exactness alongside organic warmth.
- The voice is commercial, authoritative, and obsessively refined, directing users purposefully toward partnership and conversion.

## Colors

The palette operates primarily in a dark tonal ecosystem with deliberate hot points of radiance:

- **Primary (`#F5A623`)**: Radiant Solar Gold. Reserved for primary conversion triggers, hero focal points, active states, and focal aureole glows.
- **Secondary (`#E8791A`)**: Warm Amber. Used for subtle linear gradients, hover accent variations, and secondary illustrative geometric lines.
- **Tertiary (`#C1440E`)**: Ember Red. Used strictly as an editorial accent for status badges, metric indicators, and limited-availability alerts.
- **Neutral Base (`#120E0A`)**: Midnight Charcoal. The deep, warm-tinted dark ground across all default surfaces.
- **Surface Elevation Layers**:
  - `surface-base`: `#120E0A`
  - `surface-card`: `#1B1510`
  - `surface-elevated`: `#241C15`
  - `surface-border`: `rgba(245, 166, 35, 0.15)`
  - `surface-border-hover`: `rgba(245, 166, 35, 0.45)`
- **Ivory Accent (`#FDF6EC`)**: High-contrast warm text and inverted editorial display cards, bringing high-end publication polish.

## Typography

The typographic hierarchy establishes tension between the classical editorial authority of **Newsreader** (featuring italic flourishes and sharp serifs reminiscent of boutique foundry type) and the hyper-precise, balanced geometry of **Plus Jakarta Sans**.

- Headlines leverage optical sizing and slight negative tracking at large formats to heighten dramatic impact.
- Body copy is set in Plus Jakarta Sans with generous line heights to preserve effortless readability against charcoal surfaces.
- Labels, badges, navigation links, and pricing metrics use all-caps or small-caps treatments in Plus Jakarta Sans with expanded letter-spacing (`0.04em` to `0.12em`) to evoke Swiss typographic precision.

## Layout & Spacing

This design system uses a strictly measured, responsive 12-column fluid grid system bounded by a maximum container width of `1380px`.

- **Desktop (1024px+)**: 12 columns, `1.5rem` gutters, `4rem` outer boundary margins. Editorial layouts prioritize dramatic asymmetry (e.g., 5-column narrative copy offset with 7-column media displays).
- **Tablet (768px - 1023px)**: 8 columns, `1.25rem` gutters, `2.5rem` outer canvas margins. Multi-column cards compress to 2 columns.
- **Mobile (Below 768px)**: 4 columns, `1rem` gutters, `1.25rem` canvas margins. Grid collapses to single-column stacking with edge-to-edge interactive previews.
- **Structural Rhythm**: Vertical pacing is open and architectural. Sections are separated by generous gaps (`space-xl` scaled dynamically up to `8rem` on ultra-wide viewports) coupled with thin geometric solar-ray line dividers.

## Elevation & Depth

Elevation does not rely on sterile gray dropshadows; depth is achieved through layered darkness, semi-opaque borders, and chromatic radiance:

- **Surface Tiers**: Base canvas sits at `#120E0A`. Resting cards step up to `#1B1510`. Floating navigation, tooltips, and elevated modals sit at `#241C15`.
- **Radiant Aureoles (Glows)**: Key call-to-action sections and hero typography sit directly atop soft radial gradients: `radial-gradient(circle at center, rgba(245, 166, 35, 0.12) 0%, rgba(232, 121, 26, 0.04) 45%, transparent 75%)`.
- **Low-Contrast Golden Filaments**: All elevated planes use a hairline border (`1px solid rgba(245, 166, 35, 0.14)`).
- **Interactive Depth (Card Hover)**: Upon hover, card surfaces shift their border to `rgba(245, 166, 35, 0.45)` and project a diffused amber-gold ambient backlight (`0 20px 48px -12px rgba(245, 166, 35, 0.15)`).
- **Glassmorphic Floating Chrome**: Sticky navigation utilizes `background: rgba(18, 14, 10, 0.78)` paired with `backdrop-filter: blur(16px)` and a subtle bottom divider of `1px solid rgba(245, 166, 35, 0.12)`.

## Shapes

The shape architecture harmonizes structured classical geometry with tactile modern curvatures. The base roundedness is `0.5rem` (Level 2):

- **Interactive Standard Controls**: Buttons, inputs, chips, and pills utilize standard rounded geometry (`0.5rem` to full pill `9999px` for chips and inline tags).
- **Content Cards & Containers**: Feature `rounded-lg` (`1rem`) to keep large surface blocks contemporary and softly framed against dark backgrounds.
- **Modals & Hero Showcases**: Feature `rounded-xl` (`1.5rem`) with razor-sharp 1px golden outline treatments.
- **Solar Motif Elements**: Sun-glyphs, status badges, and decorative solar-ray terminators maintain strict circular symmetry (`border-radius: 50%`).

## Components

### Buttons
- **Primary CTA ("Start a Project")**: High-impact solid Radiant Gold (`#F5A623`) background with dark obsidian text (`#120E0A`), font weight 600, roundedness of `0.5rem`, padded with `0.875rem 1.75rem`. Resting box-shadow: `0 4px 16px rgba(245, 166, 35, 0.25)`. Hover transition shifts tone toward warm Amber (`#E8791A`) with an intensified glow (`0 8px 24px rgba(245, 166, 35, 0.4)`).
- **Secondary / Ghost Button**: Semi-transparent dark background (`rgba(253, 246, 236, 0.04)`), `1px solid rgba(245, 166, 35, 0.3)` border, Warm Ivory text (`#FDF6EC`). On hover, the border becomes solid Radiant Gold with a subtle golden inner wash.

### Sticky Top Navigation
- Anchored to the viewport top, floating with `16px` backdrop blur over Midnight Charcoal.
- Features a solar emblem glyph (stylized geometric radiant sun) accompanied by the brand wordmark in Newsreader.
- Right-aligned menu contains concise uppercase navigation links (`label-md`) ending in a high-priority "Start a Project" pill button.

### Cards
- **Dark Tiered Cards**: `#1B1510` surface with `1px solid rgba(245, 166, 35, 0.15)` border and `1rem` radius. Subtle inner highlight on top edge (`inset 0 1px 0 rgba(253, 246, 236, 0.08)`).
- **Inverted Ivory Feature Cards**: Background in `#FDF6EC` paired with `#120E0A` text, offering tactile editorial contrast for client case studies, featured quotes, or flagship deliverables.

### Badge Tags & Chips
- Fully radiused pills (`rounded-full`) with `label-sm` uppercase text.
- Standard Chip: Dark translucent amber fill (`rgba(245, 166, 35, 0.1)`), border `1px solid rgba(245, 166, 35, 0.25)`, text `#F5A623`.
- Ember Alert Badge: Ember-red fill (`rgba(193, 68, 14, 0.15)`), border `1px solid rgba(193, 68, 14, 0.4)`, text `#FDF6EC`, indicating studio project availability.

### Form Inputs
- Background `#18120D`, `1px solid rgba(253, 246, 236, 0.12)`, text `#FDF6EC`, placeholder `rgba(253, 246, 236, 0.35)`.
- Focused state: Border transitions to `#F5A623` with a focused ring shadow of `0 0 0 3px rgba(245, 166, 35, 0.18)`.

### Trust-Signal Strips & Metrics
- Horizontal row layouts segmented by geometric solar-ray line dividers (`1px solid rgba(245, 166, 35, 0.15)` with centered diamond or sun markers).
- Metrics display oversized Newsreader numbers with gold gradient accents, paired with muted Plus Jakarta Sans descriptions.

### Structured Footer
- 4-column layout against base surface `#120E0A` bounded by a top solar-ray keyline.
- Columns: Brand ethos & office time zones, Services & Solutions, Insights/Case Studies, and direct Contact/Project Start form.