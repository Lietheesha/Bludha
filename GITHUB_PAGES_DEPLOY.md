# Deploy to GitHub Pages

This guide will help you deploy your Bludha static website to GitHub Pages.

## Prerequisites

- A GitHub account
- Git installed on your computer
- Your code pushed to a GitHub repository

## Deployment Steps

### Step 1: Clean up and commit your changes

```bash
# Add all files for the static site
git add index.html
git add static/
git add .gitignore
git add GITHUB_PAGES_DEPLOY.md

# Remove deleted Django files
git add -u

# Commit changes
git commit -m "Convert to static HTML/CSS site for GitHub Pages"
```

### Step 2: Push to GitHub

```bash
# If you want to deploy from main branch
git checkout main
git merge font-fix
git push origin main

# Or if you want to deploy from font-fix branch
git push origin font-fix
```

### Step 3: Enable GitHub Pages

1. Go to your GitHub repository on GitHub.com
2. Click on **Settings** (top menu)
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select:
   - **Branch**: Choose `main` (or `font-fix` if you pushed to that branch)
   - **Folder**: Select `/ (root)`
5. Click **Save**

### Step 4: Access your site

Your site will be available at:
- `https://YOUR_USERNAME.github.io/REPOSITORY_NAME/`

For example: `https://yourusername.github.io/Bludha-1/`

**Note:** It may take a few minutes for the site to be available after enabling Pages.

## Custom Domain (Optional)

If you have a custom domain:

1. Create a file named `CNAME` in the root directory
2. Add your domain name (e.g., `www.yourdomain.com`)
3. Commit and push the file
4. Configure DNS settings as instructed by GitHub

## Troubleshooting

### Site not loading?
- Wait 5-10 minutes after enabling Pages
- Check the **Actions** tab for build errors
- Verify `index.html` is in the root directory
- Check that all static files (CSS, images, fonts) are committed

### 404 errors for assets?
- Make sure all paths in `index.html` start with `static/`
- Verify all files in the `static/` folder are committed

### Need to update the site?
- Just commit and push changes to the selected branch
- GitHub Pages will automatically rebuild

## File Structure

Your repository should have this structure:
```
/
├── index.html          ← Main HTML file
├── static/
│   ├── css/
│   │   └── home.css    ← Styles
│   ├── fonts/          ← Font files
│   └── images/         ← Images
└── .gitignore
```

## Quick Deploy Script

You can also use this quick script:

```bash
#!/bin/bash
# Quick deploy to GitHub Pages

git add index.html static/ .gitignore
git add -u
git commit -m "Deploy static site to GitHub Pages"
git push origin main
```

Then enable Pages in GitHub Settings as described above.
