from decimal import Decimal
from typing import Union
from pydantic import BaseModel

class Asset(BaseModel):
    id: int
    name: str
    description: str
    model: str
    owner: int
    status: str
    health_level: Decimal

class Create(BaseModel):
    name: str
    description: str
    model: str
    owner: int
    status: str
    health_level: Decimal

class Response(Asset):
    pass