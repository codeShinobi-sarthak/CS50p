print('Reading from ./file_handling_and_exceptions/goals.txt')

file = open('./file_handling_and_exceptions/goals.txt', 'r')

for line in file:
    print(line.strip())


file.close()

print("\nEnd of file reading.")