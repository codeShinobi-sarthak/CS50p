"""
    This script contains two infinite loops that prompt the user to enter a number.
    The first loop: #! will not break
    - Continuously prompts the user to enter a number.
    - If the input is not a valid integer, it prints "Not a number".
    - If the input is a valid integer, it prints the entered number twice.
    The second loop:#! will break i.e print "End of loop"
    - Continuously prompts the user to enter a number.
    - If the input is not a valid integer, it prints "Not a number".
    - If the input is a valid integer, it prints the entered number and breaks the loop.
    -After the second loop ends, the script prints "End of loop".
"""
    
    
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print("You entered: ", x)
#     except ValueError:
#          print("Not a number")
#     else:
#         print(f"you entered: {x}")
    


while True:
    try:
        x = int(input("Please enter a number: "))
        print("You entered: ", x)
        # break; also works here
    except ValueError:
         print("Not a number")
    else:
        break;
    

print("End of loop")