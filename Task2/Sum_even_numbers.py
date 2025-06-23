try:
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    print("Sum of even numbers is:", even_sum)
except ValueError:
    print("Invalid input! Please enter only integers separated by spaces.")
