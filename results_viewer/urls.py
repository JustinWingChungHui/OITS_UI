from django.urls import path
from results_viewer.views import get_paths, get_results_values

urlpatterns = [
    path('results/<str:uid>/paths/', get_paths),
    path('results/<int:id>/values/', get_results_values),
]