import django_filters

from ambassadors.models import Ambassador


class AmbassadorFilter(django_filters.FilterSet):
    telegram_exists = django_filters.BooleanFilter(
        field_name="telegram",
        method="filter_telegram_exists"
    )
    promocode_exists = django_filters.BooleanFilter(
        field_name="promocode",
        method="filter_promocode_exists"
    )

    class Meta:
        model = Ambassador
        fields = (
            "status", "telegram_exists", "promocode_exists",
            "onboarding", "guide_one", 'guide_one'
        )

    def filter_telegram_exists(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(telegram__isnull=False)
        return queryset.filter(telegram__isnull=True)

    def filter_promocode_exists(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(promocode__isnull=False)
        return queryset.filter(promocode__isnull=True)
