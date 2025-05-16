'''
Class Methods
Bound to the class rather than instances

Take cls parameter instead of self

Defined with @classmethod decorator

Often used for alternative constructors
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2023
        age = current_year - birth_year
        return cls(name, age)

person = Person.from_birth_year("Alice", 1990)
print(person.age)  # 33 (assuming current year is 2023)