from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test instances of the Menu model
        MenuItem.objects.create(title="Pizza", price=10)
        MenuItem.objects.create(title="Burger", price=8)
        MenuItem.objects.create(title="Salad", price=6)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
