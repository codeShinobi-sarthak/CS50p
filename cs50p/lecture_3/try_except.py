try:
    x = int(input("Please enter a number: "))
    print("You entered: ", x)
except ValueError:
    print("Not a number")
else:
    print(f"you entered: {x}")
    
    
