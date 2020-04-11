from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from oits_params.models import OitsParams


class OitsParamsForm(forms.ModelForm):
    class Meta:
        model = OitsParams
        fields = ('parameters',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Start Processing'))

