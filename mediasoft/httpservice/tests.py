import json

from rest_framework.test import APITestCase

from django.urls import reverse

from httpservice.models import City


class CityViewSetTestCase(APITestCase):
    url = reverse("city-list")

    def test_create_city(self):
        response = self.client.post(self.url, {"name": "Ulyanovsk"})
        self.assertEqual(201, response.status_code)

    def test_cities(self):
        City.objects.create(name="Ulyanovsk")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == City.objects.count())
