# Campaign Landing Page Recipes

## Banner (verified on the live site, 2026-08-17)

The Single Page Template (692) does **not** apply to the campaign CPT — the published campaign 3951 renders its own in-content banner.
So every campaign page's first section is either `components/campaign-banner.json` (image + H1 `{post_title}` + breadcrumbs) or a self-built full-bleed hero per the design-tokens Display mega-type mode.
The banner background reads `{featured_image @fallback-image:398}`: setting `featured_media` swaps the banner image.

`create_campaign_draft` must always receive: `title` (= the H1), `featured_media` (banner background — `search_media` first), `excerpt` (when the page uses `{post_excerpt}`).

## Section menu

| Section | Component / approach | When to use |
|---|---|---|
| Banner / Hero | `campaign-banner.json`, or a self-built full-bleed hero in Display mega-type mode | **Required** |
| Offer intro | `offer-intro.json` or self-built two-column (statement + paragraphs + quick facts) | **Required** |
| Conversion CTA | `hubspot-form.json` (see HubSpot notes below) or a static CTA | **Required** |
| Footnotes | `footnotes.json` | **Required** (compliance) |
| Fact strip | Self-built: 4 cells of "label + Alumni Sans large value" | When there are hard facts (date/price/quantity) |
| Features / schedule | `feature-carousel-iconbox.json` / `highlights-slider.json` / self-built (e.g. a rally-style Run Sheet) | Pick the form per campaign type |
| Social proof | `social-proof-loop.json` (live reviews feed) | **Optional** — only when trust is the conversion barrier (promos, new-customer acquisition); community/event pages usually don't need it |
| FAQ | Self-built Q&A rows (or a toggle component, once added) | Events / complex offers |

Components are raw material, not a template — combine freely and build sections from primitives per the brief, but the spacing system and design tokens are non-negotiable. Alternate dark/light backgrounds.

## HubSpot form (important)

Embedded via a `code` element (see `hubspot-form.json`):
```html
<script src="https://js.hsforms.net/forms/embed/22233931.js" defer></script>
<div class="hs-form-frame" data-region="na1" data-form-id="<per-campaign form id>" data-portal-id="22233931"></div>
```
- portal-id is fixed: `22233931`; **form-id differs per campaign** — marketing creates the form in HubSpot first and supplies the id
- Set the form's redirect target to this campaign's thanks child page URL (configured in HubSpot form settings)
- ⚠️ **Code signatures**: Bricks code elements carry a tamper-proof signature. Changing the form-id invalidates it and the form won't render on the front end. Not a bug — the admin re-signs by opening the page in the Bricks editor and saving once during review. Mention this in the review notification.

## Thanks child page (form redirect target)

- `create_campaign_draft` with `parent: <landing page post_id>` → URL becomes `/campaign/xxx/thanks/`
- Start from `components/thanks-page.json` and rewrite the copy (thank-you headline + confirmation + button)
- Live reference: post 3966

## Referencing existing pages

`get_campaign` (no args) lists all campaigns; `get_campaign {post_id: 3951}` returns the full structure of the published reference page.

## Workflow reminder

Copy is written and approved in markdown before any JSON is assembled; copy edits happen at the markdown level — never ask a human to edit JSON.
