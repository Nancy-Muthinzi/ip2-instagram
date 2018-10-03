from django.test import TestCase
from .models import Profile, Image

class ProfileTestClass(TestCase):
    '''
    Set up method.
    '''
    def setUp(self):
        self.nancy = Profile(name = 'Nancy')

    def test_instance(self):
        self.assertTrue(isinstance(self.nancy, Profile))

    def test_save_method(self):
        self.nancy.save_profile()
        profile = Profile.objetcs.all()
        self.assertTrue(len(profiles) > 0)   

    def delete_profile_method(self):
        self.nancy.save_profile()
        self.nancy.delete_profile()
        self.assertTrue(len(profiles) == 0)     



