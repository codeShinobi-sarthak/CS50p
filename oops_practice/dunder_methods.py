class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # For the user (e.g., print())
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # For the developer (e.g., interactive console)
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


# --- Let's try again ---
my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")

# The print() function now automatically calls __str__
print(my_book)

# The repr() function calls __repr__
print(repr(my_book))


# Method    | __str__         | __repr__
# Audience  | End-user        | Developer
# Goal      | Readability     | Unambiguous, complete
# Called by | print(), str()  | repr(), interactive prompt
