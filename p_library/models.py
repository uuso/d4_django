from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField()
    country = models.CharField(max_length=2)
    city = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    publisher = models.ForeignKey(Publisher,
                                  null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


# >>> from p_library.models import Author, Book
# >>> for book in Book.objects.all().order_by('price'):
# ...     print(book.title, book.price)
#           ---
# >>> Book.objects.all().order_by('-price')[0].price
# Decimal('2284.66')
#           ---
# >>> from django.db.models import Max
# >>> Book.objects.aggregate(Max('price'))
# {'price__max': Decimal('2284.66000000000')}
#           ---

# from django.db.models import Count
# gte2Authors = Author.objects.annotate(num_books=Count('book')).filter(num_books__gte=2)
# >>> for gA in gte2Authors:
# ...     print(gA.full_name, gA.num_books)
# >>> books = Book.objects.all().filter(author__in=gte2Authors)
# >>> total = 0
# >>> for book in books:
# ...     total += book.price*book.copy_count
# ...
# >>> total
# Decimal('27169.59')

# >>> foreignAuthors = Author.objects.exclude(country="RU")
# >>> for book in foreignBooks:
# ...     total += book.price*book.copy_count
# ...     print(book.author.full_name, book.author.country, "{} * {}".format(book.price, book.copy_count))
# Douglas Adams UK 2044.16 * 3
# Douglas Adams UK 2092.53 * 4
# Jerome David Salinger US 803.60 * 3
# Knut Hamsun NO 939.70 * 2
# >>> total
# Decimal('18792.80')

# >>> push = Author.objects.get(full_name__contains="Пушкин")
# >>> push.full_name
# 'Пушкин Александр Сергеевич'
# >>> total = 0
# >>> for book in Book.objects.filter(author=push):
# ...     total += book.price * book.copy_count
# ...
# >>> total
# Decimal('12666.99')

# >>> Book.objects.filter(author__full_name__contains="Adams").aggregate(Sum('price'))
# {'price__sum': Decimal('4136.69000000000')}