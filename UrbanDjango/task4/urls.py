from django.urls import path
from task4 import views


urlpatterns = [
    path('/django', views.django_view, name='django-view-4'),
    path('/numpy', views.numpy_view, name='numpy-view-4'),
    path('', views.index_view, name='index4'),
]