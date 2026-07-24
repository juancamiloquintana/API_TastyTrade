from urllib.parse import urlencode
from uuid import uuid4

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

from app.services.auth_service import auth_service

@router.get("/token")
async def get_token():

    return await auth_service.refresh_access_token()


