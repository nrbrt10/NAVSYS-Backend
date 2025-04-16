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

class GridPositionCreate(BaseModel):
    id: int
    grid_id: int
    x: str
    y: str
    z: str

class GridPositionRead(BaseModel):
    id: int
    grid_id: int
    x: str
    y: str
    z: str
    timestamp: Optional[datetime]