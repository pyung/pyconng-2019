from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('tickets', views.TicketPricing, name='pricing'),
    path('profile', views.profile, name='update_profile'),
    path('sponsorship', views.sponsorship, name='donate'),
    path('thank-you', views.thanks, name='thanks'),
    path('ticket-pay-corp', views.ticket_pay_corporate, name='ticket_pay_corporate'),
    path('ticket-pay-indiv', views.ticket_pay_individual, name='ticket_pay_individual'),
    path('ticket-pay-stud', views.ticket_pay_students, name='ticket_pay_students'),
]
