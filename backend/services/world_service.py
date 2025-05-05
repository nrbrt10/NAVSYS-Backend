from backend.schemas.world import DxInstance_All, PointsOfInterest_Create

from backend.db.db_manager import DatabaseHandler
db = DatabaseHandler()

def create_dx(dx_instances: list[DxInstance_All]):
    with db.get_session() as session:
        try:
            session.add_all(dx_instances)
            session.commit()
            for dx in dx_instances: session.refresh(dx)
            return dx_instances
        except Exception as e:
            print(e)

def create_poi(pois: list[PointsOfInterest_Create]):
    with db.get_session() as session:
        try:
            session.add_all(pois)
            session.commit()
            for poi in pois: session.refresh(poi)
            return pois
        except Exception as e:
            print(e)