# math_utils.py - Statistical utility functions

def mean(numbers):
return sum(numbers) / len(numbers)

def maximum(numbers): return max(numbers)
  
def minimum(numbers): return min(numbers)
  
def range_of(numbers):
return max(numbers) - min(numbers)

# math_utils.py - Mathematical utility functions

def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b
  
def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    return a * b

def is_even(n: int) -> bool:
    """Return True if n is even, else False."""
    return n % 2 == 0
  

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
     if n == 0:
         return 1
