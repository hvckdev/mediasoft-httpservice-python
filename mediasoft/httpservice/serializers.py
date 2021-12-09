from rest_framework import serializers
from httpservice.models import City, Street, Shop


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name']


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    street = serializers.SlugRelatedField(read_only=True, slug_field='name')
    city = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'opens_at', 'closes_at']
