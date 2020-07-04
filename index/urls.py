from django.urls import path

from . import views

app_name = "index"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('publishers/', views.publishers_index, name="publishers"),
    path('authors/', views.authors_index, name="authors"),
]
