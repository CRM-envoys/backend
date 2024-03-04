from django.contrib import admin

from ambassadors.models import (Activity, Ambassador, AmbassadorActivity,
                                AmbassadorPreference, Content, MerchOnShipping,
                                MerchShipment, Preference, Venue)


admin.site.register(Activity)
admin.site.register(Ambassador)
admin.site.register(AmbassadorActivity)
admin.site.register(AmbassadorPreference)
admin.site.register(Content)
admin.site.register(MerchOnShipping)
admin.site.register(MerchShipment)
admin.site.register(Preference)
admin.site.register(Venue)
