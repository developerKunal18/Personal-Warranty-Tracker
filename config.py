from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "warranties.json"

DATE_FORMAT = "%Y-%m-%d"
UPCOMING_DAYS = 30
