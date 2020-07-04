from django.shortcuts import render

from books.models import Book, Author, Publisher
# Create your views here.


def homepage(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index/homepage.html', context)
    
    
def authors_index(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'index/authors_index.html', context)
    
    
def publishers_index(request):
    publishers = Publisher.objects.all()
    context = {'publishers': publishers}
    return render(request, 'index/publishers_index.html', context)