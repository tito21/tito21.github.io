
import subprocess
import pathlib
import shutil
import frontmatter
import yaml

from src.utils import *
from src.sitemap_generator import Sitemap

path_root = pathlib.Path('.')
path_site = pathlib.Path('site')
path_posts = pathlib.Path('_posts')
path_tmp = pathlib.Path('tmp')

path_site.mkdir(exist_ok=True)
path_tmp.mkdir(exist_ok=True)

args = {
    "template": "template/index.html",
    "mathjax": "",
    "metadata-file": "tmp/config.yml",
    "highlight-style": "breezeDark"
}


with open("config.yml", 'r') as f:
    config = yaml.safe_load(f)


def build_posts(post_files):
    """Returns a list of dicts with metadata from each post"""
    posts = []
    for p in post_files:
        out = site_posts / p.with_suffix(".html").name
        run_pandoc(p.as_posix(), out.as_posix(), args=args)
        with open(p, encoding='utf_8') as f:
            metadata, content = frontmatter.parse(f.read())
        p_data = {
            'title' : metadata['title'],
            'categories' : metadata['categories'],
            'description' : metadata['description'],
            'date' : format_time(metadata['date']),
            'url' : out.relative_to(path_site).as_posix(),
            'metadata' : metadata
        }
        posts.append(p_data)
    return posts

def build_front_page(input_file, output_file, posts):
    with open(path_tmp/"post.yml", 'w', encoding='utf_8') as f:
        f.write(yaml.dump({'posts': posts[::-1]}))

    # build the list of posts
    # shutil.copy(path_root/'index.md', path_tmp/'index.md')
    # use index.md as a template to fill in the posts as metadata
    cost_arg = {
        'template': str(input_file),
        'metadata-file': str(path_tmp/'post.yml')
    }
    run_pandoc(input_file, path_tmp/'index.md', cost_arg)
    # Build the post page.
    run_pandoc(path_tmp/"index.md", output_file, args)



pages = list(filter(lambda x: not x.name == 'index.md', path_root.glob('*.md')))

nav_pages = []
for p in pages:
    with open(p, encoding='utf-8') as f:
        metadata, content = frontmatter.parse(f.read())
        if metadata['nav']:
            nav_pages.append(p)

print("Nav pages: {}".format(nav_pages))

nav_items = {'nav-items': [{'name' : p.stem.capitalize(),
                                      'url': p.with_suffix(".html").name }
                                     for p in nav_pages ] }

shutil.copy(path_root/'config.yml', path_tmp/'config.yml')
with open(args['metadata-file'], 'a') as f:
    f.write(yaml.dump(nav_items))


post_files = path_posts.glob('*.md')
site_posts = path_site / "posts"
site_posts.mkdir(exist_ok=True)
posts = build_posts(post_files)

build_front_page(path_root/"index.md", path_site/"index.html", posts)
print("Build {} post".format(len(posts)))

categories = list_categories(posts)

for p in pages:
    with open(p, encoding='utf_8') as f:
        metadata, content = frontmatter.parse(f.read())
    out = path_site / p.with_suffix(".html").name
    run_pandoc(p.as_posix(), out.as_posix(), args=args)

print("Build {} pages".format(len(pages)))

shutil.copy(path_root/'template/style.css', path_site/'assets')

print("Site generated at {}".format(path_site))

sitemap = Sitemap(path_site, config['site-root'])
sitemap.make_sitemap(path_site/'sitemap.xml')
with open(path_site/'robots.txt', 'w') as f:
    f.write("Sitemap: {}/sitemap.xml\n".format(config['site-root']))

print("sitemap.xml and robots.txt generated")
