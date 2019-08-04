from django.urls import path
from . import views

app_name = 'proposals'

urlpatterns = [
	path('', views.ProposalListView.as_view(), name='home'),

    path('create', views.ProposalCreateView.as_view(), name='create_proposal'),
    path('update/<slug:proposal>/', views.ProposalUpdateView.as_view(), name='update_proposal'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]
