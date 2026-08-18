# Harvok Design Tokens

Harvested from the live site. These are values, not suggestions — `frontend-design` decides composition, this file decides what goes in it.

Every style reference must use the full triple `{hex, id, name}`; a bare hex breaks the link to the global palette. The palette has historical duplicate names, so always match by **id**, copied exactly from the component library.

## Global palette

| Name | id | hex | Use |
|---|---|---|---|
| Color #1 | `dcf36c` | `#f5f5f5` | Primary text on dark / H1 |
| Color #2 | `08a1c2` | `#e0e0e0` | Secondary text on dark, breadcrumbs |
| Color #3 | `012771` | `#9e9e9e` | Muted text **on dark only**, empty stars |
| Color #4 | `44221f` | `#616161` | Body text on light, dividers |
| Color #5 | `674088` | `#424242` | Text on light, hover on dark, active tab fill |
| Color #6 | `2430ac` | `#212121` | Dark section background, primary text on light |
| Color #19 | `upmriy` | `#e60012` | Harvok red — accent, see contrast rules |
| Color #20 | `zxmsxl` | `#eeeeee` | Light section background |
| Color #21 | `vzthfu` | `#000000` | Pure black text on light |
| Color #21 | `ilgpqi` | `#f5f5f5` | Light borders (duplicate name — check the id) |
| Color #22 | `dadthx` | `#ffffff` | White text/fill (duplicate of `oexyaf`, card fill) |
| Color #23 | `qzjihq` | `#ffffff` rgba(255,255,255,0) | Transparent (ghost button fill/border) |
| Color #25 | `nvcvug` | `#003061` | Deep blue — 48V / Power series sections only |

## Contrast rules (mandatory check, WCAG 2.1)

Measured ratios for this palette. **Text must reach 4.5:1**, except type ≥24px (or ≥19px bold), which needs 3:1.

| Text ↓ / Background → | `#212121` dark | `#eeeeee` light | `#ffffff` white | `#003061` blue |
|---|---|---|---|---|
| `#f5f5f5` Color #1 | **14.8** | 1.1 ✗ | 1.1 ✗ | **12.1** |
| `#e0e0e0` Color #2 | **12.2** | 1.1 ✗ | 1.3 ✗ | **10.0** |
| `#9e9e9e` Color #3 | **6.0** | 2.3 ✗ | 2.7 ✗ | 4.9 |
| `#616161` Color #4 | 2.6 ✗ | **5.3** | **6.2** | 2.1 ✗ |
| `#424242` Color #5 | 1.6 ✗ | **8.7** | **10.1** | 1.3 ✗ |
| `#212121` Color #6 | — | **13.9** | **16.1** | 1.2 ✗ |
| `#e60012` red | 3.4 ⚠ | 4.1 ⚠ | **4.8** | 2.7 ✗ |
| `#ffffff` Color #22 | **16.1** | 1.2 ✗ | — | **13.2** |

Reading it: **bold** = safe at any size, plain number ≥3 = large text only, ✗ = never.

Four rules follow from the table:

- **Red is not a body-text color.** On dark it is 3.4 and on light grey 4.1 — both fail at 14px. Red text is allowed only at ≥24px display sizes, or on white (4.8).
- **The 14px red eyebrow only works on white.** On a dark or light-grey section, set eyebrows in Color #2 `#e0e0e0` (on dark) or Color #4 `#616161` (on light), and carry the brand accent with a short red rule or underline instead — a non-text element has no contrast floor.
- **`#9e9e9e` is a dark-background color.** On `#eeeeee` it reads at 2.3 and effectively disappears. Muted text on light sections is Color #4 `#616161`.
- **Text over a photo needs a `_gradient` scrim** — `#212121` at ≥65%, and measure the ratio against the darkened result, not the raw image. On a bright photo, 65% over the brightest 5% of the crop still cleared 5:1 for `#e0e0e0`, so treat 65% as the floor and go darker where the text is small.

## Typography

| Role | font-family | Spec |
|---|---|---|
| Eyebrow labels | Poppins | 14px / weight 300 / uppercase (colour per the contrast rules) |
| Display — headings, names, numerals | Alumni Sans | weight 600–700, uppercase; sizes and line-heights from the scale below |
| Body and anything else | theme default (omit `font-family`) | 16 / line-height 1.8 |

### Type scale (desktop → tablet_portrait → mobile_landscape → mobile_portrait)

Two scales, and which one applies depends on where the section came from — not on taste.

**Campaign display scale — the default for anything you build yourself.** Alumni Sans 700 + uppercase + line-height 0.95 as oversized display type is the campaign-page signature.

