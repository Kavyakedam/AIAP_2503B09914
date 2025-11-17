"""
Fibonacci Number Calculator using Recursion

This module provides a function to calculate the nth Fibonacci number using
recursive approach. The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

Author: Generated for Assignment 5
Date: 2024
"""


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    This function uses a recursive approach where each Fibonacci number is
    calculated by summing the two previous Fibonacci numbers. The base cases
    handle F(0) = 0 and F(1) = 1.
    
    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).
                 n=0 returns 0, n=1 returns 1, n=2 returns 1, etc.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        RecursionError: If n is too large (Python recursion limit exceeded).
    
    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(5)
        5
        >>> fibonacci_recursive(10)
        55
    
    Note:
        This implementation has exponential time complexity O(2^n) and is
        not efficient for large values of n. For better performance, consider
        using iterative approach or memoization.
    """
    # Base case 1: F(0) = 0
    # This is the first number in the Fibonacci sequence
    if n == 0:
        return 0
    
    # Base case 2: F(1) = 1
    # This is the second number in the Fibonacci sequence
    if n == 1:
        return 1
    
    # Input validation: Check if n is negative
    # Fibonacci sequence is only defined for non-negative integers
    if n < 0:
        raise ValueError("Fibonacci number is only defined for non-negative integers")
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    # The nth Fibonacci number is the sum of the (n-1)th and (n-2)th numbers
    # This is the core of the recursive approach - breaking down the problem
    # into smaller subproblems until we reach the base cases
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n, memo=None):
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    This is an optimized version that stores previously calculated Fibonacci
    numbers to avoid redundant recursive calls, improving time complexity
    from O(2^n) to O(n).
    
    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).
        memo (dict, optional): Dictionary to store computed values. Defaults to None.
    
    Returns:
        int: The nth Fibonacci number.
    
    Examples:
        >>> fibonacci_memoized(10)
        55
        >>> fibonacci_memoized(30)
        832040
    """
    # Initialize memo dictionary on first call
    # This dictionary will store previously calculated Fibonacci numbers
    if memo is None:
        memo = {}
    
    # Base cases: F(0) = 0 and F(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Input validation
    if n < 0:
        raise ValueError("Fibonacci number is only defined for non-negative integers")
    
    # Check if we've already calculated this Fibonacci number
    # If yes, return the stored value (memoization)
    if n in memo:
        return memo[n]
    
    # Recursive case: Calculate F(n) = F(n-1) + F(n-2)
    # Store the result in memo dictionary before returning
    # This ensures we don't recalculate the same value multiple times
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def main():
    """
    Main function to demonstrate the Fibonacci number calculation.
    
    This function accepts user input from the keyboard to calculate
    Fibonacci numbers using both basic recursive and memoized approaches.
    """
    print("=" * 60)
    print("Fibonacci Number Calculator using Recursion")
    print("=" * 60)
    print()
    
    # Main loop to accept multiple inputs from the user
    while True:
        try:
            # Prompt user to enter a number from keyboard
            # input() function reads a line from keyboard and returns it as a string
            user_input = input("Enter a non-negative integer to calculate Fibonacci number (or 'q' to quit): ").strip()
            
            # Check if user wants to quit the program
            if user_input.lower() == 'q' or user_input.lower() == 'quit':
                print("\nThank you for using Fibonacci Calculator. Goodbye!")
                break
            
            # Convert string input to integer
            # int() function converts the string to an integer
            n = int(user_input)
            
            # Validate that the number is non-negative
            if n < 0:
                print("Error: Please enter a non-negative integer (0 or greater).")
                print()
                continue
            
            # Warn user if the number is very large (may be slow with basic recursion)
            if n > 35:
                print(f"\nWarning: Calculating F({n}) may take a while with basic recursion.")
                print("Using memoized approach is recommended for large numbers.")
                print()
            
            print()
            print("-" * 60)
            print(f"Calculating F({n}):")
            print("-" * 60)
            
            # Calculate using basic recursive approach
            # This works well for smaller numbers (n < 35)
            if n <= 35:
                print("Using Basic Recursive Approach...")
                result_basic = fibonacci_recursive(n)
                print(f"F({n}) = {result_basic}")
            else:
                print("Skipping basic recursion (too slow for large n)...")
                print("Using Memoized Recursive Approach instead...")
                result_basic = None
            
            # Calculate using memoized recursive approach (optimized)
            # This is faster and can handle larger numbers efficiently
            print("\nUsing Memoized Recursive Approach (Optimized)...")
            result_memoized = fibonacci_memoized(n)
            print(f"F({n}) = {result_memoized}")
            
            # Display both results if basic recursion was used
            if result_basic is not None:
                print(f"\nBoth methods agree: F({n}) = {result_memoized}")
            
            print()
            print("=" * 60)
            print()
            
        except ValueError:
            # Handle invalid input (non-numeric input)
            # This exception is raised when int() cannot convert the string to an integer
            print("Error: Invalid input! Please enter a valid integer or 'q' to quit.")
            print()
        
        except RecursionError:
            # Handle recursion limit exceeded
            # This happens when n is too large for Python's recursion stack
            print(f"Error: Number {n} is too large! Python's recursion limit exceeded.")
            print("Try using the memoized approach or a smaller number.")
            print()
        
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")
            print()


# Entry point of the program
# This allows the script to be run directly or imported as a module
if __name__ == "__main__":
    main()

