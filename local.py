import feedparser
import os


# ----- get sources from source file -----
def read_src(src_path):
    fp = open(src_path, 'r+')
    lst = []
    for line in fp:
        if line[-1] == '\n':
            lst.append(line[:-1])
        else:
            lst.append(line)
    fp.close()
    return lst


# ----- check data, avoid duplicate -----
def parse_url(source):
    rss = feedparser.parse(source)
    name = read_name(source)
    db_path = read_db_path(name)
    output_path = read_output_path(name)
    for i in range(len(rss.entries)):
        if has_record_by_title(db_path, rss.entries[i].title):
            continue
        add_record(db_path, rss.entries[i].title)
        output_add_title(output_path, rss.entries[i])


# ----- select or establish database file -----
def read_db_path(name):
    db_path = 'data/' + name + '.db'
    if not os.path.exists(db_path):
        fp = open(db_path, 'w')
        fp.close()
    return db_path


def read_output_path(name):
    output_path = 'out/' + name + '.md'
    if not os.path.exists(output_path):
        fp = open(output_path, 'w')
        fp.close()
    return output_path


def read_name(source):
    beg = source.find("://") + 3
    end = source.find(".", beg)
    return source[beg:end]


def has_record_by_title(db_path, title):
    fp = open(db_path, 'r+', encoding='utf-8')
    for line in fp:
        if line[:-1] == title:
            fp.close()
            return True
    fp.close()
    return False


def add_record(db_path, title):
    reverse_add(title + '\n', db_path)


# ----- output useful information -----


def output_add_title(out_path, entry):
    obverse_add(entry.published + ': [' + entry.title + '](' + entry.link + ')\n\n', out_path)


# ----- clean database information -----
def clean(src_path):
    for source in read_src(src_path):
        os.remove(read_db_path(read_name(source)))
        os.remove(read_output_path(read_name(source)))


# ----- write to some files -----
def obverse_add(content, destination):
    fp = open(destination, 'a+', encoding='utf-8')
    old = fp.read()
    fp.seek(0)
    fp.write(content)
    fp.write(old)
    fp.close()


def reverse_add(content, destination):
    fp = open(destination, 'r+', encoding='utf-8')
    old = fp.read()
    fp.seek(0)
    fp.write(content)
    fp.write(old)
    fp.close()
