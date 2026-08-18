# Campaign Page Recipes

## The HTML design file

Stage 2 produces one self-contained file at `campaign-drafts/<slug>.html` — inline CSS, real image URLs from `search_media`, no build step, opens in a browser.

It is a design, not a wireframe, and it is also a build spec. So:

- Every block must map to a row in the section menu below. If you design something with no Bricks implementation, you will not be able to build it.
- Use the real copy and the real images. A design reviewed with stand-in content gets approved on the wrong basis.
- Mirror the Bricks structure — `section (frame) > container (panel, background) > container (1400) > content` — with the same padding values the JSON will carry. Getting the frame right here is what makes it right in the build.
- Include the three breakpoints as real media queries at 991px / 767px / 478px so the user can resize and see what they are approving.
- Annotate each section with an HTML comment naming its component (`<!-- offer-intro.json -->`), so stage 3 is transcription rather than interpretation.

Offer to publish it as an Artifact when the user wants to circulate it for review; otherwise just tell them the file path.

## Section menu

Every block on the page comes from this table. Components are raw material, not a template — combine them freely and build sections from primitives where the brief needs it, but the spacing system and design tokens are non-negotiable.

| Section | Component / approach | When |
|---|---|---|
| Banner / Hero | `campaign-banner.json`, or a self-built hero panel (background image + scrim, campaign display scale) | **Required** |
| Offer intro | `offer-intro.json`, or a self-built two-column (statement + paragraphs + quick facts) | **Required** |
| Conversion CTA | `hubspot-form.json`, or a static CTA (phone / visit) | **Required** |
| Footnotes | `footnotes.json` | **Required** (compliance) |
| Fact strip | Self-built: 4 cells of "label + Alumni Sans large value" | Hard facts — date, price, quantity |
| Features / schedule | `feature-carousel-iconbox.json`, `highlights-slider.json`, or self-built (e.g. a rally-style Run Sheet) | Pick the form per campaign type |
| Excerpt statement | `excerpt-section.json` | A large pull-statement using `{post_excerpt}` |
| Cards | `card-grid.json` | 3+ parallel items — models, branches, packages |
| Social proof | `social-proof-loop.json` (live reviews feed) | Only when trust is the conversion barrier — promos, new-customer acquisition. Community and event pages usually don't need it |
| FAQ | Self-built Q&A rows | Events, complex offers |

## Banner

The Single Page Template (692) does **not** apply to the campaign CPT — the published campaign 3951 renders its own in-content banner. So the first section of every campaign page is either `campaign-banner.json` or a self-built hero.

`campaign-banner.json` reads `{featured_image @fallback-image:398}`, so setting `featured_media` swaps the banner image. `create_campaign_draft` therefore always receives `title` (= the H1) and `featured_media`, plus `excerpt` whenever the page uses `{post_excerpt}`.

## HubSpot form

Embedded via a `code` element (see `hubspot-form.json`):

```html
<script src="https://js.hsforms.net/forms/embed/22233931.js" defer></script>
<div class="hs-form-frame" data-region="na1" data-form-id="<per-campaign form id>" data-portal-id="22233931"></div>
```

- portal-id is fixed at `22233931`; the **form-id differs per campaign** — marketing creates the form in HubSpot and supplies the id
- The form's redirect target is set in HubSpot, pointing at this campaign's thanks page URL
- ⚠️ Bricks code elements carry a tamper-proof signature. Changing the form-id invalidates it and the form will not render on the front end. This is expected, not a bug: the admin re-signs by opening the page in the Bricks editor and saving once. Say so in the hand-off.

## Thanks child page

`create_campaign_draft` with `parent: <landing page post_id>` → the URL becomes `/campaign/<slug>/thanks/`.

- Start from `components/thanks-page.json` and replace the copy with the user's
- **`noindex: true` is required.** A thanks page has no search value and leaks the conversion path if indexed. The tool writes The SEO Framework's `_genesis_noindex` qubit (1 = force noindex); verify it by opening the preview and reading the `robots` meta tag, which should start with `noindex`.
- Live reference: post 3966

## Referencing existing pages

`get_campaign` with no arguments lists every campaign; `get_campaign {post_id: 3951}` returns the full structure of the published reference page.
