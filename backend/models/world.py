from . import Field, SQLModel, Column, text, String, Optional, datetime

class DxInstance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    x: str
    y: str
    z: str
    radius: float

class PointsOfInterest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    x: str
    y: str
    z: str
    radius: Optional[float] = None