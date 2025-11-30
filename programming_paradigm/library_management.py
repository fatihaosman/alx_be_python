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



# Define a Book class that stores details about a single book
class Book:
    def __init__(self, title, author):
        # Each book has a title and an author's name
        self.title = title
        self.author = author


# Define a Library class that manages many books
class Library:
    def __init__(self):
        # List of books currently available in the library
        self.books = []
        
        # List of books currently checked out by users
        self.checked_out_books = []

    # Add a new book object into the library
    def add_book(self, book):
        self.books.append(book)

    # Checkout a book by searching for its title
    def check_out_book(self, title):
        # Loop through all available books
        for book in self.books:
            if book.title == title:
                # Remove the book from available list
                self.books.remove(book)
                # Add it to checked-out list
                self.checked_out_books.append(book)
                return True   # Checkout successful
        return False  # Book not found

    # Return a book back to the library
    def return_book(self, title):
        # Loop through checked-out books
        for book in self.checked_out_books:
            if book.title == title:
                # Remove from checked-out list
                self.checked_out_books.remove(book)
                # Put back into available books list
                self.books.append(book)
                return True   # Return successful
        return False  # Book was not checked out

    # Display all books currently available
    def list_available_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")
