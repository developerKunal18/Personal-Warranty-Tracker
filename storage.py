import json
from config import DATA_DIR, DATA_FILE


def initialize_storage():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_warranties():
    initialize_storage()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_warranties(warranties):
    initialize_storage()

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(warranties, file, indent=4)
