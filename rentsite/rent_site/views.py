from __future__ import absolute_import, unicode_literals
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, HttpResponse
from .models import *
import json


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if 'http404' in self.request.GET:
            context['http404'] = self.request.GET['http404']
        return context


class PlaceView(TemplateView):
    template_name = 'renting/places.html'

    def get_context_data(self, **kwargs):
        context = super(PlaceView, self).get_context_data(**kwargs)
        the_place = Place.objects.get(slug=kwargs['place_slug'])

        coords = the_place.get_coords()

        context['coords'] = json.dumps(coords)
        context['the_place'] = the_place.get_verbose_fields_list()
        return context


def search_view(request):
    if request.is_ajax():
        query = dict(request.POST.iterlists())


        for key, val in query.items():
            if key[:-2] in Place._CHECKBOXES:
                query[key[:-2] + '__in'] = query.pop(key)
            elif key in Place._SLIDERS:
                range = [int(x) for x in query.pop(key)[0].split(',')]
                query[key + '__range'] = range


        result = Place.objects.filter(**query)

        response = list()
        for r in result:
            response.append(r.get_thumbnail_fields_list())

        return HttpResponse(json.dumps(response), content_type='json')
    search_checkboxes = Place.get_search_checkboxes()
    search_sliders = Place.get_search_sliders()
    return render(request, 'renting/search.html', {
        'search_checkboxes': search_checkboxes,
        'search_sliders': search_sliders,
        'results': Place.objects.all()
    })


def map_search_view(request):
    if request.is_ajax():
        polygon = request.POST.getlist('polygon[]')
        polygon = [[float(y) for y in x.split(',')] for x in polygon]
        print polygon

        result = Place.objects.all()

        response = list()
        for r in result:
            if r.lies_into_polygon(polygon):
                response.append(r.get_thumbnail_fields_list())


        return HttpResponse(json.dumps(response), content_type='json')

    return render(request, 'renting/map_search.html')