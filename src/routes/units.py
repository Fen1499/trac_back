from typing import List
from fastapi import APIRouter, HTTPException
import db.database as db

from core.models_web import unit
from auth import auth

router = APIRouter(
    prefix="/units",
    tags=["units"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

# @router.get("/", response_model=List[unit.Response], response_model_exclude= ["assets"])
# async def get_units():
#     result = db.get_units()
#     return result

@router.get("/{unit_id}", response_model=unit.Response)
async def get_unit(unit_id: int):
    result = db.get_unit(unit_id)
    if result == None:
        raise HTTPException(status_code=404, detail="Unit not found")

    assets_list = db.get_assets_by_owner(unit_id)
    ret = {
        "id": result['id'],
        "name": result['name'],
        "company_id": result['company_id'],
        "assets": assets_list
    }
    return ret

@router.post("/", response_model=unit.Response, status_code=201)
async def create_unit(unit: unit.Create):
    result = db.create_unit(unit)
    return result

# @router.put("/", response_model=unit.Response)
# TODO