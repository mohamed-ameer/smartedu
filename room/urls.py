from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('addroom/', views.NewRoom, name='newroom'),
    path('<slug:slug>/', views.room, name='room'),
]