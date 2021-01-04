from django.urls import path
from online_sale import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('brands/', views.BrandList.as_view()),
    path('brands/<int:pk>/', views.BrandDetail.as_view()),
]
