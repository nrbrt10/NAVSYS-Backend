from fastapi import APIRouter, HTTPException
from sqlmodel import select, join, func
from datetime import datetime

from backend.models.grids import Grids, Grid_Position
from backend.schemas.grids import GridCreate, GridRead, Grid_PositionRead, Grid_PositionCreate
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/api/v1/grids/", response_model=list[GridRead], tags="grids")
async def get_grids(id: int | None, name: str | None, owner: str | None, faction: str | None):
    with db.get_session() as session:
        grids = session.exec(select(Grids)).all()
        return grids
    
@router.post("/api/v1/grids/", response_model=list[GridRead], tags="grids")
async def create_grids(grid_list: list[GridCreate]):

    grids = [Grids(**grid_data.model_dump(exclude_unset=True)) for grid_data in grid_list]

    try:
        with db.get_session() as session:
            session.add_all(grids)
            session.commit()
            for grid in grids: session.refresh(grid)
            return grids
    except Exception as e:
        print(e)
    

@router.get("/api/v1/grid_positions/", response_model=list[Grid_PositionRead], tags="grid_positions")
async def get_positions(grid_id: int | None, timestamp: datetime | None):
    with db.get_session() as session:
        positions = session.exec(select(Grid_Position)).all()
        return positions

@router.post("/api/v1/grid_positions/", response_model=list[Grid_PositionRead], tags="grid_positions")
async def create_positions(position_list: list[Grid_PositionCreate]):

    positions = [Grid_Position(**position_data.model_dump(exclude_unset=True)) for position_data in position_list]

    with db.get_session() as session:
        session.add_all(positions)
        session.commit()
        for position in positions: session.refresh(position)
        return positions
    
# @router.get("/api/v1/grid_positions/latest/", response_model=list[Grid_PositionRead], tags="grid_positions")
# async def get_latest_position():
#     with db.get_session() as session:
#         statement = (
#             select(Grid_Position, func.max(Grid_Position.timestamp).label("latest_timestamp")).join(Grids, onclause=Grids.uuid == Grid_Position.grid_uuid)
#             ).group_by(Grid_Position.grid_uuid)
#         positions = session.exec(statement).all()
#         return positions
    
@router.get("/api/v1/grid_positions/latest/", response_model=list[Grid_PositionRead], tags=["grid_positions"])
async def get_latest_positions():
    with db.get_session() as session:
        # Subquery: latest timestamp per grid
        subq = (
            select(
                Grid_Position.grid_uuid,
                func.max(Grid_Position.timestamp).label("latest_timestamp")
            )
            .group_by(Grid_Position.grid_uuid)
            .subquery()
        )

        # Main query: get full Grid_Position rows matching grid_uuid and timestamp
        statement = (
            select(Grid_Position)
            .join(subq, onclause=(
                (Grid_Position.grid_uuid == subq.c.grid_uuid) &
                (Grid_Position.timestamp == subq.c.latest_timestamp)
            ))
        )

        results = session.exec(statement).all()

        return results