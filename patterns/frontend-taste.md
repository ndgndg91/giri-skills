# Frontend Taste & Anti-Slop Design Principles

Core design principles distilled from curated art-directed web standards (e.g., Awwwards, One Page Love). Eliminates generic AI-generated frontend templates ("AI slop") and enforces distinct, substance-driven interfaces.

---

## 1. Core Philosophy: Substance Over Avoidance
- **Never Settle for Default AI Aesthetics**: Eliminate predictable layout recipes (e.g., centered hero, 3 identical cards, violet gradients).
- **Substance Over Restraint**: Removing ornaments (drop shadows, pill badges) is only half the job. Replace them with **substance**:
  - Deliberate, high-contrast typography hierarchy (large display type vs. readable body).
  - Intentional fields of color and solid ink rather than ambient blurs and gradients.
  - Authentic, subject-derived imagery or real working UI fragments instead of placeholder graphics or stock icons.

---

## 2. Banned Registry (AI Tells)

Strictly avoid the following repetitive generation tropes:

| Category | Banned AI Trope | Required Alternative |
| :--- | :--- | :--- |
| **Colors & Lighting** | Violet/indigo/cyan glows, ambient gradients, gradient text | Solid ink, flat palette, high-contrast tone stepping |
| **Surfaces** | Glassmorphism, backdrop-blur floating panels, soft blurry drop shadows | Opaque surfaces, 1-tone ground offsets, crisp borders |
| **Decorations** | Pill badges above titles (`New`, `Beta`, `Introducing`), status dots (`pulsing green dot`) | State facts directly in supporting prose; remove vanity dots |
| **Micro-labels** | Eyebrow/kicker tracked uppercase labels above headings, monospace micro-meta | Fold into the heading text or delete entirely |
| **Grid & Cards** | Row of 3 identical feature cards with rounded square icons; generic bento-grid filler | Argument-driven asymmetric layouts, varied section blueprints |
| **Recent Clichés** | Yellow-cream background + terracotta/rust accents (the 2025-2026 "editorial fix" slop) | Palettes derived strictly from the subject's domain and materials |
| **Ornaments** | Faux design-tool chrome (crosshairs `+`, crop marks, hairline grids, index numbers `01/02`) | Structure built strictly from white space and tonal boundaries |

---

## 3. Page vs. App Screen Separation

Treat marketing pages and working application screens with distinct rules:

### 3.1 Public Pages (Landing, Marketing, Portfolio)
- **Scrolled & Read**: Driven by an editorial argument, strong narrative flow, and brand voice.
- **Section Order**: Never follow the stock formula (`Hero → Logos → 3 Features → Testimonial → Pricing → CTA`). Order sections strictly by the logical claims of the product.
- **Embedded App Previews**: If showcasing the product, embed **real working UI fragments** (real tables, realistic data, true CSS components) — never wireframe grey bars or fake donut charts.

### 3.2 App Screens (Dashboards, Admin, Settings, Workspaces)
- **Worked In**: High information density, quiet functional borders, immediate utility.
- **Rules**:
  - No decorative gradients, glowing buttons, or rainbow metric charts.
  - Consistent layout grids, tabular figures (`font-variant-numeric: tabular-nums`) for data alignment.
  - Action-oriented button labeling (e.g., "Create Workspace", "Export CSV" instead of "Get Started").

---

## 4. Execution Workflow

When building or reviewing any web interface:

1. **Inventory the Subject**: Extract 8–12 concrete realities unique to this domain (domain terms, constraints, real numbers, materials, rituals). Design derives from these realities.
2. **Write the Argument**: List sections as claims + proofs. Any section without a distinct claim must be deleted.
3. **Type & Color Hierarchy**:
   - Limit to **3–5 distinct font sizes** spaced far apart (e.g., Display 48–64px, Title 24–32px, Body 15–16px, Caption 13px).
   - Anchor with left-aligned structures; reserve centered text only for single focal moments.
4. **Inspect & Verify**:
   - Verify responsive behavior across Mobile (375px), Tablet (768px), and Desktop (1280px+).
   - Check against the Banned Registry before finalizing.
