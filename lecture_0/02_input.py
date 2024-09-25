"""
This script prompts the user to input their name and then prints a greeting message in three different ways:
1. Using string concatenation.
2. Using a comma to separate the string and the variable.
3. Using an f-string for formatted output.

Functions:
- None

Usage:
Run the script and input your name when prompted. The script will then print the greeting messages.
"""

name = input("what is your name? ")
print("Hello, "+ name) 
print("Hello, ",name)
#! you can also use f-string to print the output
print(f"hello, {name}")