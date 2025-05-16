class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call parent's __init__
        self.employee_id = employee_id
    
    def display_info(self):
        # Extend parent's method rather than completely replacing it
        parent_info = super().display_info()
        return f"{parent_info}, ID: {self.employee_id}"

emp = Employee("Alice", 30, "E12345")
print(emp.display_info())  # Output: Name: Alice, Age: 30, ID: E12345