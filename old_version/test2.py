import configparser
import os
config = configparser.ConfigParser()
config.read(os.getcwd()+'\src.ini')
settings = {'src_path': '', 'db_path': '', 'out_path': ''}
paths = {'src_path', 'db_path', 'output_path'}
for path in paths:
    settings[path] = config.get('settings', path)
print(settings)
