from django.contrib import admin
from django.urls import path, include
from FitnessChallenge import views, Diets

diets = Diets()

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('slim_diet/', diets.slim_diet, name='slim_diet'),
    path('avr_diet/', diets.avr_diet, name='avr_diet'),
    path('bulk_diet/', diets.bulk_diet, name='bulk_diet'),
]