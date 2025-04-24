from fastapi import APIRouter, HTTPException
from sqlmodel import select, join, func
from datetime import datetime

from backend.models.grids import Grids, Grid_Positions
from backend.schemas.grids import GridsCreate, GridsRead, Grid_PositionsRead, Grid_PositionsCreate, Latest_PositionsRead
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/api/v1/grids/", response_model=list[GridsRead], tags="grids")
async def get_grids(id: int | None, name: str | None, owner: str | None, faction: str | None):
    with db.get_session() as session:
        grids = session.exec(select(Grids)).all()
        return grids
    
@router.post("/api/v1/grids/", response_model=list[GridsRead], tags="grids")
async def create_grids(grid_list: list[GridsCreate]):

    grids = [Grids(**grid_data.model_dump(exclude_unset=True)) for grid_data in grid_list]

    try:
        with db.get_session() as session:
            session.add_all(grids)
            session.commit()
            for grid in grids: session.refresh(grid)
            return grids
    except Exception as e:
        print(e)
    

@router.get("/api/v1/grid_positions/", response_model=list[Grid_PositionsRead], tags="grid_positions")
async def get_positions(grid_id: int | None, timestamp: datetime | None):
    with db.get_session() as session:
        positions = session.exec(select(Grid_Positions)).all()
        return positions

@router.post("/api/v1/grid_positions/", response_model=list[Grid_PositionsRead], tags="grid_positions")
async def create_positions(position_list: list[Grid_PositionsCreate]):

    positions = [Grid_Positions(**position_data.model_dump(exclude_unset=True)) for position_data in position_list]

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
    
@router.get("/api/v1/grid_positions/latest/", response_model=list[Latest_PositionsRead], tags=["grid_positions"])
async def get_latest_positions():
    with db.get_session() as session:
        g = Grids
        gp = Grid_Positions

        cte = (
            select(
                g.uuid,
                g.grid_name,
                gp.x,
                gp.y,
                gp.z,
                gp.created_at

            )
            .join(gp, g.uuid == gp.grid_uuid)
            .cte('cte')
        )

        ts_filter = (
            select(func.max(gp.created_at).label('max_ts'))
            .cte('ts_filter')
        )

        query = (
            select(
            cte.c.uuid,
            cte.c.grid_name,
            cte.c.x,
            cte.c.y,
            cte.c.z,
            cte.c.created_at
            )
                 .join(ts_filter, cte.c.created_at == ts_filter.c.max_ts)
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