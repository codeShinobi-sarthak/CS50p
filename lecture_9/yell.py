def main():
    yell("This", "is", "CS50")


# list comprehension
def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
