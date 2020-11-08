from datetime import datetime
from pydantic import BaseModel
from typing import List


class Appointment(BaseModel):
    date: datetime
    
    title: str
    text: str

    tags: List[Tag]
