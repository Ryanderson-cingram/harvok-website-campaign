# Bricks JSON Format

Three levels of enforcement, and it matters which is which:

| | Checked by | Failure mode |
|---|---|---|
| ids, parent/children agreement, `settings` present, `themeStyles` on primitives, `_cssCustom` | the server, on write | request rejected with an error you can read |
| root backgrounds, gutters, root `_margin`, contrast | `check.py`, before you write | you have to run it |
| everything else on this page | nobody | ships silently wrong |

## Element record

Each element is `{id, name, parent, children, settings}`, plus an optional `label` shown in the editor.

- `id`: exactly 6 lowercase alphanumerics, unique across the page
- `parent`: integer `0` for roots, otherwise the parent's id string
- `children`: array of child ids — **must agree with each child's `parent` in both directions**
- `settings`: an empty array `[]` when there are none; never omit the key

Hierarchy is three levels before content, per the design-tokens layout rule:

```
section  (frame) → container (panel, has the background) → container (1400) → block → content
```

## `div` is not a flex container

`.brxe-section`, `.brxe-container` and `.brxe-block` render as `display:flex`. **`.brxe-div` renders as `display:block`.** Put `_direction: row` on a `div` and Bricks emits `flex-direction:row` with no `display:flex` to act on: the setting is silently inert and every child stacks vertically at full width.

So **every horizontal row must be a `block`** (or a container). Reach for `div` only as a plain non-layout wrapper.

Two things that go wrong the same way:

- `.brxe-text-basic` is `display:block` and fills its parent, so as a flex child it eats the whole row. A label sitting beside something (an icon, a rule) needs `_width: "auto"`.
- Size sibling columns explicitly — `X%` and `calc((100-X)% - gap)` — rather than relying on grow/shrink.

## Forbidden

- **`themeStyles` on primitives** (section / container / block / div / heading / text-basic / button) renders the element unstyled. Only complex widgets — carousel, rating, icon, video — carry it, copied from the component library.
- **`_cssCustom`** is invisible to Bricks editors. Exactly one element in the library carries it — the splide pagination in `highlights-slider.json` — and using that component means passing `allow_custom_css: true`. Nothing else qualifies.
- **`_conditions`** — the live site uses it for temporary admin-only gating. Drafts are not public and do not need it. The server does *not* reject it, so strip it yourself when importing a live export.
- **Settings keys with no precedent in the library.** `_flexGrow`, `_flexShrink`, `_objectFit` and `_aspectRatio` all look plausible and none appear in any component. Grep `references/components/` before using a key you have not seen here; size flex children with explicit widths instead.

## Colors

Global colors are the full triple: `{"hex":"#212121","id":"2430ac","name":"Color #6"}`. One-off colors use `{"raw":"#e6e6e6"}` — avoid them; they sit outside the palette and outside the contrast table.

## Responsive

Breakpoint-suffixed keys: `_typography:mobile_portrait`, `_padding:tablet_portrait`. Desktop is the baseline and you write only the overrides — but check all three breakpoints.

## Dynamic tags

- `{post_title}` / `{post_excerpt}` / `{featured_image}` — the campaign CPT has excerpt and featured image support enabled
- JetEngine fields: `{je_cct_customer_reviews_*}`, `{je_branch_*}` — only the ones already present in the component library
- Inline array loop: `{query_array @key:'title'}` paired with `arrayEditor` — the first choice for campaign-scoped data, since it needs no CCT

## Paste envelope

Component files use the Bricks right-click-paste format:

```json
{"content":[...],"source":"bricksCopiedElements","sourceUrl":"https://harvok.com.au","version":"2.3.11"}
```

The MCP tools take only the flat array under `content`. Regenerate non-colliding ids for every element when merging components.

## Known silent failure: Bricks drops meta writes from non-builder users

Writes to `_bricks_page_content_2` from a user Bricks doesn't recognise as a builder are **silently discarded** — the tool reports success with the right `element_count`, but the stored content never changes.

**Always read back after writing.** `get_campaign` returns the element list; compare the count and a couple of ids against what you sent. A write that "succeeded" but read back as the previous content is this bug, not a caching artifact.

Measured 2026-08-18 on plugin v0.2.2: the `harvok_marketing` role can write ordinary post fields (title, excerpt, parent, featured image) but its Bricks content writes are dropped, while the same payload from an `administrator` lands. Granting the `bricks_full_access` capability is **not** sufficient — Bricks gates on its own Builder Access setting. Until an admin grants the Harvok Marketing role builder access in Bricks → Settings, marketing accounts can create and edit drafts but cannot populate their layout.
