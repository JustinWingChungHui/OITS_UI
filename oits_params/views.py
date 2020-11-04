from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.decorators.http import require_http_methods


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


@require_http_methods(["GET"])
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


@require_http_methods(["GET", "POST"])
def mission_api(request):
    '''
    Api calls to create a new mission
    '''

    if request.method=='POST':
        content = request.body.decode("utf-8")

        received_json_data = json.loads(content)

        model = OitsParams()
        model.description = received_json_data['description']
        model.parameters = content
        model.clean()
        model.save()

        return JsonResponse(model_to_dict(model))

    else:
        models = list(OitsParams.objects.all())
        json_result = serializers.serialize('json', models,fields=('id','uid', 'description', 'status', 'created_at'))
        return HttpResponse(json_result, content_type='application/json')


@require_http_methods(["GET", "DELETE"])
def mission_single_api(request, pk):
    '''
    Api calls to create a new mission
    '''
    model = OitsParams.objects.get(pk=pk)

    if request.method=='GET':

        return JsonResponse(model_to_dict(model))

    else:
        model.delete()
        return HttpResponse("OK")


