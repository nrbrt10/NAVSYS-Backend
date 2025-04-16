from fastapi import APIRouter, HTTPException
from sqlmodel import select
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

    with db.get_session() as session:
        session.add_all(grids)
        session.commit()
        for grid in grids: session.refresh(grid)
        return grids

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
    