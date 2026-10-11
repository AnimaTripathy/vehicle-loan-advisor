from backend.db.database import get_connection


class VehicleService:

    @staticmethod
    def get_all_vehicles():
        """
        Return all vehicles sorted by price.
        """
        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM vehicles
            ORDER BY price ASC
        """)

        vehicles = cursor.fetchall()

        connection.close()

        return [dict(vehicle) for vehicle in vehicles]

    @staticmethod
    def get_recommended_vehicles(total_budget: int):
        """
        Recommend vehicles between 70% and 100% of the customer's budget.
        Return only the top 5 most suitable vehicles.
        """

        minimum_budget = int(total_budget * 0.70)

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM vehicles
            WHERE price BETWEEN ? AND ?
            ORDER BY price DESC
            LIMIT 5
            """,
            (minimum_budget, total_budget)
        )

        vehicles = cursor.fetchall()

        connection.close()

        return [dict(vehicle) for vehicle in vehicles]

    @staticmethod
    def get_vehicle(vehicle_id: int):
        """
        Return details of a single vehicle.
        """

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM vehicles
            WHERE id = ?
            """,
            (vehicle_id,)
        )

        vehicle = cursor.fetchone()

        connection.close()

        if vehicle:
            return dict(vehicle)

        return None