from . import BaseModel, Optional, datetime

class DxInstance_All(BaseModel):
    id: int
    name: str
    x: float
    y: float
    z: float
    radius: float
    gps: str

class PointsOfInterest_Create(BaseModel):
    name: str
    x: float
    y: float
    z: float
    radius: Optional[float] = None
    gps: str

class PointsOfInterest_Read(BaseModel):
    name: str
    x: str
    y: str
    z: str
    radius: Optional[float] = None
    gps: str