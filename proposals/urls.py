from django.urls import path
from . import views

urlpatterns = [
    path('proposals', views.ProposalView.as_view(), name='proposal'),
]
