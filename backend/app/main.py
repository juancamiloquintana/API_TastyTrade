from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="TastyTrade Pro",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "application": "TastyTrade Pro",
        "client_id": settings.CLIENT_ID,
        "environment": settings.ENVIRONMENT
    }

from app.auth.token_manager import save_tokens
from app.auth.token_manager import load_tokens


@app.get("/test-token")
def test_token():

    save_tokens(
        {
            "access_token": "ABC123",
            "refresh_token": "XYZ789"
        }
    )

    return load_tokens()


