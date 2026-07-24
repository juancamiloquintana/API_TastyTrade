from fastapi import FastAPI

from app.config import settings
from app.auth.oauth import router as auth_router
from app.api.accounts import router as accounts_router

app = FastAPI(
    title="TastyTrade Pro",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(accounts_router)


@app.get("/")
def home():

    return {
        "application": "TastyTrade Pro",
        "client_id": settings.CLIENT_ID,
        "environment": settings.ENVIRONMENT
    }

@app.get("/config")
def config():
    return {
        "client_id": settings.CLIENT_ID,
        "has_client_secret": settings.CLIENT_SECRET is not None,
        "has_refresh_token": settings.REFRESH_TOKEN is not None,
        "environment": settings.ENVIRONMENT,
    }