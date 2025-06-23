try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is Odd")
except ValueError:
    print("Value Error: Please enter a valid integer.")
except TypeError:
    print("Type Error: Invalid input type.")
except Exception as e:
    print("Unexpected error occurred:", e)
