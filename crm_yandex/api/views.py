from django.shortcuts import render, HttpResponse
from djoser.views import UserViewSet
from rest_framework.viewsets  import ModelViewSet

from ambassadors.models import Ambassador
from api.serializers import AmbassadorSerializer


def index(request):
    return HttpResponse("Привет Амбассадорам!")


class AmbassadorViewSet(ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
