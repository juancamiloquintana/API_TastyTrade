from app.config import settings
from app.auth.token_manager import TokenManager
from app.services.auth_service import auth_service
from app.services.http_client import http_client
from app.utils.logger import logger


class TastytradeClient:
    """
    Cliente principal para consumir la API de Tastytrade.
    Toda la comunicación con la API debe pasar por esta clase.
    """

    async def _get_token(self) -> str:
        token = TokenManager.get_access_token()

        if token:
            logger.info(f"Using access token: {token[:40]}...")
            return token

        logger.info("Refreshing access token...")

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

        logger.info(f"GET {endpoint}")
        logger.info(f"STATUS {response.status_code}")
        logger.info(response.text)

        if response.is_error:
            logger.error(
                f"Request failed | Endpoint: {endpoint} | "
                f"Status: {response.status_code} | Body: {response.text}"
            )

        response.raise_for_status()

        return response.json()

    async def get_accounts(self):
        return await self.get("/customers/me/accounts")

    async def get_customer(self):
        return await self.get("/customers/me")


client = TastytradeClient()