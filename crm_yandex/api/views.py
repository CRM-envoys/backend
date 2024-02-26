from django.shortcuts import render, HttpResponse
from djoser.views import UserViewSet
from rest_framework.viewsets  import ModelViewSet

from ambassadors.models import Course
from api.serializers import CourseSerializer

def index(request):
    return HttpResponse("Привет Амбассадорам!")


class CustomUserViewSet(UserViewSet):
    pass


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

