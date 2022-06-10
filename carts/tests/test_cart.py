import json
from urllib import response
from django.test import TestCase, Client
from http.cookies import SimpleCookie
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from products.models import *
client = Client()

class CartsTest(TestCase):
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

    def test_cart_create(self):
        data = {
            'user_info' : 1,
            'product_info' :1,
            'quantity' : 2
        }
        user =  User.objects.create(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123'
        )
  
        refresh_token = RefreshToken.for_user(user=user)
        access_token = refresh_token.access_token
        self.client.cookies = SimpleCookie({'access_token': access_token})
        response = self.client.post('/carts/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_cart_get(self):
        user =  User.objects.create(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123'
        )
        refresh_token = RefreshToken.for_user(user=user)
        access_token = refresh_token.access_token
        self.client.cookies = SimpleCookie({'access_token': access_token,'refresh_token':refresh_token})
        response = self.client.get('/carts/')
        self.assertEqual(response.status_code, 200)