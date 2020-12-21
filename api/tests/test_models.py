from django.test import TestCase
from api.models import Category, City, Country, Hotel, Route, Escaparate
from django.utils.text import slugify
from sbtur.settings import development


class CategoryTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """
    @classmethod
    def setUpTestData(cls):
        development.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
        Category.objects.create(name="Hospedagem de Verão")

    def test_field_name(self):
        category = Category.objects.get(id=1)
        field_name = category._meta.get_field('name').verbose_name
        field_slug = category._meta.get_field('slug').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_slug, 'slug')

    def test_field_max_length(self):
        category = Category.objects.get(id=1)
        max_length_name = category._meta.get_field('name').max_length
        self.assertEquals(max_length_name, 50)

    def test_field_slug(self):
        category = Category.objects.get(id=1)
        my_slug = slugify("Hospedagem de Verão")
        self.assertEqual(category.slug, my_slug)


class CityTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """
    @classmethod
    def setUpTestData(cls):
        development.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
        City.objects.create(
            name="Porto Alegre",
            state="RS"
        )

    def test_field_name(self):
        city = City.objects.get(id=1)
        field_name = city._meta.get_field('name').verbose_name
        field_slug = city._meta.get_field('slug').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_slug, 'slug')

    def test_field_max_length(self):
        city = City.objects.get(id=1)
        max_length_name = city._meta.get_field('name').max_length
        max_length_state = city._meta.get_field('state').max_length
        self.assertEquals(max_length_name, 200)
        self.assertEquals(max_length_state, 2)

    def test_field_slug(self):
        city = City.objects.get(id=1)
        my_slug = slugify("Porto Alegre")
        self.assertEqual(city.slug, my_slug)


class CountryTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """
    @classmethod
    def setUpTestData(cls):
        development.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
        Country.objects.create(
            name="Brasil"
        )

    def test_field_name(self):
        country = Country.objects.get(id=1)
        field_name = country._meta.get_field('name').verbose_name
        field_slug = country._meta.get_field('slug').verbose_name
        self.assertEquals(field_name, 'name')
        self.assertEquals(field_slug, 'slug')

    def test_field_max_length(self):
        country = Country.objects.get(id=1)
        max_length_name = country._meta.get_field('name').max_length
        self.assertEquals(max_length_name, 200)

    def test_field_slug(self):
        country = Country.objects.get(id=1)
        my_slug = slugify("Brasil")
        self.assertEqual(country.slug, my_slug)


class HotelTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """
    @classmethod
    def setUpTestData(cls):
        development.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
        Category.objects.create(name="Hospedagem de Verão")
        City.objects.create(
            name="",
            state="SC"
        )

        Country.objects.create(
            name="Brasil"
        )

        category = Category.objects.get(id=1)
        city = City.objects.get(id=1)
        country = Country.objects.get(id=1)

        Hotel.objects.create(
            hotel_name="Alameda Alegra",
            image="http://sbtur.com/images/alameda-alegra.jpg",
            city=city,
            country=country,
            category=category,
            price=3000
        )

    def test_field_name(self):
        hotel = Hotel.objects.get(id=1)
        field_name = hotel._meta.get_field('hotel_name').verbose_name
        field_slug = hotel._meta.get_field('slug').verbose_name
        field_image = hotel._meta.get_field('image').verbose_name
        field_city = hotel._meta.get_field('city').verbose_name
        field_country = hotel._meta.get_field('country').verbose_name
        field_category = hotel._meta.get_field('category').verbose_name
        field_price = hotel._meta.get_field('price').verbose_name
        self.assertEquals(field_name, 'hotel name')
        self.assertEquals(field_slug, 'slug')
        self.assertEquals(field_image, 'image')
        self.assertEquals(field_city, 'city')
        self.assertEquals(field_country, 'country')
        self.assertEquals(field_category, 'category')
        self.assertEquals(field_price, 'price')

    def test_field_max_length(self):
        hotel = Hotel.objects.get(id=1)
        max_length_name = hotel._meta.get_field('hotel_name').max_length
        self.assertEquals(max_length_name, 200)

    def test_field_slug(self):
        hotel = Hotel.objects.get(id=1)
        my_slug = slugify("Alameda Alegra")
        self.assertEqual(hotel.slug, my_slug)


class RouteTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """
    @classmethod
    def setUpTestData(cls):
        development.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
        Route.objects.create(route="/destino")

    def test_field_name(self):
        route = Route.objects.get(id=1)
        field_name = route._meta.get_field('route').verbose_name
        self.assertEquals(field_name, 'route')


class EscaparateTestClass(TestCase):
    """
    Responsible for testing the data structure.
    """
    @classmethod
    def setUpTestData(cls):
        development.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
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
            image="http://sbtur.com/images/alameda-alegra.jpg",
            city=city_floripa,
            country=country,
            category=category,
            price=3000.
        )

        Hotel.objects.create(
            hotel_name="Ibis Poços de Caldas",
            image="http://sbtur.com/images/ibis-pocos-de-caldas.jpg",
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

        escaparate = Escaparate.objects.create(
            title="Hotéis na região sul",
            subtitle="Veja os melhores hotéis do RS"
        )
        for route in routes:
            escaparate.routes.add(route)

        for hotel in hoteles:
            escaparate.itens.add(hotel)

    def test_campo_nome(self):
        escaparate = Escaparate.objects.get(id=1)
        campo_title = escaparate._meta.get_field('title').verbose_name
        campo_subtitle = escaparate._meta.get_field('subtitle').verbose_name
        campo_routes = escaparate._meta.get_field('routes').verbose_name
        campo_itens = escaparate._meta.get_field('itens').verbose_name
        self.assertEquals(campo_title, 'title')
        self.assertEquals(campo_subtitle, 'subtitle')
        self.assertEquals(campo_routes, 'routes')
        self.assertEquals(campo_itens, 'itens')

    def test_campo_nome_max_length(self):
        escaparate = Escaparate.objects.get(id=1)
        max_length_title = escaparate._meta.get_field('title').max_length
        max_length_subtitle = escaparate._meta.get_field('subtitle').max_length
        self.assertEquals(max_length_title, 150)
        self.assertEquals(max_length_subtitle, 150)
