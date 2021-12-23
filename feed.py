import feedparser
import local


def parse_url():
    for name, source in local.sources:
        feedparser.parse(source)
    pass
    # get xml and parse it
    # get json information
    # save to markdown
