from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import ActivitySerializer, AmbassadorSerializer, ContentSerializer
from ambassadors.models import Activity, Ambassador, Content


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.prefetch_related(
        "ambassador_activities__activity"
    ).all()
    serializer_class = AmbassadorSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ambassador', 'venue']
