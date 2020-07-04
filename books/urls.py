from django.urls import path

from . import views


app_name = "books"
urlpatterns = [

    path('addBook/', views.add_book, name="addBook"),
    path('removeBook/<int:pk>', views.remove_book, name="removeBook"),
    path('editBook/<int:pk>', views.edit_book, name="editBook"),


    path('addAuthor/', views.add_author, name="addAuthor"),
    path('removeAuthor/<int:pk>', views.remove_author, name="removeAuthor"),
    path('editAuthor/<int:pk>', views.edit_author, name="editAuthor"),
    

    path('addPublisher/', views.add_publisher, name="addPublisher"),
    path('removePublisher/<int:pk>', views.remove_publisher, name="removePublisher"),
    path('editPublisher/<int:pk>', views.edit_publisher, name="editPublisher"),
    

]
