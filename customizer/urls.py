from django.urls import path
from . import views

app_name='customizer'
urlpatterns=[path('', views.index, name='index')]
