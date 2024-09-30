def main():
    x = get_int()
    print(f"x is {x}")


#?  frist function
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? \n"))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x


#?  second function
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? \n"))
#         except ValueError:
#             print("x is not an integer")


#?  third function
def get_int():
    while True:
        try:
            return int(input("What's x? \n"))
        except ValueError:
            pass #* just not print not a interger every time


main()
