from typing import Self
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Create Author and Book objects
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Book 1", publication_year=2020, author=self.author)

    def test_create_book(self):
        """Test creating a new book"""
        url = reverse('book-list')
        data = {'title': 'Book 2', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_books(self):
        """Test retrieving all books"""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        """Test updating an existing book"""
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book 1', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book 1')

    def test_delete_book(self):
        """Test deleting a book"""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        url = f'/books/?author={self.author.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_search_books(self):
        """Test searching books by title"""
        url = '/books/?search=Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year"""
        url = '/books/?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_unauthenticated_access(self):
        """Test that unauthenticated users can't create or delete books"""
        self.client.logout()  # Logout user
        url = reverse('book-list')
        
        # Try to create a book
        data = {'title': 'Unauthorized Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
