from django.urls import path

from . import views

app_name = "index"
urlpatterns = [
    path('', views.HomepageView.as_view(), name="homepage"),
    path('authors/', views.AuthorsView.as_view(), name="authors"),
    path('publishers/', views.PublishersView.as_view(), name="publishers"),

]
