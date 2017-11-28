"""
Copyright (C) 2017 Espressive Inc

"""
from django.conf.urls import url, include

from pinger import views

# router.register(r'typeahead', views.meh, base_name='lol')

urlpatterns = [
    # API
    # url(r'^', include(router.urls)),
    url(r'^$', views.my_view),
]
