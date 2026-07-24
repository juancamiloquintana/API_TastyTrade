from app.services.tastytrade_client import client


class BalanceService:

    async def get_balances(self, account_number: str):
        return await client.get(
            f"/accounts/{account_number}/balances"
        )


balance_service = BalanceService()