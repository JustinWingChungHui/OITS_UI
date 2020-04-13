from django.core.exceptions import ValidationError
from django.test import TestCase
from oits_params.default_data import esa_mission
from oits_params.models import OitsParams
import json

class OitsParamsTestCase(TestCase):
    '''
    Defines tests for OitsParams
    '''

    def test_clean_validates(self):

        model = OitsParams()
        model.parameters = esa_mission

        try:
            model.clean()
        except:
            self.fail("clean() raised ExceptionType unexpectedly!")


    def get_altered_params(self, key, value):
        params = json.loads(esa_mission)
        params[key] = value

        return json.dumps(params)

    def test_clean_trajectory_optimization(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('trajectory_optimization', 'blah')
        self.assertRaises(ValidationError, model.clean)

    def test_clean_Nbody(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('Nbody', 0)
        self.assertRaises(ValidationError, model.clean)

    def test_clean_ID(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('ID', 'blah')
        self.assertRaises(ValidationError, model.clean)

    def test_clean_NIP(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('NIP', -1)
        self.assertRaises(ValidationError, model.clean)

    def test_clean_rip(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('rIP', -1)
        self.assertRaises(ValidationError, model.clean)

    def test_clean_thilb(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('thilb', ["not a float"])
        self.assertRaises(ValidationError, model.clean)

    def test_clean_t01(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('t01', "21/01/2018")
        self.assertRaises(ValidationError, model.clean)