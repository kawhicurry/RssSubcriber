import os
import configparser

settings = {'src_path': '', 'db_path': '', 'out_path': ''}


# ----- get sources from source file -----
def read_urls():
    global src_path
    fp = open(src_path, 'r+')
    urls = []
    for line in fp:
        if line[-1] == '\n':
            urls.append(line[:-1])
        else:
            urls.append(line)
    fp.close()
    return urls

# ----- end -----
# ----- clean database information -----


def clean():
    clean_db()
    clean_src()


def clean_db():
    global db_path
    os.remove(db_path+'/*')


def clean_src():
    global db_path
    os.remove(src_path+'/*')
# ----- end -----
# ----- write to some files -----


def add_output(entry):
    global src_path
    obverse_add(entry.published +
                ': [' + entry.title + '](' + entry.link + ')\n\n', out_path)


def add_record(entry):
    global db_path
    reverse_add(entry.title + '\n', db_path)


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
