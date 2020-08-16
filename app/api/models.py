from typing import List
from pydantic import BaseModel

class Mountain(BaseModel):
    name: str
    elevation: str
    coordinate: str
    links: List[str]
