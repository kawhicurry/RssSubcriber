import os
import sys
import getopt
import configparser

import local


def init():
    pass
    # parse command options
    parse_opt()
    # get init value
    init_value()


def init_value():
    if local.settings['src_path'] == '':
        local.settings['src_path'] = os.path.join(
            os.getcwd(), 'src.ini')
    config = configparser.ConfigParser()
    config.read(local.settings['src_path'])
    for option, value in config.items('settings'):
        if local.settings[option] != '':
            local.settings[option] = value
    for option, value in config.items('sources'):
        local.sources[option] = value
    pass


def parse_opt():
    def check(path):
        if not os.path.exists(path):
            print(path, 'not available')
            exit(1)

    options, args = getopt.getopt(sys.argv[1:], "hvVi:d:o:cC", [
        "version", "help", "config=", "database=", "output=", "clean-out", "clean-db", "clean-all"])
    for opt_name, opt_value in options:
        if opt_name in ('-h', '--help'):
            help()
            return
        elif opt_name in ('-v', '-V', '--version'):
            version()
            return
        elif opt_name in ('-i', '--config'):
            check(opt_value)
            local.settings['src_path'] = opt_value
        elif opt_name in ('-d', '--database'):
            check(opt_value)
            local.settings['db_path'] = opt_value
        elif opt_name in ('-o', '--output'):
            check(opt_value)
            local.settings['out_path'] = opt_value
        elif opt_name in ('-s', '--specific'):
            pass
        elif opt_name in ('-c', '--clean-out'):
            local.clean_out()
        elif opt_name in ('--clean-db'):
            local.clean_db()
        elif opt_name in ('-C', '--clean-all'):
            local.clean_all()
    pass


def help():
    version()
    print("""
    -h  --help       show help
    -v
    -V  --version    show version information
    -i  --config     set config file
    -d  --database   set database directory
    -o  --output     set output directory
    -s  --specific   specific a source to parse
        --clean-out  clean output directory
        --clean-db   clean database
    -C  --clean-all  clean all database and output""")
    # show help message


def version():
    print("RssSubversion v0.2 beta")
    pass
    # show version message
