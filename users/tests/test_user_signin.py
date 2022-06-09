import json
from users.models import *
from django.test import Client,TestCase
from rest_framework.test import APITestCase, DjangoClient
from unittest.mock import patch, MagicMock

from django.contrib.auth.hashers import make_password, check_password

from django.conf   import settings
from django.test   import TestCase, Client

client = Client()
class UserSignInTest(TestCase):
    def setUp(self):
        user =User.objects.create(
            id = 1,
            email = 'test@test.com',
            password = make_password('1q2w3e4r5t!'),
            refreshtoken = 'refreshtoken',
            nickname = 'user'
        )
    def tearDown(self):
        User.objects.all().delete()

    def test_users_signin_post_success_test(self):
        user = User.objects.get(id =1)
        data = {
            'email' : 'test@test.com',
            'password':'1q2w3e4r5t!'
        }
        if user.email == data['email'] and check_password(data['password'],user.password):
            response = 200    
        else:
            response = 400

        response = client.post('/users/signin/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_users_signin_post_wrong_password_test(self):
        user = User.objects.get(id =1)
        data = {
            'email' : 'test@test.com',
            'password':'1q2w3e4r!'
        }
        if user.email == data['email'] and check_password(data['password'],user.password):
            response = 200    
        else:
            response = 400

        response = client.post('/users/signin/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_users_signin_post_wrong_email_test(self):
        user = User.objects.get(id =1)
        data = {
            'email' : 'testm',
            'password':'1q2w3e4r!'
        }
        if user.email == data['email'] and check_password(data['password'],user.password):
            response = 200    
        else:
            response = 400

        response = client.post('/users/signin/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)