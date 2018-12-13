from django.urls import path

from . import views


app_name = 'superAdmin'

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:client_id>/client', views.client, name='client')
]
