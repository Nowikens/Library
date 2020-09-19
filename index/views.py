from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from books.models import Book, Author, Publisher

from itertools import chain
# Create your views here.


class HomepageView(LoginRequiredMixin, ListView):
    template_name = 'index/index.html'
    queryset = Book.objects.all().order_by('title')
    context_object_name = 'objects'
    



    
class AuthorsView(LoginRequiredMixin, ListView):
    template_name = 'index/index.html'
    queryset = Author.objects.all()
    context_object_name = 'objects'




class PublishersView(LoginRequiredMixin, ListView):
    template_name = 'index/index.html'
    queryset = Publisher.objects.all()
    context_object_name = 'objects'
    
