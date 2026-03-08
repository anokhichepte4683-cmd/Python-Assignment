class Library:

    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
            print(self.book_name, "checked out")
        else:
            print(self.book_name, "is not available")

    def return_book(self):
        self.available = True
        print(self.book_name, "returned")

    def display(self):
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Available:", self.available)


# creating objects
book1 = Library("2000", "Radha Shyam ")
book2 = Library("Harry Potter", "J.K Rowling")

# using methods
book1.display()
book1.checkout()
book1.display()
book1.return_book()
book1.display()