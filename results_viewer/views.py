from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from results_viewer.models import TrajectoryResult


def get_results_values(request, id):
    result = get_object_or_404(TrajectoryResult, oits_params_id=id)
    return HttpResponse(result.values, content_type='text/plain')


