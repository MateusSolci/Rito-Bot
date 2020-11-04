from Database_Controller.connection import Connection

def get_latest_version():
    db = Connection()
    db.query(
        "select * from tabela_info " +
        "order by versao desc limit 1"
    )
    response = db.cur.fetchone()
    return response


def get_version_details(version):
    db = Connection()
    try:
        db.cur.execute("""
            select versao, data_versao, detalhes_versao from tabela_info
            where versao like %s
            """, (version,)
        )
        response = db.cur.fetchone()
    except:
        response = None
    return response
