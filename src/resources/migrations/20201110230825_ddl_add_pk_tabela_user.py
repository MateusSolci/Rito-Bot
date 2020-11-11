# -*- coding: utf-8 -*-


# Uncomment should_run if this is a repeat migration
# def should_run(cursor):
#     # TODO return True if migration should run


def up(cursor):
    cursor.execute(
        """
        ALTER TABLE tabela_user
        DROP COLUMN id_consulta;
        ALTER TABLE tabela_user
        ADD CONSTRAINT consulta PRIMARY KEY (id_summoner, discord_id)
        """
    )


def down(cursor):
    # TODO rollback code
    pass
