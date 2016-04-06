# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    _NONDISPLAYABLE = ['id', 'image', 'slug', 'latitude', 'longitude']
    _NONSEARfrCHABLE = ['street', 'building', 'description']
    _THUMBNAIL = ['price', 'street', 'building', 'city', 'type']
    _SLIDERS = ['price', 'rooms', 'total_footage', 'living_footage', 'floor_number']
    _CHECKBOXES = ['city', 'region', 'planning', 'wall_type', 'type']

    city = models.CharField(max_length=75, verbose_name="Город", blank=True, null=True)
    street = models.CharField(max_length=75, verbose_name="Улица", blank=True, null=True)
    building = models.CharField(max_length=75, verbose_name="Дом",  blank=True, null=True)
    region = models.CharField(max_length=75, verbose_name="Район",  blank=True, null=True)

    rooms = models.IntegerField(verbose_name="Количество комнат",  blank=True, null=True)
    total_footage = models.IntegerField(verbose_name="Общая площадь",  blank=True, null=True)
    living_footage = models.IntegerField(verbose_name="Жилая площадь",  blank=True, null=True)
    floor_number = models.IntegerField(verbose_name="Этаж",  blank=True, null=True)
    planning = models.CharField(max_length=75, verbose_name="Планировка",  blank=True, null=True)
    wall_type = models.CharField(max_length=75, verbose_name="Тип стен",  blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена",  blank=True, null=True)

    # House or apartment
    type = models.CharField(max_length=75, verbose_name="Тип")

    ## image = models.ImageField(upload_to='rentsite/', verbose_name="Изображение",  blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000, verbose_name="Описание",  blank=True, null=True)

    # Coords for ympas
    latitude = models.FloatField(verbose_name="Широта",  blank=True, null=True)
    longitude = models.FloatField(verbose_name="Долгота",  blank=True, null=True)

    def __str__(self):
        return self.slug

    def get_thumbnail_fields_list(self):
        answer = list()
        for field in Place._meta.fields:
            if field.name in Place._THUMBNAIL:
                answer.append((field.name, field.value_to_string(self)))

        return answer

    def get_verbose_fields_list(self):
        answer = list()
        for field in Place._meta.fields:
            if field.name not in Place._NONDISPLAYABLE:
                answer.append((field.verbose_name, field.value_to_string(self)))

        return answer

    def get_coords(self):
        answer = dict()

        answer['latitude'] = self.latitude
        answer['longitude'] = self.longitude
        return answer

    @staticmethod
    def get_search_checkboxes():
        answer = dict()
        for field in Place._meta.fields:
            if field.name in Place._CHECKBOXES:
                answer[field.name] = field.verbose_name, list(set([x[field.name] for x in Place.objects.values(field.name)]))

        return answer

    @staticmethod
    def get_search_sliders():
        answer = dict()
        for field in Place._meta.fields:
            if field.name in Place._SLIDERS:
                answer[field.name] = field.verbose_name, \
                                     [Place.objects.all().aggregate(models.Min(field.name)).values()[0],
                                      Place.objects.all().aggregate(models.Max(field.name)).values()[0]]

        return answer
