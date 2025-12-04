class Book:
  def __init__(self, title, year, author):
    self.title = title
    self.year = year
    self.author = author
    
  def __del__(self):
      print (f"Deleting({self.title}")
      
  def __str__(self):
        return f"Title: {self.title}, by {self.author}, published in {self.year}"
      
  def __repr__(self):
        return f"Book('{self.title}', {self.author}, '{self.year}')"