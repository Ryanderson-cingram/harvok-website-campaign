---
name: harvok-campaign-pages
description: Generate Bricks Builder campaign landing page DRAFTS for harvok.com.au via the harvok-campaign MCP server. Use when marketing wants a campaign/promo/launch landing page, a thanks page, or edits to a campaign draft. Assembles pages from the approved component library following Harvok design tokens; publishing stays with the site admin.
---

# Harvok Campaign Landing Page Generation

The deliverable is always a **draft** plus a review link. Publishing happens in wp-admin, by an admin — no tool can publish. Don't try.

## Prerequisites

MCP server `harvok-campaign` (5 tools: search_media / upload_media / get_campaign / create_campaign_draft / update_campaign_draft). If it's not configured, point the user to the plugin's README.md — they connect with their own WP username + Application Password.

## Workflow

1. **Take the brief**: goal (what's being sold/promoted), audience, offer, CTA, deadline. Ask for anything missing — all in one round.
2. **Pick the recipe**: read `references/page-recipes.md` and decide the section lineup; `get_campaign` (no args) lists existing campaigns — pull a published one as a structural reference when useful.
3. **Copy first**: write all copy per `references/copy-guidelines.md`, present it in markdown by section, and **wait for approval before going further**. Copy changes happen at the markdown stage, never inside JSON.
4. **Pick imagery**: for every image slot run `search_media` first (English keywords); check the image actually matches the copy. Only when nothing fits, ask the user for a local file → `upload_media` (alt text required).
5. **Assemble the JSON**: build from `references/components/` and Bricks primitives, following `references/design-tokens.md` and `references/bricks-format.md`. Regenerate fresh, non-colliding 6-char ids for every element when merging.
6. **Create the draft**: `create_campaign_draft` with title + elements + excerpt + featured_media. Pages with a form also get a thanks child page (`parent` pointing at the landing page). If server validation rejects, fix and retry.
7. **Self-check**: run through `checklist.md` and report the results.
8. **Deliver**: hand over the preview link + wp-admin edit link. Once the user approves, re-run update with `notify: true` (or let the user forward the link). Remind the reviewer: previews require a logged-in wp-admin session.

## Hard rules

- Styling comes only from the component library and design tokens — never invent colors, fonts, attachment ids or query ids
- `_cssCustom` is allowed only where the component library already ships it (pass `allow_custom_css: true`)
- Responsive coverage across all three breakpoints is mandatory, not a nice-to-have
- Compliance-sensitive copy you're unsure about gets a TODO for human review — never decide it yourself
