try:
    num = int(input("Enter a number to print its multiplication table: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
