from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_category_menu, name='category-menu-list'),
    
]