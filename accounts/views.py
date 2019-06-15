import os
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from.forms import SignUpForm

# Create your views here.


class index(TemplateView):
	template_name = 'accounts/index.html'

	def get_context_data(self, **kwargs):
		context = super(index, self).get_context_data(**kwargs)
		context['images'] = os.listdir(os.path.join(settings.STATICFILES_DIRS[0],'img', "past_event"))

		return context


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.occupation = form.cleaned_data.get('occupation')
            user.profile.tagline = form.cleaned_data.get('tagline')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})