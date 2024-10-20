with open("names.txt", "r") as file:
    # lines = file.readlines()
    for line in file:
        print(line.rstrip())

# print(lines) #? print the list of names

# for line in lines:
#     print(line, line.rstripr()) #? print each name in the list