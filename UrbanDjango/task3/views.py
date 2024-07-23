from django.shortcuts import render


# Create your views here.
def index_view(request):
    context = {
        'title': 'Библиотеки Python',
        'page_header': 'Главная'
    }
    
    return render(request, 'third_task/index.html', context)


def django_view(request):
    context = {
        'title': 'Библиотека Django',
        'page_header': 'Django'
    }
    
    return render(request, 'third_task/django.html', context)


def numpy_view(request):
    context = {
        'title': 'Библиотека Numpy',
        'page_header': 'Numpy'
    }
    
    return render(request, 'third_task/numpy.html', context)
