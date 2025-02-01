# Personal Blog Website

A modern, feature-rich static blog website with clean design and enhanced user experience.

## Features

### Core Functionality
- Static blog generation from markdown files
- Clean and responsive design
- Navigation system with active page highlighting
- Dynamic blog listing with dates and previews
- Automatic copyright year updates

### Content Organization
- **Tags System**
  - Tag-based post organization
  - Tag cloud visualization
  - Filtered post viewing by tag

- **Series System**
  - Group related posts into series
  - Automatic series navigation
  - Series progress tracking

- **Backlinks**
  - Automatic backlink generation
  - Two-way post linking
  - Reference tracking

### Reading Experience
- **Table of Contents**
  - Auto-generated from headings
  - Smooth scroll navigation
  - Hierarchical structure
  - Dynamic highlighting

- **Progress Bar**
  - Reading progress indicator
  - Smooth animations
  - Adaptive colors for dark/light modes
  - Fixed position for easy tracking

- **Dark Mode**
  - System preference detection
  - Toggle button in header
  - Persistent preference saving
  - Optimized color schemes

### Technical Features
- Markdown support with extended syntax
- JSON-based data management
- Automated page generation
- Client-side JavaScript enhancements
- CSS-based theming system

## File Structure 

```
├── assets/
│ ├── css/
│ │ ├── styles.css
│ │ └── ...
│ └── js/
│ ├── dark-mode.js
│ ├── toc-generator.js
│ ├── progress-bar.js
│ └── ...
├── blogs/
│ └── (markdown files)
├── templates/
│ ├── blog-template.html
│ └── ...
└── data/
├── blog_data.json
├── tags_data.json
└── series_data.json
```

## Technologies Used
- HTML5
- CSS3
- JavaScript (Vanilla)
- Python (for static site generation)
- Markdown
- JSON

## Setup and Usage

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add markdown files to the `blogs/` directory
4. Run the blog generator:
   ```bash
   python generate_blog_pages.py
   ```

## Blog Post Format

```markdown
---
tags: tag1, tag2
series: series_name
series_part: 1
---
Post Title
Content goes here...
```

## Customization

### Theme Colors
Main colors can be customized in `styles.css`:
- Light mode colors
- Dark mode colors
- Progress bar gradients
- Link and accent colors

### Templates
Blog templates can be modified in the `templates/` directory to change:
- Page layout
- Header/footer content
- Navigation structure

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing
Feel free to submit issues and enhancement requests.

## License
[Your chosen license]

## Author
[Your Name] 