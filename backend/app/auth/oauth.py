from urllib.parse import urlencode
from uuid import uuid4

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/login")
async def login():

    state = str(uuid4())

    params = {
        "client_id": settings.CLIENT_ID,
        "redirect_uri": settings.REDIRECT_URI,
        "response_type": "code",
        "scope": "openid read trade",
        "state": state,
    }

    authorization_url = (
        f"{settings.AUTH_URL}/oauth2/authorize?"
        f"{urlencode(params)}"
    )

    return RedirectResponse(authorization_url)


from app.services.auth_service import auth_service

@router.get("/token")
async def get_token():

    return await auth_service.refresh_access_token()