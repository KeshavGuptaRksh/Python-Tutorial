from abc import ABC, abstractmethod

# Without DIP
class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on")
    
    def turn_off(self):
        print("LightBulb: turned off")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()
    
    def operate(self):
        # Direct dependency on LightBulb
        pass

# With DIP
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    # implements Switchable
    pass

class Fan(Switchable):
    # implements Switchable
    pass

class Switch:
    def __init__(self, device: Switchable):
        self.device = device  # Depends on abstraction
    
    def operate(self):
        # Works with any Switchable device
        pass