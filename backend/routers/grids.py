from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select, join, func
from datetime import datetime, timedelta, timezone
from typing import Optional

from backend.models.grids import Grids, Grid_Positions
from backend.schemas.grids import Grids_Create, Grids_Read, GridPositions_Read, GridPositions_Create, LatestPositions_Read
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/api/v1/grids/", response_model=list[Grids_Read], tags="grids")
async def get_grids(id: int | None, name: str | None, owner: str | None, faction: str | None):
    with db.get_session() as session:
        grids = session.exec(select(Grids)).all()
        return grids
    
@router.post("/api/v1/grids/", response_model=list[Grids_Read], tags="grids")
async def create_grids(grid_list: list[Grids_Create]):

    grids = [Grids(**grid_data.model_dump(exclude_unset=True)) for grid_data in grid_list]

    try:
        with db.get_session() as session:
            session.add_all(grids)
            session.commit()
            for grid in grids: session.refresh(grid)
            return grids
    except Exception as e:
        print(e)
    

@router.get("/api/v1/grid_positions/", response_model=list[GridPositions_Read], tags="grid_positions")
async def get_positions(
    from_ts: Optional[datetime] = Query(None, alias='from'),
    to_ts: Optional[datetime] = Query(None, alias='to')
    ):
    
    statement = select(Grid_Positions)

    if from_ts:
        statement = statement.where(Grid_Positions.created_at >= from_ts)
    if to_ts:
        statement = statement.where(Grid_Positions.created_at <= to_ts)

    with db.get_session() as session:
        positions = session.exec(statement).all()
        return positions

@router.post("/api/v1/grid_positions/", response_model=list[GridPositions_Read], tags="grid_positions", status_code=201)
async def create_positions(position_list: list[GridPositions_Create]):

    positions = [Grid_Positions(**position_data.model_dump(exclude_unset=True)) for position_data in position_list]

    with db.get_session() as session:
        try:
            session.add_all(positions)
            session.commit()
            for position in positions: session.refresh(position)
            return positions
        
        except Exception as e:
            print(e)
            return HTTPException
    
@router.get("/api/v1/grid_positions/latest/", response_model=list[LatestPositions_Read], tags=["grid_positions"])
async def get_latest_positions():
    with db.get_session() as session:
        now = datetime.now(timezone.utc)
        five_seconds_ago = now - timedelta(seconds=5)

        subq = (
            select(
                Grid_Positions.grid_uuid,
                func.max(Grid_Positions.created_at).label("latest_ts")
            )
            .where(Grid_Positions.created_at >= five_seconds_ago)
            .group_by(Grid_Positions.grid_uuid)
            .cte("latest_per_grid")
        )

        query = (
            select(
                Grids.uuid,
                Grids.grid_name,
                Grid_Positions.x,
                Grid_Positions.y,
                Grid_Positions.z,
                Grid_Positions.created_at,
            )
            .join(Grid_Positions, Grids.uuid == Grid_Positions.grid_uuid)
            .join(subq, (subq.c.grid_uuid == Grid_Positions.grid_uuid) & 
                        (subq.c.latest_ts == Grid_Positions.created_at))
        )

        results = session.exec(query).all()

        return [
            {
                "uuid": row[0],
                "grid_name": row[1],
                "x": row[2],
                "y": row[3],
                "z": row[4],
                "created_at": row[5]
            }
            for row in results
        ]
