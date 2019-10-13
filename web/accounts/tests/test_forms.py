from django.test import TestCase
from accounts.forms import SignUpForm


class SignUpFormTest(TestCase):
    '''
    Unit Test For The Sign Up Form
    To Run The Test :  python manage.py test accounts.tests.test_forms
    '''
    def test_bio_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['bio'].label == None or form.fields['bio'] == 'bio')
    
    def test_gender_label(self):
        form= SignUpForm()
        self.assertTrue(form.fields['gender'].label==None or form.fields['gender']== 'gender')


    def test_tagline_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['tagline'].label == None or form.fields['tagline'] =='tagline')
        
    def test_occupation_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['occupation'].label == None or form.fields['occupation'] =='occupation')
    
    def test_first_name_label(self):
        form = SignUpForm()
        self.assertEquals(form.fields['first_name'].label,'First name')

    def test_last_name_label(self):
        form = SignUpForm()
        self.assertEquals(form.fields['last_name'].label,'Last name')

    def test_username_label(self):
        form = SignUpForm()
        self.assertEquals(form.fields['username'].label,'Username')
    
    def test_email_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['email'].label,'Email address')
    
    def test_password1_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['password1'].label,'Password')
    
    def test_password2_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['password2'].label,'Password confirmation')
