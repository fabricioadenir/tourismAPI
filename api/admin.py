from django.contrib import admin
from .models import (
    Category,
    City,
    Country,
    Hotel,
    Route,
    Escaparate
)


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    field_category = ['name', 'slug']
    list_display = field_category
    list_filter = field_category
    search_fields = field_category


admin.site.register(Category, CategoryAdmin)


class CityAdmin(admin.ModelAdmin):
    model = City
    field_city = ['name', 'slug', 'state']
    list_display = field_city
    list_filter = field_city
    search_fields = field_city


admin.site.register(City, CityAdmin)


class CountryAdmin(admin.ModelAdmin):
    model = Country
    field_country = ['name', 'slug']
    list_display = field_country
    list_filter = field_country
    search_fields = field_country


admin.site.register(Country, CountryAdmin)


class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    field_hotel = [
        'hotel_name',
        'slug',
        'image',
        'city',
        'country',
        'category',
        'price'
    ]
    list_display = field_hotel
    list_filter = field_hotel
    search_fields = field_hotel


admin.site.register(Hotel, HotelAdmin)


class RouteAdmin(admin.ModelAdmin):
    model = Route
    field_route = ['route']
    list_display = field_route
    list_filter = field_route
    search_fields = field_route


admin.site.register(Route, RouteAdmin)


class EscaparateAdmin(admin.ModelAdmin):
    model = Escaparate
    field_escaparate = ['title', 'subtitle']
    list_display = field_escaparate
    list_filter = field_escaparate
    search_fields = field_escaparate


admin.site.register(Escaparate, EscaparateAdmin)
