# Personal Blog Website

A modern, minimalist static blog generator that creates a feature-rich website from markdown files. Built with vanilla JavaScript and Python, focusing on clean design and enhanced reading experience.

## Key Features

### Content Management
- **Markdown-Based**: Write blog posts in markdown with YAML frontmatter
- **Tags & Series**: Organize content with tags and group related posts into series
- **Backlinks**: Automatic bi-directional linking between related posts
- **Static Generation**: Fast, secure, and SEO-friendly static HTML pages

### User Experience
- **Dark Mode**: System-aware theme with toggle switch
- **Reading Progress**: Visual indicator of reading progress
- **Table of Contents**: Auto-generated, hierarchical navigation
- **Responsive Design**: Mobile-first, clean interface

## Project Structure

```
├── src/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── dark-mode.js
│       ├── site-config.js
│       ├── load-nav.js
│       ├── load-blog-list.js
│       ├── toc-generator.js
│       └── progress-bar.js
├── data/
│   ├── blog_data.json
│   ├── series_data.json
│   └── tags_data.json
├── blogs/
│   ├── *.md (markdown files)
│   └── *.html (generated blog pages)
├── templates/
│   ├── blog-template.html
│   └── blogs-listing-template.html
├── index.html
├── about.html
├── blogs.html
├── series.html
├── tags.html
├── navigation.html
├── requirements.txt
├── generate_blog_pages.py
└── README.md
```

## Quick Start

1. **Setup**
   ```bash
   # Clone repository
   git clone [repository-url]
   cd [repository-name]

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Create Content**
   ```markdown
   # blogs/my-post.md
   ---
   tags: tech, tutorial
   series: getting-started
   series_part: 1
   ---
   # My First Blog Post
   Content goes here...
   ```

3. **Generate Site**
   ```bash
   python3 generate_blog_pages.py

4. **Preview Locally**
   ```bash
   python3 -m http.server
   ```
   Then open `http://localhost:8000`.
   ```

## Writing Posts

### Frontmatter Options
```markdown
---
tags: tag1, tag2          # Comma-separated tags
series: series-name       # Optional series name (leave empty to exclude from series page)
series_part: 1           # Optional series part number
---
```

### Supported Features
- Standard Markdown syntax
- Inline annotations with `[[word]]`
- Image references from `assets/` directory
- Internal links between posts
- Code blocks with syntax highlighting

## Development

### Prerequisites
- Python 3.7+
- Web browser (Chrome/Firefox/Safari/Edge latest versions)
- Basic knowledge of HTML, CSS, and JavaScript

### Dependencies
- `markdown`: Markdown to HTML conversion
- `beautifulsoup4`: HTML processing

## Customization

### Styling
Edit `src/css/styles.css` to modify:
- Color schemes (light/dark modes)
- Typography and spacing
- Layout and responsive breakpoints

### Templates
Modify templates in `templates/` to change:
- Page structure
- Navigation elements
- Meta tags and SEO elements

### Site Identity (Single Source)
Edit `src/js/site-config.js` to change site-wide identity settings:
- `ownerName`: used in footer and dynamic page titles
- `siteTitle`: used in page headers

The site also uses `resolvePath()` in `site-config.js` to keep navigation/data loading stable across local preview and GitHub Pages.

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[MIT]

## Author
@simoncos

---
Built with vanilla JavaScript and Python. No frameworks, no complexity. 