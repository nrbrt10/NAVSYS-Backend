from . import BaseModel, Optional, datetime

class GridCreate(BaseModel):
    id: int
    name: str
    owner: str
    faction: str
    pilot: Optional[str]

class GridRead(BaseModel):
    id: int
    name: str
    owner: str
    faction: str
    pilot: Optional[str]

class Grid_PositionCreate(BaseModel):
    grid_id: int
    x: float
    y: float
    z: float

class Grid_PositionRead(BaseModel):
    id: int
    grid_id: int
    x: float
    y: float
    z: float
    timestamp: Optional[datetime]