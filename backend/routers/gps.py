from fastapi import APIRouter, HTTPException
from typing import Union
from datetime import datetime

from backend.schemas.world import DxInstance_Read, PointsOfInterest_Read
from backend.schemas.gpsdata import GPSData
from backend.services.gpsdata_service import normalize_gps_data

router = APIRouter()

@router.post("/api/v1/gps/", response_model=Union[DxInstance_Read, PointsOfInterest_Read])
async def create_gps(gps_list: list[GPSData]):

    try:
        normalize_gps_data(gps_list)
    except Exception as e:
        raise HTTPException(status_code=404)