try:
    n = int(input("How many numbers you want to enter? "))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    x = int(input("Enter the number to find frequency of: "))

    count = numbers.count(x)
    print(f"The number {x} appears {count} times in the list.")

except ValueError:
    print("Invalid input! Please enter valid integers only.")
