from django.urls import path

from . import views

urlpatterns = [
    path('get_shortest_path', views.get_shortest_path),
]
