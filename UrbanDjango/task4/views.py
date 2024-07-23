from django.shortcuts import render



def get_menut_items():
    return [
            {
                'link': '/task4/django',
                'title': 'Django',
            },
            {
                'link': '/task4/numpy',
                'title': 'Numpy',
            },
        ]

# Create your views here.
def index_view(request):
    context = {
        'menu_items': get_menut_items()
    }
    
    return render(request, 'fourth_task/index.html', context)


def django_view(request):
    context = {
        'menu_items': get_menut_items()
    }
    
    return render(request, 'fourth_task/django.html', context)


def numpy_view(request):
    context = {
        'menu_items': get_menut_items(),
        'features': [
            'поддержка многомерных массивов (включая матрицы);',
            'поддержка высокоуровневых математических функций, предназначенных для работы с многомерными массивами.'
            ]
    }
    
    return render(request, 'fourth_task/numpy.html', context)
