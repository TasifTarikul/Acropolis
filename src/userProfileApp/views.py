import ast
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, AcropolisForm, SarawakForm, VisaForm
from django.contrib import auth
from .models import BirthCertificateFile
from coreApp.custom_utils import add_notification


@login_required
def usr_profile(request):
    if request.user.is_superuser:  # checks wether the user is a superuser.
        return HttpResponseRedirect(reverse('superAdmin:dashboard'))

    acropolis_form = AcropolisForm(instance=request.user.acropolismodel)
    sarawak_form = SarawakForm(instance=request.user.sarawakmodel)
    visa_form = VisaForm(instance=request.user.visamodel)

    # print(request.user.acropolismodel.user_profile.first_name)
    if request.method == 'POST':
        if request.POST['submit'] == 'AcropolisForm':                               # if acropolis form is submitted
            user = request.user  # get current user
            acropolis_form = AcropolisForm(request.POST,instance=user.acropolismodel )
            if acropolis_form.is_valid():
                acropolis_form.save(commit=True)

        elif request.POST['submit'] == 'SarawakForm':                               # if sarawak form is submitted
            user = request.user
            sarawak_form = SarawakForm(request.POST, instance=user.sarawakmodel)
            if sarawak_form.is_valid():
                sarawak_form.save(commit=True)

        elif request.POST['submit'] == 'VisaForm':                               # if Visa form is submitted
            user = request.user
            visa_form = VisaForm(request.POST, instance=user.visamodel)
            if visa_form.is_valid():
                visa_form.save(commit=True)
                visa_form = VisaForm()
            

        elif request.POST['submit'] == 'AllForm':
            user = request.user
            acropolis_form = AcropolisForm(request.POST, instance=user.acropolismodel)
            sarawak_form = SarawakForm(request.POST, instance=user.sarawakmodel)
            visa_form = VisaForm(request.POST, instance=user.visamodel)
            if acropolis_form.is_valid() and sarawak_form.is_valid() and visa_form.is_valid():
                acropolis_form.save()
                sarawak_form.save()
                visa_form.save()
        elif request.POST['submit'] == 'profile_pic_upload':

            # docs = request.FILES.getlist('profile_pic')
            doc = request.FILES.get('profile_pic', False)
            
            if doc:
                fs = FileSystemStorage(location='media/profile_pic')

                filename = fs.save(doc.name, doc)
                uploaded_file_url = fs.url(filename)
                request.user.profile_pic = '/profile_pic/'+filename
                request.user.save()
            else:
                request.user.profile_pic = None
                request.user.save()


        elif request.POST['submit'] == 'UploadBirthCertificateFile':


            #make sure we check first existing file and than add new file. Otherwise if no file exist means in the <li> we will see no file. So even if we add new file because of having <li>(list of current file) as blank this view will think no file exists and will remove all from database. 
            # So first update than add new files

            #update already existing files
            crnt_files = request.POST.get('currentBirthCertificateFiles', False)
            if crnt_files:
                crnt_files = ast.literal_eval(crnt_files)   #convert string into real iterable list

                if isinstance(crnt_files,int):      #if only one file remain it will not come as a tuple but integer
                    delete_and_check = request.user.birthcertificatefile_set.exclude(id=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification
                else:
                    for crnt_file in crnt_files:
                        pass
                    delete_and_check = request.user.birthcertificatefile_set.exclude(id__in=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification

            else:   #no crnt files means all removed
                delete_and_check = request.user.birthcertificatefile_set.all().delete()
                if delete_and_check[0] != 0:
                    add_notification(request.user)   #to add notification

            # add new files


            # addFileOnList = request.FILES.getlist('addFileOnList', False)

            docs = request.FILES.getlist('addBirthCertificateFileOnList', False)
            if docs:
                for doc in docs:
                    if doc:
                        fs = FileSystemStorage(location='media/BirthCertificateFile')

                        file_name = fs.save(doc.name, doc)
                        uploaded_file_url = fs.url(file_name)
                        file_real_url = '/BirthCertificateFile/'+file_name
                        
                        request.user.birthcertificatefile_set.create(file=file_real_url, file_name=file_name)
                    else:
                        pass
                        # request.user.userfiles.birth_certificates = None
                        # request.user.save()
            
            return HttpResponseRedirect(reverse('userProfileApp:usrProfile')+'?tab=file_upload')







        elif request.POST['submit'] == 'uploadMarriageCertificateFile':


            #make sure we check first existing file and than add new file. Otherwise if no file exist means in the <li> we will see no file. So even if we add new file because of having <li>(list of current file) as blank this view will think no file exists and will remove all from database. 
            # So first update than add new files

            #update already existing files
            crnt_files = request.POST.get('currentMarriageCertificateFiles', False)
            
            if crnt_files:
                crnt_files = ast.literal_eval(crnt_files)   #convert string into real iterable list

                if isinstance(crnt_files,int):      #if only one file remain it will not come as a tuple but integer
                    delete_and_check = request.user.marriagecertificatefile_set.exclude(id=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification
                else:
                    for crnt_file in crnt_files:
                        # 
                        pass
                    delete_and_check = request.user.marriagecertificatefile_set.exclude(id__in=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification

            else:   #no crnt files means all removed
                # 
                delete_and_check = request.user.marriagecertificatefile_set.all().delete()
                if delete_and_check[0] != 0:
                    add_notification(request.user)   #to add notification




            # add new files
            # addFileOnList = request.FILES.getlist('addMarriageCertificateFileOnList', False)

            docs = request.FILES.getlist('addMarriageCertificateFileOnList', False)
            
            if docs:
                for doc in docs:
                    if doc:
                        fs = FileSystemStorage(location='media/MarriageCertificateFile')

                        file_name = fs.save(doc.name, doc)
                        uploaded_file_url = fs.url(file_name)
                        file_real_url = '/MarriageCertificateFile/'+file_name
                        
                        request.user.marriagecertificatefile_set.create(file=file_real_url, file_name=file_name)
                    else:
                        pass
                        # request.user.userfiles.birth_certificates = None
                        # request.user.save()
            
            return HttpResponseRedirect(reverse('userProfileApp:usrProfile')+'?tab=file_upload')




        elif request.POST['submit'] == 'uploadPassportCopyFile':


            #make sure we check first existing file and than add new file. Otherwise if no file exist means in the <li> we will see no file. So even if we add new file because of having <li>(list of current file) as blank this view will think no file exists and will remove all from database. 
            # So first update than add new files

            #update already existing files
            crnt_files = request.POST.get('currentPassportCopyFiles', False)

            if crnt_files:
                crnt_files = ast.literal_eval(crnt_files)   #convert string into real iterable list

                if isinstance(crnt_files,int):      #if only one file remain it will not come as a tuple but integer
                    delete_and_check = request.user.passportcopyfile_set.exclude(id=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification
                else:
                    for crnt_file in crnt_files:
                        
                        pass
                    delete_and_check = request.user.passportcopyfile_set.exclude(id__in=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification

            else:   #no crnt files means all removed
                
                delete_and_check = request.user.passportcopyfile_set.all().delete()
                if delete_and_check[0] != 0:
                    add_notification(request.user)   #to add notification




            # add new files
            # addFileOnList = request.FILES.getlist('addMarriageCertificateFileOnList', False)

            docs = request.FILES.getlist('addPassportCopyFileOnList', False)
            
            if docs:
                for doc in docs:
                    if doc:
                        fs = FileSystemStorage(location='media/PassportCopyFile')

                        file_name = fs.save(doc.name, doc)
                        uploaded_file_url = fs.url(file_name)
                        file_real_url = '/PassportCopyFile/'+file_name
                        
                        request.user.passportcopyfile_set.create(file=file_real_url, file_name=file_name)
                    else:
                        pass
                        # request.user.userfiles.birth_certificates = None
                        # request.user.save()
            
            return HttpResponseRedirect(reverse('userProfileApp:usrProfile')+'?tab=file_upload')






        elif request.POST['submit'] == 'uploadBankStatementFile':


            #make sure we check first existing file and than add new file. Otherwise if no file exist means in the <li> we will see no file. So even if we add new file because of having <li>(list of current file) as blank this view will think no file exists and will remove all from database. 
            # So first update than add new files

            #update already existing files
            crnt_files = request.POST.get('currentBankStatementFiles', False)

            if crnt_files:
                crnt_files = ast.literal_eval(crnt_files)   #convert string into real iterable list

                if isinstance(crnt_files,int):      #if only one file remain it will not come as a tuple but integer
                    delete_and_check = request.user.bankstatementfile_set.exclude(id=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification
                else:
                    for crnt_file in crnt_files:
                        
                        pass
                    delete_and_check = request.user.bankstatementfile_set.exclude(id__in=crnt_files).delete()
                    if delete_and_check[0] != 0:
                        add_notification(request.user)   #to add notification

            else:   #no crnt files means all removed
                
                delete_and_check = request.user.bankstatementfile_set.all().delete()
                if delete_and_check[0] != 0:
                    add_notification(request.user)   #to add notification




            # add new files
            # addFileOnList = request.FILES.getlist('addMarriageCertificateFileOnList', False)

            docs = request.FILES.getlist('addBankStatementFileOnList', False)
            if docs:
                for doc in docs:
                    if doc:
                        fs = FileSystemStorage(location='media/BankStaementsFile')

                        file_name = fs.save(doc.name, doc)
                        uploaded_file_url = fs.url(file_name)
                        file_real_url = '/BankStaementsFile/'+file_name
                        request.user.bankstatementfile_set.create(file=file_real_url, file_name=file_name)
                    else:
                        pass
                        # request.user.userfiles.birth_certificates = None
                        # request.user.save()
            
            return HttpResponseRedirect(reverse('userProfileApp:usrProfile')+'?tab=file_upload')






        return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))








    context = {
        'current_birth_certificate_file_ids': list(request.user.birthcertificatefile_set.all().values_list('id', flat=True)),
        'current_marriage_certificate_file_ids': list(request.user.marriagecertificatefile_set.all().values_list('id', flat=True)),
        'current_passport_copy_ids': list(request.user.passportcopyfile_set.all().values_list('id', flat=True)),
        'current_bank_statement_file_ids': list(request.user.bankstatementfile_set.all().values_list('id', flat=True)),
        'this_user': request.user,
        'acropolis_form': acropolis_form,
        'sarawak_form': sarawak_form,
        'visa_form' : visa_form
    }
    return render(request, 'userProfileApp/userProfilePage.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            try:
                # print("form is saved")
                auth.login(request, user)
                if request.user.is_authenticated:
                    return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))
            except Exception as e:
                print('user can\'t logged in after register')
    else:
        form = UserSignUpForm()

    return render(request, 'userProfileApp/signUpPage.html', {'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            try:
                user = auth.login(request, form.get_user())
                return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))
            except Exception as e:
                print('user can\'t logged in after register')

        else:
            print('error ase ', form.errors.as_data())

    else:
        form = AuthenticationForm()

    return render(request, 'userProfileApp/signInPage.html', {'user_signinform': form})


