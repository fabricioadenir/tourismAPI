from django.conf.urls import url, include
from .views import (EscaparateViewSet, CategoryViewSet,
                    CityViewSet, CountryViewSet, HotelViewSet, RouteViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("vitrines", EscaparateViewSet, basename="windows")
router.register("categorias", CategoryViewSet, basename="categories")
router.register("cidades", CityViewSet, basename="cities")
router.register("paises", CountryViewSet, basename="countries")
router.register("hoteis", HotelViewSet, basename="hotels")
router.register("rotas", RouteViewSet, basename="routes")

urlpatterns = [
    url('', include(router.urls))
]
