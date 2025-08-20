names = []; #? empty list

name = input("What is your name? \n")

"""
# ! create the file names.txt if not exist
file = open("names.txt", "a") #? a for append 
file.write(f"{name}\n")
file.close()
"""

# to automate the process of opening and closing the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")