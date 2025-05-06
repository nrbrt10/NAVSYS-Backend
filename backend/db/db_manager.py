import os

from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.exc import IntegrityError

from backend import config
from backend.models import grids, combat_events, world

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

    def batch_insert(self, data: list[object], batch_size=1000, max_retries=2):
        successful = []
        errors = []
        retry_count = 0
        while data and retry_count < max_retries:
            for batch in self.batch_gen(data, batch_size):
                try:
                    with self.get_session() as session:
                        session.add_all(batch)
                        session.commit()
                        for row in batch: session.refresh(row)
                        successful.extend(batch)
                        
                except IntegrityError as e:
                    print(f'Error on batch {batch}: {e}')
                    if batch_size > 1:
                        batch_size //= 2
                    elif batch_size == 1:
                        errors.extend(batch)
                        
            if not errors:
                break

            data = errors
            errors = []
            retry_count += 1

        return successful

    @staticmethod
    def batch_gen(data: list, batch_size: int):
        for i in range(0, len(data), batch_size):
            yield data[i: i + batch_size]

if __name__ == '__main__':
    db_handler = DatabaseHandler()
    db_handler.drop_tables()
    db_handler.create_tables()