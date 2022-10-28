class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# Create a class called Book. It should have an __init__() method that should receive:
# • name: string
# • author: string
# • pages: int
#
#
#
# Test code:
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

#
# Expected output:
# My Book
# Me
# 200
