from django.urls import path
from . import views

app_name='ai_tools'
urlpatterns=[path('', views.advisor, name='index')]
