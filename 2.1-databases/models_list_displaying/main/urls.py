from django.contrib import admin
from django.urls import path, register_converter, include

from books.converters import PubDateConverter
from books.views import books_view

register_converter(PubDateConverter, 'date')

urlpatterns = [
    path('books/<date:dt>/', books_view, name='books'),
    path('books/', books_view, name='books'),
    path('', books_view, name='books'),
    path('admin/', admin.site.urls),
]
