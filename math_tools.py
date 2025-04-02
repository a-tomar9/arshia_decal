# math_tools.py

def add(a, b):
    return a + b
'''Returns the sum of a and b. '''

def subtract(a, b):
    return a - b
'''Returns the difference between a and b.'''

def multiply(a, b):
    return a * b
'''Returns the product of a and b.'''
    
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b
'''Returns the quotient of a divided by b. Handles division by zero.'''


