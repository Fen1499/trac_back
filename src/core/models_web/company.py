from typing import List
from pydantic import BaseModel

from core.models_web.unit import Unit
from core.models_web.user import User

class Company(BaseModel):
    id: int
    name: str
    units: List[Unit] = []
    users: List[User] = []

class Create(BaseModel):
    name: str
    units: List[Unit] = []
    users: List[User] = []

class Response(Company):
    pass