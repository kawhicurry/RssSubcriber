# !/usr/bin/python3
import command
import local
import feed


def main():
    pass
    command.init()
    urls = local.read_urls()
    for url in urls:
        print(url)
        feed.parse_url(url)


if __name__ == '__main__':
    main()
