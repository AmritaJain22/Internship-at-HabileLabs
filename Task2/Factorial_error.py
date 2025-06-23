def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a number to find factorial: "))
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")
except ValueError as ve:
    print("Value Error:", ve)
except TypeError:
    print("Type Error: Please enter a valid number.")
except Exception as e:
    print("Unexpected error occurred:", e)
