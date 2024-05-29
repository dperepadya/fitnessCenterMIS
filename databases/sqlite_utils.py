import sqlite3


class SQLLiteDatabase:
    def __init__(self, dp_path):
        self.db_path = dp_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def fetch(self, query, fetch_all=True):
        cursor = self.conn.cursor()
        cursor.execute(query)
        if fetch_all:
            return cursor.fetchall()
        return cursor.fetchone()

    def commit(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

