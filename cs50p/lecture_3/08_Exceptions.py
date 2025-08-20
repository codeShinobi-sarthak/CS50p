def get_int(prompt):
    while True:
        try:
             return int(input(prompt))
        except ValueError:
             print("Not a number")                           
            #  pass  #? pass - just dont print the above print and yes you have to comment it or remove it  

def main():
    x = get_int("x: ")
    y = get_int("y: ")
    
    print(x+y)
    
main()
        
        