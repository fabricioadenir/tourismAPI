from api.models import Escaparate, Route, Hotel, Category, City, Country
from rest_framework import serializers
import json

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'slug', 'state']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'slug']


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    country = CountrySerializer()
    category = CategorySerializer()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'slug', 'image', 'city', 'country', 'category', 'price']


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['route']


class EscaparateSerializer(serializers.ModelSerializer):
    itens = HotelSerializer(many=True)
    routes = serializers.SerializerMethodField()

    class Meta:
        model = Escaparate
        fields = ['id', 'title', 'subtitle', 'routes', 'itens']
        depth = 1
        
    def get_routes(self, instance):
        teste = []
        for item in instance.routes.all():
            teste.append(item.route)
        return teste