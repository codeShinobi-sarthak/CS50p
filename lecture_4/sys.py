import sys

try:
    if len(sys.argv) < 2:
        sys.exit("less than 2 argv")
    # elif len(sys.argv) > 2:
    #     sys.exit("too many argv")

    print("Hello, how are you", sys.argv[1])
    # print(sys.argv[1])
    print(sys.argv)  # ? returns array 
    print(sys.argv[2:])  # ? returns sliced array from index 2
except:
    print("Error")
