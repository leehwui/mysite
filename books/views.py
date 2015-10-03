from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.



def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__contains=q)
            context = {'books': books, 'query': q}
            return render(request, 'books/search_results.html', context)

    return render(request, 'books/search_form.html', {'error': error})
