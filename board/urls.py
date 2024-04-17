from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.CategoryLV.as_view(), name='index'),
    path('category', views.CategoryLV.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDV.as_view(), name='category_detail'),
    path('item/<int:pk>/', views.ItemDV.as_view(), name='item_detail'),
]