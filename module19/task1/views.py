from django.shortcuts import render, redirect

from task1.forms import UserRegister, UserSignIn
from task1.models import Buyer, Game


# Create your views here.
def index_view(request):
    return render_template(request, 'second_task/index.html')


def shop_cart_view(request):
    return render_template(request, 'second_task/shop-cart.html')


def games_view(request):
    context = {
        'games' : Game.objects.all()
    }
    return render_template(request, 'second_task/games.html', **context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            
            # Проверки
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            # elif username in users:
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                buyer = Buyer.objects.create(name=username, balance=50, age=age, password=password)
                
                if request.session.get(get_buyer_tag_in_session()):
                    request.session.clear()
                    
                request.session[get_buyer_tag_in_session()] = buyer.name
                request.session.modified = True
                return redirect('task1:games-view')

        # Добавление формы в контекст, если есть ошибка
        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form
    
    return render_template(request, 'second_task/registration_page.html', **info)


def sign_in_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserSignIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            buyer = Buyer.objects.filter(name=username)
            
            if buyer.exists():
                buyer = buyer.get()
                
                if buyer.password == password:
                    request.session[get_buyer_tag_in_session()] = buyer.name
                    request.session.modified = True
                    return redirect('task1:games-view')
                else:
                    info['error'] = 'Пароль не подходит'
            else:
                info['error'] = 'Пользователь не найден'

        # Добавление формы в контекст, если есть ошибка
        info['form'] = form
    else:
        form = UserSignIn()
        info['form'] = form
    
    return render_template(request, 'second_task/sign_in_page.html', **info)


def logout(request):
    del request.session[get_buyer_tag_in_session()]
    request.session.modified = True
    return redirect('task1:index-view')
    
    
# --------------------------- Utils
def get_buyer_tag_in_session():
    return 'current_buyer'


def get_menut_items():
    return [
            {
                'link': '/task1/games',
                'title': 'Games',
            },
            {
                'link': '/task1/shop-cart',
                'title': 'Shop Cart',
            },
        ]


def render_template(request, template_path, **kwargs):
    
    buyer_username = request.session.get(get_buyer_tag_in_session(), None)
    buyer = None
    
    if buyer_username:
        buyer = Buyer.objects.get(name=buyer_username)
    
    context = {
        'menu_items': get_menut_items(),
        'show_move_back': 
                'shop-cart' in request.path 
                or 'games' in request.path
                or 'register' in request.path,
        'buyer': buyer
    }
    
    context.update(kwargs)
    
    return render(request, template_path, context)
