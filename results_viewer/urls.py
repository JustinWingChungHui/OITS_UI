from django.urls import path
from results_viewer.views import get_results_values

urlpatterns = [
    path('results/<int:id>/values/', get_results_values),
]