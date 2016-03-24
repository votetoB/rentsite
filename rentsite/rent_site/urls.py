# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),

    url(
        regex=r'^place/(?P<category_slug>[\w.@+-]+)/$',
        view=views.PlaceView.as_view(),
        name='place'
    ),
]
