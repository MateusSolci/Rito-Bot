import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Connection(object):
    _db = None


    def __init__(self):
        self._db = psycopg2.connect(host = os.environ["host"],
        database = os.environ["database"],
        user = os.environ["db_user"],
        password = os.environ["db_passwd"])


