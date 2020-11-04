from Database_Controller.connection import Connection

def get_latest_version():
    db = Connection()
    db.query(
        "select * from tabela_info " +
        "order by versao desc limit 1"
    )
    response = db.cur.fetchone()
    return response
