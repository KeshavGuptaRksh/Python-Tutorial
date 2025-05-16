class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    
    # Overriding the info method
    def info(self):
        return f"{super().info()} with {self.battery_size}kWh battery"

# Using the classes
regular_car = Vehicle("Toyota", "Corolla")
ev = ElectricCar("Tesla", "Model S", 100)

print(regular_car.info())  # Output: Toyota Corolla
print(ev.info())          # Output: Tesla Model S with 100kWh battery