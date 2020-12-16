from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False)
    state = models.CharField(max_length=2)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    # TODO foi usado o nome hotel na classe
    # por não saber se é um cadastro de hotel
    # ou uma promoção
    hotel_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False)
    image = models.URLField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.hotel_name)
        super(Hotel, self).save(*args, **kwargs)

    def __str__(self):
        return self.hotel_name


class Route(models.Model):
    route = models.TextField()

    def __str__(self):
        return self.route


class Escaparate(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    routes = models.ManyToManyField(Route, blank=True)
    itens = models.ManyToManyField(Hotel)

    def __str__(self):
        return self.title
