class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    
class Library:
  def __init__(self):
    self.books = []
    self.checked_out_books = []
    
  def add_book(self, book):
    self.books.append(book)
    
  def check_out_book(self, title):
    for book in self.books:
      if book.title == title:
        self.books.remove(book)
        self.checked_out_books.append(book)
        return True
    return False
  
  def return_book(self, title):
    for book in self.checked_out_books:
      if book.title == title:
        self.checked_out_books.remove(book)
        self.books.append(book)
        return True
    return False
  
  def list_available_books(self):
    for book in self.books:
      print(f"{book.title} by {book.author}")