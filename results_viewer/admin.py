from django.contrib import admin
from results_viewer.models import TrajectoryResult


class TrajectoryResultAdmin(admin.ModelAdmin):
    list_display  = ('oits_params', 'created_at')

admin.site.register(TrajectoryResult, TrajectoryResultAdmin)
