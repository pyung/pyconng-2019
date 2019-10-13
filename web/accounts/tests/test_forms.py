from django.test import TestCase
from accounts.forms import SignUpForm
from accounts.models import Profile


class SignUpFormTest(TestCase):
    '''
    Unit Test For The Sign Up Form
    To Run The Test :  python manage.py test accounts.tests.test_forms
    '''

    # Testing Form Label
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


    # Testing Form Help Text
    def test_bio_help_text(self):
        form = SignUpForm()
        self.assertEquals(form.fields['bio'].help_text,"Let us know a bit more about you")

    def test_tagline_help_text(self):
        form = SignUpForm()
        self.assertEquals(form.fields['tagline'].help_text,"A catch phrase of you")
    
    # Testing Form Choices

    def test_gender_choices(self):
        form = SignUpForm()
        self.assertEquals(tuple(form.fields['gender'].choices),Profile.GENDER)

    def test_occupation_choices(self):
        form = SignUpForm()
        self.assertEquals(tuple(form.fields['occupation'].choices),Profile.OCCUPATION)


    # Valid/Invalid
    def test_valid_form_data(self):
        form =SignUpForm()
        data= {
            'bio':'A Passionate Developer',
            'tagline':'Great Guy',
            'gender':'M',
            'occupation':'P',
            'first_name':'testuserfirstname',
            'last_name':'testuserlastname',
            'username':'testusername',
            'password1':'testuserpassword',
            'password2':'testuserpassword',
            'email':'testuser@gmail.com'
        }
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())
    def test_invalid_form_data(self):
        form =SignUpForm()
        data= {
            'bio':'A Passionate Developer',
            'tagline':'Great Guy',
            'gender':'M',
            'occupation':'P',
            'first_name':'testuserfirstname',
            'last_name':'testuserlastname',
            'username':'',
            'password1':'testuserpassword',
            'password2':'testuserpassword',
            'email':'testuser@gmail.com'
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())