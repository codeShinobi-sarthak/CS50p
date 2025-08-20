# 1. Ask the user for the filename
filename = input("Please enter the filename you want to read (e.g., my_goals.txt): ")

try:
    # 2. The ONLY thing we 'try' is opening the file
    print(f"\nAttempting to open '{filename}'...")
    file = open(filename, 'r') # This is the line that might fail

except FileNotFoundError:
    # 3. This runs ONLY if the file was not found
    print(f"Error: The file '{filename}' was not found.")

else:
    # 4. This runs ONLY if the file was found and opened successfully
    print("File found! Here are the contents:")
    with file: # Use 'with' to ensure it closes
        for line in file:
            print(line.strip())

finally:
    # 5. This ALWAYS runs, no matter what happened
    print("\nFile reading operation finished.")