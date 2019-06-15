from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard.as_view(), name='dashboard'),
]
