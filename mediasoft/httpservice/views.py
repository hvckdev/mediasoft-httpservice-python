from datetime import datetime

from django.db.models import F
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from httpservice.models import City, Street, Shop
from httpservice.serializers import CitySerializer, StreetSerializer, ShopSerializer


# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopListCreateAPIView(ListCreateAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        now = datetime.now().time()
        street = self.request.query_params.get('street')
        city = self.request.query_params.get('city')
        opn = self.request.query_params.get('open')

        filters = {}

        if street:
            filters['street__name'] = street

        if city:
            filters['city__name'] = city

        if opn:
            if int(opn) == 1:
                filters['opens_at__lte'] = F('closes_at')
                filters['opens_at__lte'] = now
                filters['closes_at__gte'] = now
            else:
                filters['opens_at__gte'] = F('closes_at')
                filters['opens_at__gte'] = now
                filters['closes_at__lte'] = now

        return Shop.objects.filter(**filters)

    def perform_create(self, serializer):
        serializer.save(city_id=self.request.data['city_id'], street_id=self.request.data['street_id'])
