'''
A generator function is a special kind of function that returns a generator iterator (a type of iterator) using the yield keyword.
'''

def generator_function(max):
    current = 0
    while current < max:
        current += 1
        yield current

# Usage
for num in generator_function(5):
    print(num)  # Output: 1 2 3 4 5