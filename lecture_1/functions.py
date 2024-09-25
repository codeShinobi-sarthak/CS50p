def hello(name="world"):
    print("Hello, " + name)
    return "how are you"


name = input("let me know your name: ")
hello(name)

# ? calling hello with printing return value
print(hello()) 

