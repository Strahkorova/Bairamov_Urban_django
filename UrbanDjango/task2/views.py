from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'second_task/index.html')


def class_tempalte_view(request):
    return render(request, 'second_task/class_template.html')


def func_template_view(request):
    return render(request, 'second_task/func_template.html')
