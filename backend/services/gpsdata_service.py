import re
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional

from backend.schemas.gpsdata import GPSData
from backend.models.world import DxInstance, PointsOfInterest
from backend.schemas.world import DxInstance_Read, PointsOfInterest_Read
from backend.services.world_service import create_dx, create_poi

class Response(BaseModel):
    dx: Optional[list[DxInstance_Read]] = None
    pois: Optional[list[PointsOfInterest_Read]] = None

def decode_gps_string(gps: str, radius: float):

    data = gps.split(':')
    if len(data) < 6:
        raise ValueError(f'Malformed GPS string: {gps}')
    gps_data = {
        'name': data[1],
        'x': data[2],
        'y': data[3],
        'z': data[4],
        'color': data[5],
        'gps' : gps
    }

    label = data[6] if len(data) >= 7 else None
    is_dx = re.search(r'(DX\d)', label) if label is not None else None
    if is_dx:
        gps_data['dx'] = str(is_dx.group(1)).lower()
  
    has_radius = re.search(r'R(\d+)km', gps_data.get('name', ''))
    if has_radius:
        gps_data['radius'] = int(has_radius.group(1)) * 1000
    elif radius:
        gps_data['radius'] = radius
    else:
        gps_data['radius'] = 1000
    return gps_data

def partition_by_type(decoded_gps: list[tuple[str, dict]]):
    dx = [DxInstance(**data) for type, data in decoded_gps if type == 'dx']
    
    poi = [PointsOfInterest(**data) for type, data in decoded_gps if type == 'poi']
    
    return dx, poi

def normalize_gps_data(data: list[GPSData]):
    decoded_gps = [(obj.type, decode_gps_string(obj.gps, obj.radius)) for obj in data]
    dx, poi = partition_by_type(decoded_gps)

    try:
        dx_models = create_dx(dx) if len(dx) > 0 else None

        pois_models = create_poi(poi)if len(poi) > 0 else None
            
        return Response(dx=dx_models, pois=pois_models)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))