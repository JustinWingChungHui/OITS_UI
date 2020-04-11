from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import OitsParams
from oits_params.default_data import esa_mission

class OitsParamsListView(ListView):
    model = OitsParams
    ordering = ['-created_at']
    context_object_name = 'oitsParams'

class OitsParamsCreateView(CreateView):
    model = OitsParams
    fields = ('parameters',)
    success_url = reverse_lazy('params_list')

    def get_initial(self, *args, **kwargs):
        initial = super(OitsParamsCreateView, self).get_initial(**kwargs)

        initial['parameters'] = esa_mission
        return initial