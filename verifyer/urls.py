# verifyer/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # Example: veritas1.herokuapp.com/content/facebook.com/
    url(r'^/(?P<url>)/$', views.test, name='verify-url')
]
