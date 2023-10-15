from django.contrib import admin
from user.models import BaseUser

@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', "phone_number", 'store_instagram_id', 'store_type', 'email', 'address', 'postal_code']