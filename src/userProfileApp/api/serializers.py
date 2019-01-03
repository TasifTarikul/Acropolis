from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import serializers
from userProfileApp.models import AcropolisModel, SarawakModel
from coreApp.custom_utils import add_notification

User = get_user_model()
# class TagSerializer(serializers.Serializer):		#as tag is a many to many field
# 	id = serializers.IntegerField()	#to return the name not id
# 	name = serializers.CharField()	#to return the name not id

# class DisabilitiesSerializer(serializers.Serializer):		#as tag is a many to many field
# 	id = serializers.IntegerField()	#to return the name not id
# 	name = serializers.CharField()	#to return the name not id



class UserProfileSerializer(serializers.ModelSerializer):	

	# category = serializers.CharField(source="category.name", read_only=True)	#to return the name not id
	# tags = TagSerializer(many=True)		#many=True for manytomany relation
	# disabilities = DisabilitiesSerializer(many=True)		#many=True for manytomany relation

	phone_no = serializers.CharField(source='acropolismodel.phone_no')
	country_of_residence = serializers.CharField(source='acropolismodel.country_of_residence')
	application_status = serializers.CharField(source='acropolismodel.application_status')
	application_type = serializers.CharField(source='acropolismodel.application_type')
	nationality = serializers.CharField(source='acropolismodel.nationality')
	his_age = serializers.CharField(source='acropolismodel.his_age')
	passport_no = serializers.CharField(source='acropolismodel.passport_no')
	referenceID = serializers.CharField(source='acropolismodel.referenceID')
	date_of_birth = serializers.CharField(source='acropolismodel.date_of_birth')
	occupation = serializers.CharField(source='acropolismodel.occupation')
	no_of_chldrn_U21 = serializers.CharField(source='acropolismodel.no_of_chldrn_U21')
	current_add = serializers.CharField(source='acropolismodel.current_add')
	permanent_add = serializers.CharField(source='acropolismodel.permanent_add')

	gender = serializers.CharField(source='sarawakmodel.gender')

	class Meta:
		model = get_user_model()
		# fields = ('first_name', 'last_name', 'email', 'phone_no')
		fields = ('id', 'first_name', 'last_name', 'full_name', 'email', 'phone_no', 'country_of_residence', 'application_status', 'application_type', 'passport_no', 'date_joined', 'gender', 'client_status', 'nationality', 'his_age', 'referenceID', 'date_of_birth', 'occupation', 'no_of_chldrn_U21', 'current_add', 'permanent_add')
		# exclude = ('content',)
		# read_only_fields = ('category',)


	# def update(self, *args, **kwargs):
	def update(self, instance, validated_data):

		"""
		Since we are workign with 3 model in one model form so while updating we need to define which value for which model rather sending all the data(value) to model Meta. With pop we are brining out the value for each model and updating filed for that. And since this serializer is for User model so at the end the rest data we are sending(using to update) to User model.
		"""

		# instance = get_object_or_404(User, pk= kwargs['pk'])

		# del validated_data['full_name']	#it's also a custom field but no need since it's from the same model # also no need django ignore it by default
		
		try:	#if put request than might not have these field
			acropolismodel = validated_data.pop('acropolismodel')
			# del acropolismodel['his_age']	#since it's a custom method # no need lookslike doesn't matter. Rather throw error if not get called with other filed in the request
			AcropolisModel.objects.filter(user_profile=instance).update(**acropolismodel)
			add_notification(instance)
		except Exception as e:
			# print(e)
			pass

		try:	#if put request than might not have these field
			sarawakmodel = validated_data.pop('sarawakmodel')
			SarawakModel.objects.filter(user_profile=instance).update(**sarawakmodel)
			add_notification(instance)
		except:
			pass

		User.objects.filter(id=instance.id).update(**validated_data)
		add_notification(instance)
		instance = User.objects.filter(id=instance.id).get()
		
		return instance

