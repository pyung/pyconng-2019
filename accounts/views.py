import os
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

# Create your views here.


class index(TemplateView):
	template_name = 'accounts/index.html'

	def get_context_data(self, **kwargs):
		context = super(index, self).get_context_data(**kwargs)
		context['images'] = os.listdir(os.path.join(settings.STATICFILES_DIRS[0],'img', "past_event"))
		for img in context['images']:
			print(img)

		return context


