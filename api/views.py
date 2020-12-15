from django.shortcuts import render
from rest_framework.response import Response
from api.models import Category, City, Country, Hotel, Route, Escaparate
from rest_framework import viewsets, permissions
from api.serializers import EscaparateSerializer, CategorySerializer, CitySerializer, CountrySerializer, RouteSerializer, HotelSerializer
from rest_framework import filters


#Classe solicitada no teste
class EscaparateViewSet(viewsets.ModelViewSet):
    serializer_class = EscaparateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        routes = self.request.data.get('routes', None)
        if routes:
            escaparate = Escaparate.objects.filter(routes__route__in=routes)
        else:
            escaparate = Escaparate.objects.all()
        return escaparate


# Classes implementadas em bonus
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category = Category.objects.all()
        return category


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        city = City.objects.all()
        return city


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        country = Country.objects.all()
        return country


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        route = Route.objects.all()
        return route


class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        hotel = Hotel.objects.all()
        return hotel
