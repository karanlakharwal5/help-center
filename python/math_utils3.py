# math_utils3.py - Mathematical utility functions

def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers and return the sum.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b
  
def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers and return the product.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b

def is_even(n: int) -> bool:
    """Check if a number is even.

    Args:
        n: Integer to check

    Returns:
        True if n is even, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return n % 2 == 0
  
def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n (n!)

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
