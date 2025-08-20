try:
    with open('file.txt', 'r') as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"An error occurred: {e}")


print("This line will always execute after the try-except block.")