# Design System (shared by AI agents)

Goal: Claude Code, Codex, Antigravity (agy) and Grok Build produce the same-looking UI from the same request.

Status (2026-11-23): **foundation tokens decided** (color, type, spacing, radius, surfaces). Components, page templates, decision tables and the verification script are not written yet.

Taste rules (what to avoid and why) live in `patterns/frontend-taste.md`. This folder fixes the concrete values.

## Files
| File | Role |
| :--- | :--- |
| `tokens.json` | Source of truth (W3C Design Tokens format). Edit only this file. |
| `tokens.css` | CSS variables generated from `tokens.json`. Do not edit by hand. |
| `build_tokens.py` | `python3 design/build_tokens.py` regenerates `tokens.css`. `--check` exits 1 if it is stale. Standard library only. |

## Using the tokens
1. Load fonts with the stylesheet link printed at the top of `tokens.css` (Google Fonts).
2. Include `tokens.css`: link it, or paste its contents into a single-file HTML page.
3. Use only `var(--...)` tokens for color, font, spacing, radius and shadow. No raw hex, rgba or px values outside `tokens.json`.
4. Typography: `font: var(--text-h1); letter-spacing: var(--text-h1-letter-spacing);`
5. Theme: light by default. Dark follows `prefers-color-scheme`. `data-theme="light"` or `data-theme="dark"` on `<html>` overrides it.

## Decisions

### Color
- Neutrals: light = graphite (cool gray), dark = slate (blue gray).
- One accent, cobalt. Use it only for primary buttons, links, selected state, chart marks and focus rings. Everything else stays neutral.
- Success, warning and danger colors mark status only. Never use them as decoration or accent.
- `text-disabled` is for disabled controls only (contrast 3:1).
- Contrast (WCAG 2.x, computed from `tokens.json` on 2026-11-23): every readable text pair is at least 4.5:1. Lowest: light `accent-text` 4.7:1, light `success-text` and `warning-text` 5.0:1.
- Dark-mode primary button is a light blue fill with dark text, because white text on the dark-mode accent is below 4.5:1.

### Typography
- Body: Inter (Latin and digits) with Noto Sans KR (Hangul). Mono: JetBrains Mono for code, logs and IDs.
- Scale (px): display 36, h1 28, h2 22, h3 18, body 16, small 14, caption 13.
- Numbers in tables and KPI values use `font-variant-numeric: tabular-nums`.
- JetBrains Mono has no Hangul, so log lines that mix Korean will not align. Accepted.

### Spacing (comfortable density)
- Only the 4px scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64.
- Roles: card padding 24, gap between elements 20, gap between sections 48, gap between buttons 12, table cell 16 x 20, control height 40, page padding 40.

### Radius
- Buttons and inputs 6, cards 8, floating layers 12, badges fully rounded.

### Surfaces
- Cards are separated from the page by background color only: no border, no shadow.
- Exceptions:
  - Inputs and secondary buttons keep a `border-strong` outline.
  - Table rows keep `border` dividers.
  - Floating layers (menus, popovers, dialogs) use `border` and `shadow-overlay`.

## Open conflicts with `patterns/frontend-taste.md` (decide before components)
1. The type scale has 7 sizes. frontend-taste section 4 says 3 to 5 sizes.
2. `shadow-overlay` is a soft blurred shadow. frontend-taste section 2 bans soft blurry drop shadows.
3. `radius-badge` is fully rounded, and the comparison pages drew a dot inside status badges. frontend-taste section 2 bans pill badges above titles and decorative status dots. Whether status badges inside tables are allowed is not decided.
4. The comparison pages put a small label above the page title. frontend-taste section 2 bans eyebrow labels. Templates must not copy it.

## Not done yet
- Components with states: button, input, select, tabs, table, badge, alert, card, menu, empty state.
- Page templates: report, dashboard, form.
- Decision table (which component when) and banned list for agents.
- Verification script: raw values, unknown classes, contrast.
- `SKILL.md` and wiring into each agent's instruction file (Claude Code, Codex, agy, Grok Build).
