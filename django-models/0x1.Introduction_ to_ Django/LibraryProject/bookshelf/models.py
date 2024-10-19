from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import Book

# Customizing the BookAdmin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in the list view
    list_filter = ('author', 'publication_year')  # Add filters for author and publication year
    search_fields = ('title', 'author')  # Enable search by title and author

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
