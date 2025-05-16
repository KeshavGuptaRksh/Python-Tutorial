class MyClass:
    def __init__(self):
        self.public_var = "I'm public"
    
    def public_method(self):
        return "Public method"

obj = MyClass()
print(obj.public_var)      # Accessible
print(obj.public_method()) # Accessible