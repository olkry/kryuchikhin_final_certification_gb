
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-recipe/', views.recipe_form, name='add_recipe'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]

