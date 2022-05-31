from http import client
import json
from pydoc import cli

from django.shortcuts import redirect
from requests import request
from users.models import *
from django.test import Client
from rest_framework.test import APITestCase, DjangoClient
from unittest.mock import patch, MagicMock

from django.contrib.auth.hashers import make_password, check_password

from django.conf   import settings
from django.test   import TestCase, Client

class UserSigninTest(APITestCase):
    def setUp(self):
        User.objects.create(
            id = 1,
            email = 'test@test.com',
            password = make_password('1q2w3e4r5t!'),
            refreshtoken = "token_refresh",
            username = "test"
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_user_signin_success(self):
        
        user = User.objects.get(id =1)
        print(user)
        data = {
            'email' : user.email,
            'password' : '1q2w3e4r5t!'
        }

        if user.email == data['email'] and check_password(data['password'],user.password):
            response = 200
        else:
            response = False
        
        self.assertEqual(response,200)
        
    def test_user_signin_success(self):
        
        user = User.objects.get(id =1)
        print(user)
        data = {
            'email' : user.email,
            'password' : '1q2w3e4r5t'
        }

        if user.email == data['email'] and check_password(data['password'],user.password):
            response = 200
        else:
            response = 400
        
        self.assertEqual(response,400)