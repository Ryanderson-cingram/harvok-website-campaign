# Pre-delivery Checklist

Run through every item after building the draft, before sending the review link:

## Structure
- [ ] title / excerpt / featured_media are all set (the banner and any `{post_excerpt}` section depend on them)
- [ ] Dark/light sections alternate — no two identical backgrounds in a row
- [ ] Pages with a form have a thanks child page (correct `parent`, form redirect points at it)

## Responsive (check all three breakpoints)
- [ ] tablet_portrait / mobile_landscape / mobile_portrait overrides are complete — font sizes, padding, direction (per the design-tokens scale)
- [ ] Images don't overflow or crop out their subject on mobile

## Content
- [ ] Copy was human-approved (at the markdown stage)
- [ ] `<b>Harvok®</b>` usage and product spellings follow copy-guidelines.md
- [ ] Every image has alt text; image and adjacent copy describe the same thing
- [ ] Button/link targets are valid (internal postId exists, external URL reachable)
- [ ] Compliance-uncertain claims are marked TODO for human review

## Technical
- [ ] No invented ids (attachments / global colors / query builders all come from search_media or the component library)
- [ ] No `_cssCustom` (other than the library's slider pagination), no `_conditions`
- [ ] Server validation passed (create/update returned no errors)
- [ ] No root-section `_margin`; spacing follows the 96/64/48 padding system

## Wrap-up
- [ ] Review email sent via `notify: true`, or the preview link handed to the admin manually
- [ ] Reviewer told: previews require a logged-in wp-admin session
- [ ] If the page contains a HubSpot/code element: remind the admin to save once in Bricks to re-sign (otherwise the form won't render)
- [ ] HubSpot form redirect points at this campaign's thanks child page
