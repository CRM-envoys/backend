from django.contrib import admin

from ambassadors.models import Ambassador


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    pass
