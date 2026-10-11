from pathlib import Path
import sys
import pandas as pd

# Add current folder to Python path
CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from backend.db.database import get_connection

# Project root
PROJECT_ROOT = CURRENT_DIR.parent.parent

CSV_PATH = PROJECT_ROOT / "data" / "raw" / "vehicle_catalog.csv"

# Read CSV
df = pd.read_csv(CSV_PATH)

connection = get_connection()

df.to_sql(
    "vehicles",
    connection,
    if_exists="append",
    index=False
)

connection.close()

print(f"✅ {len(df)} vehicles loaded successfully.")