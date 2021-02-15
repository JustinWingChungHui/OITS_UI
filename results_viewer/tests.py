from django.conf import settings
from django.test import TestCase, Client, override_settings
from oits_params.default_data import esa_mission
from oits_params.models import OitsParams
from results_viewer.models import TrajectoryResult
import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_file_path = os.path.join(BASE_DIR, 'results_viewer/test_files')
test_guid = '4b8e997c-0ce5-45d8-87fb-0f314505754a'

@override_settings(MEDIA_ROOT=test_file_path)
class ViewsTestCase(TestCase):

    def setUp(self):
        pass


    def test_get_results_values(self):
        oitsParams = OitsParams()
        oitsParams.uid = test_guid
        oitsParams.parameters = esa_mission
        oitsParams.save()

        result = TrajectoryResult(oits_params = oitsParams)
        result.values = 'PROBE\n7.0739567e+08,-0.32819958,-0.95950251,4.9871959e-05'
        result.save()


        client = Client()
        response = client.get('/results/{0}/values/'.format(oitsParams.id))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'PROBE\n7.0739567e+08,-0.32819958,-0.95950251,4.9871959e-05' in response.content)


@override_settings(MEDIA_ROOT=settings.MEDIA_ROOT_TEST)
class ModelsTestCast(TestCase):

    def setUp(self):

        source = os.path.join(test_file_path, test_guid + '.zip')

        self.destination_file_path = os.path.join(settings.MEDIA_ROOT, test_guid + '.zip')
        shutil.copy2(source, self.destination_file_path)

    def test_populate_values_from_output_file(self):
        oitsParams = OitsParams()
        oitsParams.uid = test_guid
        oitsParams.parameters = esa_mission
        oitsParams.save()

        result = TrajectoryResult(oits_params = oitsParams)
        result.populate_values_from_output_file()

        self.assertTrue('PROBE\n7.0739567e+08,-0.32819958,-0.95950251,4.9871959e-05' in result.values)
        #self.assertFalse(os.path.isfile(self.destination_file_path))

        client = Client()
        response = client.get('/results/{0}/values/'.format(oitsParams.id))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'PROBE\n7.0739567e+08,-0.32819958,-0.95950251,4.9871959e-05' in response.content)
