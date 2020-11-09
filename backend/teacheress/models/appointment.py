from datetime import datetime
from pydantic import BaseModel
from typing import List

from .tag import Tag


class Appointment(BaseModel):
    date: datetime
    
    title: str
    text: str

    tags: List[Tag]
