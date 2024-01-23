from django.urls import path

from . import views

urlpatterns = [
    # Страница с корзиной
    path('basket/', views.basket),
    # Страница с личным кабинетом
    path('lk/', views.personal_account),
    # Страница с оплатой
    path('payment/', views.payment),
]