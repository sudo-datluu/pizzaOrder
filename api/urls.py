from django.urls import path, include
from api import views

urlpatterns = [
    path('auth/login', views.Login.as_view()),
    path('auth/customer/signup', views.CustomerSignUp.as_view()),
    path('auth/employer/signup', views.createEmployerAccount),
    path('products/', views.ProductList.as_view()),
    path('products/search', views.search_product),
    path('products/<int:product_id>', views.ProductDetail.as_view())
]