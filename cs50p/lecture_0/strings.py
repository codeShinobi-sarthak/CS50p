name = input("what is your name? ")

#! remove whitespace for name
name = name.strip()

#! capatalize the first letter of the name
name = name.capitalize();

""" 
NOTE: 
chainig the methods
name = name.strip().capitalize();
name = input("what is your name? ").split().capatalize();

"""

first, last = name.split(" ");

print("name :  "+ name);
print("first name :  "+ first);
print("last name :  "+ last);
