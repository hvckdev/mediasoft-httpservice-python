from datetime import datetime

import django_filters as filters
from django.db.models import F, Q

from httpservice.models import Shop


class ShopFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city__name')
    street = filters.CharFilter(field_name='street__name')
    open = filters.NumberFilter(method='is_open_filter')

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def is_open_filter(self, queryset, name, value):
        now = datetime.now().time()

        if int(value) == 0:
            return queryset.filter(Q(opens_at__gte=now) | Q(closes_at__lte=now), opens_at__lt=F('closes_at'))
        else:
            return queryset.filter(opens_at__lte=now, closes_at__gte=now)
