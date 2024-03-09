from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from ambassadors.models import Activity, Ambassador, Content
from .serializers import ActivitySerializer, AmbassadorSerializer, ContentSerializer
from .filters import AmbassadorFilter


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.prefetch_related(
        "ambassador_activities__activity"
    ).all()
    serializer_class = AmbassadorSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_class = AmbassadorFilter
    search_fields = ("fio", "telegram")
    ordering_fields = ("fio", "status", "-date_registration")



class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ambassador', 'venue']
