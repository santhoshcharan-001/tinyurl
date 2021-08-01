from django.contrib import admin
from django.urls import path
from .views import shortme,go_to
urlpatterns = [
    path('',shortme),
    path('<str:text>',go_to),
]
