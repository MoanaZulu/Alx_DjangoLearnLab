from django.shortcuts import render

# Create your views here.



from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request): ...

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id): ...

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id): ...
