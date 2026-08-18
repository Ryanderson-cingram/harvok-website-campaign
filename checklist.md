# Checklists

Two gates. § Design runs before the HTML goes to the user; § Build runs before the draft link goes to the admin.

## § Design — before showing the HTML

- [ ] Every text/background pair passes the design-tokens contrast table — no red body text, no `#9e9e9e` on light, no unscrimmed text over photos
- [ ] Every coloured block sits in the 20px frame with the `#f5f5f5` ground showing at both edges — backgrounds on the panel, never on the root section (frame drops to 0 only at mobile_portrait)
- [ ] Text lands ~80px from the viewport edge between 750 and 1450, and centres from the 1400 cap above that — compare against the live page before calling it done
- [ ] Vertical rhythm is section padding only (96 / 64 / 48), no root `_margin`
- [ ] Dark / light sections alternate — no two identical backgrounds in a row
- [ ] All three breakpoints render correctly when the window is resized
- [ ] Every block maps to a section-menu row, and is annotated with its component name
- [ ] Copy is the user's, verbatim; user-marked placeholders are visibly still placeholders
- [ ] Images are real `search_media` results, and each matches the copy beside it

## § Build — before sending the review link

**Structure**
- [ ] `title` / `excerpt` / `featured_media` all set — the banner and any `{post_excerpt}` block depend on them
- [ ] Thanks page created with the right `parent` **and `noindex: true`**, and the HubSpot redirect points at it
- [ ] Preview matches the approved HTML — spacing, order, imagery

**Technical**
- [ ] `python3 check.py <elements.json>` passes
- [ ] Server validation passed
- [ ] **Read the draft back with `get_campaign` and confirm the element count and ids match what you sent** — Bricks drops content writes from non-builder accounts while still reporting success
- [ ] Every horizontal row is a `block`, not a `div` (`div` is not a flex container)
- [ ] No invented ids — attachments, global colors and query builders all come from `search_media` or the component library
- [ ] No `_cssCustom` beyond the library's slider pagination; no `_conditions`
- [ ] Breakpoint overrides complete: font sizes, padding, direction
- [ ] Every image has alt text; button and link targets resolve

**Hand-off**
- [ ] Preview link + edit link delivered, with the note that previews need a logged-in wp-admin session
- [ ] Outstanding placeholders and any compliance TODOs listed explicitly
- [ ] If the page has a HubSpot/code element: admin reminded to open it in Bricks and save once, to re-sign it
