from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Python Basics",
            publication_year=2024,
            author=self.author
        )

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Python Basics", str(response.data))

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Python Basics")

    def test_create_book_requires_authentication(self):
        url = reverse("book-create")
        data = {"title": "New Book", "publication_year": 2025, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticate and try again
        self.client.login(username="tester", password="pass123")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        self.client.login(username="tester", password="pass123")
        url = reverse("book-update", args=[self.book.id])
        data = {"title": "Updated Title", "publication_year": 2024, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        self.client.login(username="tester", password="pass123")
        url = reverse("book-delete", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_title(self):
        url = reverse("book-list") + "?title=Python Basics"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Python Basics")

    def test_search_books(self):
        url = reverse("book-list") + "?search=Python"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Python Basics", str(response.data))

    def test_order_books(self):
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
