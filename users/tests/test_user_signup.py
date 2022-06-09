import json
from django.test import TestCase, Client

client = Client()

class UserSignUpTest(TestCase):

    def test_users_signup_post_success_test(self):
        data = {
            'email' : 'test@test.com',
            'password' : 'password1!',
            'password2' : 'password1!',
            'nickname' : 'test'
        }
        response = client.post('/users/signup/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_users_signup_post_validateEmail_test(self):
        data = {
            'email' : 'test',
            'password' : 'password1!',
            'password2' : 'password1!',
            'nickname' : 'test'
        }
        response = client.post('/users/signup/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_users_signup_post_wrong_password2_test(self):
        data = {
            'email' : 'test@test.com',
            'password' : 'password1!',
            'password2' : 'password1',
            'nickname' : 'test'
        }
        response = client.post('/users/signup/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_users_signup_post_null_nickname_test(self):
        data = {
            'email' : 'test@test.com',
            'password' : 'password1!',
            'password2' : 'password1',
            'nickname' : ''
        }
        response = client.post('/users/signup/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)