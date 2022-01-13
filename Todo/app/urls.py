from django.contrib import admin
from django.urls import path,include
from . import  views

urlpatterns = [
    path('',views.index,name='index'),
    path('completed/<int:pk>/',views.completed,name='completed'),
    path('notcomplete/<int:pk>/', views.notcomplete, name='notcomplete'),
    path('add/',views.add,name="add"),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('deleteall',views.deleteall,name='deleteall')
]