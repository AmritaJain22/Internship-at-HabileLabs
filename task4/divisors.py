num = int(input("Enter a number: "))
print(f"Divisors of {num} are:")
for i in range(1, abs(num) + 1):
    if num % i == 0:
        print(i)
