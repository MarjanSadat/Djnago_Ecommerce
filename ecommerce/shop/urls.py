from django.contrib import admin
from django.urls import path

from .views import home_page, contact_us_page

urlpatterns = [
    path("",home_page),
    path('contact_us', contact_us_page),
]
