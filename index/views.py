from django.shortcuts import render

from books.models import Book
# Create your views here.


def homepage(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index/homepage.html', context)