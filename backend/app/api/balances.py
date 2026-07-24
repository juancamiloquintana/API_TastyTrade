from fastapi import APIRouter

from app.services.balance_service import balance_service

router = APIRouter(
    prefix="/balances",
    tags=["Balances"]
)


@router.get("/{account_number}")
async def get_balances(account_number: str):
    return await balance_service.get_balances(account_number)