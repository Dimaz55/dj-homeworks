from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, DjangoFilterBackend

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    status = DjangoFilterBackend()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
