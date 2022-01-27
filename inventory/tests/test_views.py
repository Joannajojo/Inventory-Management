from django.urls import reverse
from django.test import TestCase
from django.test import Client
from inventory.models import Inventory,Supplier


class InventoryTestClass(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.supplier=Supplier.objects.create(name='Aikeyar')
        Inventory.objects.create(name='Fantasia', description = 'Dining table', note = '', stock = 5,availability = True, supplier = self.supplier)

    def test_inventory_list_view(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        

    def test_inventory_detail_view(self):
        response = self.client.get('/inventory/1')
        self.assertEqual(response.status_code, 200)

    def test_inventory_api_view(self):
        response = self.client.get('/inventory/api/inventory')
        self.assertEqual(response.status_code, 200)