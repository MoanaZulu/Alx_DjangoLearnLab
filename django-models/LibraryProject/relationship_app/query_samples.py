from .models import Author, Book, Library, Librarian

# Query all books by a specific author
books_by_author = Book.objects.filter(author__name="Some Author")

# List all books in a library
library_books = Library.objects.get(name="Central Library").books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library__name="Central Library")






from relationship_app.models import Author, Book, Library

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
