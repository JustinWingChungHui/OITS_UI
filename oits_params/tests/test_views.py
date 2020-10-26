from django.test import TestCase, Client
from oits_params.models import OitsParams
from oits_params.default_data import esa_mission
import json

class ViewsTestCase(TestCase):

    def setUp(self):

        self.params = OitsParams.objects.create(parameters='{test: "test"}', description='mydesc')

    def test_list_view_loads(self):
        client = Client()
        response = client.get('/runs/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'mydesc' in response.content)

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


    def test_mission_api(self):

        client = Client()
        data = json.loads(esa_mission)
        data['description'] = 'test data'
        response = client.post('/missions/', json.dumps(data), content_type="application/json")

        self.assertEqual(response.status_code, 200)

        response = client.get('/missions/')
        data = json.loads(response.content)

        self.assertTrue(len(data) > 0)


    def test_mission_single_api(self):

        model = OitsParams()
        model.description = 'description'
        model.parameters = esa_mission
        model.save()

        client = Client()
        response = client.get('/missions/{0}/'.format(model.id))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        self.assertEqual(model.id, data['id'])


    def test_mission_single_api(self):

        model = OitsParams()
        model.description = 'description'
        model.parameters = esa_mission
        model.save()

        client = Client()
        response = client.delete('/missions/{0}/'.format(model.id))
        self.assertEqual(response.status_code, 200)

        count = OitsParams.objects.filter(id=model.id).count()

        self.assertEqual(0, count)

