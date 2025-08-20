class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            print("Book is already checked out.")
            return

        self.is_checked_out = True
        print(f"{self.title} has been checked out successfully.")

    def check_in(self):
        if not self.is_checked_out:
            print("Book is not checked out.")
            return
        
        self.is_checked_out = False
        print(f"{self.title} has been checked in successfully.")


# --- Using the Objects and Their Methods ---

# Create an instance of the Book class.
my_book = Book("1984", "George Orwell", 328)

# Let's check its initial status.
print(f"Initial status - Is '{my_book.title}' checked out? {my_book.is_checked_out}")

# Now, let's call the check_out method on our object.
my_book.check_out()

# Check the status again. Notice how the method changed the object's attribute.
print(f"After checkout - Is '{my_book.title}' checked out? {my_book.is_checked_out}")

# Let's try to check it out again.
my_book.check_out()

# Now, let's check it back in.
my_book.check_in()

# And check the final status.
print(f"After checkin - Is '{my_book.title}' checked out? {my_book.is_checked_out}")