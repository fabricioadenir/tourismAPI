from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from api.models import Route
from api.views import RouteViewSet


class RouteViewSetTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """

    def setUp(self):
        self.route = Route.objects.create(route="/destinos")
        self.username = 'tourism'
        self.password = 'tourism_pwd'
        self.user = User.objects.create_superuser(
            self.username, 'test@example.com', self.password)

    def test_without_authentication(self):
        """
        Test without authentication
        """
        api_request = APIRequestFactory().get("")
        detail_view = RouteViewSet.as_view({'get': 'retrieve'})
        response = detail_view(api_request, pk=self.route.pk)
        self.assertEqual(response.status_code, 403)

    def test_with_authentication(self):
        """
        Auth using force_authenticate
        """
        factory = APIRequestFactory()
        user = User.objects.get(username=self.username)
        detail_view = RouteViewSet.as_view({'get': 'retrieve'})

        api_request = factory.get('')
        force_authenticate(api_request, user=user)
        response = detail_view(api_request, pk=self.route.pk)
        self.assertEqual(response.status_code, 200)
