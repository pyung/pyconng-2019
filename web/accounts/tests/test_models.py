from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile


class ProfileModelTest(TestCase):
    '''
    To Run The Test : python manage.py test accounts.tests.test_models
    '''
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser",
            password = "TestPassword"
        )
        profile = test_user.profile
        profile.bio = "A Dev"
        profile.tagline = "Python"
        profile.gender = "M"
        profile.save()
    

    #Testing Profile Model String Representation
    def test_str_representation(self):
        profile = Profile.objects.get(id=1)
        expected_ouput = f'{profile.user} profile'
        self.assertEquals(expected_ouput, str(profile))
    def test_profile_vals(self):
        test_user = User.objects.latest('id')
        profile = Profile.objects.get(id=1)
        self.assertEquals(profile.user,test_user)
        self.assertEquals(profile.bio,"A Dev")
        self.assertEquals(profile.tagline,"Python")
        self.assertEquals(profile.gender,"M")
        
        
    # Testing Profile Fields Labels
    def test_user_label(self):
        '''
        testing the user field in the Profile model
        '''
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'user')

    def test_bio_label(self):
        '''
            testing the bio field in the Profile model
        '''
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('bio').verbose_name
        self.assertEquals(field_label,'bio')

    def test_tagline_label(self):
        '''
        testing the tagline field in the Profile model
        '''
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('tagline').verbose_name
        self.assertEquals(field_label,'tagline')
    
    def test_gender_label(self):
        '''
        testing the gender field in the Profile model
        '''
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('gender').verbose_name
        self.assertEquals(field_label,'gender')
    

    # Testing Profile Fields Maxlength
    def test_bio_max_length(self):
        profile = Profile.objects.get(id=1)
        maxlength = profile._meta.get_field('bio').max_length
        self.assertEquals(maxlength,500)

    
    def test_tagline_max_length(self):
        profile = Profile.objects.get(id=1)
        maxlength = profile._meta.get_field('tagline').max_length
        self.assertEquals(maxlength,35)

    
    def test_gender_max_length(self):
        profile = Profile.objects.get(id=1)
        maxlength = profile._meta.get_field('gender').max_length    
        self.assertEquals(maxlength,1)
 
    







