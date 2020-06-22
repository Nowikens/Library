from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book
# Create your views here.

def add_book(request):
    new_book = BookForm()
    
    if request.method == 'POST':
        new_book = BookForm(request.POST)
        if new_book.is_valid():
            new_book.save()
            
            return redirect('index:homepage')
    
    context = {
        'new_book': new_book
    }
    return render(request, 'books/add_book.html', context)
    
def remove_book(request, pk):
    book = Book.objects.get(id=pk)
    
    if request.method == "POST":
        book.delete()
        return redirect('index:homepage')
    context = {'book': book}
    return render(request, 'books/remove_book.html', context)
    
   
   
def edit_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index:homepage')
    
    context = {'form': form}
    return render(request, 'books/edit_book.html', context)