from django.urls import path
from . import views

app_name='payments'
urlpatterns=[path('', views.checkout, name='index')]
