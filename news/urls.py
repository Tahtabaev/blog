from django.conf.urls import url, include
from django.contrib import admin
from news import views

urlpatterns = [
    url(r'^news/', views.news, name='news'),
]