class MyClass:
    def __init__(self):
        self._protected_var = "I'm protected"
    
    def _protected_method(self):
        return "Protected method"

class SubClass(MyClass):
    def access_protected(self):
        print(self._protected_var)      # Accessible in subclass
        print(self._protected_method()) # Accessible in subclass

obj = SubClass()
obj.access_protected()  # Works
print(obj._protected_var)  # Still accessible (just a convention)