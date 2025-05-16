class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def pet_factory(pet_type):
    pets = {
        "dog": Dog,
        "cat": Cat
    }
    return pets[pet_type]()

dog = pet_factory("dog")
print(dog.speak())  # Woof!