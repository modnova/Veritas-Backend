# verifyer/urls.py
from django.conf.urls import url
from verifyer import views

urlpatterns = [
    url(r'^$', views.test.as_view()),
]
