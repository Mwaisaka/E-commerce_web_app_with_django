from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.login import Login, logout
from .views.signup import Signup
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from .views.cart import Cart

urlpatterns = [
    path('', store, name='homepage'),
    path('store/', store, name='store'),
    path('cart/', Index.as_view(), name='cart'),  # cart actions
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
     path('check-out', CheckOut.as_view(), name='checkout'),
     path('cart', auth_middleware(Cart.as_view()), name='cart'),
     path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
