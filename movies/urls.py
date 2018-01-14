from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
]
