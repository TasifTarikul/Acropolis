from django.urls import path

from . import views


app_name = 'userProfileApp'

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/', views.usr_profile, name='usrProfile'),
]
