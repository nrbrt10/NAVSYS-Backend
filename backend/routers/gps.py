from fastapi import APIRouter, HTTPException
from datetime import datetime

from backend.models.world import DxInstance, PointsOfInterest
from backend.schemas.gpsdata import GPSData
from backend.services.gpsdata_service import process_gpsdata

router = APIRouter()

@router.post("/api/v1/gps/", response_model=list[GPSData])
async def create_gps(gps_list: list[GPSData]):
    
    gpsdata = [GPSData(**data) for data in gps_list]

    try:
        process_gpsdata(gpsdata)
    except Exception as e:
        raise HTTPException(status_code=404)