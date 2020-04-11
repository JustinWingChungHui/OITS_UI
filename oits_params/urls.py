from django.urls import path

from oits_params.views import OitsParamsCreateView, OitsParamsListView


urlpatterns = [
    path('', OitsParamsListView.as_view(), name='params_list'),
    path('add/', OitsParamsCreateView.as_view(), name='params_add'),
]