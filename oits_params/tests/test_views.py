from django.test import TestCase, Client
from oits_params.models import OitsParams
import json

class ViewsTestCase(TestCase):

    def setUp(self):

        self.params = OitsParams.objects.create(parameters='{test: "test"}')

    def test_list_view_loads(self):
        client = Client()
        response = client.get('/runs/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(self.params.uid).encode() in response.content)

    def test_create_view_loads(self):
        client = Client()
        response = client.get('/runs/add/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_loads(self):
        client = Client()
        response = client.get('/runs/{0}/'.format(self.params.id))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'{test: &quot;test&quot;}' in response.content)


    def test_get_status_loads(self):
        client = Client()
        response = client.get('/runs/{0}/status/'.format(self.params.id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual('N', data['status'])