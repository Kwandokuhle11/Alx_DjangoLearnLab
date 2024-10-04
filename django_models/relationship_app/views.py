from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query all Book instances
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify the template to be used
    context_object_name = 'library'  # Specify the context variable name
