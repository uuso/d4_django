import datetime
from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Friend(models.Model):
    full_name = models.TextField()
    city = models.TextField()
    is_library = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.full_name, self.city)


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
    # copy_count = models.SmallIntegerField(default=1)
    # len(Book.objects.filter(author=1).first().leasing.values().filter(is_library=False))
    price = models.DecimalField(decimal_places=2, max_digits=10)
    publisher = models.ForeignKey(Publisher,
                                  null=True,
                                  on_delete=models.SET_NULL)
    leasing = models.ManyToManyField(Friend,
                                     through="Lease",
                                     through_fields=("book", "friend"))

    def __str__(self):
        return self.title


class Lease(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_lease = models.DateField(auto_now_add=True)
    date_back = models.DateField(default=datetime.datetime.now().date() +
                                 datetime.timedelta(days=14))
                                 