from django.contrib import admin

from ambassadors.models import (Action, Address, Ambassador, AmbassadorAction,
                                AmbassadorProfileStatus, AmbassadorStatus,
                                ClothingSize, Content, Course, FootSize, Goal,
                                GuideStatus, MerchOnShipping, MerchShipment,
                                OnboardingStatus, Venue)


admin.site.register(Action)
admin.site.register(Address)
admin.site.register(Ambassador)
admin.site.register(AmbassadorAction)
admin.site.register(AmbassadorProfileStatus)
admin.site.register(AmbassadorStatus)
admin.site.register(ClothingSize)
admin.site.register(Content)
admin.site.register(Course)
admin.site.register(FootSize)
admin.site.register(Goal)
admin.site.register(GuideStatus)
admin.site.register(MerchOnShipping)
admin.site.register(MerchShipment)
admin.site.register(OnboardingStatus)
admin.site.register(Venue)
