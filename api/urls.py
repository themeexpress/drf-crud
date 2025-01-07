from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.getProducts, name="products"),
    path('product-detail/<int:pk>/', views.getProductDetail, name="product-detail"),
    path('product-create/', views.createProduct, name="product-create"),
    path('product-update/<int:pk>/', views.updateProduct, name="product-update"),
    path('product-delete/<int:pk>/', views.deleteProduct, name="product-delete"),
]