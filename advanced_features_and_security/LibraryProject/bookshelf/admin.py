# ============================
# Groups and Permissions Setup
# ============================
# In Django admin, create the following groups:
# - Viewers: assign "can_view" permission
# - Editors: assign "can_create" and "can_edit" permissions
# - Admins: assign "can_view", "can_create", "can_edit", and "can_delete" permissions
#
# These groups control access to Book model actions.






from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
