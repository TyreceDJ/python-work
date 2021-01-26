# TODO:
# Create a class called "Movie" with the attributes title, genre, and rating. Then define a method
# called "printer()". The method should print the statement "[title] is a(n) [genre] movie with a
# [rating]% rating on Rotten Tomatoes."
class Movie():

  def __init__(self, title, genre, rating):
    self.title = title
    self.genre = genre
    self.rating = rating

  def printer(self):
    print(f"{self.title} is a(n) {self.genre} movie with a {self.rating}% rating on Rotten Tomatoes.")

# TODO:
# After solving the above, think about why methods have a parameter of "self" whereas functions
# do not. Why would a method defined on a class have this set as a parameter? What does it do?