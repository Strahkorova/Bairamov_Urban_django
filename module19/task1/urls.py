from django.urls import path

from task1 import views

urlpatterns = [
    path('/games', views.games_view, name='games-view'),
    path('/shop-cart', views.shop_cart_view, name='shop-cart-view'),
    path('/register', views.sign_up_by_django, name='django_sign_up'),
    path('/logout', views.logout, name='logout'),
    path('/sign_in', views.sign_in_by_django, name='sign_in_by_django'),
    path('', views.index_view, name='index-view'),
]
