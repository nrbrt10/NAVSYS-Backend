from backend.schemas.gpsdata import GPSData
from backend.schemas.world import DxInstance_All, PointsOfInterest_Create

from backend.services.world_service import create_dx, create_poi

def decode_gps_string(gps: str):
    import re

    data = gps.split(':')
    gps_data = {
        'name': data[1],
        'x': data[2],
        'y': data[3],
        'z': data[4]
    }

    label = data[6] if len(data) == 7 else None
  
    match = re.search(r'R:(\d+)km', gps_data.get('name', ''))
    if match:
        gps_data['radius'] = int(match.group(1)) * 1000
    else:
        gps_data['radius'] = None
    
    return gps_data

def partitionby_type(decoded_gps: list[tuple[str, dict]]):
    dx = [DxInstance_All(**gps[1]) for gps in decoded_gps if gps[0] == 'dx']
    poi = [PointsOfInterest_Create(**gps[1]) for gps in decoded_gps if gps[0] == 'poi']

    return dx, poi

def process_gpsdata(data: list[GPSData]):
    decoded_gps = [(obj.type, decode_gps_string(obj.gps)) for obj in data]
    dx, poi = partitionby_type(decoded_gps)

    try:
        if len(dx) > 0:
            create_dx(dx)

        if len(poi) > 0:
            create_poi(poi)
    except Exception as e:
        print(e)

    return 0

""" def __process_gpsdata(gps: list[GPSData]): #to be superseded?
    decoded_gps = [(gps_obj, decode_gps(gps_obj)) for gps_obj in gpsdata]
    assigned_gpsdata = [assign_xyz(gpsdata[0], gpsdata[1]) for gpsdata in decoded_gps]

    dx, poi = partitionby_type(assigned_gpsdata)

    try:
        if len(dx) > 0:
            create_dx(dx)

        if len(poi) > 0:
            create_poi(poi)
    except Exception as e:
        print(e)

def __process_gpsdata2(gpsdata: list[GPSData]):
    gpsdata_with_xyz = (
        assign_xyz(gps, decoded)
        for gps, decoded in (
            (gpsdata_obj, decode_gps(gpsdata_obj)) for gpsdata_obj in gpsdata
            )
        )
    
    dx, poi = partitionby_type(list(gpsdata_with_xyz))

    try:
        if len(dx) > 0:
            dx_models = create_dx(dx)

        if len(poi) > 0:
            poi_models = create_poi(poi)
        
        if dx_models and poi_models:
            return dx_models, poi_models
        elif dx_models and not poi_models:
            return dx_models, None
        elif not dx_models and poi_models:
            return None, poi_models
        
    except Exception as e:
        print(e) """