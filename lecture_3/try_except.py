try:
    x = int(input("Please enter a number: "))
    print("You entered: ", x)
except ValueError:
    print("That was not a valid number")

