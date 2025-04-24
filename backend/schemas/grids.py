from . import BaseModel, Optional, datetime

class GridsCreate(BaseModel):
    uuid: str
    entity_id: int
    grid_name: str
    owner_id: int
    faction_tag: Optional[str]
    pilot: Optional[str] = None

class GridsRead(BaseModel):
    uuid: str
    entity_id: int
    grid_name: str
    owner_id: int
    faction_tag: Optional[str]
    pilot: Optional[str] = None

class Grid_PositionsCreate(BaseModel):
    grid_uuid: str
    x: float
    y: float
    z: float

class Grid_PositionsRead(BaseModel):
    grid_uuid: str
    x: float
    y: float
    z: float
    created_at: Optional[datetime]

class Latest_PositionsRead(BaseModel):
    uuid: str
    grid_name: str
    x: float
    y: float
    z: float
    created_at: Optional[datetime]
    