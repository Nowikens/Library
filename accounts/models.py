from django.db import models

from books.models import Book
from django.contrib.auth.models import User

# Create your models here.




class LibraryUser(models.Model):
    
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    books       = models.ForeignKey(Book, null=True, blank=True, on_delete=models.DO_NOTHING)
    books_limit = models.IntegerField(default=3)
    
    
    

    

