from django.forms import ModelForm

from .models import Author, Publisher, Book 


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'