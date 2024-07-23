"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task5', include(('task5.urls', 'task5'), namespace='task5'), name='task5'),
    path('task4', include(('task4.urls', 'task4'), namespace='task4'), name='task4'),
    path('task3', include(('task3.urls', 'task3'), namespace='task3'), name='task3'),
    path('', include(('task2.urls', 'task2'), namespace='task2'), name='task2'),
]
