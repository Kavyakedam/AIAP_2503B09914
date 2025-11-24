def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


# Take input from keyboard
num = int(input("Enter a number: "))

result = factorial(num)
print("Factorial of", num, "is:", result)