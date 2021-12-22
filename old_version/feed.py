import feedparser
import os
import local


url_list = []

# ----- check data, avoid duplicate -----


def parse_url(url):
    rss = feedparser.parse(url)
    for i in range(len(rss.entries)):
        if has_record_by_title(local.db_path, rss.entries[i].title):
            continue
        local.add_record(rss.entries[i])
        local.add_output(rss.entries[i])

# ----- parse path and name -----


def name_to_db_path(name):
    db_path = 'data/' + name + '.db'
    if not os.path.exists(db_path):
        fp = open(db_path, 'w')
        fp.close()
    return db_path


def has_record_by_title(db_path, title):
    fp = open(db_path, 'r+', encoding='utf-8')
    for line in fp:
        if line[:-1] == title:
            fp.close()
            return True
    fp.close()
    return False


def name_to_output_path(name):
    output_path = 'out/' + name + '.md'
    if not os.path.exists(output_path):
        fp = open(output_path, 'w')
        fp.close()
    return output_path


def url_to_name(url):
    beg = url.find("://") + 3
    end = url.find(".", beg)
    return url[beg:end]
