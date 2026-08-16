# Bricks JSON Format Rules (condensed)

The server-side create/update tools enforce these rules — violations are rejected outright.

## Element record

Each element: `{id, name, parent, children, settings}` (optional `label` shown in the editor).

- `id`: exactly 6 lowercase alphanumerics, unique across the page
- `parent`: integer `0` for roots, otherwise the parent element's id string
- `children`: array of child ids — **must agree with each child's `parent` in both directions**
- `settings`: use an empty array `[]` when there are none; never omit the key
- Hierarchy convention: `section → container (1400 wide) → block/div → content elements`

## Forbidden

- **`themeStyles` must never appear on primitives** (section/container/block/div/heading/text-basic/button) — it renders the element unstyled; only complex widgets (carousel/rating/icon/video …) carry it (copy from the component library)
- **`_cssCustom` is forbidden by default** — its styling is invisible to Bricks editors; the only exemption is the slider-pagination block shipped in the component library (requires `allow_custom_css: true`)
- **Don't use `_conditions`** — the live site uses it for temporary admin-only gating; drafts don't need it (drafts aren't public anyway)
- Never invent attachment ids, global color ids, or query builder ids — everything comes from `search_media` results or the component library

## Color references

Global colors must be the full triple: `{"hex":"#212121","id":"2430ac","name":"Color #6"}`. One-off colors (avoid where possible) use `{"raw":"#e6e6e6"}`.

## Responsive

Breakpoint-suffixed keys: `_typography:mobile_portrait`, `_padding:tablet_portrait`, etc. Desktop values are the baseline; write only the overrides — but check all three breakpoints.

## Dynamic tags

- `{post_title}` / `{post_excerpt}` / `{featured_image}` — the campaign CPT has excerpt + featured image support enabled
- JetEngine fields: `{je_cct_customer_reviews_*}`, `{je_branch_*}` etc. (only ones already present in the component library)
- Inline array loop: `{query_array @key:'title'}` paired with `arrayEditor`

## Known silent failure: Bricks drops meta writes by user capability

For users without the `bricks_full_access` capability, writes to `_bricks_page_content_2` are **silently discarded** (the tool reports success, element_count looks right, but the page renders blank). The harvok_marketing role receives this capability from plugin v0.2.1+. If a fresh draft previews blank: read it back with `get_campaign` — an empty string for elements means exactly this; check the account's role / the plugin version.

## Paste / import envelope

Component files use the Bricks right-click-paste format: `{"content":[...],"source":"bricksCopiedElements","sourceUrl":"https://harvok.com.au","version":"2.3.11"}`.
The MCP tools take only the flat array under `content` (regenerate non-colliding ids for every element when merging multiple components).
