from rest_framework import routers
from mission_api.views import MissionViewSet

# Add in our routing for the mission api

router = routers.DefaultRouter()
router.register(r'api/mission', MissionViewSet, basename='mission')

urlpatterns = router.urls