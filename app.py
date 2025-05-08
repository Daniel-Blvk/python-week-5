class Book:
    def __init__(self, title, author):
         self.title = title
         self.author = author
         self.isreading = False

    def readbook(self):
         self.isreading = True
         print(f"You are reading:  '{self.title}' by {self.author}.")

    def buybook(self):
         self.isbuying = False
         print(f"you have bought '{self.title}' by {self.author}.")

class joural(Book):
    def __init__(self, title, author):
         self.isbuying = False
         self.title = title
         self.author = author
    def publish(self):
         print(f"'{self.title}' by {self.author} has been published.")
   

# # Created instances
book1 = Book("Purpose driven life", "rick warren")
journal1= joural("Nature", "Various Authors")

 # Used the methods
book1.buybook()# book1.readbook()


print("\n")
journal1.publish()


