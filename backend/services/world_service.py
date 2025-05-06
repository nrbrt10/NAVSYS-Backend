from fastapi import HTTPException
from backend.schemas.world import DxInstance_All, PointsOfInterest_Create

from backend.db.db_manager import DatabaseHandler
db = DatabaseHandler()

def create_dx(dx_instances: list[DxInstance_All]):
    try:
        dx_instances = db.batch_insert(dx_instances)
        return dx_instances
    except Exception as e:
        print(e)
            

def create_poi(pois: list[PointsOfInterest_Create]):
    try:
        pois = db.batch_insert(pois)
        return pois
    except Exception as e:
        print(e)