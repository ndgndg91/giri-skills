# Design System (shared by AI agents)

Goal: Claude Code, Codex, Antigravity (agy) and Grok Build produce the same-looking UI from the same request.

Status (2026-11-23): **foundations decided** (color, chart colors, type, spacing, radius, surfaces, icons, number and date formats). Components, page templates, decision tables and the verification script are not written yet.

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
4. Typography: `font: var(--text-h1); letter-spacing: var(--text-h1-letter-spacing);` Roles: `display`, `h1`, `h2`, `body`, `small`.
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
- Scale, 5 sizes (px): display 36 (KPI numbers), h1 24 (page title), h2 18 (section title), body 16, small 14 (tables, buttons, inputs, labels, timestamps). Do not add sizes.
- `font-variant-numeric: tabular-nums` only where digits line up vertically: table columns and chart axes. Large standalone values (KPI numbers) keep the default proportional figures.
- Monospace only for real data values: IDs, hashes, code, logs. Never for decorative meta labels.
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
  - Floating layers (menus, popovers, dialogs) use `border` and `shadow-overlay`. This is the only place a shadow is allowed.

### Charts
- Categorical palette, 8 slots in fixed order: 1 cobalt, 2 orange, 3 aqua, 4 yellow, 5 pink, 6 green, 7 violet, 8 red (`--color-chart-1` to `--color-chart-8`). Light mode uses the vivid steps, dark mode the muted steps of the same hues.
- One series: slot 1 only, no legend (the title says what is plotted).
- Two or more series: assign from slot 1 in order. Never skip or cycle. The same entity keeps the same slot in every chart on the page, and a filter never repaints the remaining series.
- More than 8 series: fold the rest into "기타". Scatter, bubble and map charts: at most 3 series.
- Every chart ships a table view (for example `<details>표로 보기</details>`). Light slots 3 to 5 are below 3:1 on white, so the table is required, not optional.
- Legend for two or more series. Text (values, names, axes) uses text tokens, never a series color.
- Status meaning (good, warning, error) uses the status colors, never chart colors, and the two are never mixed in one chart.
- Marks: bars at most 24px thick with a 4px rounded end and a square baseline; lines 2px; end dots at least 8px with a 2px surface ring; 2px surface gap between stacked segments; 1px solid gridlines in `border`.
- Validation (dataviz `validate_palette.js`, 2026-11-23): light on `#FFFFFF` worst adjacent CVD 9.1, normal vision 19.6, slots 3 to 5 below 3:1 (2.82, 2.17, 2.69). Dark on `#111A2B` worst adjacent CVD 8.5, normal vision 16.8, all at least 3:1. First 3 slots pass all-pairs in both modes; 4 slots fail.

### Icons
- Set: Lucide (lucide-static 1.70.0, ISC; license in `icons/LICENSE-lucide.txt`). Only the 17 files in `design/icons/`. No other icon set, no emoji, no hand-drawn SVG icons.
- Use them for function only: inside buttons, inputs, table headers, menus, alerts, pagination and dialog close. Never as decoration next to headings or on feature cards.
- Paste the SVG inline. Size with CSS: `size-icon-sm` (16px) inside buttons, inputs, tables and menus; `size-icon-md` (20px) in alerts and dialog close buttons. Color follows text (`currentColor`).
- Decorative icons next to a text label get `aria-hidden="true"`. An icon-only button needs `aria-label`.
- Need another icon: take it from lucide-static 1.70.0 (`icons/<name>.svg`), keep only drawing elements, add it here first.

| File | Lucide name | Use |
| :--- | :--- | :--- |
| `search` | search | search input |
| `chevron-down` / `chevron-left` / `chevron-right` | chevron-* | select, pagination |
| `close` | x | close dialog, clear |
| `check` | check | selected item |
| `plus` | plus | add |
| `download` | download | export, download |
| `external` | external-link | open in new tab |
| `copy` | copy | copy |
| `refresh` | refresh-cw | reload |
| `filter` | funnel | filter |
| `sort` | arrow-up-down | sortable column |
| `warning` | triangle-alert | warning alert |
| `info` | info | info note |
| `calendar` | calendar | date range |
| `more` | ellipsis | row actions |

### Numbers, dates and empty values
| Item | Rule | Example |
| :--- | :--- | :--- |
| Thousands | Comma from 1,000. Not for years, IDs, port numbers or codes | `1,284,330` / `2026` / `8080` |
| Decimals | Fixed per column or per metric | `0.12%`, `0.30%` |
| Units | Space before Latin units. No space before `%`, `%p` and Korean units. Particles attach to the unit | `182 ms`, `1.2 GB` / `0.12%`, `1,284건` / `182 ms로`, `0.12%입니다` |
| Change | Always signed. Minus is `−` (U+2212) in displayed text; machine-readable output (CSV, JSON) keeps `-` | `+4.2%`, `−6 ms`, `+0.03%p` |
| Large numbers | Full number in KPI tiles and tables. Compact `k` / `M` only on chart axes and narrow cells | `1,284,330` / `200k`, `1.28M` |
| Date and time (data) | `YYYY-MM-DD HH:mm`, 24-hour, year always shown. Seconds only when needed | `2026-11-22 16:05`, log `16:05:09` |
| Range | Spaces around `~` | `2026-11-16 ~ 2026-11-22` |
| Date in sentences and titles | Korean form | `11월 16~22일 서비스 상태` |
| Time zone | KST is implied. Show the zone only when zones are mixed | `14:05 UTC` |
| Relative time | Never alone; pair it with the absolute time | `3분 전 (14:05)` |
| Empty value | `-` in `text-muted`. Zero is a value: show `0` | `-` / `0` |
| Unavailable value | Say why, in `text-muted` | `확인 불가`, `집계 중` |

### Badges and titles
- Status badges (success, warning, danger) appear only inside tables and lists: pill background (`radius-badge`) with text only. No dot, no icon.
- Never place a badge or a small label above a title. Put the context into the title itself, for example "11월 16~22일 서비스 상태".

## Conflicts with `patterns/frontend-taste.md` (resolved 2026-11-23)
| # | Conflict | Decision |
| :--- | :--- | :--- |
| 1 | Type scale had 7 sizes; frontend-taste section 4 allows 3 to 5 | Reduced to 5: 36 / 24 / 18 / 16 / 14 |
| 2 | `shadow-overlay` is a soft shadow; section 2 bans soft blurry drop shadows | Allowed for floating layers only (added as an exception in frontend-taste) |
| 3 | Pill status badges with a dot; section 2 bans pill badges above titles and status dots | Pill background kept for status in tables and lists, dot removed, no badges above titles (exception added) |
| 4 | Comparison pages used a small label above the page title; section 2 bans eyebrow labels | No label above titles; context goes into the title. Monospace stays for real data values (exception added) |

## Not done yet
- Components with states: button, input, select, tabs, table, badge, alert, card, menu, empty state.
- Page templates: report, dashboard, form.
- Decision table (which component when) and banned list for agents.
- Verification script: raw values, unknown classes, contrast.
- `SKILL.md` and wiring into each agent's instruction file (Claude Code, Codex, agy, Grok Build).
