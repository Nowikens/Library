from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book
# Create your views here.




# ------------------------------------- BOOKS ------------------------------- # 
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
    
    
    


# ------------------------------ AUTHORS -------------------------------- #
def add_author(request):
    new_author = AuthorForm()
    
    if request.method == 'POST':
        new_author = AuthorForm(request.POST)
        if new_author.is_valid():
            new_author.save()
            
            return redirect('index:homepage')
    
    context = {
        'new_author': new_author
    }
    return render(request, 'books/add_author.html', context)

    
def remove_author(request, pk):
    author = Author.objects.get(id=pk)
    
    if request.method == "POST":
        author.delete()
        return redirect('index:homepage')
    context = {'author': author}
    return render(request, 'books/remove_author.html', context)
    
      
def edit_author(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)
    
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('index:homepage')
    
    context = {'form': form}
    return render(request, 'books/edit_author.html', context)
    






# ----------------------------------------- PUBLISHERS ----------------- #
def add_publisher(request):
    new_publisher = PublisherForm()
    
    if request.method == 'POST':
        new_publisher = PublisherForm(request.POST)
        if new_publisher.is_valid():
            new_publisher.save()
            
            return redirect('index:homepage')
    
    context = {
        'new_publisher': new_publisher
    }
    return render(request, 'books/add_publisher.html', context)
    
    
def remove_publisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    
    if request.method == "POST":
        publisher.delete()
        return redirect('index:homepage')
    context = {'publisher': publisher}
    return render(request, 'books/remove_publisher.html', context)
    
   
def edit_publisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    form = PublisherForm(instance=publisher)
    
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('index:homepage')
    
    context = {'form': form}
    return render(request, 'books/edit_publisher.html', context)
