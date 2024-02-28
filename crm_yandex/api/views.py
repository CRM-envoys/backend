from django.shortcuts import render, HttpResponse
from djoser.views import UserViewSet
from rest_framework.viewsets  import ModelViewSet

from backend.crm_yandex.ambassadors.models_old import Ambassador, Course, Status
from api.serializers import AmbassadorSerializer, CourseSerializer, StatusSerializer


def index(request):
    return HttpResponse("Привет Амбассадорам!")


class CustomUserViewSet(UserViewSet):
    pass


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class AmbassadorViewSet(ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
