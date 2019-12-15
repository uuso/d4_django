from django.urls import path
from .views import AuthorEdit, FriendCreate, PublisherCreate, BookCreate

app_name = 'p_library'

urlpatterns = [
    path('authors/create', AuthorEdit.as_view(), name='author_create'),
    path('friends/create', FriendCreate.as_view(), name='friend_create'),
    path('publishers/create', PublisherCreate.as_view(), name='publisher_create'),
    path('books/create', BookCreate.as_view(), name='book_create'),
]
