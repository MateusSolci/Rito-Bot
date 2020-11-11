# -*- coding: utf-8 -*-


# Uncomment should_run if this is a repeat migration
# def should_run(cursor):
#     # TODO return True if migration should run


def up(cursor):
    cursor.execute("""
    ALTER TABLE tabela_user
    ALTER COLUMN discord_id type varchar;
    """)


def down(cursor):
    # TODO rollback code
    pass
