from django.contrib import admin
from p_library.models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass

#Альтернативная запись, т.к. в предыдущем виде внутри класса ничего не выполняется (pass)
admin.site.register(Author)