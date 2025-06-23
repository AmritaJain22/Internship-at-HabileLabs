def fibonacci_series(n):
    if n <= 0:
        raise ValueError("Number must be greater than 0.")
    
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

try:
    num = int(input("Enter how many terms of Fibonacci series you want: "))
    series = fibonacci_series(num)
    print(f"Fibonacci series ({num} terms):", series)
except ValueError as ve:
    print("Value Error:", ve)
except TypeError:
    print("Type Error: Please enter a valid integer.")
except Exception as e:
    print("Unexpected error occurred:", e)
