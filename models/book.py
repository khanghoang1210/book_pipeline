class Book:
  def __init__(self, book_name, star, price, status, poster_link):
    self.book_name = book_name
    self.star = star
    self.price = price
    self.status = status
    self.poster_link = poster_link

    def show(self):
      print(f"Movie info: [{self.book_name}]-[{self.status}]")
