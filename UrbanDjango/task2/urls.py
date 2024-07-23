from django.urls import path
from django.views.generic import TemplateView
from task2 import views


urlpatterns = [
    path("func_template", views.func_template_view, name="func-template"),
    path("class_template", TemplateView.as_view(template_name='second_task/class_template.html'), name="class-template"),
    path('', TemplateView.as_view(template_name='second_task/index.html'), name='index'),
]