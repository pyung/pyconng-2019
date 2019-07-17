from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, help_text='Let us know a bit more about you')
    gender = forms.ChoiceField(choices=Profile.GENDER)
    occupation = forms.ChoiceField(choices=Profile.OCCUPATION)
    tagline = forms.CharField(max_length=100, help_text='A catch phrase of you')

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username', 'password1', 'password2','tagline' )