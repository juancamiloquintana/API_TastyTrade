from pathlib import Path
from dotenv import load_dotenv
import os

# backend/app/config.py
BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


class Settings:

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI")

    ENVIRONMENT = os.getenv("ENVIRONMENT", "sandbox")

    if ENVIRONMENT == "sandbox":
        BASE_API = "https://api.cert.tastyworks.com"
        BASE_AUTH = "https://id.cert.tastyworks.com"
    else:
        BASE_API = "https://api.tastyworks.com"
        BASE_AUTH = "https://id.tastyworks.com"


settings = Settings()