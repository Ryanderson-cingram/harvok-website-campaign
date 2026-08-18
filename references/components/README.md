# Component Library

Exported from harvok.com.au and cleaned: `_conditions` admin gating stripped, root spacing normalised to the design-tokens system, contrast defects corrected. Files are in Bricks paste format — the `content` array is the element list.

Consistency comes from reusing these, not from regenerating them. Assemble from here first and build from primitives only where the brief genuinely needs something new.

## Index

Every file follows the same three-level layout: a root `section` carrying only the 20px frame, a `container` holding the background, and a 1400-wide `container` for the content. `Panel background` is what that middle container paints.

| File | Panel background | What it is | You replace |
|---|---|---|---|
| `campaign-banner.json` | image (`{featured_image}`) | Page banner: background image + logo + H1 `{post_title}` + breadcrumbs | `featured_media` drives the image (fallback 398) |
| `offer-intro.json` | `#212121` | Two-column offer intro: heading + image / three paragraphs | All copy, the image |
| `excerpt-section.json` | `#212121` | Display heading + `{post_excerpt}` pull-statement | Heading copy; the right column can take literal copy instead |
| `feature-carousel-iconbox.json` | `#ffffff` cards | Image carousel + icon-box feature list | Carousel images, each icon-box's icon / title / copy |
| `highlights-slider.json` | `#eeeeee` | Feature slider: video or image + icon + copy + ghost button | Per-slide media, icon, title, body, button target |
| `card-grid.json` | `#ffffff` cards | Three-column cards (carousel + title + rating + link), post loop | Query post type, field tags |
| `social-proof-loop.json` | `#eeeeee` | Live review cards + frequency tag cloud | Tag-cloud data, headings |
| `hubspot-form.json` | `#ffffff` card | Conversion form section | `data-form-id` only |
| `footnotes.json` | none — sits on the page ground | Legal footnotes strip | Footnote copy |
| `thanks-page.json` | `#212121` | Complete thanks child page: feature image + thank-you copy + button | Thank-you copy, button target |

### Dependencies and gotchas

- `highlights-slider.json` holds the library's only `_cssCustom` (splide pagination) — using it means passing `allow_custom_css: true`
- `social-proof-loop.json` needs JetEngine query builder id 41 and the `harvok_initials()` echo
- `card-grid.json` is wired to branch CPT fields — swap the dynamic tags when repurposing it
- `hubspot-form.json` carries a signed `code` element: changing the form-id needs an admin re-save in Bricks
- `thanks-page.json` has no banner above it, so its panel takes a 180px top margin to clear the sticky header — on the panel, not the root section

## Adding a component

Build or refine the section in Bricks → right-click **Copy** → hand the clipboard JSON to Claude with "add this to the component library". Claude strips `_conditions`, normalises the root spacing, runs `check.py`, saves the file and updates this table.

## Still missing

- [ ] FAQ section (tabs-nested / toggle)
- [ ] Static CTA band — phone / visit, no form
