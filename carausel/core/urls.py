from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('',HomeView),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
]