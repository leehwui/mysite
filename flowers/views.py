from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Flower 

# Create your views here.

def index(request):
    flowers_list = Flower.objects.all()
    paginator = Paginator(flowers_list, 25)

    page = request.GET.get('page')

    try:
        flowers = paginator.page(page)
    except PageNotAnInteger:
        flowers = paginator.page(1)
    except EmptyPage:
        flowers = paginator.page(paginator.num_pages)

    return render(request, 'flowers/index.html', {'flowers': flowers});


def help(request):
    return render(request, 'static_pages/help.html')
