from django.urls import path
from task5 import views


urlpatterns = [
    path('sign_up_by_html', views.sign_up_by_html, name='html_sign_up'),
    path('', views.sign_up_by_django, name='django_sign_up'),
]