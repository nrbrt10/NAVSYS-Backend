from backend.schemas.gpsdata import GPSData
from backend.models.world import DxInstance, PointsOfInterest

from backend.services.world_service import create_dx, create_poi
from fastapi import HTTPException

def decode_gps_string(gps: str, radius: float):
    import re

    data = gps.split(r':')
    gps_data = {
        'description': data[1],
        'x': data[2],
        'y': data[3],
        'z': data[4],
        'gps' : gps
    }

    label = data[6] if len(data) >= 7 else None
    is_dx = re.search(r'(DX\d)', label) if label is not None else None
    if is_dx:
        gps_data['name'] = str(is_dx.group(1)).lower()
  
    has_radius = re.search(r'R(\d+)km', gps_data.get('description', ''))
    if has_radius:
        gps_data['radius'] = int(has_radius.group(1)) * 1000
    else:
        gps_data['radius'] = radius
    return gps_data

def partitionby_type(decoded_gps: list[tuple[str, dict]]):
    dx = [DxInstance(**gps[1]) for gps in decoded_gps if gps[0] == 'dx']
    
    poi = [PointsOfInterest(**gps[1]) for gps in decoded_gps if gps[0] == 'poi']
    
    return dx, poi

def process_gpsdata(data: list[GPSData]):
    decoded_gps = [(obj.type, decode_gps_string(obj.gps, obj.radius)) for obj in data]
    dx, poi = partitionby_type(decoded_gps)

    try:
        if len(dx) > 0:
            create_dx(dx)
        if len(poi) > 0:
            create_poi(poi)
    except Exception as e:
        raise HTTPException(e)

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