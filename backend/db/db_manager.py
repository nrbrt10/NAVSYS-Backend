import sqlite3
import os

from backend import config

class DatabaseHandler:
    def __init__(self, path):
        self.path = path

    @classmethod
    def init_db(self):
        path = os.path.join(config.DB_DIR, config.DB_NAME)
        if (path):
            with sqlite3.connect(path) as conn:
                conn.execute("select sqlite_version();")

        self.path = path

    async def run_query(self, query: str):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query)
