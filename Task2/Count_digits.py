def count_digits(n):
    if n < 0:
        n = -n  # convert negative to positive manually
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

try:
    num = int(input("Enter a number: "))

    if num == 0:
        print("Number of digits: 1")
    else:
        print("Number of digits:", count_digits(num))

except ValueError:
    print("Invalid input! Please enter a valid integer.")
