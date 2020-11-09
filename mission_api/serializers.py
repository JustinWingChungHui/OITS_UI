from oits_params.models import OitsParams
from rest_framework import serializers

# Serializers define the API representation.
class OitsParamsSerializer(serializers.ModelSerializer):
    '''
    Defines fields to be serialised for a mission
    '''
    class Meta:
        model = OitsParams
        fields = ('id','uid', 'description', 'status', 'parameters', 'created_at')


class OitsParamsListSerializer(serializers.ModelSerializer):
    '''
    We only want to send limited data back when listing missions
    '''

    class Meta:
        model = OitsParams
        fields = ('id','uid', 'description', 'status', 'created_at')