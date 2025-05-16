'''
Static Methods
Belong to the class rather than instances

Don't have access to self or cls

Defined with @staticmethod decorator

Used for utility functions related to the class
'''

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(5, 3))  # 8