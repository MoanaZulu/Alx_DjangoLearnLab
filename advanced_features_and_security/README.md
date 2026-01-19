# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created via Django admin:
- **Viewers**: can_view
- **Editors**: can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

## Views
Protected with `@permission_required` decorators:
- book_list → requires can_view
- create_book → requires can_create
- edit_book → requires can_edit
- delete_book → requires can_delete
