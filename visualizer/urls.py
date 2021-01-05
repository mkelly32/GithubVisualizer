from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.user, name='user'),
    path('', views.repo, name='repo'),
]