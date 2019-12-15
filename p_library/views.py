from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic import CreateView
from p_library.models import Book, Author, Publisher, Friend, Lease
from p_library.forms import AuthorForm, BookForm, FriendForm, PublisherForm


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'authors_edit.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/index/'
    template_name = 'books_create.html'

class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    success_url = '/index/'
    template_name = 'publishers_create.html'


class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friends_list')
    template_name = 'friends_create.html'


def book_lease(request):
    if request.method == "POST":
        friend_id = request.POST['friend_id']
        book_id = request.POST['book_id']
        if friend_id and book_id:
            friend = Friend.objects.filter(id=friend_id).first()
            book = Book.objects.filter(id=book_id).first()
            if friend and book:
                if book.in_stock:
                    Lease.objects.create(book=book, friend=friend)
                    book.in_stock -= 1
                    book.save()
    return redirect('/index/book_leasing/?id={}'.format(book_id))


def book_leasing_page(request):
    # template = loader.get_template('book_leasing.html')
    book_id = request.GET['id']
    in_lease = Lease.objects.filter(book__id=book_id)
    friends = Friend.objects.all()
    data = {
        'leases': in_lease,
        'friends': friends,
        'book_id': book_id,
    }
    return render(request, 'book_leasing.html', data)


def book_return(request):
    if request.method == 'POST':
        lease_id = request.POST['id']
        if lease_id:
            lease = Lease.objects.filter(id=lease_id).first()
            if not lease:
                return redirect('/index/')
            lease.book.in_stock += 1
            lease.book.save()
            lease.delete()
    return redirect('/index/')

def index(request):
    template = loader.get_template('index.html')

    # не уверен в корректности prefetch_related
    books = Book.objects.all().prefetch_related('leasing')

    for book in books:
        book.in_lease = len(Lease.objects.filter(book=book))
    biblio_data = {
        "title": "мою библиотеку",
        "books_verbal_count": make_russian(len(books)),
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def make_russian(num):
    if 10 < num % 100 < 20:
        return f"{num} книг"

    return str(num) + \
    {
        1: " книга",
        2: " книги",
        3: " книги",
        4: " книги",
        5: " книг",
        6: " книг",
        7: " книг",
        8: " книг",
        9: " книг",
        0: " книг",
    }[num%10]

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.in_stock += 1
            book.save()
    return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.in_stock > 0:
                book.in_stock -= 1
            book.save()
    return redirect('/index/')
