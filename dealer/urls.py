from django.urls import path
from . import views

app_name='dealer'
urlpatterns=[path('', views.dealer_home, name='index')]
