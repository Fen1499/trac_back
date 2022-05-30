from typing import List
from fastapi import APIRouter, HTTPException
import db.database as db

from core.models_web import company
from auth import auth

router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[company.Response], response_model_exclude= ["units", "users"])
async def get_companies():
    result = db.get_companies()
    return result

@router.get("/{company_id}", response_model=company.Response)
async def get_company(company_id: int):
    result = db.get_company(company_id)
    if result == None:
        raise HTTPException(status_code=404, detail="Company not found")

    users_list = db.get_users_by_company(company_id)
    units_list = db.get_units_by_company(company_id)
    ret = {
        "id": result['id'],
        "name": result['name'],
        "units": units_list,
        "users": users_list
    }
    return ret

@router.post("/", response_model=company.Response, status_code=201)
async def create_company(company: company.Create):
    result = db.create_company(company)
    return result