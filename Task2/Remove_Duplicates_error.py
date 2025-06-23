try:
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))
    
    unique_numbers = list(set(numbers))  # remove duplicates
    print("List after removing duplicates:", unique_numbers)

except ValueError:
    print("Invalid input! Please enter integers only, separated by spaces.")
