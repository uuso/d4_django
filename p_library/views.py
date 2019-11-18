from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic import CreateView, ListView
from p_library.models import Book, Author, Publisher
from p_library.forms import AuthorForm


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'authors_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'


def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        # "top100": list(range(1,101)),
    }
    return HttpResponse(template.render(biblio_data, request))


def publishers(request):
    template = loader.get_template('list_publishers.html')
    pubs = Publisher.objects.all()
    data = {
        "publishers": [{
            "name": pub,
            "books": Book.objects.filter(publisher=pub),
        } for pub in pubs]
    }
    return HttpResponse(template.render(data))


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
