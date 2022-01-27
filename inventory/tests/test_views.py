from django.urls import reverse
from django.test import TestCase
from django.test import Client


class InventoryTestClass(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        

    def test_inventory_list_view(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(1 + 1, 3)

    def test_inventory_detail_view(self):
        response = self.client.get('/inventory/2/')
        self.assertEqual(response.status_code, 200)

    #def test_inventory_api_view(self):
     #   response = self.client.get('/inventory/api/inventory')
      #  self.assertEqual(response.status_code, 200)