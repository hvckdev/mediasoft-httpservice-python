from rest_framework import serializers
from httpservice.api.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = ['id', 'name', 'city']


class ShopSerializer(serializers.ModelSerializer):
    street = serializers.SlugRelatedField(read_only=True, slug_field='name')
    city = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'opens_at', 'closes_at']
