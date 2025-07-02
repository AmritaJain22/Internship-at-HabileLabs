num = int(input("Enter an integer: "))
reversed_num = int(str(abs(num))[::-1])
if num < 0:
    reversed_num = -reversed_num
print(f"Reversed number: {reversed_num}")
