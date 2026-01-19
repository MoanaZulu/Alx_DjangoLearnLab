from .forms import ExampleForm



from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm






from django.shortcuts import render
from .models import Book
from .forms import SearchForm

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        title = form.cleaned_data['title']
        # Safe ORM query instead of raw SQL
        books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})






from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # placeholder logic for creating a book
    return render(request, 'bookshelf/form_example.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # placeholder logic for editing
    return render(request, 'bookshelf/form_example.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'bookshelf/book_list.html')

