from backend.services.vehicle_service import (
    get_all_vehicles,
    get_affordable_vehicles
)

print("All Vehicles")

vehicles = get_all_vehicles()

print(len(vehicles))

print("\nAffordable Vehicles")

affordable = get_affordable_vehicles(1000000)

for vehicle in affordable:
    print(vehicle["brand"], vehicle["model"], vehicle["price"])