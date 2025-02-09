from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

User = get_user_model()



class ProduuctListCreateAPITest(TestCase):
    def setUp(self):
        self.client = APIClient
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='test123'
        )
        self.client.force_authenticate(self.user)
        self.product1 = Product.objects.create(
            user=self.user, title="Laptop", content="Powerful laptop", price=1000.00, public=True
        )
        self.product2 = Product.objects.create(
            user=self.user, title="Phone", content="Smartphone", price=500.00, public=False
        )
        self.product3 = Product.objects.create(
            user=self.user, title="Tablet", content="Tablet for kids", price=300.00, public=True
        )
        
    def test_list_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)

    def test_filter_by_min_price(self):
        response = self.client.get("/api/products/?min_price=500")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(float(product["price"]) >= 500 for product in response.data["results"]))

    def test_filter_by_max_price(self):
        response = self.client.get("/api/products/?max_price=600")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(float(product["price"]) <= 600 for product in response.data["results"]))

    def test_filter_by_title(self):
        response = self.client.get("/api/products/?title=laptop")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all("laptop" in product["title"].lower() for product in response.data["results"]))

    def test_filter_by_public(self):
        response = self.client.get("/api/products/?public=true")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(product["public"] is True for product in response.data["results"]))

    def test_filter_by_owner(self):
        response = self.client.get(f"/api/products/?owner={self.user.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(product["owner"]["id"] == self.user.id for product in response.data["results"]))
