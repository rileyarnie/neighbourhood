from django.test import TestCase
from .models import Business, User, Neighbourhood

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(name='umoja', location='eastlands', occupants=23)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))

    def test_save_method(self):
        '''
        Test whether the object is saved in the database.
        '''
        self.hood.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) >0) 
   
    def test_delete_hood(self):
        '''
        Test case to see if the object can be deleted from the database.
        '''
        self.hood.save_hood()
        self.searched_hood = Neighbourhood.objects.get(id = 1)
        self.searched_hood.delete_hood()
        self.assertTrue(len(Neighbourhood.objects.all()) ==0)

