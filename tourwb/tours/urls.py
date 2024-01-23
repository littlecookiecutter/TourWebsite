from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком туров
    path('tours/', views.tours_list),
    # Отдельная страница с информацией о туре
    # slug - Конвертер slug пропускает ASCII
    path('tours/<slug:pk>/', views.tours_detail),
]