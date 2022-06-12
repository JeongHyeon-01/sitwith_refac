import json
from django.test import TestCase,Client
from users.models import User
client = Client()
class CategoryTest(TestCase):

    def test_color_add(self):
        data={
            'name' : 'test'
        }
        User.objects.create_superuser(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123',
        )
        self.client.login(email = 'test@test.com', password='123123')
        response = self.client.post('/products/color/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_color_keyerror(self):
        data={
            'name' :''
        }
        User.objects.create_superuser(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123',
        )
        self.client.login(email = 'test@test.com', password='123123')        
        response = self.client.post('/products/color/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,400)