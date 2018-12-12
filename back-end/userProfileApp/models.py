from django.db import models
from django.conf import settings
from coreApp.models import User
from coreApp.commonData import all_countries


# -------------------------fields taken from the Acropolis Application Form


class AcropolisModel(models.Model):

    _application_type_list = (('mm2h_peninsular', 'MM2 Peninsular'), ('mm2h_sarawak', 'MM2H Sarawak'))
    _application_status_list = (('single application', 'Single Application'),
                                ('family application', 'Family Application'))

    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    referenceID = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='ProfilePics', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    passport_no = models.CharField(max_length=50, null=True,blank=True)
    country_of_residence = models.CharField(max_length=50, null=True, blank=True, choices=all_countries())
    nationality = models.CharField(max_length=100, null=True, blank=True, choices=all_countries())
    occupation = models.CharField(max_length=100, null=True, blank=True)
    name_of_the_spouse = models.CharField(max_length=100, null=True, blank=True)
    no_of_chldrn_U21 = models.IntegerField(null=True, blank=True)
    current_add = models.TextField(max_length=1000, null=True, blank=True)
    permanent_add = models.TextField(max_length=1000, null=True,blank=True)
    email_add = models.EmailField(null=True, blank=True)
    phone_no = models.CharField(max_length=50, null=True,blank=True)
    application_type = models.CharField(max_length=50, null=True, blank=True, choices=_application_type_list)
    application_status = models.CharField(max_length=50, null=True, blank=True, choices=_application_status_list)


# ------------------fileds taken from Sarawak Aaplication form----------------


class SarawakModel(models.Model):

    _application_category_type_list = (('new_application',
                                        'New Application'), ('renewal_application', 'Renewal Application'))
    _applicant_accompanied_by_list = (('spouse', 'Spouse'), ('children','Children'))
    _gender_list = (('male', 'Male'), ('female', 'Female'))
    _marital_status_list = (('single', 'Single'), ('married', 'Married'),
                            ('divorced', 'Divorced'), ('widow/widower', 'Widow/Widower'),
                            ('other', 'Other'))

    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    application_category_type = models.CharField(max_length=50, null=True, blank=True,
                                                 choices=_application_category_type_list)
    accompanied_by = models.CharField(max_length=20, null=True, blank=True, choices=_applicant_accompanied_by_list)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=_gender_list)
    marital_status = models.CharField(max_length=50, null=True, blank=True, choices=_marital_status_list)
    marital_status_other = models.CharField(max_length=100, null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, null=True, blank=True, choices=all_countries())
    date_of_expiry_passport = models.DateField(null=True, blank=True)
    mailling_add = models.TextField(max_length=1000, null=True, blank=True)
    add_in_malaysia = models.TextField(max_length=1000, null=True, blank=True)
    current_employment = models.CharField(max_length=100, null=True, blank=True)
    current_organization = models.CharField(max_length=100, null=True, blank=True)
    current_organization_add = models.TextField(max_length=1000, null=True, blank=True)
    income_per_annum = models.IntegerField(null=True, blank=True)
    last_employment = models.CharField(max_length=100, null=True, blank=True)
    last_employer = models.CharField(max_length=100, null=True, blank=True)
    pension_recieved_perannum = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    working_year_start = models.DateField(null=True, blank=True)
    working_year_end = models.DateField(null=True, blank=True)


# -----------------field taken from Visa Form--------------------


class VisaModel(models.Model):

    _type_of_pass_list = (('professional', 'Professional'), ('social', 'Social'),
                          ('business', 'Business'), ('temporary', 'Temporary'))
    _visa_req_list = (('yes', 'Yes'), ('no', 'No'))
    _visa_type_list = (('single entry', 'Single Entry'), ('multiple entry', 'Multiple Entry'))

    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    type_of_pass = models.CharField(max_length=50, null=True, blank=True)
    trvl_doc_type = models.CharField(max_length=100, null=True, blank=True)
    trvl_doc_no = models.CharField(max_length=50,null=True,blank=True)
    trvl_doc_issue_place = models.CharField(max_length=50, null=True, choices=all_countries())
    trvl_doc_valid_till = models.DateField(null=True, blank=True)
    spnsr_frst_name = models.CharField(max_length=100, null=True, blank= True)
    spnsr_last_name = models.CharField(max_length=100, null=True, blank=True)
    spnsr_NRIC_no = models.CharField(max_length=50, null=True, blank=True)
    spnsr_telephone_no = models.CharField(max_length=50, null=True, blank=True)
    spnsr_add = models.TextField(max_length=1000, null=True, blank=True)
    spnsr_state = models.CharField(max_length=100, null=True, blank=True)

    visa_req = models.CharField(max_length=10, null=True, blank=True, choices=_visa_req_list)
    visa_type = models.CharField(max_length= 50, null=True, blank=True)
