from typing import List
from pydantic import BaseModel
from core.models_web.asset import Asset

class Unit(BaseModel):
    id: int
    name: str
    company_id: int
    assets: List[Asset] = []

class Create(BaseModel):
    name: str
    company_id: int

class Response(Unit):
   pass