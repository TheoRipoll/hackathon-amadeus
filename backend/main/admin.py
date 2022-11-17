from django.contrib import admin

# Register your models here.

from .models import CustomUser, Place


# Registering the CustomUser model with the admin site.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'firstname', 'lastname')


# A decorator that registers the Place model with the admin site.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'image', 'url', 'description', 'created_at')
