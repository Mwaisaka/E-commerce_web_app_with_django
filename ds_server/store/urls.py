from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.login import Login, logout

urlpatterns = [
    path('', store, name='homepage'),
    # path('store', store, name='store'),
    path('cart/', Index.as_view(), name='cart'),  # cart actions
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
