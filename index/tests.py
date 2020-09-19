from django.test import SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse

# Create your tests here.



class IndexTests(SimpleTestCase):
    """
        Testing index app.
    """
    
    def test_index_annonymous_user(self):
        """ Testing if unauthorized user is redirected to login page from homepage."""
        response = self.client.get(reverse('index:homepage'))
        
        self.assertRedirects(response, '/accounts/login/?next=/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    
    def test_authors_index_annonymous_user(self):
        """ Testing if unauthorized user is redirected to login page from authors index."""
        response = self.client.get(reverse('index:authors'))
        
        self.assertRedirects(response, '/accounts/login/?next=/authors/', status_code=302, target_status_code=200, fetch_redirect_response=True)
    
    
    def test_publishers_index_annonymous_user(self):
        """ Testing if unauthorized user is redirected to login page from publishers index."""
        response = self.client.get(reverse('index:publishers'))
        
        self.assertRedirects(response, '/accounts/login/?next=/publishers/', status_code=302, target_status_code=200, fetch_redirect_response=True)
