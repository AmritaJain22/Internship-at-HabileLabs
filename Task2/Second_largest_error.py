try:
    n = int(input("How many numbers you want to enter? "))
    if n < 2:
        print("Need at least 2 numbers to find the second largest.")
    else:
        numbers = []
        for i in range(n):
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                

        