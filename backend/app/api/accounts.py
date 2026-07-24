from fastapi import APIRouter
from app.services.tastytrade_client import client

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)

@router.get("/")
async def get_accounts():
    return await client.get_accounts()

@router.get("/me")
async def get_me():
    return await client.get_customer()

