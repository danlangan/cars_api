from django.urls import path
from . import views

urlpatters = [
    path('cars/', views.cars_list),
]