import configparser

config = configparser.ConfigParser()
config.read('development.ini')
connection_string = config['app:main']['db-connection-string']
migrations_directory = config.get('app:main', 'migrations-directory')
print(connection_string)
