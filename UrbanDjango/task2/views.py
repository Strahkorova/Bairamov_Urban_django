from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index_view(request):
    return render(request, 'second_task/index.html')


def func_template_view(request):
    return render(request, 'second_task/func_template.html')


class ClassView(TemplateView):
    template_name = 'second_task/class_template.html'
