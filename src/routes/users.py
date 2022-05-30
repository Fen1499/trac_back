from fastapi import APIRouter, HTTPException
import db.database as db

from core.models_web import user
from auth import auth

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=user.Response, status_code=201)
async def create_user(usr: user.Create):
        hashed = auth.hash_password(usr.password)
        usr.password = hashed
        result = db.create_user(usr)
        return result

@router.get("/{user_id}", response_model=user.Response)
async def get_user(user_id: int):
        result = db.get_user(user_id)
        if result == None:
                raise HTTPException(status_code=404, detail="User not found")

        return result 

@router.put("/{user_id}", response_model=user.Response)
async def edit_user(user_id: int, usr: user.Edit):
        hashed = auth.hash_password(usr.password)
        usr.password = hashed
        result = db.edit_user(user_id, usr)
        if result == None:
                raise HTTPException(status_code=404, detail="User not found")
                
        return result 

@router.delete("/{user_id}", response_model=user.Response)
async def delete_user(user_id: int):
        result = db.delete_user(user_id)
        if result == None:
                raise HTTPException(status_code=404, detail="User not found")
                
        return result 
