from django.urls import path

from oits_params.views import OitsParamsCreateView


urlpatterns = [
    path('add/', OitsParamsCreateView.as_view(), name='params_add'),
]