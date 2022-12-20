# We want to print books, but before printing the book, we should format it.
# To accomplish this, we have a class Printer that can print books and a class Formatter which is used by the Printer.
# Refactor the provided code that breaks the DIP because both Printer and Formatter depend on concretions, not
# abstractions, by creating abstractions and injecting them wherever needed.
#
#
# Code to refactor:
#
# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book


class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PrePrintFlayer:
    def format(self, book):
        return f"<---------->\n{book.title}\n<---------->\n{book.author}\n|------------|"


class Printer:
    def get_book(self, book: Book, formatter):
        return formatter.format(book)


nf = Formatter()
ff = PrePrintFlayer()
b = Book("t1", "a1", "c1")
p = Printer()
p2 = Printer()
print(p.get_book(b, nf))
print(p2.get_book(b, ff))
