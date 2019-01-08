from django.db import models
from django.urls import reverse
from django.conf import settings
import datetime
from coreApp.models import User, Notification
from coreApp.commonData import all_countries
from coreApp.custom_utils import GetCurrentUserMiddleWare, add_notification


# -------------------------fields taken from the Acropolis Application Form


class AcropolisModel(models.Model):

    _application_type_list = (
            ('mm2h_peninsular', 'MM2 Peninsular'),
            ('mm2h_sarawak', 'MM2H Sarawak'),
            )
    _application_status_list = (('single_application', 'Single Application'),
                                ('family_application', 'Family Application'))

    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    referenceID = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='ProfilePics/', null=True, blank=True)
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
    is_business_set_up = models.BooleanField(default=False, null=True,blank=True)

    country_code_1= models.CharField(max_length=50, null=True,blank=True)
    area_code_1= models.CharField(max_length=50, null=True,blank=True)
    phone_no_1 = models.CharField(max_length=50, null=True,blank=True)
    country_code_2 = models.CharField(max_length=50, null=True, blank=True)
    area_code_2 = models.CharField(max_length=50, null=True, blank=True)
    phone_no_2 = models.CharField(max_length=50, null=True, blank=True)
    application_type = models.CharField(max_length=50, null=True, blank=True, choices=_application_type_list)
    application_status = models.CharField(max_length=50, null=True, blank=True, choices=_application_status_list)

    # to add notification
    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save
            super(AcropolisModel, self).save(*args, **kwargs)
        else:
            # get the original
            old = AcropolisModel.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in AcropolisModel._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:
                add_notification(self.user_profile)
                
                
            super(AcropolisModel, self).save(*args, **kwargs)    


    @property
    def his_age(self):
        if self.date_of_birth:
            return int(datetime.datetime.now().year - self.date_of_birth.year)
        else:
            return None

# ------------------fileds taken from Sarawak Aaplication form----------------


class SarawakModel(models.Model):

    _application_category_type_list = (('new_application',
                                        'New Application'), ('renewal_application', 'Renewal Application'))
    _gender_list = (('male', 'Male'), ('female', 'Female'))
    _marital_status_list = (('single', 'Single'), ('married', 'Married'),
                            ('divorced', 'Divorced'), ('widow/widower', 'Widow/Widower'),
                            ('other', 'Other'))

    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    application_category_type = models.CharField(max_length=50, null=True, blank=True,
                                                 choices=_application_category_type_list)
    accompanied_by_spouse = models.BooleanField(default=False, null=True,blank=True)
    accompanied_by_children = models.BooleanField(default=False, null=True, blank=True)
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
    last_employer_add = models.CharField(max_length=100, null=True, blank=True)
    pension_recieved_perannum = models.IntegerField(null=True, blank=True)
    position1 = models.CharField(max_length=100, null=True, blank=True)
    organization1 = models.CharField(max_length=100, null=True, blank=True)
    working_year_start1 = models.DateField(null=True, blank=True)
    working_year_end1 = models.DateField(null=True, blank=True)
    position2 = models.CharField(max_length=100, null=True, blank=True)
    organization2 = models.CharField(max_length=100, null=True, blank=True)
    working_year_start2 = models.DateField(null=True, blank=True)
    working_year_end2 = models.DateField(null=True, blank=True)
    position3 = models.CharField(max_length=100, null=True, blank=True)
    organization3 = models.CharField(max_length=100, null=True, blank=True)
    working_year_start3 = models.DateField(null=True, blank=True)
    working_year_end3 = models.DateField(null=True, blank=True)
    position4 = models.CharField(max_length=100, null=True, blank=True)
    organization4 = models.CharField(max_length=100, null=True, blank=True)
    working_year_start4 = models.DateField(null=True, blank=True)
    working_year_end4 = models.DateField(null=True, blank=True)
    position5 = models.CharField(max_length=100, null=True, blank=True)
    organization5 = models.CharField(max_length=100, null=True, blank=True)
    working_year_start5 = models.DateField(null=True, blank=True)
    working_year_end5 = models.DateField(null=True, blank=True)


    # to add notification
    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save
            super(SarawakModel, self).save(*args, **kwargs)
        else:
            # get the original
            old = SarawakModel.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in SarawakModel._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:
                add_notification(self.user_profile)
                

            super(SarawakModel, self).save(*args, **kwargs)    



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
    visa_type = models.CharField(max_length=50, null=True, blank=True, choices=_visa_type_list)




    # to add notification
    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save
            super(VisaModel, self).save(*args, **kwargs)
        else:
            # get the original
            old = VisaModel.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in VisaModel._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:
                add_notification(self.user_profile)
                

            super(VisaModel, self).save(*args, **kwargs)    




class BirthCertificateFile(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='BirthCertificateFile/', null=True, blank=True)
    file_name = models.CharField(max_length= 150, null=True, blank=True)

    def __str__(self):
        if self.user_profile:
            return str(self.file)
        else:
            return 'No User Found'

    # to add notification
    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save

            add_notification(self.user_profile)

            super(BirthCertificateFile, self).save(*args, **kwargs)
        else:
            # get the original
            old = BirthCertificateFile.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in BirthCertificateFile._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:

                add_notification(self.user_profile)
                
            super(BirthCertificateFile, self).save(*args, **kwargs)    






class MarriageCertificateFile(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='MarriageCertificateFile/', null=True, blank=True)
    file_name = models.CharField(max_length= 150, null=True, blank=True)

    def __str__(self):
        if self.user_profile:
            return str(self.file)
        else:
            return 'No User Found'

    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save

            add_notification(self.user_profile)

            super(MarriageCertificateFile, self).save(*args, **kwargs)

        else:
            # get the original
            old = MarriageCertificateFile.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in MarriageCertificateFile._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:

                add_notification(self.user_profile)
                
            super(MarriageCertificateFile, self).save(*args, **kwargs)    






class PassportCopyFile(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='PassportCopyFile/', null=True, blank=True)
    file_name = models.CharField(max_length= 150, null=True, blank=True)

    def __str__(self):
        if self.user_profile:
            return str(self.file)
        else:
            return 'No User Found'


    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save
            
            add_notification(self.user_profile)

            super(PassportCopyFile, self).save(*args, **kwargs)
        else:
            # get the original
            old = PassportCopyFile.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in PassportCopyFile._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:

                add_notification(self.user_profile)
                
            super(PassportCopyFile, self).save(*args, **kwargs)    





class BankStatementFile(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='BankStaementsFile/', null=True, blank=True)
    file_name = models.CharField(max_length= 150, null=True, blank=True)

    def __str__(self):
        if self.user_profile:
            return str(self.file)
        else:
            return 'No User Found'



    def save(self, *args, **kwargs):
        if not self.pk: # if this is new, just save
                
            add_notification(self.user_profile)

            super(BankStatementFile, self).save(*args, **kwargs)
        else:
            # get the original
            old = BankStatementFile.objects.get(id=self.pk)


            field_changed = False

            # field_changed = []
            # for field in self._meta.get_all_field_names():
            for field in BankStatementFile._meta.fields:
                if getattr(self, field.name, None) != getattr(old, field.name, None):
                    # field_changed.append(old)
                    field_changed = True
                    break
            
            if field_changed:

                add_notification(self.user_profile)
                
            super(BankStatementFile, self).save(*args, **kwargs)    
