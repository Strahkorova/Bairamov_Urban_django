from django.urls import path
from task3 import views


urlpatterns = [
    path('/django', views.django_view, name='django-view'),
    path('/numpy', views.numpy_view, name='numpy-view'),
    path('', views.index_view, name='index3'),
]