from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from httpservice.filters import ShopFilter
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
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ShopFilter

    def perform_create(self, serializer):
        serializer.save(city_id=self.request.data['city_id'], street_id=self.request.data['street_id'])
