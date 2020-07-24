from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import LibraryUser

class LibraryUserForm(ModelForm):
    class Meta:
        model = LibraryUser
        exclude = ['books_limit', 'books', 'django_user']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']