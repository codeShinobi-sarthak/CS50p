names = []; #? empty list

for _ in range(3):
    names.append(input("What is your name? "))


for name in sorted(names):
    print(name);