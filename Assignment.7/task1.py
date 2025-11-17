def add(a, b):
    return a + b


# Example usage
if __name__ == "__main__":
    # Get numbers from keyboard
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")

