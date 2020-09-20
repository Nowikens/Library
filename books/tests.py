from django.test import TestCase

from .models import Book, Author, Publisher
# Create your tests here.




class BookTesting(TestCase):
    """ Testing books app. Checking process of creating book, publisher, and author object. """
   
    def setUp(self):
        """ Setting up 1 publisher, 1 author and 1 book. """
        new_author      = Author.objects.create(names = 'Stanisław', surname = 'Lem')
        new_publisher   = Publisher.objects.create(name = 'Wydawnictwo literackie', adress = 'Kraków')
        
        new_book        = Book.objects.create(
            title     = 'Solaris',
            author    = new_author,
            publisher = new_publisher,
            year      = 1986,
            status    = 'In Stock',
        )
        
        
        
    def test_objects_number(self):
        """ Testing number of created objects. """
        authors     = Author.objects.all().count()
        publishers  = Publisher.objects.all().count()
        books       = Book.objects.all().count()
        
        self.assertEqual(authors, 1)
        self.assertEqual(publishers, 1)
        self.assertEqual(books, 1)
    
    
    
    def test_author_data(self):
        """ Testing proper relations of set up author object. """
        self.author = Author.objects.get(names='Stanisław')
        self.publisher = Publisher.objects.get(name='Wydawnictwo literackie')
        
        # number of related books
        self.assertEqual(self.author.book_set.all().count(), 1)
        # relations
        self.assertEqual(self.author.book_set.get(title='Solaris').year, 1986)
        self.assertEqual(self.author.book_set.get(publisher=self.publisher).author, self.author)
        # __str__ method
        self.assertEqual(str(self.author), self.author.surname)



    def test_publisher_data(self):
        """ Testing proper relations of set up publisher object. """
        self.publisher = Publisher.objects.get(name='Wydawnictwo literackie')
        self.author = Author.objects.get(names='Stanisław')
        
        # number of related books
        self.assertEqual(self.publisher.book_set.all().count(), 1)
        # relations
        self.assertEqual(self.publisher.book_set.get(author=self.author).status, 'In Stock')
        self.assertEqual(self.publisher.book_set.get(author=self.author).publisher, self.publisher)
        # __str__ method
        self.assertEqual(str(self.publisher), self.publisher.name)
    
    
    
    def test_book_data(self):
        """ Testing proper relations of set up book object. """
        self.author = Author.objects.get(names='Stanisław')
        self.book = Book.objects.get(author=self.author)
        
        # attributes
        self.assertEqual(self.book.title, 'Solaris')
        self.assertEqual(self.book.year, 1986)
        self.assertEqual(self.book.publisher.name, 'Wydawnictwo literackie')
        # __str__ method
        self.assertEqual(str(self.book), 'Solaris 1986')
        
     
        
