try:
    n = int(input("Enter number of rows: "))
    for i in range(1, n + 1):
        print("*" * i)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
