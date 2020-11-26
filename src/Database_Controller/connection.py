import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class SingletonMeta(type):

    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Connection(metaclass=SingletonMeta):

    def __init__(self):
        self.conn = psycopg2.connect(host=os.environ["PGHOST"],
                                     database=os.environ["PGDATABASE"],
                                     user=os.environ["PGUSER"],
                                     password=os.environ["PGPASSWORD"])
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


