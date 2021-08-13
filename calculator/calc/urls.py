from django.urls import path
from calc import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.addition, name="add"),
    path('sub/', views.sub, name="sub"),
    path('mul/', views.multiplication, name="mul"),
    path('div/', views.division, name="div"),
    path('cube/', views.cube, name="cube"),
]
