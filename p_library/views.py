from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from p_library.models import Book

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "top100": list(range(1,101)),
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()    
    return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()    
    return redirect('/index/')
        
