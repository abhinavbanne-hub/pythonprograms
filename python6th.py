class Library:
    
    # Constructor to initialize book details
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True   # Availability status

    # Method to check out a book
    def checkout_book(self):
        if self.available:
            self.available = False
            print(f"'{self.book_name}' has been checked out.")
        else:
            print(f"'{self.book_name}' is currently not available.")

    # Method to return a book
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.book_name}' has been returned.")
        else:
            print(f"'{self.book_name}' was not checked out.")

    # Method to display book details
    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print("\nBook Name:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)


# ---- Main Program ----
book1 = Library("Python Programming", "Guido van Rossum")
book2 = Library("Data Structures", "Mark Allen Weiss")

book1.display_book()
book1.checkout_book()
book1.display_book()
book1.return_book()
book1.display_book()

book2.display_book()