import threading
from django.shortcuts import redirect, reverse
from django.utils.deprecation import MiddlewareMixin
from userProfileApp.models import Notification

class GetCurrentUserMiddleWare(MiddlewareMixin):

	thread_local = threading.local()

	def process_request(self, request):
		GetCurrentUserMiddleWare.thread_local.current_user = request.user
		


def add_notification(updated_in_user):
	# to get current user
	thread_local = GetCurrentUserMiddleWare.thread_local
	if hasattr(thread_local, 'current_user'):
	    user = thread_local.current_user
	    if not user.is_authenticated:
	        user = None
	else:
	    user = None

	# if changes make by superuser (current user) send notification to user, and if change make by kep the user filed blank(user send to superuser)
	if user:
		if user.is_superuser:
		    Notification.objects.create(
		            for_user = updated_in_user,
		            msg = 'Field updated for '+updated_in_user.email,
		            redirect_uri = reverse('userProfileApp:usrProfile')
		        )
		else:   # if changed made by user
		    Notification.objects.create(
		            msg = 'Field updated for '+updated_in_user.email,
		            redirect_uri = reverse('superAdmin:client', args=[updated_in_user.id])
		        )

