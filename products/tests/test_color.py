import json
from django.test import TestCase,Client

client = Client()
class CategoryTest(TestCase):

    def test_color_add(self):
        data={
            'name' : 'test'
        }
        response = client.post('/products/color/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_color_keyerror(self):
        data={
            'name' :''
        }
        response = client.post('/products/color/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,400)