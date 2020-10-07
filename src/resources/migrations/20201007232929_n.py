# -*- coding: utf-8 -*-


# Uncomment should_run if this is a repeat migration
# def should_run(cursor):
#     # TODO return True if migration should run


def up(cursor):
    # TODO migration code
    cursor.execute('CREATE TABLE tabela_info(' +
    'data_versao date,' +
    'versao varchar(10) PRIMARY KEY,' +
    'quantidade_usuarios int,' +
    'info_time_dev varchar(1000),' +
    'detalhes_versao text)')

    # if a super user database connection is needed
    # from dbmigrator import super_user
    # with super_user() as super_cursor:
    #     pass


def down(cursor):
    # TODO rollback code
    pass
