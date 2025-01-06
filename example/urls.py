# example/urls.py
from django.urls import path

from example import views


urlpatterns = [
    path('', views.index, name='index'),
    path('message/', views.message, name='message'),
    path('chat/', views.chat_view, name='chat'),

    ]