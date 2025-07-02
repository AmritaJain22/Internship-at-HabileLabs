n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a positive integer greater than 0.")
else:
    total = sum(range(1, n + 1))
    print(f"The sum of all numbers from 1 to {n} is {total}.")
