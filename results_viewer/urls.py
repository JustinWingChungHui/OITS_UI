from django.urls import path
from results_viewer.views import get_results_csv

urlpatterns = [
    path('results/<str:uid>/csv/', get_results_csv),
]