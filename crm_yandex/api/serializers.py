from rest_framework import serializers

from ambassadors.models import Ambassador, Course, Status


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = "__all__"


class AmbassadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ambassador
        fields = "__all__"
