from app.config import settings
from app.services.http_client import http_client
from app.auth.token_manager import TokenManager


class AuthService:

    async def refresh_access_token(self):

        response = await http_client.post(
            f"{settings.API_URL}/oauth/token",
            json={
                "grant_type": "refresh_token",
                "client_secret": settings.CLIENT_SECRET,
                "refresh_token": settings.REFRESH_TOKEN,
            },
        )

        response.raise_for_status()

        tokens = response.json()

        TokenManager.save(tokens)

        return tokens


auth_service = AuthService()