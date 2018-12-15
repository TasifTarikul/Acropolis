from django.urls import path, include

from . import views


app_name = 'superAdmin'

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client/<int:client_id>', views.client, name='client'),
	path('api/',include(('superAdmin.api.urls','UserApi'),namespace='UserApi')),
]
