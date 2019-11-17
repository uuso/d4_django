from django.shortcuts import render, redirect
from p_library.models import Book, Author
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "top100": list(range(1,101)),
    }
    return HttpResponse(template.render(biblio_data, request))


