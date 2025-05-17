from . import BaseModel, Optional, datetime

class Grids_Create(BaseModel):
    uuid: str
    entity_id: int
    static_grid: bool
    grid_name: str
    owner_id: int
    iff_id: str
    faction_tag: Optional[str]
    pilot: Optional[str] = None

class Grids_Read(BaseModel):
    uuid: str
    entity_id: int
    static_grid: bool
    grid_name: str
    owner_id: int
    iff_id: str
    faction_tag: str
    pilot: str

class GridPositions_Create(BaseModel):
    grid_uuid: str
    x: float
    y: float
    z: float

class GridPositions_Read(BaseModel):
    grid_uuid: str
    x: float
    y: float
    z: float
    created_at: datetime

class LatestPositions_Read(BaseModel):
    uuid: str
    grid_name: str
    faction_tag: str
    iff_id: str
    position: dict
    created_at: Optional[datetime]
    