from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from api.views import index, CustomUserViewSet, CourseViewSet


router = routers.DefaultRouter()
router.register("users", CustomUserViewSet)
router.register("course", CourseViewSet)

urlpatterns = [
    path("index", index),
    path("auth", include ("djoser.urls.authtoken")),
    path("", include(router.urls))
]
