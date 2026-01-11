# Delete a Book

Run the following in the Django shell:

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Delete the book
book.delete()

print("Book deleted successfully")
