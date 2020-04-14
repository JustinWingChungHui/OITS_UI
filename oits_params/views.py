from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from oits_params.default_data import esa_mission, example_list
from oits_params.models import OitsParams
import json

class OitsParamsListView(ListView):
    model = OitsParams
    ordering = ['-created_at']
    context_object_name = 'oitsParams'


class OitsParamsCreateView(CreateView):
    model = OitsParams
    fields = ('description','parameters',)
    success_url = reverse_lazy('params_list')

    def get_initial(self, *args, **kwargs):
        initial = super(OitsParamsCreateView, self).get_initial(**kwargs)

        initial['parameters'] = esa_mission
        initial['description'] = 'ESA Mission'

        return initial

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a examples
        context['examples'] = example_list
        return context


class OitsParamsDetailView(DetailView):
    model = OitsParams
    context_object_name = 'oitsParams'



def get_status(request, pk):
    try:
        p = OitsParams.objects.get(pk=pk)
    except:
        raise HttpResponseNotFound("id does not exist")


    data = {
       'id': p.id,
       'status': p.status,
       'status_description': p.get_status_display()
    }

    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')