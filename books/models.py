from django.db import models
from accounts.models import LibraryUser
# Create your models here.

class Author(models.Model):
    names    = models.CharField(null=True, blank=True, max_length=100)
    surname  = models.CharField(null=True, blank=True, max_length=100)
    nickname = models.CharField(null=True, blank=True, max_length=100)
    
    def __str__(self):
        return self.surname


class Publisher(models.Model):
    name   = models.CharField(null=False, blank=False, max_length=100)
    adress = models.CharField(null=False, blank=False, max_length=100)
    
    def __str__(self):
        return self.name
        
        
        
class Book(models.Model):
    STATUS = (
        ('In stock', 'In Stock'),
        ('Borrowed', 'Borrowed')
    )

    title      = models.CharField(null=False, blank=False, max_length=100)  
    author     = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publisher  = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    year       = models.IntegerField(null=True, blank=True)
    status     = models.CharField(max_length=100, choices=STATUS)
    date_added = models.DateTimeField(auto_now_add=True)
    borrower   = models.ForeignKey(LibraryUser, null=True, blank=True, on_delete=models.DO_NOTHING)
    
    
    def __str__(self):
        return "{} {}".format(self.title, self.year)
    

    