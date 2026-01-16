from django.shortcuts import render

# Create your views here.





from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

@permission_required('relationships.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return HttpResponse("Book added successfully")
    return HttpResponse("Add book form")

@permission_required('relationships.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.save()
        return HttpResponse("Book updated successfully")
    return HttpResponse("Edit book form")

@permission_required('relationships.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("Book deleted successfully")
