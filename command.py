import getopt
import os
import sys
from local import clean


def init():
    flag = 0
    src_path = './src.md'
    options, args = getopt.getopt(sys.argv[1:], "vhd:o:c", ["version", "help", "db=", "output=", "clean"])
    for opt_name, opt_value in options:
        if opt_name in ('-h', '--help'):
            show_help()
        if opt_name in ('-v', '--version'):
            show_version()
        if opt_name in ('-i', '--config'):
            src_path = opt_value
        if opt_name in ('-o', '--output'):
            os.chdir(opt_value)
        if opt_name in ('-c', '--clean'):
            flag = 1
    if flag == 1:
        clean(src_path)
        exit(0)
    return src_path


def show_help():
    show_version()
    print("""
    -h --help       show help
    -v --version    show version information
    -i --config     set database location
    -o --output     set output location
    -c --clean      clean all db and output""")


def show_version():
    print("version : 0.1 beta")
