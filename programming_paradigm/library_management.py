

class Book:
    """Represents a book with title, author, and availability status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Marks a book as checked out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        """Prints all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
