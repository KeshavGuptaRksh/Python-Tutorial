class Person:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"{self.name} is being destroyed")

p = Person("Bob")
del p  # Output: "Bob is being destroyed"