def sum_even_odd(numbers):
    """
    Calculate and return the sum of even and odd numbers in a given list.
    
    Args:
        numbers: A list of integers
        
    Returns:
        tuple: A tuple containing (sum_of_even, sum_of_odd)
    """
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd


# Example usage
if __name__ == "__main__":
    # Test the function
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_sum, odd_sum = sum_even_odd(test_list)
    
    print(f"List: {test_list}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")

