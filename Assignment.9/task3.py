def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract second number from first number."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide first number by second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def main():
    """Main function to get user input and perform calculations."""
    print("Simple Calculator")
    print("=" * 30)
    
    try:
        # Get first number from keyboard
        num1 = float(input("Enter the first number: "))
        
        # Get second number from keyboard
        num2 = float(input("Enter the second number: "))
        
        # Perform all operations
        print("\nResults:")
        print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
        print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
        print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
        
        # Handle division separately to catch zero division error
        try:
            print(f"Division: {num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(f"Division: Error - {e}")
            
    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == "__main__":
    main()

