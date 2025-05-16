class Engine:
    def __init__(self, type):
        self.type = type
    
    def start(self):
        print(f"{self.type} engine started")

class Car:
    def __init__(self, model, engine_type):
        self.model = model
        self.engine = Engine(engine_type)  # Composition - Engine cannot exist without Car
    
    def start(self):
        print(f"Starting {self.model}")
        self.engine.start()

# Usage
my_car = Car("Toyota", "V6")
my_car.start()
# When my_car is destroyed, its engine is destroyed too