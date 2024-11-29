# Base class: Vehicle
class Vehicle:
    def move(self):
        """
        Base class method to be overridden in subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Subclass: Train
class Train(Vehicle):
    def move(self):
        return "Chugging along the tracks 🚂"

# Function to demonstrate polymorphism
def demonstrate_movement(vehicles):
    """
    Takes a list of vehicles and demonstrates their move() actions.
    """
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.move()}")

# Main program
if __name__ == "__main__":
    # Create instances of each vehicle
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()
    train = Train()

    # List of vehicles
    vehicles = [car, plane, boat, bicycle, train]

    # Demonstrate polymorphism
    demonstrate_movement(vehicles)
