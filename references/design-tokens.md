# Harvok Design Tokens (v0 · harvested from the live site, refined over time)

Every style reference must use the full triple `{hex, id, name}` — a bare hex breaks the link to the global palette.

## Global palette

| Name | id | hex | Use |
|---|---|---|---|
| Color #1 | `dcf36c` | `#f5f5f5` | Primary text on dark / H1 |
| Color #2 | `08a1c2` | `#e0e0e0` | Secondary text on dark, breadcrumbs |
| Color #3 | `012771` | `#9e9e9e` | Body / muted text on dark, empty stars |
| Color #4 | `44221f` | `#616161` | Dividers, dark grey fills |
| Color #5 | `674088` | `#424242` | Hover on dark, active tab fill |
| Color #6 | `2430ac` | `#212121` | Dark section background, primary text on light |
| Color #19 | `upmriy` | `#e60012` | Harvok red: eyebrows, stars, emphasis (use sparingly) |
| Color #20 | `zxmsxl` | `#eeeeee` | Light section background |
| Color #21 | `vzthfu` | `#000000` | Pure black text on light ⚠️ |
| Color #21 | `ilgpqi` | `#f5f5f5` | Light borders ⚠️ duplicate name — distinguish by id |
| Color #22 | `dadthx` | `#ffffff` | White text/fill ⚠️ duplicate of `oexyaf` (#ffffff, card fill) |
| Color #23 | `qzjihq` | `#ffffff` rgba(255,255,255,0) | Transparent (ghost button fill/border) |
| Color #25 | `nvcvug` | `#003061` | Deep blue: 48V/Power series sections only |

⚠️ The palette has historical duplicate names. Always reference by **id** — copy the exact form used in the component library.

## Typography

| Role | font-family | Spec |
|---|---|---|
| Eyebrow labels | Poppins | 14px / weight 300 / uppercase / Color #19 red |
| Display (names, numerals, feature titles) | Alumni Sans | 22–54px / weight 500–700 / line-height ~1 |
| Headings & body | theme default (omit font-family) | see type scale |

## Type scale (desktop → tablet_portrait → mobile_landscape → mobile_portrait)

| Level | Scale |
|---|---|
| H1 (banner) | 52 → 48 → 42 → 38 |
| Section heading (visual h3, tag h2/h3) | 42 → 38 → 34 → 32 |
| Excerpt display heading | 38 → 42 → 36 → 28 |
| Feature title (Alumni Sans) | 30 → – → – → 24 |
| Card title | 28 → – → 28 → 26 |
| Body | 14–16, line-height 1.8 |
| Eyebrow / meta | 13–14 |

## Layout & spacing system (mandatory, revised 2026-08-17)

**One rule**: vertical rhythm comes only from section padding and alternating backgrounds — **root sections must never use `_margin`**.
When assembling components from different sources, strip the component root's `_margin` first, then apply the uniform padding — otherwise you get "some sections have gaps, some don't".

- Every root section: `_padding {top:96, right:24, bottom:96, left:24}`; `:tablet_portrait {top:64,bottom:64}`; `:mobile_portrait {top:48,bottom:48,left:20,right:20}`
- Exceptions: hero (custom padding + `_heightMin`), narrow bands (fact strip 64, footnote bar 28)
- Content container is always `_width: 1400`
- Gap between a section's header block and its content: `_margin bottom 56` (on inner elements only, never the section itself)
- Alternate dark (`#212121`) and light (`#eeeeee`) sections, with white interleaved — never two identical backgrounds in a row
- Breakpoints use only the Bricks default keys: `tablet_portrait` / `mobile_landscape` / `mobile_portrait`, and every section must cover all three (font sizes, padding, widths, direction)

## Display mega-type mode (event/campaign pages)

Alumni Sans 700 + uppercase + line-height 0.95 as oversized display type is the campaign-page signature:
- Hero H1: 150 → 110 → 80 → 56
- Section headings: 64 → 52 → – → 40
- Numerals / times (run sheet times, fact-strip values): 44–52, red Color #19
- Emphasis words inside headings may use `<span style='color:#e60012'>` (copy-level emphasis only)

## Section header pattern

```
heading (tag h2, customTag div)  ← eyebrow: 14px uppercase Poppins red
heading (tag h3)                 ← main title 42px, brand word bold: <b>Harvok®</b>
text-basic (optional)            ← 14px intro, line-height 1.8
```

## Common interaction patterns

- **Ghost button**: transparent fill (Color #23) + 1px bottom border + themify `ti-arrow-right` icon + `_cssTransition: "0.3s all"`, border color swaps on hover
- **Card hover**: `_boxShadow:hover` 2/2/0/8 + `_cssTransition: "0.3s all"`
- **Slider**: `slider-nested` with `optionsType: custom` splide JSON (perPage 1, focus center, gap 40px, speed 400, arrows false, pagination true); pagination styling uses the `_cssCustom` shipped in the component library (the only approved `_cssCustom` use)
- **Video**: mp4 via media (autoplay/mute/loop/inline, objectFit cover), `themeStyles: {customPlayer: true}`
- **Background-image banner**: `_background` image + `_gradient` overlay (#212121 at 65% to darken for text contrast)

## Images

- Prefer existing site media via `search_media`; new uploads must include alt text
- Icon PNGs: height 64 (mobile 24), `_objectFit: contain`
- Loop data, three modes: JetEngine query builder (reviews = 41), post query (branch), inline `arrayEditor` array (first choice for campaign-scoped data — no CCT needed)
