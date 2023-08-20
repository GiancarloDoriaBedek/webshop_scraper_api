from django.urls import path

from . import views


urlpatterns = [
    path('', views.api_home),
    path('ProductCategories/', views.get_product_categories),
    path('Product/', views.get_product),
    path('Products/', views.get_products),
    path('Pages/', views.get_pages),
    path('StoreInfo/', views.get_store_info),
]