from typing import List
from pydantic import BaseModel
from .tag import Tag


class Category(BaseModel):
    """ A possibility to organize tags into categories. """

    name: str

    tags: List[Tag]
