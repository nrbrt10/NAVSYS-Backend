from . import BaseModel, Optional, datetime

class DxInstance_Create(BaseModel):
    name: str
    x: float
    y: float
    z: float
    radius: Optional[float] = None
    gps: str

class DxInstance_Read(BaseModel):
    id: str
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
    id: int
    name: str
    x: str
    y: str
    z: str
    radius: float
    gps: str