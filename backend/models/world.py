from . import Field, SQLModel, Column, text, String, Optional, datetime
from sqlmodel import UniqueConstraint

class DxInstance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dx: str
    name: str
    x: str
    y: str
    z: str
    color: Optional[str] = None
    radius: Optional[float] = None
    gps: str

    class Config:
        __table_args__ = (
            UniqueConstraint("name", "x", "y", "z", name="unique_dx")
        )

    @property
    def position(self) -> dict:
        return {'x': self.x, 'y': self.y, 'z': self.z}

class PointsOfInterest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    x: str
    y: str
    z: str
    color: Optional[str] = None
    radius: Optional[float] = None
    gps: str

    @property
    def position(self) -> dict:
        return {'x': self.x, 'y': self.y, 'z': self.z}