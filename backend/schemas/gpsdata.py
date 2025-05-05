from . import BaseModel, Optional, datetime
from typing import Literal
from pydantic import model_validator, Field
import re

class GPSData(BaseModel):
    type: Literal['dx', 'poi']
    gps: str = Field(pattern=r"^(GPS:)+(.*:)")

    @model_validator(mode='after')
    def validate_input(self):
        if self.type == 'dx' and re.search(r'R:[0-9]*km', self.gps) is None:
            raise ValueError('DX GPS cannot be missing radius value.')
        
        return self

    
            

