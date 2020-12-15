from django.conf.urls import url, include
from .views import EscaparateViewSet, CategoryViewSet, CityViewSet, CountryViewSet, HotelViewSet, RouteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("vitrine", EscaparateViewSet, basename="vitrine")
router.register("categorias", CategoryViewSet, basename="categorias")
router.register("cidades", CityViewSet, basename="cidades")
router.register("paises", CountryViewSet, basename="paises")
router.register("hoteis", HotelViewSet, basename="hoteis")
router.register("rotas", RouteViewSet, basename="rotas")

urlpatterns = [
    url('', include(router.urls))
]
