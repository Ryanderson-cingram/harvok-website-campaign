---
name: harvok-campaign-pages
description: Generate Bricks Builder campaign landing page DRAFTS for harvok.com.au via the harvok-campaign MCP server. Use when marketing wants a campaign/promo/launch landing page, a thanks page, or edits to a campaign draft. Designs in HTML first, gets sign-off, then builds the page from the approved component library; publishing stays with the site admin.
---

# Harvok Campaign Landing Page Generation

The deliverable is always a **draft** plus a review link. Publishing happens in wp-admin, by an admin — no tool can publish.

**This skill does not write copy.** Marketing supplies the section list and the words for every section. If copy is missing, stop and ask for it — never invent a headline, a claim, a price or a date.

## Prerequisites

MCP server `harvok-campaign` (5 tools: search_media / upload_media / get_campaign / create_campaign_draft / update_campaign_draft). If it isn't configured, point the user to `README.md`.

## Workflow

Four stages. Each one ends at a gate you may not walk past on your own.

### 1. Content intake

Collect the section list and the copy for each section per `references/content-intake.md`. Ask for everything missing in one round.
**Gate:** every section on the list has real copy. No placeholder text goes into a design.

### 2. HTML design

Design the page as a single self-contained HTML file at `campaign-drafts/<slug>.html` in the current working directory (create the folder if it isn't there).

- Invoke the **`frontend-design`** skill first (it may be listed as `frontend-design:frontend-design`) and design under its guidance — this stage is a real design pass, not a wireframe. If it isn't installed, say so and design against the tokens alone.
- The visual system is fixed by `references/design-tokens.md`: palette, contrast pairings, type scale and the three-level layout. `frontend-design` governs composition, hierarchy and craft; the tokens govern the values.
- Pick the section lineup from `references/page-recipes.md` so every block has a known Bricks implementation.
- Source real imagery now, not later: `search_media` with English keywords, and check each image actually matches its copy. Only when nothing fits, ask for a local file → `upload_media` (alt text required).
- Run `checklist.md` § Design **before** showing it. Contrast and the 20px frame are the two defects that keep reaching review — check both against the design-tokens tables.

**Gate:** the user has reviewed the rendered HTML and said it is final. Iterate on the HTML for as many rounds as they want. Design changes happen here, never in JSON.

### 3. Bricks implementation

Translate the approved HTML into a flat Bricks element list, built from `references/components/` and Bricks primitives, following `references/bricks-format.md`. Regenerate fresh, non-colliding 6-char ids for every element when merging components.

Save the element list to a file and run this skill's checker before you send it: `python3 <skill-dir>/check.py <file>`. It catches what the server does not — a root section that paints, a missing side gutter, root `_margin`, `themeStyles` on a primitive, and text that fails contrast against its inherited background. Do not send a draft that fails.

Create the draft with `create_campaign_draft`: `title` + `elements` + `excerpt` + `featured_media`. A page with a form also gets a thanks child page — `parent` set to the landing page, and **`noindex: true`**.

**Then read it straight back with `get_campaign` and compare the element count and a few ids against what you sent.** Bricks silently discards content writes from accounts it doesn't treat as builders, and the tool still reports success — an unverified write is how a whole page quietly goes missing.

### 4. Preview and hand-off

Run `checklist.md` § Build and report the results. Open the preview URL and compare it against the approved HTML; fix any drift before handing it over. Then deliver the preview link plus the wp-admin edit link, and note that previews require a logged-in wp-admin session.

## Hard rules

- Copy comes from the user. Design comes from the tokens. Neither is improvised.
- Styling comes only from the component library and design tokens — never invent colors, fonts, attachment ids or query ids.
- `_cssCustom` is allowed only where the component library already ships it (pass `allow_custom_css: true`).
- All three breakpoints are mandatory: `tablet_portrait` / `mobile_landscape` / `mobile_portrait`.
- Compliance-sensitive copy you are unsure about gets a TODO for human review — never decide it yourself.
