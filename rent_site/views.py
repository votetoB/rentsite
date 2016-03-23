from __future__ import absolute_import, unicode_literals
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import *


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
        context['places_list'] = list()
        return context