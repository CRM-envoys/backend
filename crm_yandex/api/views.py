from rest_framework import viewsets

from .serializers import ActivitySerializer, AmbassadorSerializer
from ambassadors.models import Activity, Ambassador


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.prefetch_related(
        "ambassador_activities__activity"
    ).all()
    serializer_class = AmbassadorSerializer
