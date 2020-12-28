from django.test import TestCase
from rest_framework.test import APIClient
from oits_params.models import OitsParams
from oits_params.default_data import esa_mission
import json

class ViewsTestCase(TestCase):

    def setUp(self):
        self.params = OitsParams.objects.create(parameters='{test: "test"}', description='mydesc')


    def test_mission_api_list(self):

        model = OitsParams()
        model.description = 'description'
        model.parameters = esa_mission
        model.save()

        client = APIClient()
        response = client.get('/api/mission/', format='json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        self.assertTrue(len(data) > 0)


    def test_mission_api_create_validation_error(self):

        client = APIClient()
        data = json.loads(esa_mission)
        data['description'] = 'test data'
        data['Nbody'] = 4
        response = client.post('/api/mission/', data, format='json')

        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)



    def test_mission_api_create(self):

        client = APIClient()
        data = json.loads(esa_mission)
        data['description'] = 'test data'
        response = client.post('/api/mission/', data, format='json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        new_model = OitsParams.objects.get(pk=data['id'])

        self.assertIsNotNone(new_model)


    def test_mission_api_retrieve(self):

        model = OitsParams()
        model.description = 'description'
        model.parameters = esa_mission
        model.save()

        client = APIClient()
        url = '/api/mission/{0}/'.format(model.id)
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)

        self.assertEqual(model.id, data['id'])


    def test_mission_api_delete(self):

        model = OitsParams()
        model.description = 'description'
        model.parameters = esa_mission
        model.save()

        client = APIClient()
        response = client.delete('/api/mission/{0}/'.format(model.id), format='json')
        self.assertEqual(response.status_code, 200)

        count = OitsParams.objects.filter(id=model.id).count()

        self.assertEqual(0, count)