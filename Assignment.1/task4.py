# Recursive version of factorial
def factorial_recursive(n):
    """
    Calculate factorial using recursive approach.
    Args:
        n (int): The number to calculate factorial for
    Returns:
        int: The factorial of n
    """
    # Base case: if n is 0 or 1, return 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

# Iterative version of factorial
def factorial_iterative(n):
    """
    Calculate factorial using iterative approach.
    Args:
        n (int): The number to calculate factorial for
    Returns:
        int: The factorial of n
    """
    # Initialize result to 1
    result = 1
    # Multiply all numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    number = 5
    print(f"Recursive Factorial of {number}: {factorial_recursive(number)}")
    print(f"Iterative Factorial of {number}: {factorial_iterative(number)}")
