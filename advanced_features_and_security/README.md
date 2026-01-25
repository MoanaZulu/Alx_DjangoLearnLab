# Advanced Features and Security — Permissions & Groups

## Objective
Implement and manage permissions and groups to control access to various parts of the Django application.

## Setup
- Custom permissions defined in `models.py`:
  - `can_view`, `can_create`, `can_edit`, `can_delete`
- Groups created in Django Admin:
  - **Viewers** → can_view
  - **Editors** → can_create, can_edit
  - **Admins** → all permissions

## Usage
- Views protected with `@permission_required` decorators.
- Example:
  ```python
  @permission_required('LibraryProject.can_edit', raise_exception=True)
  def book_edit(request, pk):
      ...






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
