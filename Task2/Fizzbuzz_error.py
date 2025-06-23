try:
    n = int(input("Enter a number for FizzBuzz: "))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)
