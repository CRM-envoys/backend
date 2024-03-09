from django.contrib import admin

from .models import (Activity, Ambassador, AmbassadorActivity, Content, Merch,
                     MerchOnShipping, MerchShipment, Notification, Venue)


class AmbassadorActivityInline(admin.TabularInline):
    model = AmbassadorActivity
    extra = 1


class AmbassadorContentInline(admin.TabularInline):
    model = Content
    extra = 1


class MerchOnShippingInline(admin.TabularInline):
    model = MerchOnShipping
    extra = 1


class ActivityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    empty_value_display = "-пусто"


class MerchAdmin(admin.ModelAdmin):
    list_display = ("merch_type", "cost")
    empty_value_display = "-пусто"


class VenueAdmin(admin.ModelAdmin):
    list_display = ("name",)
    empty_value_display = "-пусто"


class MerchShipmentAdmin(admin.ModelAdmin):
    list_display = ("curator", "ambassador", "status", "date")
    list_filter = ("status", "ambassador", "curator")
    inlines = (MerchOnShippingInline,)
    empty_value_display = "-пусто"


class ContentAdmin(admin.ModelAdmin):
    list_display = ("ambassador", "link", "created", "guide_followed")
    list_filter = ("ambassador", "venue", "guide_followed")
    empty_value_display = "-пусто"


class AmbassadorAdmin(admin.ModelAdmin):
    list_display = ("fio", "telegram", "promocode", "status")
    list_filter = ("fio", "status")
    inlines = (AmbassadorActivityInline, AmbassadorContentInline)
    empty_value_display = "-пусто"


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("text", "created")
    list_filter = ("created",)
    empty_value_display = "-пусто"


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Ambassador, AmbassadorAdmin)
admin.site.register(AmbassadorActivity)
admin.site.register(Content, ContentAdmin)
admin.site.register(MerchOnShipping)
admin.site.register(MerchShipment, MerchShipmentAdmin)
admin.site.register(Merch, MerchAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Notification, NotificationAdmin)
