import getopt
import os
import sys
import local
import configparser


def init():
    flag = 0
    try:
        config = configparser.ConfigParser()
        config.read(os.getcwd()+'\src.md')
        paths = {'src_path', 'db_path', 'output_path'}
        for path in paths:
            local.settings[path] = config.get('settings', path)
    except configparser.ParsingError:
        print("can not read settings file")
    except configparser.NoOptionError:
        print("cannot find options")

    options, args = getopt.getopt(sys.argv[1:], "vhd:o:c", [
                                  "version", "help", "db=", "output=", "clean"])
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
        local.clean(local.src_path)
        exit(0)


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
