# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),

    url(
        regex=r'^rent/(?P<place_slug>[\w.@+-]+)/$',
        view=views.PlaceView.as_view(),
        name='rent'
    ),

    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^faq/$', TemplateView.as_view(template_name='pages/faq.html'), name="faq"),
    url(r'^contacts/$', TemplateView.as_view(template_name='pages/contacts.html'), name="contacts"),
    url(r'^search/$', view= views.search_view, name="search"),
    url(r'^map_search/$', view=views.map_search_view, name="map-search")

]
