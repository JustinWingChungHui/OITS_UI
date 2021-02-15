import json
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny #IsAuthenticated

from mission_api.serializers import OitsParamsSerializer, OitsParamsListSerializer
from oits_params.models import OitsParams


# ViewSets define the view behavior for Django REST
class MissionViewSet(viewsets.ModelViewSet):

    permission_classes = (AllowAny,)

    def list(self, request):
        '''
        Lists all missions
        '''

        queryset = OitsParams.objects.all(
                        ).order_by('-created_at')

        serializer = OitsParamsListSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        '''
        Gets a single mission record
        '''

        queryset = OitsParams.objects.all()
        mission = get_object_or_404(queryset, pk=pk)
        serializer = OitsParamsSerializer(mission)
        return Response(serializer.data)



    def destroy(self, request, pk=None):
        '''
        Deletes a mission record
        '''

        queryset = OitsParams.objects.all()

        mission = get_object_or_404(queryset, pk=pk)
        if mission.readonly:
            raise ValidationError('Mission is readonly')
        else:
            mission.delete()
            return Response('OK')



    def create(self, request):
        '''
        Creates a new mission record
        '''

        try:
            received_json_data = json.loads(request.body)

            model = OitsParams()
            model.description = received_json_data['description']
            model.parameters = request.body.decode('utf-8')
            model.clean()
            model.save()


            serializer = OitsParamsSerializer(model)
            return Response(serializer.data)

        except Exception as e:
            raise ValidationError(str(e))




    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        '''
        Cancels a mission
        '''

        queryset = OitsParams.objects.all()
        mission = get_object_or_404(queryset, pk=pk)

        if mission.readonly:
            raise ValidationError('Mission is readonly')

        if mission.status in [OitsParams.NEW, OitsParams.PROCESSING]:
            mission.status = OitsParams.CANCELLING
            mission.save()

        serializer = OitsParamsSerializer(mission)

        return Response(serializer.data)







