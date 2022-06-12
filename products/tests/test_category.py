import json
from django.test import TestCase,Client
from users.models import User

client = Client()

class CategoryTest(TestCase):

    def test_category_add(self):

        User.objects.create_superuser(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123',
        )
        
        data={
            'title' : 'test'
        }
        self.client.login(email = 'test@test.com', password='123123')
        response = self.client.post('/products/category/',json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_category_get(self):
        User.objects.create_superuser(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123',
        )
        response = client.get('/products/category/')
        self.assertEqual(response.status_code, 200)


    def test_category_keyerror(self):
        User.objects.create_superuser(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123',
        )
        data={
            'title' :''
        }
        self.client.login(email = 'test@test.com', password='123123')
        response = self.client.post('/products/category/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_category_permission_error(self):
        User.objects.create(
            nickname = 'test',
            email = 'test@test.com',
            password = '123123',
        )
        data={
            'title' :''
        }
        self.client.login(email = 'test@test.com', password='123123')
        response = self.client.post('/products/category/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,403)
