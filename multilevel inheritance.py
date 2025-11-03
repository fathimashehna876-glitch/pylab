# Base class (Grandparent)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

# Derived class (Parent)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        self.show_brand()
        print(f"Model: {self.model}")

# Derived class (Child)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def show_details(self):
        self.show_model()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Create object of ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)

# Display full details
tesla.show_details()
