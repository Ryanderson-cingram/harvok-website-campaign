# Setup — Harvok Campaign Pages

Two things get set up once per person: the **skill** (this folder) and the **MCP connection** (your own WP credentials). Takes ~5 minutes.

## 0. What you need from the admin

Ask the site admin for a WordPress account on harvok.com.au with the **Harvok Marketing** role. (Admin instructions live in the `harvok-campaign` plugin's README.md.)

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

## 4. Use it

Describe your campaign to Claude (or invoke `/harvok-campaign-pages`):

> I need a landing page for the spring stock clearance — audience is …, the offer is …, CTA is a HubSpot form

Claude walks the workflow: brief → copy (you approve it in markdown) → imagery from the site media library → draft page + thanks page → review link to the admin. **Everything you create is a draft — only the admin can publish, in wp-admin.**

## Notes & limits

- Draft preview links require a logged-in wp-admin session — reviewers must be logged in
- HubSpot forms: create the form in HubSpot first and give Claude the form-id; the admin re-signs the code block during review
- claude.ai / Desktop app usage (no terminal) is packaged separately — ask the maintainer
