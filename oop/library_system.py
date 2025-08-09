
class Book:
    def __init__(self, title, author):
        """Initialize base Book class."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size (in MB)."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} [E-Book, {self.file_size} MB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

def __str__(self):
    return f"{self.title} by {self.author} [Print Book, {self.page_count} pages]"


class Library:
    def __init__(self):
        """Initialize library with an empty book list."""
        self.books = []
    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Only instances of Book or its subclasses can be added.")
            
    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("Library is empty.")
        else:
            print("\nLibrary Collection:")

        for book in self.books:
            print(f"- {book}")
