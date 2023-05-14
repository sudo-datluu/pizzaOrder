from django.urls import path, include
from api import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login', views.Login.as_view()),
    path('auth/customer/signup', views.CustomerSignUp.as_view()),
    path('auth/employer/signup', views.createEmployerAccount),
    path('products/', views.ProductList.as_view()),
    path('products/pizza', views.PizzaList.as_view()),
    path('products/top', views.get_top_products),
    path('products/search', views.search_product),
    path('products/<int:product_id>', views.ProductDetail.as_view()),
    path('orders/create', views.create_order),
    path('orders/<int:order_id>', views.OrderDetail.as_view()),
    path('orders/<int:order_id>/fullfill', views.FullfillOrder.as_view()),
    path('customers/<int:customer_id>/orders', views.CustomerOrderList.as_view())
]