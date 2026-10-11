from backend.db.database import get_connection
connection = get_connection()

cursor = connection.cursor()

cursor.execute("PRAGMA table_info(vehicles)")

columns = cursor.fetchall()

print("\nVehicle Table Schema\n")

for column in columns:
    print(
    f"Column: {column['name']}, "
    f"Type: {column['type']}, "
    f"Primary Key: {column['pk']}"
    )

connection.close()