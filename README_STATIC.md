# Bludha - Static HTML/CSS Website

This is a standalone HTML/CSS version of the Bludha homepage. No server or framework needed!

## File Structure

```
/
├── index.html          # Main HTML file
├── static/
│   ├── css/
│   │   └── home.css    # All styles
│   ├── images/         # All images
│   └── fonts/          # Custom fonts (Negrita Pro, Rokkitt)
```

## How to Use

### Option 1: Open Directly in Browser
Simply double-click `index.html` or right-click and select "Open with" your preferred browser.

### Option 2: Use a Local Server (Recommended)

**Python:**
```bash
# Python 3
python3 -m http.server 8000

# Then visit: http://localhost:8000
```

**Node.js:**
```bash
npx http-server

# Then visit: http://localhost:8080
```

**VS Code:**
- Install "Live Server" extension
- Right-click `index.html` → "Open with Live Server"

## Features

- ✅ Fully responsive design
- ✅ Custom fonts (Negrita Pro, Rokkitt)
- ✅ Google Fonts (Roboto) as fallback
- ✅ All images and assets included
- ✅ No dependencies required
- ✅ Works offline

## Deployment

You can deploy this to any static hosting service:

- **Netlify**: Drag and drop the folder
- **Vercel**: Connect your Git repository
- **GitHub Pages**: Push to a repository and enable Pages
- **Surge.sh**: `surge . your-domain.surge.sh`

## Notes

- All paths are relative, so the folder structure must remain intact
- The `static/` folder must be in the same directory as `index.html`
- Fonts are loaded from the `static/fonts/` directory
- Images are loaded from the `static/images/` directory
