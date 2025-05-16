'''
First-Class Function
In Python, functions are first-class citizens, meaning they can be:

Assigned to variables

Passed as arguments to other functions

Returned from other functions

Stored in data structures
'''

# 1. Assign to variable
def greet(name):
    return f"Hello, {name}!"

my_func = greet
print(my_func("Alice"))  # Output: Hello, Alice!

# 2. Pass as argument
def apply(func, value):
    return func(value)

print(apply(greet, "Bob"))  # Output: Hello, Bob!

# 3. Return from function
def create_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

morning_greet = create_greeter("Good morning")
print(morning_greet("Charlie"))  # Output: Good morning, Charlie!

# 4. Store in data structure
funcs = [greet, morning_greet]
for f in funcs:
    print(f("Dana"))