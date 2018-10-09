from django.test import TestCase
from .models import Profile, Image, Tags, Like

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

class CommentTestClass(TestCase):

    def test_save_method(self):
        self.comment.save_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comments) > 0)  

    def delete_comment_method(self):
        self.comment.save_comment()
        self.comment.delete_comment()
        self.assertTrue(len(comments) == 0)     
     

class UserTestClass(TestCase):
    def test_save_method(self):
        self.user.save_user()
        user = User.objects.all()
        self.assertTrue(len(user) > 0)  

    def delete_user_method(self):
        self.user.save_comment()
        self.user.delete_users()
        self.assertTrue(len(users) == 0)     


class ImageTestClass(TestCase):

    #setup method
     '''
    Set up method to run before each test cases.
    '''
    def setUp(self):
        nancy = Profile(name='nancy')
        nancy.save()
                
        self.beach= Image(image = 'jpg', image_name= 'beach', image_caption= 'daydreaming'
        self.beach.save()

    def test_instance(self):
    '''
    This test tests if an object is initialized properly.
    '''
        self.assertTrue(isinstance(self.beach,Image))

    #save method
    def test_save_method(self):
    '''
    This is to to test if images are saved.
    '''    
        self.beach.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    #delete method
    def delete_image_method(self):
    '''
    This is to test if an image can be deleted.
    '''    
        self.beach.save_image()
        self.beach.delete_image()
        images = Image.objects.all()   
        self.assertTrue(len(images) == 0)




    
