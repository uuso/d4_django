from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendList, FriendCreate, PublisherCreate, BookCreate

app_name = 'p_library'

urlpatterns = [
    path('authors', AuthorList.as_view(), name='author_list'),
    path('authors/create', AuthorEdit.as_view(), name='author_create'),
    path('authors/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many',
         books_authors_create_many,
         name='books_authors_create_many'),
    path('friends', FriendList.as_view(), name='friends_list'),
    path('friends/create', FriendCreate.as_view(), name='friend_create'),
    path('publishers/create', PublisherCreate.as_view(), name='publisher_create'),
    path('books/create', BookCreate.as_view(), name='book_create'),
]
