from django.urls import path
from apps.core import views

urlpatterns = [
    path(r'', views.home, name='home'),

    path('size/', views.SizeListView.as_view(), name='size-list'),
    path('size/create/', views.SizeCreateView.as_view(), name='size-create'),

    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),

    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),

    path('inventory/', views.InventoryListView.as_view(), name='inventory-list'),
    path('inventory/create/', views.InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/detail/<pk>', views.InventoryDetailView.as_view(), name='inventory-detail'),
    path('inventory/', views.InventoryDetailView.as_view(), name='inventory-restock'),

    path('barcode/detail/<pk>', views.BarCodeListView.as_view(), name='barcode-detail'),

]
