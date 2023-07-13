from django.urls import path
from appTwo import views

urlpatterns = [
    path(r'^$',views.help,name='help'),
]
