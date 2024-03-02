from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from api.views import index, AmbassadorViewSet


router = routers.DefaultRouter()
router.register("ambassador", AmbassadorViewSet)

urlpatterns = [
    path("index", index),
    path("", include(router.urls))
]
