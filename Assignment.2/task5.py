"""
task5.py

Calculate the sum of even numbers and odd numbers in a list.
"""

def sum_even_odd(numbers):
    """Calculate sums of even and odd integers from a list.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        A tuple (sum_even, sum_odd) containing the sum of even and odd numbers
    """
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        try:
            n = int(num)
        except (ValueError, TypeError):
            # Ignore values that cannot be converted to int
            continue
        
        if n % 2 == 0:
            sum_even += n
        else:
            sum_odd += n
    
    return sum_even, sum_odd


if __name__ == "__main__":
    # Test with example list
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_sum, odd_sum = sum_even_odd(test_list)
    
    print(f"List: {test_list}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
    print(f"Total sum: {even_sum + odd_sum}")
