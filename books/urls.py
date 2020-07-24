from django.urls import path

from . import views


app_name = "books"
urlpatterns = [

    path('addBook/', views.CreateBook.as_view(), name="addBook"),
    path('removeBook/<int:pk>', views.RemoveBook.as_view(), name="removeBook"),
    path('editBook/<int:pk>', views.EditBook.as_view(), name="editBook"),


    path('addAuthor/', views.CreateAuthor.as_view(), name="addAuthor"),
    path('removeAuthor/<int:pk>', views.RemoveAuthor.as_view(), name="removeAuthor"),
    path('editAuthor/<int:pk>', views.EditAuthor.as_view(), name="editAuthor"),
    

    path('addPublisher/', views.CreatePublisher.as_view(), name="addPublisher"),
    path('removePublisher/<int:pk>', views.RemovePublisher.as_view(), name="removePublisher"),
    path('editPublisher/<int:pk>', views.EditPublisher.as_view(), name="editPublisher"),
    

]
