def sum_to_n(n):
    """
    Calculate the sum of first n numbers using different looping approaches.
    
    Args:
        n (int): The number of first natural numbers to sum
        
    Returns:
        tuple: (sum_using_for, sum_using_while)
    """
    # Method 1: Using for loop
    sum_for = 0
    for i in range(1, n + 1):
        sum_for += i
    
    # Method 2: Using while loop
    sum_while = 0
    counter = 1
    while counter <= n:
        sum_while += counter
        counter += 1
    
    return sum_for, sum_while


def main():
    """Main function to get input from keyboard and display results."""
    print("=" * 50)
    print("Sum of First N Numbers Calculator")
    print("=" * 50)
    
    # Get input from keyboard
    while True:
        try:
            n = int(input("\nEnter a positive integer (n): "))
            if n < 0:
                print("Please enter a non-negative integer!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    # Calculate sum using both methods
    sum_for, sum_while = sum_to_n(n)
    
    # Display results
    print("\n" + "=" * 50)
    print(f"Sum of first {n} numbers:")
    print(f"  Using for loop:   {sum_for}")
    print(f"  Using while loop: {sum_while}")
    print(f"  Formula (n*(n+1)/2): {n * (n + 1) // 2}")
    print("=" * 50)
    
    # Verify both methods give same result
    if sum_for == sum_while:
        print("\n✓ Both methods produce the same result!")
    else:
        print("\n✗ Error: Methods produce different results!")


if __name__ == "__main__":
    main()

