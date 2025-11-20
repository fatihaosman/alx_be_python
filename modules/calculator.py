# calculator.py

def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
