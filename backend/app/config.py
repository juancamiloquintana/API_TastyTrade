from pathlib import Path
from dotenv import load_dotenv
import os

# Directorio backend/
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables del .env
load_dotenv(BASE_DIR / ".env")


class Settings:

    def __init__(self):
        self.CLIENT_ID = os.getenv("CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self.REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
        self.REDIRECT_URI = os.getenv("REDIRECT_URI")

        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "sandbox").lower()

        # URLs según el entorno
        if self.ENVIRONMENT == "sandbox":
            self.API_URL = "https://api.cert.tastyworks.com"
        elif self.ENVIRONMENT == "production":
            self.API_URL = "https://api.tastyworks.com"
        else:
            raise ValueError(
                f"ENVIRONMENT inválido: {self.ENVIRONMENT}. "
                "Debe ser 'sandbox' o 'production'."
            )

        # User-Agent requerido por la API
        self.USER_AGENT = "TastyTrade-Pro/1.0"


settings = Settings()