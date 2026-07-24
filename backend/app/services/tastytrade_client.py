from app.config import settings
from app.auth.token_manager import TokenManager
from app.services.auth_service import auth_service
from app.services.http_client import http_client


class TastytradeClient:

    async def _get_token(self) -> str:
        """
        Obtiene un access token válido.
        Si no existe, solicita uno nuevo usando el refresh token.
        """

        token = TokenManager.get_access_token()

        if token:
            return token

        tokens = await auth_service.refresh_access_token()

        return tokens["access_token"]

    async def get(self, endpoint: str):

        token = await self._get_token()

        response = await http_client.get(
            f"{settings.API_URL}{endpoint}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        response.raise_for_status()

        return response.json()

    async def get_accounts(self):

        return await self.get("/customers/me/accounts")


client = TastytradeClient()