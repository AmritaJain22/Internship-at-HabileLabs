import random
secret = random.randint(1, 10)
try:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print(" Correct! ")
    else:
        print(f" Wrong guess!")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
