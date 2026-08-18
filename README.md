# Setup — Harvok Campaign Pages

Two things get set up once per person: the **skill** (this folder) and the **MCP connection** (your own WP credentials). Takes ~5 minutes.

## 0. What you need from the admin

Ask the site admin for **two** things (instructions for them live in the `harvok-campaign` plugin's README.md):

1. A WordPress account on harvok.com.au with the **Harvok Marketing** role
2. **Builder access for that role in Bricks → Settings.** Without it Bricks throws away every layout you write and reports success anyway — you end up with a page that has a title and no content, and no error to tell you why. Confirm this is done before your first real campaign.

Then create your own API key:
1. Log in to https://harvok.com.au/wp-admin/
2. Top right → **Profile** → scroll to **Application Passwords**
3. Name it `claude-mcp` → **Add New** → copy the 24-character password (shown only once, keep the spaces)

Never share this password; the admin can revoke it from your profile at any time.

## 1. Install the skill (Claude Code)

Clone this repo straight into your personal skills directory (ask the admin for read access on GitHub):

```bash
git clone git@github.com:Ryanderson-cingram/harvok-website-campaign.git ~/.claude/skills/harvok-campaign-pages
# no git / no GitHub access? ask the admin for a zip and unzip to the same path
```

Updating later: `cd ~/.claude/skills/harvok-campaign-pages && git pull` (zip users: re-copy the folder).

## 2. Connect the MCP server

Replace username and password with your own:

```bash
claude mcp add --transport http harvok-campaign \
  https://harvok.com.au/wp-json/harvok/v1/mcp \
  --header "Authorization: Basic $(printf 'YOUR_WP_USERNAME:xxxx xxxx xxxx xxxx xxxx xxxx' | base64)"
```

Note: it's your WordPress **username** (not email), and the Application Password keeps its spaces.

## 3. Verify

Start Claude Code anywhere and ask:

> List the existing campaigns

You should get back the campaign list from harvok.com.au. If you get an auth error, re-check username and password; if the tools are missing, run `claude mcp list` to confirm the server was added.

If a page you build previews as blank or keeps its old content, that is the Bricks builder access from step 0 — not something you did wrong. Ask the admin to grant it.

## 4. Use it

**Write your copy first.** Claude designs and builds the page; it does not write the words. Bring a section list with the actual copy for each section — headline, body, button labels, footnotes. Claude will ask for anything missing before it starts.

Then describe your campaign (or invoke `/harvok-campaign-pages`):

> Landing page for the spring stock clearance. Audience is …, the offer is …, CTA is a HubSpot form. Sections and copy: …

Claude then works in four stages:

1. **Intake** — checks your copy is complete, asks for whatever is missing
2. **Design** — builds an HTML design of the page and hands you a file to open. Review it, ask for changes, repeat until you're happy
3. **Build** — turns the approved design into the real Bricks page, plus a thanks page if there's a form
4. **Hand-off** — a preview link for the admin

**Everything Claude creates is a draft — only the admin can publish, in wp-admin.**

## Notes & limits

- Design changes belong in stage 2. Once the page is built, changing the layout means going back to the HTML — so take your time with the design review
- Draft preview links require a logged-in wp-admin session — reviewers must be logged in
- HubSpot forms: create the form in HubSpot first and give Claude the form-id; the admin re-signs the code block during review
- Thanks pages are set to noindex automatically
- claude.ai / Desktop app usage (no terminal) is packaged separately — ask the maintainer
