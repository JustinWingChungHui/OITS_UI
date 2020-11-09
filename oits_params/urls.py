from django.urls import path

from oits_params.views import OitsParamsCreateView, OitsParamsListView, OitsParamsDetailView, get_status


urlpatterns = [
    path('runs/', OitsParamsListView.as_view(), name='params_list'),
    path('runs/add/', OitsParamsCreateView.as_view(), name='params_add'),
    path('runs/<int:pk>/', OitsParamsDetailView.as_view(), name='params_detail'),
    path('runs/<int:pk>/status/', get_status),
]