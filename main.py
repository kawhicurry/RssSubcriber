#!/usr/bin/python3
from local import *
from command import *


def main():
    pass
    src_path = init()
    sources = read_src(src_path)
    for source in sources:
        parse_url(source)


if __name__ == '__main__':
    main()
