from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book
# Create your views here.




# ------------------------------------- BOOKS ------------------------------- # 
class CreateBook(LoginRequiredMixin, CreateView):
    template_name = 'books/add.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:addBook')



class RemoveBook(DeleteView, LoginRequiredMixin):
    template_name = 'books/remove.html'
    model = Book
        
    def get_success_url(self):
        return reverse('index:homepage')
    
    
    
class EditBook(LoginRequiredMixin, UpdateView):
    template_name = 'books/edit.html'
    model = Book
    fields = ['title', 'author', 'publisher', 'year', 'status']
    
    def get_success_url(self):
        return reverse('index:homepage')
    
   


# ------------------------------ AUTHORS -------------------------------- #
class CreateAuthor(LoginRequiredMixin, CreateView):
    template_name = 'books/add.html'
    form_class = AuthorForm

    def get_success_url(self):
        return reverse('books:addAuthor')



class RemoveAuthor(LoginRequiredMixin, DeleteView):
    template_name = 'books/remove.html'
    model = Author
        
    def get_success_url(self):
        return reverse('index:homepage')
    
    
    
class EditAuthor(LoginRequiredMixin, UpdateView):
    template_name = 'books/edit.html'
    model = Author
    fields = ['names', 'surname', 'nickname']
    
    def get_success_url(self):
        return reverse('index:homepage')





# ----------------------------------------- PUBLISHERS ----------------- #
class CreatePublisher(LoginRequiredMixin, CreateView):
    template_name = 'books/add.html'
    form_class = PublisherForm

    def get_success_url(self):
        return reverse('books:addBook')



class RemovePublisher(LoginRequiredMixin, DeleteView):
    template_name = 'books/remove.html'
    model = Publisher
        
    def get_success_url(self):
        return reverse('index:homepage')
    
    
    
class EditPublisher(LoginRequiredMixin, UpdateView):
    template_name = 'books/edit.html'
    model = Publisher
    fields = ['name', 'adress']
    
    def get_success_url(self):
        return reverse('index:homepage')
      