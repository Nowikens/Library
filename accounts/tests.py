from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from books.models import Book, Publisher, Author

# Create your tests here.





class Authentication_tests(TestCase):

    def setUp(self):
        """ Setting up 1user, 1 publisher, 1 author and 1 book. """
        new_user = User.objects.create(username="testuser")
        new_author      = Author.objects.create(names = 'Stanisław', surname = 'Lem')
        new_publisher   = Publisher.objects.create(name = 'Wydawnictwo literackie', adress = 'Kraków')
        
        new_book        = Book.objects.create(
            title     = 'Solaris',
            author    = new_author,
            publisher = new_publisher,
            year      = 1986,
            status    = 'In Stock',
        )
        
    def test_index_view_authenticated_user(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        
        response = self.client.get(reverse('index:homepage'))
        
        self.assertEqual(response.status_code, 200)

        
        
    def test_register_redirect(self):
        """ Posting data to register new user, then testing reirect, and number of user objects in database. """
        response = self.client.post(reverse('accounts:register'), 
            {
                'username': 'testing',
                'password1': 'totallysuperstrongpassword123',
                'password2': 'totallysuperstrongpassword123',
            }
        )

        self.assertRedirects(response, reverse('accounts:login'), status_code=302, target_status_code=200)
        self.assertEqual(User.objects.all().count(), 2)