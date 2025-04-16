from sqlmodel import create_engine, Session, SQLModel
import os

from backend import config
from backend.models import grids, combat_events

class DatabaseHandler:
    def __init__(self):
        db_path = os.path.join(config.DB_DIR, config.DB_NAME).replace("\\", "/")
        self.db_url = f"sqlite:///{db_path}"
        self.engine = create_engine(self.db_url, echo=True)

    def get_session(self):
        return Session(self.engine)
    
    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def drop_tables(self):
        SQLModel.metadata.drop_all(self.engine)

if __name__ == '__main__':
    db_handler = DatabaseHandler()
    db_handler.create_tables()