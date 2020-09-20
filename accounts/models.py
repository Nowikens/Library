from django.db import models


from django.contrib.auth.models import User

# Create your models here.




class LibraryUser(models.Model):
    
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    books_limit = models.IntegerField(default=3)
    
    
    

    

