from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # /my_app --> my_app/urls.py
]