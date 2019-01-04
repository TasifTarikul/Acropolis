import datetime
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from rest_framework import viewsets, permissions, generics, pagination
from rest_framework.response import Response
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .serializers import UserSerializer
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

		# return True
		return False


# ViewSets define the view behavior.
class UserProfileViewSet(viewsets.ModelViewSet):


	def get_queryset(self):
		to_return = User.objects.all()
		filters_kwargs = dict()
		filters_args = [Q()]	#blank search
		order_by_args = ['-id']

		"""
		Filter by
		"""

		#search with full name
		full_name = self.request.GET.get('full_name', False)
		if full_name:
			to_filter = Q(first_name__icontains=full_name) | Q(last_name__icontains=full_name)
			filters_args.append(to_filter)
			
		#search with email
		email = self.request.GET.get('email', False)
		if email:
			filters_kwargs['email__icontains'] = email


		#search with passport_no
		passport_no = self.request.GET.get('passport_no', False)
		if passport_no:
			filters_kwargs['acropolismodel__passport_no__icontains'] = passport_no


		#search with phone_no
		phone_no = self.request.GET.get('phone_no', False)
		if phone_no:
			filters_kwargs['acropolismodel__phone_no__icontains'] = phone_no



		#search with date_joined_after
		date_joined_after = self.request.GET.get('date_joined_after', False)
		if date_joined_after:
			filters_kwargs['date_joined__gt'] = date_joined_after

		#search with date_joined_before
		date_joined_before = self.request.GET.get('date_joined_before', False)
		if date_joined_before:
			filters_kwargs['date_joined__lt'] = date_joined_before

		#search with age_greater_than
		age_greater_than = self.request.GET.get('age_greater_than', False)
		if age_greater_than:
			to_check_from = datetime.datetime.now() - datetime.timedelta(days=365*int(age_greater_than))
			# print(to_check_from)
			filters_kwargs['acropolismodel__date_of_birth__lt'] = to_check_from.date()	#means greater than their difference(age)

		# search with age_less_than
		age_less_than = self.request.GET.get('age_less_than', False)
		if age_less_than:
			to_check_from = datetime.datetime.now() - datetime.timedelta(days=365*int(age_less_than))
			# print(to_check_from)
			filters_kwargs['acropolismodel__date_of_birth__gt'] = to_check_from.date()	#means less than their difference(age)


		"""
		Order By
		"""
		#order by id
		id = self.request.GET.get('order_by_id', False)
		if id == 'asc':
			order_by_args.insert(0, 'id')
		if id == 'desc':
			order_by_args.insert(0, '-id')


		#order by country_of_residence
		order_by_country_of_residence = self.request.GET.get('order_by_country_of_residence', False)
		if order_by_country_of_residence == 'asc':
			order_by_args.insert(0, 'acropolismodel__country_of_residence')
		if order_by_country_of_residence == 'desc':
			order_by_args.insert(0, '-acropolismodel__country_of_residence')


		#order by application_status
		order_by_application_status = self.request.GET.get('order_by_application_status', False)
		if order_by_application_status == 'asc':
			order_by_args.insert(0, 'acropolismodel__application_status')
		if order_by_application_status == 'desc':
			order_by_args.insert(0, '-acropolismodel__application_status')


		#order by application_type
		order_by_application_type = self.request.GET.get('order_by_application_type', False)
		if order_by_application_type == 'asc':
			order_by_args.insert(0, 'acropolismodel__application_type')
		if order_by_application_type == 'desc':
			order_by_args.insert(0, '-acropolismodel__application_type')



		#order by nationality
		order_by_nationality = self.request.GET.get('order_by_nationality', False)
		if order_by_nationality == 'asc':
			order_by_args.insert(0, 'acropolismodel__nationality')
		if order_by_nationality == 'desc':
			order_by_args.insert(0, '-acropolismodel__nationality')



		#order by client_status
		order_by_client_status = self.request.GET.get('order_by_client_status', False)
		if order_by_client_status == 'asc':
			order_by_args.insert(0, 'client_status')
		if order_by_client_status == 'desc':
			order_by_args.insert(0, '-client_status')



		#order by gender
		order_by_gender = self.request.GET.get('order_by_gender', False)
		if order_by_gender == 'asc':
			order_by_args.insert(0, 'sarawakmodel__gender')
		if order_by_gender == 'desc':
			order_by_args.insert(0, '-sarawakmodel__gender')


		#order by full name
		order_by_full_name = self.request.GET.get('order_by_full_name', False)
		if order_by_full_name == 'asc':
			order_by_args.insert(0, 'first_name')
		if order_by_full_name == 'desc':
			order_by_args.insert(0, '-first_name')


		#order by email
		order_by_email = self.request.GET.get('order_by_email', False)
		if order_by_email == 'asc':
			order_by_args.insert(0, 'email')
		if order_by_email == 'desc':
			order_by_args.insert(0, '-email')

		#order by passort_no
		order_by_passport_no = self.request.GET.get('order_by_passport_no', False)
		if order_by_passport_no == 'asc':
			order_by_args.insert(0, 'acropolismodel__passport_no')
		if order_by_passport_no == 'desc':
			order_by_args.insert(0, '-acropolismodel__passport_no')


		#order by phone_no
		order_by_phone_no = self.request.GET.get('order_by_phone_no', False)
		if order_by_phone_no == 'asc':
			order_by_args.insert(0, 'acropolismodel__phone_no')
		if order_by_phone_no == 'desc':
			order_by_args.insert(0, '-acropolismodel__phone_no')




		#order by date_joined
		order_by_date_joined = self.request.GET.get('order_by_date_joined', False)
		if order_by_date_joined == 'asc':
			order_by_args.insert(0, 'date_joined')
		if order_by_date_joined == 'desc':
			order_by_args.insert(0, '-date_joined')


		#order by age
		order_by_date_joined = self.request.GET.get('order_by_age', False)
		if order_by_date_joined == 'asc':
			order_by_args.insert(0, '-acropolismodel__date_of_birth')	#date of birth is reverse of age
		if order_by_date_joined == 'desc':
			order_by_args.insert(0, 'acropolismodel__date_of_birth')	#date of birth is reverse of age

		to_return = User.objects.filter(*filters_args, **filters_kwargs).order_by(*order_by_args).distinct()
		# to_return = User.objects.filter().order_by('-id').distinct()

		return to_return

	# queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	permission_classes = (CustomerAccessPermission,)
	pagination_class = LargeResultsSetPagination
	

	filterset_fields = ('id', 'acropolismodel__country_of_residence', 'acropolismodel__application_status', 'acropolismodel__application_type', 'acropolismodel__nationality', 'client_status', 'sarawakmodel__gender')
	http_method_names = ['get', 'patch', 'put']


	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)
		# response = {
		# 	'result': response.data
		# }
		single_page_url = reverse('superAdmin:client', args=[0,])		# since we must add the training_id argument
		response.data['single_page_url'] = single_page_url[:-1]			# removing the id argument to use it globally / need to use "/<id>" format. Will only work if id in last
		
		return response

		"""
		if not using paginaiton use this for adding extra argument
		"""
		# response = {
		# 	'result': response.data
		# }
		# response['single_page_url'] = single_page_url
		# return Response(response)




	# def retrieve(self, request, *args, **kwargs):

	# 	response = {
	# 		'result':'You don\'t have permission for this'
	# 	}

	# 	if request.user.is_authenticated:
	# 		if request.user.id == int(kwargs['pk']):
				
	# 			response = super().retrieve(request, *args, **kwargs)
	# 			return response

		
	# 	return Response(response)











"""
	### API documentation

	Table Head: Date, month, gender, client_status: name , nationality, age ,application type , passport_no , email , client_status, gender,

	Filter By:
		full_name
		email
		passport_no
		phone_no
		date_joined_after
		date_joined_before
		age_greater_than
		age_less_than
		id
		acropolismodel__country_of_residence
		acropolismodel__application_status
		acropolismodel__application_type
		acropolismodel__nationality
		client_status
		sarawakmodel__gender

	Order By:	(only asc or desc)
		order_by_id
		order_by_country_of_residence
		order_by_application_status
		order_by_application_type
		order_by_nationality
		order_by_client_status
		order_by_gender
		order_by_full_name
		order_by_email
		order_by_passport_no
		order_by_phone_no
		order_by_date_joined
		order_by_age
	Pagination:
		page_size
		page

		#excepted result
			result.pagination
			{
		        "next": null,
		        "previous": null,
		        "total_value": 3,
		        "num_of_pages": 1,
		        "current_page": 1,
		        "page_range": [
		            1
		            2
		            3
		        ]
		    },
	"""