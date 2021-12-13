from django.urls import path, include
from rest_framework_extensions.routers import ExtendedSimpleRouter

from httpservice.apps.api.views import CityViewSet, StreetViewSet, ShopListCreateAPIView

router = ExtendedSimpleRouter()
(
    router.register(r'city', CityViewSet, basename='city')
          .register(r'street', StreetViewSet, parents_query_lookups=['city'], basename='street')
)

urlpatterns = [
    path('', include(router.urls)),
    path('shop/', ShopListCreateAPIView.as_view())
]
