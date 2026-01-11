# Retrieve Books

Run the following in the Django shell:

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
print(books)

# Retrieve a single book by title
book = Book.objects.get(title="1984")
print(book)
