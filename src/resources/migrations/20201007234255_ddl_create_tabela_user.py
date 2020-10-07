# -*- coding: utf-8 -*-


# Uncomment should_run if this is a repeat migration
# def should_run(cursor):
#     # TODO return True if migration should run


def up(cursor):
    # TODO migration code
    cursor.execute(
        'CREATE TABLE tabela_user(' +
        'ID_consulta int PRIMARY KEY,' +
        'ID_summoner int,' +
        'level_consultado int,' +
        'regiao varchar(30),' +
        'ultima_consulta date);'
    )

    # if a super user database connection is needed
    # from dbmigrator import super_user
    # with super_user() as super_cursor:
    #     pass


def down(cursor):
    # TODO rollback code
    pass
