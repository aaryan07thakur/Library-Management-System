# urls.py

from django.urls import path
from .views import (
    create_user, list_all_users, get_user_by_id,
    add_new_book, list_all_books, get_book_by_id, assign_update_book_details,
    borrow_book, return_book, list_all_borrowed_books
)

urlpatterns = [
    # User APIs
    path('create_user/', create_user, name='create_user'),
    path('list_all_users/', list_all_users, name='list_all_users'),
    path('get_user_by_id/<int:user_id>/', get_user_by_id, name='get_user_by_id'),

    # Book APIs
    path('add_new_book/', add_new_book, name='add_new_book'),
    path('list_all_books/', list_all_books, name='list_all_books'),
    path('get_book_by_id/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('assign_update_book_details/<int:book_id>/', assign_update_book_details, name='assign_update_book_details'),

    # BorrowedBooks APIs
    path('borrow_book/', borrow_book, name='borrow_book'),
    path('return_book/<int:borrow_id>/', return_book, name='return_book'),
    path('list_all_borrowed_books/', list_all_borrowed_books, name='list_all_borrowed_books'),
]
