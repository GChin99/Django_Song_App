from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('main_page', views.main_page),
    path('create/album', views.create_album),
]