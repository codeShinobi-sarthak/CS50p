# Part 1: Writing to the file using a context manager
with open('./file_handling_and_exceptions/my_goals_2.txt', 'w') as file:
    print("Writing to file...")
    file.write("Master Python for Machine Learning\n")
    file.write("Build a real-world AI project")
print("Writing complete. File is now closed.\n")


# Part 2: Reading from the file using a context manager
print("Reading from file...")
with open('./file_handling_and_exceptions/my_goals_2.txt', 'r') as file:
    for line in file:
        print(line.strip())
print("Reading complete. File is now closed.")