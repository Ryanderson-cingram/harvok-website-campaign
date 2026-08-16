# Component Library Index (extended with the skill over time)

Source: exported from harvok.com.au, cleaned (`_conditions` admin gating removed). Files are in Bricks paste format; the `content` array is the element list.

| File | Contents | Replaceable slots | Dependencies |
|---|---|---|---|
| `excerpt-section.json` | Dark two-column: display heading + `{post_excerpt}` | Heading copy; right column can take literal copy | none |
| `highlights-slider.json` | Feature slider (video/image + icon + copy + ghost button), splide single-slide centered | Per-slide media, icon, title, body, button link | ships approved `_cssCustom` (pagination) — needs `allow_custom_css: true` |
| `social-proof-loop.json` | Review cards feed (JetEngine query 41) + frequency tag cloud (arrayEditor) | Tag cloud data, headings | JetEngine query builder id 41, `harvok_initials()` echo |
| `card-grid.json` | Three-column image cards (carousel + title + rating + link), post loop | Query post_type, field tags | branch CPT fields (swap dynamic tags when repurposing) |
| `campaign-banner.json` | Campaign banner: background image + logo + H1 `{post_title}` + breadcrumbs | featured_media drives the background (fallback 398) | none (campaign pages must carry their own banner — no template provides one) |
| `offer-intro.json` | Two-column offer intro: heading + image / three paragraphs | All copy, image | none |
| `feature-carousel-iconbox.json` | Carousel + icon-box feature list | Carousel images, each icon-box's icon/title/copy | none |
| `hubspot-form.json` | HubSpot form section (code element) | `data-form-id` (differs per campaign) | ⚠️ any change requires an admin re-save in Bricks to re-sign |
| `thanks-page.json` | Complete thanks child page (feature hotspot image + thank-you copy + button) | Thank-you copy, button link | none |
| `footnotes.json` | Legal footnotes section | Footnote copy | none |

## To add

- [ ] FAQ section (tabs-nested / toggle)
- [ ] Static CTA band (no form — phone / visit)

## Intake workflow (marketing can self-serve)

Build/refine the section in Bricks → right-click **Copy** → hand the clipboard JSON to Claude with "add this to the component library" → Claude cleans it (strips `_conditions`, checks forbidden keys) → saves the file + updates this index.
