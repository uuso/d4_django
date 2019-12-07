from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, Lease

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass

# Альтернативная запись, т.к. в предыдущем виде внутри класса ничего не выполняется (pass)
admin.site.register(Author)
admin.site.register(Publisher)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'city', 'is_library')

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('friend', 'book', 'date_lease', 'date_back')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    # Если в классе Author определён __str__, то достаточно следующей строки:
    # list_display = ('title', 'author')

    # Иначе - создадим возможность получать поле через именованый метод
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    @staticmethod
    def total_count(obj):
        return "Not calculated yet"
    @staticmethod
    def ready_for_lease(obj):
        return "Not calculated yet"

    list_display = ('title', 'author_full_name', "ready_for_lease", "total_count")

    # Укажем поля для отображения (неуказанные нельзя будет редактировать из админки)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author',
              'price', 'publisher')
