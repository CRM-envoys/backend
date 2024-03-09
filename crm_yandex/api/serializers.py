from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from rest_framework import serializers

from ambassadors.constants import (AMBASSADOR_STATUS_CHOICES,
                                   CLOTHING_SIZE_CHOICES, COURSE_CHOICES,
                                   SEX_CHOICES)
from ambassadors.models import (Activity, Ambassador, AmbassadorActivity,
                                Content, Venue)


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ("id", "name")


class AmbassadorSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(required=False, many=True)
    sex = serializers.ChoiceField(choices=SEX_CHOICES)
    course = serializers.ChoiceField(choices=COURSE_CHOICES)
    clothing_size = serializers.ChoiceField(choices=CLOTHING_SIZE_CHOICES)
    status = serializers.ChoiceField(
        choices=AMBASSADOR_STATUS_CHOICES,
        default="active"
    )

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

    def to_internal_value(self, data):
        course = data.pop("course")
        for course_choice in COURSE_CHOICES:
            if course == course_choice[1]:
                course = course_choice[0]
                break
        else:
            raise ValidationError(
                {"course": "Нет в списке курсов"}
            )

        data["course"] = course
        return super().to_internal_value(data)

    def create(self, validated_data):
        if 'activities' in validated_data:
            activities = validated_data.pop("activities")
        else:
            activities = []
        ambassador = Ambassador.objects.create(**validated_data)
        if activities:
            for activity in activities:
                current_activity = Activity.objects.get(**activity)
                AmbassadorActivity.objects.create(
                    ambassador=ambassador,
                    activity=current_activity
                )
        return ambassador


class ContentSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = [
            'id',
            'ambassador',
            'link',
            'file',
            'venue',
            'created',
            'updated',
            'guide_followed',
        ]

    def to_internal_value(self, data):
        if 'ambassadors' not in data:
            ambassador = Ambassador.objects.filter(
                fio=data.get('fio'), telegram=data.get('telegram')
            )
            if ambassador.exists():
                data['ambassador'] = Ambassador.objects.filter(
                    fio=data.pop('fio'), telegram=data.pop('telegram')
                )[0]
                return data
            raise serializers.ValidationError(
                {'ambassador': 'Амбассадор с указанными даннми не найден'}
            )
        return super().to_internal_value(data)

    def validate(self, attrs):
        venue = Venue.objects.get_or_create(
            name=urlparse(attrs.get('link', '')).netloc
        )
        attrs['venue'] = venue[0]
        return super().validate(attrs)

    def get_image(self, obj):
        if obj.file:
            return obj.file.url
        return None