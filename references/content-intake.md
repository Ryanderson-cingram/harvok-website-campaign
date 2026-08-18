# Content Intake

Marketing writes the words. This skill designs and builds. Nothing on the page is text you invented — not a headline, not a subhead, not a button label, not a footnote.

## What to ask for

Ask for all of it in one round, and show this shape so the user knows what "a section" means:

```
Campaign:   <name>            Goal: <what the page is for>
Audience:   <who>             Deadline: <live date>
URL slug:   <slug>            Excerpt: <1–2 sentences, used by the banner/excerpt block>

Sections, in page order:
1. Hero          — H1: "…"   subhead: "…"   button: "…" → <target>
2. The offer     — heading: "…"   body: "…"   3 quick facts: "…", "…", "…"
3. …
Form:            HubSpot form-id <uuid>, or "no form"
Footnotes:       "…"          (required — compliance)
```

## Rules for the intake

- **A section with no copy is not a section.** If something is missing, list exactly what is missing and stop. Do not proceed to design with "TBC" or lorem text.
- Placeholders the user marks themselves (`[date TBC]`, `[form-id TBC]`) are fine — carry them through verbatim so they stay visible in review, and list them in the hand-off.
- Every section needs its own copy, even short ones. "Same as the other page" means fetch that page with `get_campaign` and quote what you found back for confirmation.
- Images: the user may name what they want; you find it with `search_media`. If they supply files, `upload_media` needs alt text from them.

## What you check on supplied copy

Report problems, do not silently rewrite. If a fix is obvious (a missing `®`), propose it and let the user confirm.

**Brand usage**
- The brand word in headings takes the fixed form `<b>Harvok®</b>` — bold, with the ®
- In body copy the first mention is Harvok®; later mentions may be plain Harvok
- Fixed spellings: Monocoque Uni-Body, 48V Electric Power System, Aluminium Monocoque Body (Australian spelling: Aluminium)

**Structural fit** — flag when supplied copy will not fit the design, before designing around it:
- Eyebrow labels: 2–3 words, uppercase
- Feature list items: 3–7 words each
- Button copy: starts with a verb, title case
- A headline far longer than the type scale allows — say so and ask for a shorter version rather than shrinking the type

**Compliance** — flag for human review, never decide yourself:
- Price claims (the site convention is "From $X", never a promised drive-away figure)
- Stock and lead-time promises
- Performance or capability claims that need a matching footnote entry
- Quoted reviews, if attribution is unclear

When a compliance question is unclear, mark the copy TODO and raise it in the hand-off. Nothing about compliance is your call.
