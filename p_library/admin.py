from django.contrib import admin
from p_library.models import Book, Author


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass

# Альтернативная запись, т.к. в предыдущем виде внутри класса ничего не выполняется (pass)
admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    # Если в классе Author определён __str__, то достаточно следующей строки:
    # list_display = ('title', 'author')

    # Иначе - создадим возможность получать поле через именованый метод
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
        
    list_display = ('title', 'author_full_name')
    
    # Укажем поля для отображения (неуказанные нельзя будет редактировать из админки)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')