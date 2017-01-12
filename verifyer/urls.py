# verifyer/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<url>.+)/$', views.test, name='verify-url')
]
