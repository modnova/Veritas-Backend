# verifyer/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # Example: veritas1.herokuapp.com/content/get/
    url(r'^get/$', views.test),
    # Example: vertias1.herokuapp.com/
    url(r'^$', views.default)
]
