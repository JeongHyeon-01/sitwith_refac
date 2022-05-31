from http import client
import json, jwt

from unittest.mock import patch, MagicMock
from rest_framework.test import APITestCase
from django.conf   import settings
from django.test   import TestCase, Client

from users.models  import *

class UserSignUpTest(APITestCase):
    def setUp(self):
        User.objects.create(
            email = 'test@test.com',
            password = '1q2w3e4r5t!',
            refreshtoken = "token_refresh",
            username = "test"
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_user_signup_test(self):
        client = Client()
        user = {
            'email':'test1@test.com',
            'password':'1q2w3e4r5t!',
            'password2':'1q2w3e4r5t!',
            'username':'test'
            }
        response = client.post('/users/signup/', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_user_signup_wrong_password2(self):
        client = Client()
        user ={
            'email':'test@test.com',
            'password':'1q2w3e4r5t!',
            'password2':'1q2w3e4r5t',
            'username':'test'            
        }
        response = client.post('/users/signup/', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_user_signup_short_password(self):
        client = Client()
        user ={
            'email':'test@test.com',
            'password':'1q2w3e',
            'password2':'1q2w3e',
            'username':'test'            
        }
        response = client.post('/users/signup/', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_user_signup_none_special_password(self):
        client = Client()
        user ={
            'email':'test@test.com',
            'password':'1q2w3e4r',
            'password2':'1q2w3e4r',
            'username':'test'            
        }
        response = client.post('/users/signup/', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_user_signup_not_email(self):
        client = Client()
        user ={
            'email':'test',
            'password':'1q2w3e',
            'password2':'1q2w3e',
            'username':'test'            
        }
        response = client.post('/users/signup/', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,400)
