from django.shortcuts import render

# Create your views here.



from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request): ...

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id): ...

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id): ...




from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



  GNU nano 8.7               relationship_app/views.py                Modified


from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'





^G Help      ^O Write Out ^F Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^/ Go To Line



from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



def list_books(request):
    books = Book.objects.all()   # <-- must be objects, not object
    return render(request, 'relationship_app/list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
