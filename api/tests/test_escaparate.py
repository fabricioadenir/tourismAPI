from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from api.models import Category, City, Country, Hotel, Route, Escaparate
from api.views import EscaparateViewSet


class EscaparateViewSetTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """

    def setUp(self):
        Category.objects.create(name="Hospedagem de Verão")
        City.objects.create(
            name="Florianópolis",
            state="SC"
        )

        City.objects.create(
            name="Pocos de Caldas",
            state="MG"
        )

        Country.objects.create(
            name="Brasil"
        )

        category = Category.objects.get(id=1)
        city_floripa = City.objects.get(id=1)
        city_caldas = City.objects.get(id=1)
        country = Country.objects.get(id=1)

        Hotel.objects.create(
            hotel_name="Alameda Alegra",
            image="http://tourism.com/images/alameda-alegra.jpg",
            city=city_floripa,
            country=country,
            category=category,
            price=3000.
        )

        Hotel.objects.create(
            hotel_name="Ibis Poços de Caldas",
            image="http://tourism.com/images/ibis-pocos-de-caldas.jpg",
            city=city_caldas,
            country=country,
            category=category,
            price=2500
        )

        hoteles = [
            Hotel.objects.get(id=1),
            Hotel.objects.get(id=2)
        ]

        Route.objects.create(route="/")
        Route.objects.create(route="/destinos")

        routes = [
            Route.objects.get(id=1),
            Route.objects.get(id=2)
        ]

        self.escaparate = Escaparate.objects.create(
            title="Hotéis na região sul",
            subtitle="Veja os melhores hotéis do RS"
        )
        for route in routes:
            self.escaparate.routes.add(route)

        for hotel in hoteles:
            self.escaparate.itens.add(hotel)
        self.username = 'tourism'
        self.password = 'tourism_pwd'
        self.user = User.objects.create_superuser(
            self.username, 'test@example.com', self.password)

    def test_without_authentication(self):
        """
        Test without authentication
        """
        api_request = APIRequestFactory().get("")
        detail_view = EscaparateViewSet.as_view({'get': 'retrieve'})
        response = detail_view(api_request, pk=self.escaparate.pk)
        self.assertEqual(response.status_code, 403)

    def test_with_authentication(self):
        """
        Auth using force_authenticate
        """
        factory = APIRequestFactory()
        user = User.objects.get(username=self.username)
        detail_view = EscaparateViewSet.as_view({'get': 'retrieve'})

        api_request = factory.get('')
        force_authenticate(api_request, user=user)
        response = detail_view(api_request, pk=self.escaparate.pk)
        self.assertEqual(response.status_code, 200)
