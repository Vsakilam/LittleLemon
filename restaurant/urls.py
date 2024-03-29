from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
