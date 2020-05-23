from django.core.exceptions import ValidationError
from django.test import TestCase
from oits_params.default_data import esa_mission, example_list
from oits_params.models import OitsParams
import json

class OitsParamsTestCase(TestCase):
    '''
    Defines tests for OitsParams
    '''

    def test_clean_validates_all_examples(self):

        model = OitsParams()

        for example in example_list:
            model.parameters = example['value']

            try:
                model.clean()
            except:
                self.fail("clean() raised ExceptionType unexpectedly! for {0}".format(example['name']))


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

    def test_clean_Nbody_Too_Large(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('Nbody', 10)
        self.assertRaises(ValidationError, model.clean)


    def test_clean_ID_Invalid_Type(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('ID', '1')
        self.assertRaises(ValidationError, model.clean)

    def test_clean_ID_Invalid_Length(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('ID', ['1'])
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

    def test_clean_thetaIP_invalid_length(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('thetaIP', [1.0, 2.0])
        self.assertRaises(ValidationError, model.clean)


    def test_clean_t0_invalid_length(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('t0', [1.0, 2.0])
        self.assertRaises(ValidationError, model.clean)


    def test_clean_ID_Contains_Invalid_Names(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('ID', ["3","INTERMEDIATE POINT","3","5","INTERMEDIATE POINT","Not a correct name"])
        self.assertRaises(ValidationError, model.clean)


    def test_clean_ID_Contains_Consecutive_Intermediate_Points(self):
        model = OitsParams()
        model.parameters = self.get_altered_params('ID', ["3","INTERMEDIATE POINT","INTERMEDIATE POINT","5","3","9"])
        self.assertRaises(ValidationError, model.clean)



