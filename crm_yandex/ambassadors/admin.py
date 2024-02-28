from django.contrib import admin

from backend.crm_yandex.ambassadors.models_old import Ambassador, Course, Status, Recipe

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
