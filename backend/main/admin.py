from django.contrib import admin

# Register your models here.

from .models import CustomUser, Place


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'firstname', 'lastname')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'image', 'url', 'description', 'created_at')
