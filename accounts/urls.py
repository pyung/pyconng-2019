from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard.as_view(), name='dashboard'),
    path('tickets', views.TicketPricing.as_view(), name='pricing'),
    path('profile', views.profile.as_view(), name='update_profile'),
    path('sponsorship', views.sponsorship.as_view(), name='donate'),
    path('thank-you', views.thanks.as_view(), name='thanks'),
]
