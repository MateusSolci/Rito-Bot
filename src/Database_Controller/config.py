import configparser
import os

config = configparser.ConfigParser()
config.read('development.ini')
context = 'Rito-Bot'
connection_string = os.environ.get('DATABASE_URL')
migrations_directory = config.get('dbconfig', 'migrations-directory')
print(connection_string)
