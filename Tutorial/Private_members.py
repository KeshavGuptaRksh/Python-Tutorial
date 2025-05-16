class MyClass:
    def __init__(self):
        self.__private_var = "I'm private"
    
    def __private_method(self):
        return "Private method"
    
    def access_private(self):
        print(self.__private_var)      # Accessible within class
        print(self.__private_method()) # Accessible within class

obj = MyClass()
obj.access_private()  # Works

# These will raise AttributeError
# print(obj.__private_var)
# print(obj.__private_method())

# But can still be accessed with name mangling:
print(obj._MyClass__private_var)  # Not recommended!