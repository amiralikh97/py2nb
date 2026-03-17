# How to Publish py2nb to the VS Code Marketplace

After following this guide, anyone can install py2nb by searching for it in the VS Code Extensions panel.

---

## Prerequisites

- A GitHub account
- Node.js installed (check: `node --version`)

---

## Step 1 — Push the code to GitHub

1. Go to [github.com](https://github.com) and create a new **public** repository named `py2nb`
2. Do not initialise it with a README (we already have one)
3. Run these commands:

```bash
cd /rodata/osail/m309406/Current/py2nb
git init
git add .
git commit -m "Initial release v0.1.0"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/py2nb.git
git push -u origin main
```

---

## Step 2 — Create a Microsoft account

Go to [microsoft.com](https://microsoft.com) → **Sign in** → **Create one** if you don't have one.

---

## Step 3 — Create a publisher on the Marketplace

1. Go to [marketplace.visualstudio.com/manage](https://marketplace.visualstudio.com/manage)
2. Sign in with your Microsoft account
3. Click **Create publisher**
4. Fill in:
   - **ID** — this is what goes in `package.json`, e.g. `amiralikhaleghi` (lowercase, no spaces, permanent)
   - **Display name** — anything you like
5. Click **Create**

---

## Step 4 — Create a Personal Access Token

1. Go to [dev.azure.com](https://dev.azure.com) and sign in with the same Microsoft account
2. Click your avatar (top right) → **Personal access tokens**
3. Click **New Token**
4. Set:
   - **Name:** `vsce` (or anything)
   - **Organization:** All accessible organizations
   - **Expiration:** 1 year
   - **Scopes:** Custom defined → tick **Marketplace → Manage**
5. Click **Create**
6. **Copy the token immediately** — it is shown only once

---

## Step 5 — Update package.json

Edit `/rodata/osail/m309406/Current/py2nb/vscode-extension/package.json` and update these two fields:

```json
"publisher": "YOUR_PUBLISHER_ID",
"repository": {
  "type": "git",
  "url": "https://github.com/YOUR_GITHUB_USERNAME/py2nb"
},
```

Replace `YOUR_PUBLISHER_ID` with the ID you chose in Step 3, and `YOUR_GITHUB_USERNAME` with your GitHub username.

---

## Step 6 — Publish

```bash
cd /rodata/osail/m309406/Current/py2nb/vscode-extension

# Log in with your publisher ID (paste the token when prompted)
npx @vscode/vsce login YOUR_PUBLISHER_ID

# Publish
npx @vscode/vsce publish
```

You should see:
```
DONE  Published: YOUR_PUBLISHER_ID.py2nb v0.1.0
```

---

## Step 7 — Install from VS Code

Wait ~5 minutes for the Marketplace to index it, then:

1. Open VS Code
2. Click the Extensions icon in the sidebar (or `Ctrl+Shift+X`)
3. Search **py2nb**
4. Click **Install**

---

## How to release an update

1. Edit your Python or extension code
2. Bump the version in `package.json` (e.g. `0.1.0` → `0.1.1`)
3. Copy the updated Python files into the extension:
   ```bash
   cp /rodata/osail/m309406/Current/py2nb/py2nb/*.py \
      /rodata/osail/m309406/Current/py2nb/vscode-extension/py2nb/
   ```
4. Publish the new version:
   ```bash
   cd /rodata/osail/m309406/Current/py2nb/vscode-extension
   npx @vscode/vsce publish
   ```
5. VS Code will prompt existing users to update automatically

---

## What users need after installing

Only **Python** — no `pip install` required. The Python source is bundled inside the extension.

If the extension cannot find Python, users set their interpreter path in:
`Ctrl+,` → search `py2nb` → set **py2nb: Python Path** to the full path, e.g. `/usr/bin/python3`
