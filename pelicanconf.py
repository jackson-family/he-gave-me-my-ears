import json
import os
import pathlib

package_json = json.loads(pathlib.Path("package.json").read_text())
BOOTSTRAP_VERSION = package_json.get("dependencies").get("bootstrap")

SITEURL = os.getenv("SITEURL", "https://he-gave-me-my-ears.subtlecoolness.com")

ARCHIVES_SAVE_AS = ""
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{urlname}.html"
ARTICLE_URL = ARTICLE_SAVE_AS
AUTHOR = "Rebecca J"
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CACHE_PATH = "cache"
CATEGORIES_SAVE_AS = ""
CATEGORY_FEED_ATOM = None
CATEGORY_SAVE_AS = ""
CHECK_MODIFIED_METHOD = "md5"
DEBUG_LAYOUT = True
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
EXTRA_PATH_METADATA = {"images/gitignore.txt": {"path": ".gitignore"}}
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_DOMAIN = SITEURL
GZIP_CACHE = True
LOAD_CONTENT_CACHE = True
PATH = "content"
RELATIVE_URLS = True
SITENAME = "He Gave Me My Ears That I Might Hear"
SLUGIFY_SOURCE = "basename"
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
THEME = "themes/default"
TIMEZONE = "America/Chicago"
TRANSLATION_FEED_ATOM = None
