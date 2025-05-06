from . import Field, SQLModel, Column, text, String, Optional, datetime
from sqlmodel import UniqueConstraint

class DxInstance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    x: str
    y: str
    z: str
    radius: Optional[float] = None
    gps: str

    class Config:
        __table_args__ = (
            UniqueConstraint("name", "x", "y", "z", name="unique_dx")
        )

class PointsOfInterest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    x: str
    y: str
    z: str
    radius: Optional[float] = None
    gps: str