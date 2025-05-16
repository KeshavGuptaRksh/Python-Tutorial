'''Creational Patterns: Deal with object creation mechanisms

Singleton, Factory, Abstract Factory, Builder, Prototype'''

# Singleton 
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True