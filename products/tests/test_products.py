import json

from urllib import response
from django.test import TestCase,Client
from products.models import Product,Category,Color
from users.models import User
client = Client()
class CategoryTest(TestCase):
    def setUp(self):
        category = Category.objects.create(id=1,title='test')
        color = Color.objects.create(id=1,name='red')
        Product.objects.create(
            category = Category.objects.get(id=category.id),
            colors = Color.objects.get(id=color.id),
            name = 'chair_test',
            price = 15000,
            inventory = 20
        )
    def tearDown(self):
        return Product.objects.all().delete()

    def test_prodcuts_get(self):
        response = client.get('/products/')
        self.assertEqual(response.status_code,200)

    def test_prodcuts_detail_get(self):
        response = client.get('/products/1')
        self.assertEqual(response.status_code,200)

    def test_products_create(self):
        data = {
            'category' :1,
            'colors' : 1,
            'name' : 'test',
            'price' : 15000,
            'inventory' : 20
        }
        response = client.post('/products/create/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_products_keyerror(self):
        data = {
            'category' :1,
            'name' : 'test',
            'price' : 15000,
            'inventory' : 20
        }
        response = client.post('/products/create/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,400)
