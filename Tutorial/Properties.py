'''
Properties
Control access to instance attributes

Defined with @property decorator

Can include getters, setters, and deleters

Enable encapsulation and validation
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.area)  # 78.5
circle.radius = 10  # Uses setter
print(circle.area)  # 314.0