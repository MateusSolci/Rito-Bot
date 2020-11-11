# -*- coding: utf-8 -*-


# Uncomment should_run if this is a repeat migration
# def should_run(cursor):
#     # TODO return True if migration should run


def up(cursor):
    cursor.execute(
        """
        ALTER TABLE tabela_user
        ADD COLUMN discord_id int;
        """
    )

    


def down(cursor):
    # TODO rollback code
    pass
