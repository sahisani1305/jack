# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    path('', views.index, name='index'),
    path('message/', views.message, name='message'),
    path('messages/', views.get_messages_from_csv, name='get_messages_from_csv'),

    ]