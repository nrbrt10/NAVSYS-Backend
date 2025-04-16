from . import BaseModel, Optional, datetime

class SignalCreate(BaseModel):
    faction_tag: str
    x: float
    y: float
    z: float

class SignalRead(BaseModel):
    id: int
    faction_tag: str
    x: float
    y: float
    z: float
    dt: Optional[datetime]