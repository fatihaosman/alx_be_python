# class Book:
#   def __init__(self, title, author):
#     self.title = title
#     self.author = author
    
# class Library:
#   def __init__(self):
#     self.books = []
#     self.checked_out_books = []
    
#   def add_book(self, book):
#     self.books.append(book)
    
#   def check_out_book(self, title):
#     for book in self.books:
#       if book.title == title:
#         self.books.remove(book)
#         self.checked_out_books.append(book)
#         return True
#     return False
  
#   def return_book(self, title):
#     for book in self.checked_out_books:
#       if book.title == title:
#         self.checked_out_books.remove(book)
#         self.books.append(book)
#         return True
#     return False
  
#   def list_available_books(self):
#     for book in self.books:
#       print(f"{book.title} by {book.author}")   



# This class represents a single book object
class Book:
    def __init__(self, title, author):
        # Each book has a title and author
        self.title = title
        self.author = author
        # Track if the book is checked out or not
        self.is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self.is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self.is_checked_out = False


# This class manages a collection of book objects
class Library:
    def __init__(self):
        # List to store available books
        self.books = []
        # List to store checked-out books
        self.checked_out_books = []

    def add_book(self, book):
        """Add a Book object to the library."""
        self.books.append(book)

    def check_out_book(self, title):
        """
        Find the book by title.
        Remove it from available books.
        Add it to checked-out books.
        Mark the book as checked out.
        """
        for book in self.books:
            if book.title == title:
                book.check_out()  # mark it checked out
                self.books.remove(book)
                self.checked_out_books.append(book)
                return True
        return False

    def return_book(self, title):
        """
        Find the book by title in checked-out list.
        Move it back to available books.
        Mark it as returned.
        """
        for book in self.checked_out_books:
            if book.title == title:
                book.return_book()  # mark it returned
                self.checked_out_books.remove(book)
                self.books.append(book)
                return True
        return False

    def list_available_books(self):
        """Print all books that are NOT checked out."""
        for book in self.books:
            print(f"{book.title} by {book.author}")
