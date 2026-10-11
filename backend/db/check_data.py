from backend.db.database import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM vehicles")

print("Total Vehicles:", cursor.fetchone()[0])

connection.close()