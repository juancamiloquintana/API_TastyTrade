from fastapi import APIRouter

from app.services.position_service import position_service

router = APIRouter(
    prefix="/positions",
    tags=["Positions"]
)


@router.get("/{account_number}")
async def get_positions(account_number: str):
    return await position_service.get_positions(account_number)