from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Custom logic before saving the book
        serializer.save()

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Custom logic before updating the book
        serializer.save()

# In both views, IsAuthenticatedOrReadOnly is used, which restricts write operations to authenticated users.
# BookListCreateView: Handles listing all books and creating a new book.
# Read-only access is allowed for unauthenticated users; only authenticated users can create a new book.

# BookRetrieveUpdateDeleteView: Handles retrieving, updating, and deleting a specific book.
# Read-only access is allowed for unauthenticated users; only authenticated users can modify or delete the book.
