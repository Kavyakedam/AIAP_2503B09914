def divide(a, b):
    return a / b


# Debug: Handle division by zero error
if __name__ == "__main__":
    try:
        result = divide(10, 0)
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

