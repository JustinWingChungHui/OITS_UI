from django.contrib import admin
from oits_params.models import OitsParams


class OitsParamsAdmin(admin.ModelAdmin):
    list_display  = ('id', 'uid','description','status', 'created_at', 'readonly')

admin.site.register(OitsParams, OitsParamsAdmin)