| Level | Scale |
|---|---|
| Hero H1 | 150 → 110 → 80 → 56 |
| Section heading | 64 → 52 → – → 40 |
| Feature / row title (Alumni Sans 600) | 30 → – → – → 24 |
| Numerals and times (run sheet, fact strip) | 52–76, line-height ~0.85 |
| Body | 16, line-height 1.8 |
| Eyebrow / meta | 13–14 |

Numerals at this size clear the 3:1 large-text floor, so red Color #19 is safe on them — it is the one place red carries real weight. Emphasis words inside a heading may use `<span style='color:#e60012'>`.

**Component scale — what the shipped components already use.** Leave these alone when you drop a component in; matching them by hand in a self-built section is what makes the page look half-migrated.

| Level | Scale | Where |
|---|---|---|
| H1 | 52 → 48 → 42 → 38 | `campaign-banner.json` |
| Excerpt display heading | 38 → 42 → 36 → 28 | `excerpt-section.json`, `offer-intro.json` |
| Card title | 28 → – → 28 → 26 | `card-grid.json`, `social-proof-loop.json` |

## Layout — three levels, measured off the live site

Sections on harvok.com.au are **not full-bleed**. Every coloured block sits in a 20px frame, with the page ground (`#f5f5f5`, set on `html`) showing through at the left and right edges. Getting this wrong is what makes a generated page read as "not our site" even when the copy and colours are right.

Bricks gives `.brxe-section` no padding of its own and caps every element at `max-width:100%`, so nothing here happens by default — build all three levels:

```
section        _padding { left:20, right:20 }           ← the frame. No background, no vertical padding.
  container    _width:100% + the background
               _padding { top:96, right:60, bottom:96, left:60 }
    container  _width:1400                              ← centres only past a 1560 viewport
```

**The panel carries all the padding** — vertical and horizontal. The section is nothing but the frame. Splitting padding across both levels is what produces "some sections have gaps, some don't".

Panel vertical padding: `96` → `:tablet_portrait 64` → `:mobile_portrait 48`. Narrow bands override it (fact strip 64, footnote bar 28); a hero sets its own plus `_heightMin`.

Measured on campaign 3951, distance from the viewport edge:

| Viewport | Panel edge | Text |
|---|---|---|
| 1650 | 20 | 125 |
| 1425 | 20 | 80 |
| 1185 | 20 | 80 |
| 976 | 20 | 80 |
| 752 | 20 | 80 |
| ≤478 | **0** | 20–24 |

The 20px frame is **constant from 479px up**, the panel's 60px padding **does not shrink** at tablet, and `mobile_portrait` is the one breakpoint that drops the frame to 0 and the panel padding to 20. Above a 1560 viewport the 1400 cap starts centring the content, which is where the 125 comes from.

Three rules follow:

- **A root section never carries a background colour or image.** The background belongs to the container inside it — that is what makes the panel inset. `check.py` fails a root that paints.
- **Never set the frame to 0** except at `mobile_portrait`.
- **Root sections never use `_margin`.** Vertical rhythm is panel padding and alternating backgrounds, nothing else. Where a page has no banner and its first panel must clear the sticky header, the top margin goes on the *panel* (see `thanks-page.json`).

Two more spacing conventions:

- Gap between a section's header block and its content: `_margin bottom 56`, on inner elements only
- Alternate dark `#212121` and light `#eeeeee` panels with white interleaved; never two identical backgrounds in a row

The site header is the exception that proves the rule: its container is `_width:100%` with 40px padding and no 1400 cap, so the nav sits 40px off the edge at any width and spans the full window.

## Common interaction patterns

- **Ghost button**: transparent fill (Color #23) + 1px bottom border + themify `ti-arrow-right` icon + `_cssTransition: "0.3s all"`, border color swaps on hover
- **Card hover**: `_boxShadow:hover` 2/2/0/8 + `_cssTransition: "0.3s all"`
- **Slider**: `slider-nested` with `optionsType: custom` splide JSON (perPage 1, focus center, gap 40px, speed 400, arrows false, pagination true); pagination styling uses the `_cssCustom` shipped in the component library — the only approved `_cssCustom` use
- **Video**: mp4 via media (autoplay/mute/loop/inline, objectFit cover), `themeStyles: {customPlayer: true}`
- **Background-image panel**: `_background` image + the `_gradient` scrim from the contrast rules above

## Images

- Prefer existing site media via `search_media`; new uploads must include alt text
- Check the picture before you place it: filenames lie (`PowerBank-Family-*.jpg` is an interior shot, not a family), so open the candidate and confirm it shows what the copy beside it says
- Icon PNGs: height 64, mobile 24 — size them with `_height`, which the library uses
- Loop data, three modes: JetEngine query builder (reviews = 41), post query (branch), inline `arrayEditor` array — the first choice for campaign-scoped data, since it needs no CCT
