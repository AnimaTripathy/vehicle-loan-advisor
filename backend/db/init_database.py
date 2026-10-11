from backend.db.database import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS vehicles")

cursor.execute("""
CREATE TABLE vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    variant TEXT,
    price INTEGER NOT NULL,
    fuel_type TEXT,
    transmission TEXT,
    mileage REAL,
    engine TEXT,
    seating_capacity INTEGER,
    body_type TEXT
)
""")

connection.commit()
connection.close()

print("✅ Vehicle table created successfully!")