from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import CreateLibraryUserForm, CreateUserForm, UpdateLibraryUserForm

from accounts.models import LibraryUser
from django.contrib.auth.models import User

# Create your views here.

class RegisterUser(CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/register.html'
    
    def get_success_url(self):
        return reverse('accounts:login')




class LoginUser(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return reverse('index:homepage')
  


  
class LogoutUser(LoginRequiredMixin, LogoutView):
    template_name = 'index/homepage.html'
    
    def get_next_page(self):
        return reverse('accounts:login')



class EditUser(UpdateView):
    form_class = UpdateLibraryUserForm
    template_name = 'accounts/register.html'
    model = LibraryUser
    
    def get_object(self, queryset=None):
        library_user = LibraryUser.objects.get(django_user=self.request.user)
        
        return library_user
        
        
    def get_success_url(self):
        return reverse('accounts:login')
        
        
