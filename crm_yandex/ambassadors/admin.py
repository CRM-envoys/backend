from django.contrib import admin

from ambassadors.models import Course, Status

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
