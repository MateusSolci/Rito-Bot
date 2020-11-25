from Database_Controller.connection import Connection


def get_latest_version():
    db = Connection()
    db.query(
        "select * from tabela_info " +
        "order by versao desc limit 1"
    )
    response = db.cur.fetchone()
    return response


def get_version_details(version: str):
    db = Connection()
    try:
        db.cur.execute("""
            select versao, data_versao, detalhes_versao from tabela_info
            where versao like %s
            """, (version,)
        )
        response = db.cur.fetchone()
    except Exception as err:
        print(err)
        response = None
    return response


def get_level_by_summoner_id(discord_id, summoner_id):
    db = Connection()
    try:
        db.cur.execute(
            """
            select id_summoner, level_consultado, discord_id, ultima_consulta
            from tabela_user
            where id_summoner like %s and discord_id like '%s'
            """, (summoner_id, discord_id)
        )
        response = db.cur.fetchone()
    except Exception as err:
        print(err)
        response = None
    return response


def update_last_search(discord_id, summoner_id, summoner_level, date):
    db = Connection()
    
    try:
        db.cur.execute("""
            insert into tabela_user(id_summoner, level_consultado, discord_id, ultima_consulta)
            values (%s, %s, %s, %s)
            on conflict on constraint consulta
            do update set level_consultado = EXCLUDED.level_consultado,
            ultima_consulta = EXCLUDED.ultima_consulta
        """, (summoner_id, summoner_level, discord_id, date)
        )
        db.conn.commit()
    except Exception as err:
        print(err)
