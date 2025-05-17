from backend.models import grids
from backend.db.db_manager import DatabaseHandler

class GridsService:
    def __init__(self):
        self.db = DatabaseHandler()