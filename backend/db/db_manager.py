from sqlmodel import create_engine, Session
import os

from backend import config

class DatabaseHandler:
    def __init__(self):
        db_path = os.path.join(config.DB_DIR, config.DB_NAME).replace("\\", "/")
        self.db_url = f"sqlite:///{db_path}"
        self.engine = create_engine(self.db_url, echo=True)

    def get_session(self):
        return Session(self.engine)
