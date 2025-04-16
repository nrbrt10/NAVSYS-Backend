from fastapi import APIRouter, HTTPException
from sqlmodel import select

from backend.models.grids import Grids, Grid_Position
from backend.schemas.grids import GridCreate, GridRead, GridPositionRead, GridPositionCreate
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/api/v1/grids/", response_model=list[Grids], tags="grids")
async def get_grids():
    with db.get_session() as session:
        grids = session.exec(select(Grids)).all()
        return grids

    
#@router.get("/api/v1/grid_positions/{grid_id}", response_model=list[Grid_Position], tags="grid_positions")

@router.post("/api/v1/grid_positions", response_model=list[GridPositionRead], tags="grid_positions")
async def create_positions(position_data: GridPositionCreate):

    position_dict = position_data.model_dump(exclude_unset=True)
    positions = Grid_Position(**position_dict)

    with db.get_session() as session:
        session.add(positions)
        session.commit()
        session.refresh(positions)
        return positions
    