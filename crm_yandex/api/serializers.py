from django.core.exceptions import ValidationError
from rest_framework import serializers

from ambassadors.constants import (AMBASSADOR_STATUS_CHOICES,
                                   CLOTHING_SIZE_CHOICES, COURSE_CHOICES,
                                   SEX_CHOICES)
from ambassadors.models import Activity, Ambassador, AmbassadorActivity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ("id", "name")


class AmbassadorSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)
    sex = serializers.ChoiceField(choices=SEX_CHOICES)
    course = serializers.ChoiceField(choices=COURSE_CHOICES)
    clothing_size = serializers.ChoiceField(choices=CLOTHING_SIZE_CHOICES)
    status = serializers.ChoiceField(choices=AMBASSADOR_STATUS_CHOICES)

    class Meta:
        model = Ambassador
        fields = (
            "id", "fio", "sex",
            "course", "country", "city",
            "address", "postal_code", "email",
            "phone_number", "telegram", "education",
            "job", "goal", "activities",
            "blog_link", "clothing_size", "foot_size",
            "comment", "promocode", "status",
            "guide_one", "guide_two", "onboarding",
            "viewed"
        )

    def create(self, validated_data):
        activities = validated_data.pop("activities")
        ambassador = Ambassador.objects.create(**validated_data)

        for activity in activities:
            current_activity = Activity.objects.get(**activity)
            AmbassadorActivity.objects.create(
                ambassador=ambassador,
                activity=current_activity
            )

        return ambassador

    # def to_internal_value(self, data):
    #     if isinstance(data, dict):
    #         data = data.get("params")

    #     course = data.pop("course")

    #     for course_choice in COURSE_CHOICES:
    #         if course == course_choice:
    #             course = course_choice[0]
    #             break
    #     else:
    #         raise ValidationError(
    #             {"course": "Нет в списке курсов"}
    #         )

    #     data["course"] = course
    #     return super().to_internal_value(data)
