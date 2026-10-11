from database import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("SELECT * FROM vehicles")

rows = cursor.fetchall()

print(f"\nTotal Vehicles: {len(rows)}\n")

for row in rows[:5]:
    print(dict(row))

connection.close()