from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from userProfileApp.models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	context = {
	}
	return render(request, 'coreApp/home.html', context)


@login_required
def mark_notifications_as_read(request):
	if request.user.is_superuser:
		Notification.objects.filter(for_user=None).update(
					is_read=True
				)
	else:
		Notification.objects.filter(for_user=request.user).update(
			is_read=True
		)

	return JsonResponse('Done', safe=False)
