numbers = list(map(int, input("Enter numbers (space separated): ").split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print(f"Sum of all even numbers: {even_sum}")
