# 1. Open the file in write mode ('w')
# If 'goals.txt' doesn't exist, it will be created.
# If it exists, its contents will be erased.
file = open('./file_handling_and_exceptions/goals.txt', 'w')

# 2. Write content to the file
file.write("Become good in python\n")
file.write("get a good job")

# 3. IMPORTANT: Close the file to save the changes
file.close()

print("File 'goals.txt' has been created and written to. \n")


# ==============================================================
# Below code is for reading the text from a file

# 1. Open the file in read mode ('r')
file_read = open('./file_handling_and_exceptions/goals.txt', 'r')

# 2. Read the entire content of the file
content = file_read.read()

# 3. Close the file
file_read.close()

# 4. Print the content you read
print("Content read from the file -> ")
print(content)
