import pathlib
from xml.etree.ElementTree import ElementTree, Element

SCHEMA = "http://www.sitemaps.org/schemas/sitemap/0.9"

def format_url(base_url, path):
    file = base_url/path
    return file.as_posix()


class Sitemap:
    def __init__(self, path, base_url):
        self.local_path = pathlib.Path(path)
        self.base_url = base_url
        self.files = []
        self.root_elem = Element('urlset', xmlns=SCHEMA)
        self.sitemap = ElementTree(self.root_elem)

    def crawl(self):
        for f in self.local_path.glob("**/*.html"):
            if f.is_file() and f not in self.files:
                self.files.append(f.relative_to(self.local_path))

    def make_xml(self):
        for f in self.files:
            elem = Element('url')
            loc = Element('loc')
            loc.text = format_url(self.base_url, f)
            elem.append(loc)
            self.root_elem.append(elem)

    def make_sitemap(self, file):
        self.crawl()
        self.make_xml()
        self.sitemap.write(file, encoding="utf-8", xml_declaration=True)
