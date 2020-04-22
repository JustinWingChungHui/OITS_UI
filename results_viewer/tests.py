from django.test import TestCase, Client, override_settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_root = os.path.join(BASE_DIR, 'results_viewer/test_files')


@override_settings(MEDIA_ROOT = media_root)
class ViewsTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_results_csv(self):

        client = Client()
        response = client.get('/results/8dc3920c-89b1-447c-adba-46b786b16cf5/csv/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'MAIN\n7.0744693e+08,-0.31869156,-0.96279682,4.9987514e-05' in response.content)