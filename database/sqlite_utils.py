import sqlite3

from utils.converters import Converter as cnvrt


class SQLLiteDatabase:
    def __init__(self, dp_path, timeout=5.0):
        self.db_path = dp_path
        self.conn = None

        self.timeout = timeout

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path, timeout=self.timeout)
        self.conn.row_factory = cnvrt.dict_factory
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def fetch(self, query, fetch_all=True, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        # print(query)
        if fetch_all:
            res = cursor.fetchall()
        else:
            res = cursor.fetchone()
        # print('res', res)
        return res

    def save(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return True


