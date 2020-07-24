from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book, Author, Publisher
# Create your views here.


class HomepageView(ListView):
    template_name = 'index/homepage.html'
    queryset = Book.objects.all().order_by('title')
    context_object_name = 'books'




    
class AuthorsView(ListView):
    template_name = 'index/authors_index.html'
    queryset = Author.objects.all()
    context_object_name = 'authors'




class PublishersView(ListView):
    template_name = 'index/publishers_index.html'
    queryset = Publisher.objects.all()
    context_object_name = 'publishers'