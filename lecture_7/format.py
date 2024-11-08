import re

name = input("Enter your name: ")
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    print("Last name:", matches.group(1))
    print("First name:", matches.group(2))

print(f"hello {name}")