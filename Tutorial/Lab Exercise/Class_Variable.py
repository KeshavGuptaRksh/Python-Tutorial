class Employee:
    # Class variable
    raise_amount = 1.04  # 4% raise
    num_of_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        
        Employee.num_of_employees += 1
    
    # Regular instance method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Class method (decorator)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # Alternative constructor (class method)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    # Static method (no access to instance or class)
    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)  # Not Saturday or Sunday

# Using class method to change raise amount for all employees
Employee.set_raise_amount(1.05)

# Creating employee using alternative constructor
emp_str = "John-Doe-70000"
new_employee = Employee.from_string(emp_str)

# Using static method
import datetime
my_date = datetime.date(2023, 7, 10)
print(Employee.is_workday(my_date))  # True if weekday