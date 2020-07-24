from django.shortcuts import render, redirect

from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout

from .forms import LibraryUserForm, CreateUserForm

from accounts.models import LibraryUser
from django.contrib.auth.models import User

# Create your views here.

class RegisterUser(CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/register.html'
    
    def get_success_url(self):
        return reverse('index:homepage')
        
class LoginUser(LoginView):
    template_name = 'accounts/login.html'
    
class LogoutUser(LogoutView):
    template_name = 'index/homepage.html'




class EditUser(UpdateView):
    pass
