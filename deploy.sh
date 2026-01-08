#!/bin/bash

echo "🚀 Deploying Bludha to GitHub Pages..."
echo ""

# Add static site files
echo "📦 Adding files..."
git add index.html
git add static/
git add .gitignore
git add GITHUB_PAGES_DEPLOY.md

# Remove deleted Django files
echo "🧹 Cleaning up deleted files..."
git add -u

# Check if there are changes to commit
if ! git diff --staged --quiet; then
    echo "💾 Committing changes..."
    git commit -m "Deploy static HTML/CSS site to GitHub Pages"
    
    echo "📤 Pushing to GitHub..."
    git push origin font-fix
    
    echo ""
    echo "✅ Deployment files pushed!"
    echo ""
    echo "📝 Next steps:"
    echo "1. Go to: https://github.com/Lietheesha/Bludha/settings/pages"
    echo "2. Under 'Source', select branch: font-fix"
    echo "3. Select folder: / (root)"
    echo "4. Click Save"
    echo ""
    echo "🌐 Your site will be available at:"
    echo "   https://lietheesha.github.io/Bludha/"
else
    echo "⚠️  No changes detected. Everything is up to date!"
fi
