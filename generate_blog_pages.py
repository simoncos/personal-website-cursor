import os
import re
import json
import markdown
from datetime import datetime
from collections import defaultdict
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from xml.etree import ElementTree
from bs4 import BeautifulSoup

class AnnotatePattern(InlineProcessor):
    def handleMatch(self, m, data):
        word = m.group(1)
        el = ElementTree.Element('span')
        el.set('class', 'annotated-word')
        el.set('data-word', word)
        el.text = word
        return el, m.start(0), m.end(0)

class AnnotatePreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            new_line = re.sub(r'\[\[(.*?)\]\]', r'<span class="annotated-word" data-word="\1">\1</span>', line)
            new_lines.append(new_line)
        return new_lines

class AnnotateExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(AnnotatePreprocessor(md), 'annotate', 175)

def parse_metadata(md_content):
    metadata = {}
    metadata_match = re.match(r'---\n(.*?)\n---\n', md_content, re.DOTALL)
    if metadata_match:
        metadata_str = metadata_match.group(1)
        print(f"Raw metadata string: {metadata_str}")
        for line in metadata_str.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
            else:
                print(f"Warning: Invalid metadata line - {line}")
        content = md_content[metadata_match.end():]
    else:
        print("Warning: No metadata section found")
        content = md_content
    return metadata, content

def find_links(content):
    return re.findall(r'\[([^\]]+)\]\(([^)]+\.html)\)', content)

def get_file_times(file_path):
    stats = os.stat(file_path)
    created = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
    updated = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    return created, updated

def update_image_paths(content):
    def replace_path(match):
        alt_text = match.group(1)
        old_path = match.group(2)
        new_path = old_path
        print(f"Debug: Image path: {new_path}")  # Debug output
        return f'![{alt_text}]({new_path})'

    pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.sub(pattern, replace_path, content)

def extract_title_and_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h1 = soup.find('h1')
    if h1:
        title = h1.text
        h1.extract()  # Remove the h1 from the content
        content = str(soup)
    else:
        title = "Untitled"
        content = html_content
    return title, content

def generate_blog_pages():
    tags_data = defaultdict(list)
    backlinks = defaultdict(list)
    series_data = defaultdict(list)
    blog_posts = []

    # Load the blog template
    with open('blog-template.html', 'r') as template_file:
        template = template_file.read()

    # Get all markdown files from the blogs folder
    markdown_files = [f for f in os.listdir('blogs') if f.endswith('.md')]

    # First pass: collect backlinks, tags, and generate HTML content
    for md_file in markdown_files:
        markdown_path = os.path.join('blogs', md_file)
        html_file = md_file.replace('.md', '.html')
        
        with open(markdown_path, 'r') as file:
            md_content = file.read()
            metadata, content = parse_metadata(md_content)
            
        content = update_image_paths(content)
        html_content = markdown.markdown(content, extensions=['markdown.extensions.fenced_code', AnnotateExtension()])
        
        title, html_content = extract_title_and_content(html_content)
        
        blog_posts.append({
            "title": title,
            "file": html_file,
            "markdown": md_file,
            "html_content": html_content
        })

        tags = metadata.get('tags', '').split(',')
        tags = [tag.strip() for tag in tags if tag.strip()]

        for tag in tags:
            tags_data[tag].append({
                'title': title,
                'file': html_file
            })

        links = find_links(content)
        for link_text, link_url in links:
            backlinks[link_url].append({"title": title, "file": html_file})

    # Second pass: generate pages and collect series data
    for post in blog_posts:
        markdown_path = os.path.join('blogs', post['markdown'])
        with open(markdown_path, 'r') as md_file:
            md_content = md_file.read()
            metadata, _ = parse_metadata(md_content)

        created, updated = get_file_times(markdown_path)

        tags = metadata.get('tags', '').split(',')
        tags = [tag.strip() for tag in tags if tag.strip()]
        tags_html = '<ul class="tag-list">' + ''.join([f'<li><a href="/tags.html#{tag}">{tag}</a></li>' for tag in tags]) + '</ul>'

        html_content = f"""
        <h1>{post['title']}</h1>
        <p class="post-meta">Created: {created} | Last Updated: {updated}</p>
        {post['html_content']}
        """

        page_content = template.replace('{{TITLE}}', post['title'])
        page_content = page_content.replace('{{CONTENT}}', html_content)
        page_content = page_content.replace('{{BACKLINKS}}', json.dumps(backlinks[post['file']]))
        page_content = page_content.replace('{{TAGS}}', tags_html)

        with open(os.path.join('blogs', post['file']), 'w') as f:
            f.write(page_content)

        if 'series' in metadata:
            series_data[metadata['series']].append({
                'title': post['title'],
                'file': post['file'],
                'part': metadata.get('series_part', '')
            })

    with open('series_data.json', 'w') as f:
        json.dump(series_data, f, indent=2)

    with open('tags_data.json', 'w') as f:
        json.dump(tags_data, f, indent=2)

    print("Blog pages and tags data generated successfully!")
    print("Tags data:", json.dumps(tags_data, indent=2))
    print("Backlinks data:", json.dumps(backlinks, indent=2))

    return blog_posts

def get_creation_date(file_path):
    return datetime.fromtimestamp(os.path.getctime(file_path))

def generate_blogs_page(blog_posts):
    # Sort blog posts by creation date (newest first)
    sorted_posts = sorted(blog_posts, key=lambda x: get_creation_date(os.path.join('blogs', x['markdown'])), reverse=True)
    
    # Group posts by month
    posts_by_month = defaultdict(list)
    for post in sorted_posts:
        date = get_creation_date(os.path.join('blogs', post['markdown']))
        month_key = date.strftime("%B %Y")
        posts_by_month[month_key].append(post)
    
    # Generate HTML content
    html_content = ""
    for month, posts in posts_by_month.items():
        html_content += f"<h3>{month}</h3>"
        for post in posts:
            with open(os.path.join('blogs', post['markdown']), 'r') as md_file:
                md_content = md_file.read()
                metadata, content = parse_metadata(md_content)
                excerpt = content.split('\n\n')[0][:200] + '...' if len(content) > 200 else content
            
            date = get_creation_date(os.path.join('blogs', post['markdown']))
            html_content += f"""
            <article class="blog-preview">
                <h4><a href="blogs/{post['file']}">{post['title']}</a></h4>
                <p class="post-meta">Posted on {date.strftime('%B %d, %Y')}</p>
                <p>{excerpt}</p>
                <a href="blogs/{post['file']}" class="read-more">Read more</a>
            </article>
            """
    
    # Write to blogs.html
    with open('blogs-listing-template.html', 'r') as template_file:
        template = template_file.read()
    
    page_content = template.replace('{{BLOG_LISTINGS}}', html_content)
    
    with open('blogs.html', 'w') as f:
        f.write(page_content)

if __name__ == "__main__":
    blog_posts = generate_blog_pages()
    generate_blogs_page(blog_posts)