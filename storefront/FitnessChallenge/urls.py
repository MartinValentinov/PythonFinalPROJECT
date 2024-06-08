from django.contrib import admin
from django.urls import path, include
from FitnessChallenge import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('diet-calculator/', views.diet_calculator, name='diet_calculator'),
    path('diet/<int:diet_id>/', views.diet_detail, name='diet_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('ingredient/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),
]

