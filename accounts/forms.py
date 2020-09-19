from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory

from django.contrib.auth.models import User
from .models import LibraryUser

class CreateLibraryUserForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        exclude = ['books_limit', 'books', 'django_user']
 

 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        
        
        
class UpdateLibraryUserForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        exclude = ['books_limit', 'books', 'django_user']
        
        
        