'''
An iterator function is any function that returns an iterator object, which implements the iterator protocol (__iter__() and __next__() methods).
'''

class MyIterator:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

def iterator_function(max):
    return MyIterator(max)

# Usage
for num in iterator_function(5):
    print(num)  # Output: 1 2 3 4 5


