
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('logout/', views.logout_view, name='logout'),  # Страница выхода
    path('add-recipe/', views.recipe_form, name='add_recipe'),  # Страница добавления рецепта
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),  # Страница просмотра рецепта
]

