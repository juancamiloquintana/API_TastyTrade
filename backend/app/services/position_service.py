from app.services.tastytrade_client import client


class PositionService:
    """
    Servicio encargado de obtener las posiciones de una cuenta.
    """

    async def get_positions(self, account_number: str):
        return await client.get(
            f"/accounts/{account_number}/positions"
        )


position_service = PositionService()