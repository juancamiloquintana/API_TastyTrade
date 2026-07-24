from pathlib import Path
import json

# backend/storage/tokens.json
STORAGE_DIR = Path(__file__).resolve().parent.parent.parent / "storage"
STORAGE_DIR.mkdir(exist_ok=True)

TOKEN_FILE = STORAGE_DIR / "tokens.json"


class TokenManager:

    @staticmethod
    def save(tokens: dict):
        with open(TOKEN_FILE, "w", encoding="utf-8") as file:
            json.dump(tokens, file, indent=4)

    @staticmethod
    def load():
        if not TOKEN_FILE.exists():
            return None

        with open(TOKEN_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def clear():
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()

    @staticmethod
    def has_token():
        return TOKEN_FILE.exists()

    @staticmethod
    def get_access_token():
        token = TokenManager.load()

        if not token:
            return None

        return token.get("access_token")