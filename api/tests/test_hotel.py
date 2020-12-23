from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from api.models import Hotel, Category, City, Country
from api.views import HotelViewSet


class HotelViewSetTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """

    def setUp(self):
        Category.objects.create(name="Hospedagem de Verão")
        City.objects.create(
            name="Florianópolis",
            state="SC"
        )

        Country.objects.create(
            name="Brasil"
        )

        category = Category.objects.get(id=1)
        city = City.objects.get(id=1)
        country = Country.objects.get(id=1)

        
        self.hotel = Hotel.objects.create(
            hotel_name="Alameda Alegra",
            image="http://sbtur.com/images/alameda-alegra.jpg",
            city=city,
            country=country,
            category=category,
            price=3000
        )
        self.username = 'sbtur'
        self.password = 'sbtur_pwd'
        self.user = User.objects.create_superuser(
            self.username, 'test@example.com', self.password)

    def test_without_authentication(self):
        """
        Test without authentication
        """
        api_request = APIRequestFactory().get("")
        detail_view = HotelViewSet.as_view({'get': 'retrieve'})
        response = detail_view(api_request, pk=self.hotel.pk)
        self.assertEqual(response.status_code, 403)

    def test_with_authentication(self):
        """
        Auth using force_authenticate
        """
        factory = APIRequestFactory()
        user = User.objects.get(username=self.username)
        detail_view = HotelViewSet.as_view({'get': 'retrieve'})

        api_request = factory.get('')
        force_authenticate(api_request, user=user)
        response = detail_view(api_request, pk=self.hotel.pk)
        self.assertEqual(response.status_code, 200)
