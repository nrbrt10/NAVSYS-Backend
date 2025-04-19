from . import BaseModel, Optional, datetime

class GridCreate(BaseModel):
    uuid: str
    entity_id: int
    grid_name: str
    owner_id: int
    faction_tag: Optional[str]
    pilot: Optional[str] = None

class GridRead(BaseModel):
    uuid: str
    entity_id: int
    grid_name: str
    owner_id: int
    faction_tag: Optional[str]
    pilot: Optional[str] = None

class Grid_PositionCreate(BaseModel):
    grid_uuid: str
    x: float
    y: float
    z: float

class Grid_PositionRead(BaseModel):
    grid_uuid: str
    x: float
    y: float
    z: float
    timestamp: Optional[datetime]