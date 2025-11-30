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



class Book:
    """Represents a single book with a title and author."""
    def __init__(self, title, author):
        # Store book title
        self.title = title
        # Store book author
        self.author = author


class Library:
    """Represents a library that stores, checks out, and returns books."""
    def __init__(self):
        # A private list that stores all available books in the library
        self._books = []

        # A private list that stores books that have been checked out
        self._checked_out_books = []

    def add_book(self, book):
        """
        Adds a new Book object to the library.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Removes a book from available books and adds it to checked-out books.
        Returns True if successful, False if book not found.
        """
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                self._checked_out_books.append(book)
                return True
        return False

    def return_book(self, title):
        """
        Moves a book from checked-out list back to available books.
        Returns True if successful, False if book is not found.
        """
        for book in self._checked_out_books:
            if book.title == title:
                self._checked_out_books.remove(book)
                self._books.append(book)
                return True
        return False

    def list_available_books(self):
        """
        Prints all books that are currently available in the library.
        """
        for book in self._books:
            print(f"{book.title} by {book.author}")
