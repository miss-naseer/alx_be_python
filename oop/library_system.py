class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def _str_(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size  # in KB

    def _str_(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def _init_(self, title, author, page_count):
        super()._init_(title, author)
        self.page_count = page_count

    def _str_(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        # self.books.append

    def list_books(self):
        for book in self.books:
            print(book)