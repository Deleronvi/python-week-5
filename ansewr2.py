# Vehicle Base Class
class Vehicle:
    def move(self):
        pass  # Base method to be overridden

# Car Class
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Plane Class
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Boat Class
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example Usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
