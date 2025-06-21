class Book:
    def __init__(self, title, author, year):
        """
        Constructor method.
        This method is automatically called when you create a new instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method.
        Automatically called when an object is deleted or goes out of scope.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        User-friendly string representation (when you use print()).
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Developer/debug representation (used by repr()).
        Should ideally allow recreating the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
