from django.urls import path
from . import views

urlpatterns = [
	path('', views.ProposalListView.as_view(), name='proposals'),

    path('create', views.ProposalCreateView.as_view(), name='create_proposal'),
    path('update/<slug:proposal>/', views.ProposalUpdateView.as_view(), name='update_proposal'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]
