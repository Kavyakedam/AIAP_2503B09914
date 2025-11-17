def print_multiples_while(number):
    """
    Prints the first 10 multiples using a while loop.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"Method 1 - While Loop - First 10 multiples of {number}:")
    i = 1
    while i <= 10:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
        i += 1


def print_multiples_for_range(number):
    """
    Prints the first 10 multiples using a for loop with range().
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"Method 2 - For Loop with range() - First 10 multiples of {number}:")
    for i in range(1, 11):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


def print_multiples_for_list(number):
    """
    Prints the first 10 multiples using a for loop with a list.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"Method 3 - For Loop with List - First 10 multiples of {number}:")
    multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in multipliers:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


def print_multiples_for_enumerate(number):
    """
    Prints the first 10 multiples using a for loop with enumerate().
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"Method 4 - For Loop with enumerate() - First 10 multiples of {number}:")
    multipliers = list(range(1, 11))
    for index, i in enumerate(multipliers, start=1):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


def print_multiples_while_break(number):
    """
    Prints the first 10 multiples using a while loop with break control.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"Method 5 - While Loop with break - First 10 multiples of {number}:")
    i = 1
    while True:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
        i += 1
        if i > 10:
            break


# Main function that uses a loop (for demonstration)
def print_multiples(number):
    """
    Prints the first 10 multiples using a for loop with range().
    This is the default implementation.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"First 10 multiples of {number}:")
    for i in range(1, 11):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Multiples Calculator - Using Different Loop Methods")
    print("=" * 60)
    
    # Get number from keyboard input
    while True:
        try:
            number = int(input("\nEnter a number to find its first 10 multiples: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Display all loop methods
    print("\n" + "=" * 60)
    print_multiples_while(number)
    print()
    
    print("=" * 60)
    print_multiples_for_range(number)
    print()
    
    print("=" * 60)
    print_multiples_for_list(number)
    print()
    
    print("=" * 60)
    print_multiples_for_enumerate(number)
    print()
    
    print("=" * 60)
    print_multiples_while_break(number)
    print()
    
    print("=" * 60)
    print("Default function:")
    print_multiples(number)

