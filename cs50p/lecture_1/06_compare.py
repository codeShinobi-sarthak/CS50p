s = input("Do you agree").lower()
#! another way
# s = s.lower() 

if s == "Y" or s == "y":
    print("Agreed")
elif s == "N" or s == "n":
    print("Disagree")
else:
    print("enter valid values")  
       
    
#* more better approach 
if s in ["yes", "y"]:
    print("Agreed")
elif s in ["no", "n"]:
    print("Disagreed")
else:
    print("enter valid values")        