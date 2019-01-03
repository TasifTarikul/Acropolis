from django.urls import path

from . import views


app_name = 'coreApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_notifications_as_read', views.mark_notifications_as_read, name='mark_notifications_as_read'),
]
