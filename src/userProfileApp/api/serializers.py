from django.contrib.auth import get_user_model
from rest_framework import serializers

# class TagSerializer(serializers.Serializer):		#as tag is a many to many field
# 	id = serializers.IntegerField()	#to return the name not id
# 	name = serializers.CharField()	#to return the name not id

# class DisabilitiesSerializer(serializers.Serializer):		#as tag is a many to many field
# 	id = serializers.IntegerField()	#to return the name not id
# 	name = serializers.CharField()	#to return the name not id



class UserSerializer(serializers.ModelSerializer):	

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
	gender = serializers.CharField(source='sarawakmodel.gender')

	class Meta:
		model = get_user_model()
		# fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'status')
		fields = ('id', 'full_name', 'email', 'phone_no', 'country_of_residence', 'application_status', 'application_type', 'passport_no', 'date_joined', 'gender', 'client_status', 'nationality', 'his_age')
		# exclude = ('content',)
		# fields = ('id', 'title', 'summary', 'image', 'category', 'tags', 'disabilities')
		# fields = ('id',)
		# read_only_fields = ('category',)
