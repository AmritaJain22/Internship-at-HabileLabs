n = int(input("Enter how many numbers: "))
if n < 2:
    print("Need at least two numbers to find the second largest.")
else:
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        print("There is no second largest number (all numbers are the same).")
    else:
        unique_numbers.sort(reverse=True)
        print(f"The second largest number is {unique_numbers[1]}.")
