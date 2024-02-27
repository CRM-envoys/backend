from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from api.views import index, CourseViewSet, StatusViewSet


router = routers.DefaultRouter()
router.register("course", CourseViewSet)
router.register("status", StatusViewSet)

urlpatterns = [
    path("index", index),
    path("", include(router.urls))
]
