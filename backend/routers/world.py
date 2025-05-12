from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select, join, func
from datetime import datetime, timedelta, timezone
from typing import Optional

from backend.models.world import DxInstance, PointsOfInterest
from backend.schemas.world import DxInstance_Read, PointsOfInterest_Read
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/api/v1/dx_instances/", response_model=list[DxInstance_Read], tags="dx_instances")
async def get_dx():
    with db.get_session() as session:
        try:
            dx = session.exec(select(DxInstance)).all()
        except Exception as e:
            return HTTPException(status_code=500, detail=e)
        return [
            DxInstance_Read(
                id=row.id,
                dx=row.dx,
                name=row.name,
                position=row.position,
                radius=row.radius,
                color=row.color[:7]
            )
            for row in dx
        ]
    
@router.get("/api/v1/pois/", response_model=list[PointsOfInterest_Read])
async def get_pois():
    with db.get_session() as session:
        try:
            pois = session.exec(select(PointsOfInterest)).all()
        except Exception as e:
            return HTTPException(status_code=500, detail=e)
        return [
            PointsOfInterest_Read(
                id=row.id,
                name=row.name,
                position=row.position,
                radius=row.radius,
                color=row.color[:7]
            )
            for row in pois
        ]