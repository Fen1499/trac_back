from venv import create
from fastapi import APIRouter, HTTPException
import db.database as db
from core.models_web import asset

router = APIRouter(
    prefix="/assets",
    tags=["assets"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{asset_id}", response_model=asset.Response)
async def get_asset(asset_id):
    result = db.get_asset(asset_id)
    if result == None:
            raise HTTPException(status_code=404, detail="Asset not found")

    return result

@router.post("/", response_model=asset.Response, status_code=201)
async def create_asset(asset: asset.Create):
    result = db.create_asset(asset)
    breakpoint()
    return result