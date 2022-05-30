from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    email: str
    name: str

class Create(BaseModel):
    username: str
    email: str
    name: str
    password: str
    company_id: int
    
class Edit(BaseModel):
    password: str

class Login(BaseModel):
    username: str
    password: str

class Response(User):
    company_id: str

    class Config:
        orm_mode = True



