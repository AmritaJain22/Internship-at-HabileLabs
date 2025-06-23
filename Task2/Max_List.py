numbers = []
print("Enter 5 numbers:")
i = 0
while i < 5:
    try:
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
        i += 1
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
print("Numbers you entered:", numbers)
print("Maximum number is:", max(numbers))
