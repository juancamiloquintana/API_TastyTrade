import httpx

from app.config import settings


class TastyHTTPClient:

    def __init__(self):

        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "User-Agent": settings.USER_AGENT,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    async def get(self, url: str, **kwargs):
        return await self.client.get(url, **kwargs)

    async def post(self, url: str, **kwargs):
        return await self.client.post(url, **kwargs)

    async def close(self):
        await self.client.aclose()


http_client = TastyHTTPClient()