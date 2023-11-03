def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number:"))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

# Input from the user
number = float(input("Enter a number: "))

# Calculate the square
square = number ** 2

print(f"The square of {number} is {square}")
