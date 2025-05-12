from . import BaseModel, Optional, datetime

class DxInstance_Create(BaseModel):
    dx: str
    name: str
    x: float
    y: float
    z: float
    color: Optional[str] = None
    radius: Optional[float] = None
    gps: str

class DxInstance_Read(BaseModel):
    id: int
    dx: str
    name: str
    position: dict
    color: str
    radius: float

class PointsOfInterest_Create(BaseModel):
    name: str
    x: float
    y: float
    z: float
    color: Optional[str] = None
    radius: Optional[float] = None
    gps: str

class PointsOfInterest_Read(BaseModel):
    id: int
    name: str
    position: dict
    color: str
    radius: Optional[float] = None