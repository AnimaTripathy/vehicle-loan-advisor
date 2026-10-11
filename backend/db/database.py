import sqlite3
from pathlib import Path

# Path to SQLite database
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "vehicle_database.db"


def get_connection():
    """
    Create and return a SQLite connection.
    """
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection