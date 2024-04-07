from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author_name']
    search_fields = ['name', 'author_name']


admin.site.register(Book, BookAdmin)
