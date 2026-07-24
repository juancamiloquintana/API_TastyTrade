import json
from pathlib import Path

TOKEN_FILE = Path("tokens.json")


def save_tokens(tokens: dict):
    with open(TOKEN_FILE, "w") as file:
        json.dump(tokens, file, indent=4)


def load_tokens():
    if TOKEN_FILE.exists():
        with open(TOKEN_FILE, "r") as file:
            return json.load(file)

    return None