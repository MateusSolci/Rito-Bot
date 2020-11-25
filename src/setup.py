from setuptools import setup

setup(
    name='Rito-Bot',
    version='0.8',
    packages=['Test', 'resources', 'resources.migrations', 'API_Requests', 'Bot_Services', 'Database_Controller',
              'Database_Controller.models'],
    url='',
    license='',
    author='Giacomo, Lucas e Mateus',
    author_email='',
    description='',
    entry_points={
        'dbmigrator': [
            'migrations_directory = Database_Controller.config:migrations_directory',
            'db-connection-string = Database_Controller.config:connection_string',
            'context = Database_Controller.config:context',
        ],
    },
)
