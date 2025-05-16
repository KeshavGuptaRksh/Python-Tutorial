class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Instance attributes (unique to each instance)
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects (instances of the Dog class)
dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 3
print(Dog.species)  # Output: Canis familiaris