# Create your views here.
from django.views.generic import CreateView
from .models import OitsParams

class OitsParamsCreateView(CreateView):
    model = OitsParams
    fields = ('parameters')