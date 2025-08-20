import re 

email = input("Enter your email: ")

if re.match(r"\w+@(\w\.)?\w+\.(edu|com|org|gov)$", email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")