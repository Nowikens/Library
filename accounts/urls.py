from django.urls import path

from . import views


app_name = "accounts"
urlpatterns = [
    path('register/', views.register_account, name="register"),
    path('login/', views.login_account, name="login"),
    path('edit/', views.edit_account, name="eit"),
]
