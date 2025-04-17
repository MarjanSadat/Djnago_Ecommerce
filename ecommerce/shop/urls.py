from django.contrib import admin
from django.urls import path

from .views import home_page, about_us_page, contact_us_page, login_page, register_page

urlpatterns = [
    path("",home_page),
    path('about_us', about_us_page),
    path('contact_us', contact_us_page),
    path('login', login_page),
    path('register', register_page),
]
