numbers = list(map(int, input("Enter numbers (space separated): ").split()))
x = int(input("Enter the number to count: "))
count = numbers.count(x)
print(f"{x} appears {count} time(s) in the list.")
