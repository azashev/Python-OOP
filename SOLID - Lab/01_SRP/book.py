# Refactor the code below, so there is a separate class called Library, which contains books and has a method called
# find_book(title) that returns the book with the given title.
# Remove the unnecessary code from the Book class.
#
#
# Code to refactor:
#
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page
