import datetime
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from rest_framework import viewsets, permissions, generics, pagination
from rest_framework.response import Response
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .serializers import UserProfileSerializer
User = get_user_model()



class LargeResultsSetPagination(pagination.PageNumberPagination):
	page_size = 9		#default won't work if page_size_query_param is set
	page_size_query_param = 'page_size'	
	# django_paginator_class = None
	# max_page_size = 1	

	def get_paginated_response(self, data):
		# print(dir(self.page))
		return Response({
				'pagination': {
				'next': self.get_next_link(),
				'previous': self.get_previous_link(),
				'total_value': self.page.paginator.count,
				'this_page_start_index_no': self.page.start_index(),
				'this_page_end_index_no': self.page.end_index(),
				'num_of_pages': self.page.paginator.num_pages,
				'current_page': self.page.number,
				'page_range': list(self.page.paginator.page_range)
			},
			'results': data
		})


class CustomerAccessPermission(permissions.BasePermission):
	message = 'Not Allowed.'

	def has_permission(self, request, view):
		# if request.user.is_superuser:
		if request.user.is_authenticated:
			if request.user.is_superuser:
				return True

		return True
		# return False


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):


	def get_queryset(self):
		to_return = User.objects.all()
		filters_kwargs = dict()
		filters_args = [Q()]	#blank search
		order_by_args = ['-id']

		to_return = User.objects.filter(*filters_args, **filters_kwargs).order_by(*order_by_args).distinct()
		# to_return = User.objects.filter().order_by('-id').distinct()

		return to_return

	# queryset = get_user_model().objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (CustomerAccessPermission,)
	pagination_class = LargeResultsSetPagination
	

	filterset_fields = ('id', 'acropolismodel__country_of_residence', 'acropolismodel__application_status', 'acropolismodel__nationality', 'client_status', 'sarawakmodel__gender')
	# http_method_names = ['get', 'put']
	http_method_names = ['get', 'patch', 'put']


	def list(self, request, *args, **kwargs):
		
		response = {}
		
		return Response(response)

	def retrieve(self, request, *args, **kwargs):	#retrive will do the work for put and patch as it's for single object like them

		response = {
			'result':'You don\'t have permission for this'
		}

		if request.user.is_authenticated:
			if request.user.is_superuser:
				response = super().retrieve(request, *args, **kwargs)
				return response
			elif request.user.id == int(kwargs['pk']):
				response = super().retrieve(request, *args, **kwargs)
				return response

		
		return Response(response)














"""
	### API documentation
	argument to send request with 
	('id', 'first_name', 'last_name', 'full_name', 'email', 'phone_no', 'country_of_residence(has options)', 'application_status(has options)', 'application_type(has options)', 'passport_no', 'date_joined', 'gender(has options)', 'client_status(has options)', 'nationality(has options)', 'his_age (no need)', 'referenceID', 'date_of_birth ("1996-11-19" format)', 'occupation', 'no_of_chldrn_U21 ("1996-11-19" format)', 'current_add', 'permanent_add')
	
	
"""