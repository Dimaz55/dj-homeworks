from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request, dt=None):
    template = 'books/books_list.html'
    all_books = Book.objects.all().order_by('pub_date')
    context = {'books': all_books}

    if dt:
        dt_book = all_books.filter(pub_date=dt)
        for i, book in enumerate(all_books, 1):
            if dt_book.first() == book:
                page_num = i
        paginator = Paginator(all_books, 1)
        page = paginator.get_page(page_num)

        next_page = prev_page = None
        if page.has_next():
            next_page = paginator.get_page(page.next_page_number())
        if page.has_previous():
            prev_page = paginator.get_page(page.previous_page_number())
        context = {'books': dt_book,
                   'page': page,
                   'next': next_page,
                   'prev': prev_page}
    return render(request, template, context)
