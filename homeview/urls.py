from django.urls import path
from homeview import views


urlpatterns = [
    path('show', views.homeshow),
    path('show2', views.index),
]