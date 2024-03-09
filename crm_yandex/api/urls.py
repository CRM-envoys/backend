from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, AmbassadorViewSet, ContentViewSet


router = DefaultRouter()
router.register("activities", ActivityViewSet, basename="activities")
router.register("ambassadors", AmbassadorViewSet, basename="ambassadors")
router.register(r'content', ContentViewSet, basename='content')

app_name = "api"

urlpatterns = [
    path("v1/", include(router.urls)),
]
