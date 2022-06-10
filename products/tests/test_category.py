import json
from django.test import TestCase,Client

client = Client()
class CategoryTest(TestCase):

    def test_category_add(self):
        data={
            'title' : 'test'
        }
        response = client.post('/products/category/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_category_get(self):
        response = client.get('/products/category/')
        self.assertEqual(response.status_code, 200)


    def test_category_keyerror(self):
        data={
            'title' :''
        }
        response = client.post('/products/category/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,400)