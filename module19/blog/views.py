from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


# Create your views here.
def post_list(request):
    post_list = Post.objects.all().select_related('author', 'category').prefetch_related('tags')
    
    # Получение количества элементов на странице из параметров GET
    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(post_list, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'per_page': per_page,
    }
    
    return render(request, 'pagination_task/index.html', context)

