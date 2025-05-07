from fastapi import HTTPException
from backend.models.world import DxInstance, PointsOfInterest

from backend.db.db_manager import DatabaseHandler
db = DatabaseHandler()

def create_dx(dx_instances: list[DxInstance]):
    try:
        dx_instances = db.batch_insert(dx_instances)
        return dx_instances
    except Exception as e:
        print(e)
            

def create_poi(pois: list[PointsOfInterest]):
    try:
        pois = db.batch_insert(pois)
        return pois
    except Exception as e:
        print(e)